#!/usr/bin/env python3
"""Resolve the reviewed discovery curation to standard ontology identifiers.

``scripts/discovery_curation.json`` names each model's species, drugs, targets,
indications, routes and readout analytes by label. This script resolves every
label with an exact match and writes ``qspquest_models/discovery.json``:

- species: NCBITaxon; indications: MONDO; drugs, routes and modalities: NCIt;
  cell analytes: CL; matrices: UBERON; small-molecule targets: ChEBI (OLS4);
- human targets: HGNC symbols with alias and previous symbols (HGNC REST);
- non-human protein targets: UniProt; citations: Europe PMC, then Crossref.

A label that does not resolve exactly stops the build; nothing is guessed. A
name without an ontology entry is curated with no identifier and kept as is.
``--check`` resolves again and fails if the stored file differs.
"""
from __future__ import annotations

import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
import time
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
CURATION = Path(__file__).with_name('discovery_curation.json')
OUTPUT = ROOT / 'qspquest_models' / 'discovery.json'
SCHEMA = 'qspquest.models.discovery/v1'
HEADERS = {'User-Agent': 'qspquest-models-catalog/1.0', 'Accept': 'application/json'}

MODALITIES = {
    'monoclonal_antibody': 'Monoclonal Antibody', 'antibody_drug_conjugate': 'Antineoplastic Antibody-Drug Conjugate',
    'bispecific_antibody': 'Bispecific Antibody', 'antibody_fragment': 'Fab Fragment',
    'immunotoxin': 'Immunotoxin', 'fusion_protein': 'Fusion Protein', 'gene_therapy': 'Gene Therapy',
    'small_molecule': 'Small Molecule', 'targeted_protein_degrader': None}
ROUTES = {
    'intravenous': 'Intravenous Route of Administration', 'subcutaneous': 'Subcutaneous Route of Administration',
    'intramuscular': 'Intramuscular Route of Administration', 'oral': 'Oral Route of Administration',
    'intracisternal': 'Intracisternal Route of Administration', 'intracerebral': 'Intracerebral Route of Administration'}
CONTEXTS = ('clinical', 'preclinical', 'in_vitro', 'hypothetical')
QUANTITIES = ('concentration', 'amount', 'exposure', 'cell_density', 'cell_count', 'percent_of_baseline', 'percent',
              'fraction', 'occupancy', 'score', 'probability', 'clearance', 'rate', 'tumor_size', 'parameter')
_cache = {}


def get(url):
    if url not in _cache:
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=60) as r:
                    _cache[url] = json.load(r)
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(2 * (attempt + 1))
        time.sleep(0.1)
    return _cache[url]


def synonyms(values, exclude=()):
    seen, out = {s.casefold() for s in exclude}, []
    for value in values or []:
        value = str(value).strip()
        if value and len(value) <= 80 and value.casefold() not in seen:
            seen.add(value.casefold())
            out.append(value)
    return out[:25]


def ols(label, ontology):
    """The defining-ontology term whose label matches exactly (case-insensitive)."""
    url = ('https://www.ebi.ac.uk/ols4/api/search?' + urllib.parse.urlencode({
        'q': label, 'ontology': ontology, 'exact': 'true', 'rows': 20,
        'fieldList': 'obo_id,label,synonym,is_defining_ontology'}))
    docs = [d for d in get(url)['response']['docs']
            if d.get('label', '').casefold() == label.casefold() and d.get('obo_id', '').upper().startswith(ontology.upper() + ':')]
    if len({d['obo_id'] for d in docs}) != 1:
        raise ValueError(f'{ontology}: no unique exact term for {label!r}')
    doc = docs[0]
    return {'id': doc['obo_id'], 'label': doc['label'], 'synonyms': synonyms(doc.get('synonym'), [doc['label']])}


def hgnc(symbol):
    docs = get('https://rest.genenames.org/fetch/symbol/' + urllib.parse.quote(symbol))['response']['docs']
    if len(docs) != 1 or docs[0]['symbol'] != symbol:
        raise ValueError(f'HGNC: no approved symbol {symbol}')
    doc = docs[0]
    return {'symbol': doc['symbol'], 'id': doc['hgnc_id'], 'label': doc['name'],
            'synonyms': synonyms([*(doc.get('alias_symbol') or []), *(doc.get('prev_symbol') or []),
                                  *(doc.get('alias_name') or [])], [doc['symbol']]),
            'uniprot': (doc.get('uniprot_ids') or [None])[0]}


def uniprot(accession):
    doc = get(f'https://rest.uniprot.org/uniprotkb/{accession}.json')
    if doc.get('primaryAccession') != accession:
        raise ValueError(f'UniProt: no entry {accession}')
    names = doc['proteinDescription']
    full = names['recommendedName']['fullName']['value']
    alternatives = [n['fullName']['value'] for n in names.get('alternativeNames', [])]
    alternatives += [s['value'] for n in [names['recommendedName'], *names.get('alternativeNames', [])]
                     for s in n.get('shortNames', [])]
    return {'symbol': None, 'id': 'UniProt:' + accession, 'label': f"{full} ({doc['organism']['scientificName']})",
            'synonyms': synonyms(alternatives, [full]), 'uniprot': accession}


def citation(doi):
    query = urllib.parse.urlencode({'query': f'DOI:"{doi}"', 'format': 'json', 'resultType': 'core'})
    results = get('https://www.ebi.ac.uk/europepmc/webservices/rest/search?' + query)['resultList']['result']
    results = [r for r in results if (r.get('doi') or '').casefold() == doi.casefold()]
    if results:
        r = results[0]
        journal = ((r.get('journalInfo') or {}).get('journal') or {}).get('title') or (r.get('bookOrReportDetails') or {}).get('publisher')
        authors = (r.get('authorList') or {}).get('author') or [{}]
        return {'doi': doi, 'pmid': r.get('pmid'), 'pmcid': r.get('pmcid'), 'title': r['title'].rstrip('.'),
                'journal': journal, 'year': int(r['pubYear']), 'first_author': authors[0].get('lastName')}
    message = get('https://api.crossref.org/works/' + urllib.parse.quote(doi))['message']
    return {'doi': doi, 'pmid': None, 'pmcid': None, 'title': message['title'][0].rstrip('.'),
            'journal': (message.get('container-title') or [None])[0],
            'year': message['issued']['date-parts'][0][0],
            'first_author': (message.get('author') or [{}])[0].get('family')}


def source_dois(library, row):
    folder = (library / row['archive']).parent
    dois = json.loads((folder / 'SOURCE_REPRODUCTION.json').read_text()).get('source_dois') or []
    if not dois:
        text = (folder / 'SOURCE_REFERENCE.md').read_text()
        dois = sorted({d.rstrip('.') for d in re.findall(r'10\.\d{4,9}/[^\s"\)\]>,;]+', text)})
    return [d.lower() for d in dois]


def resolve_model(entry, dois):
    if entry['context'] not in CONTEXTS:
        raise ValueError('Unknown context ' + entry['context'])
    drugs = []
    for drug in entry['drugs']:
        term = ols(drug['ncit'], 'ncit') if drug['ncit'] else {'id': None, 'label': drug['name'], 'synonyms': []}
        if drug['modality'] is not None and drug['modality'] not in MODALITIES:
            raise ValueError('Unknown modality ' + drug['modality'])
        drugs.append({'name': drug['name'], **term, 'modality': drug['modality']})
    keys = []
    for drug in drugs:
        if drug['modality'] and drug['modality'] not in keys:
            keys.append(drug['modality'])
    modalities = [{'key': k, **({'id': None, 'label': k.replace('_', ' ')} if MODALITIES[k] is None
                                else {x: v for x, v in ols(MODALITIES[k], 'ncit').items() if x != 'synonyms'})}
                  for k in keys]
    targets = []
    for target in entry['targets']:
        if isinstance(target, str):
            targets.append(hgnc(target))
        elif 'uniprot' in target:
            targets.append(uniprot(target['uniprot']))
        elif 'chebi' in target:
            term = ols(target['chebi'], 'chebi')
            targets.append({'symbol': None, **term, 'uniprot': None})
        else:
            targets.append({'symbol': None, 'id': None, 'label': target['label'], 'synonyms': [],
                            'uniprot': None, 'hypothetical': True})
    routes = [{'key': k, **{x: v for x, v in ols(ROUTES[k], 'ncit').items() if x != 'synonyms'}} for k in entry['routes']]
    by_drug = {d['name']: d for d in drugs}
    by_target = {t['symbol'] or t['label']: t for t in targets}
    readouts = {}
    for name, spec in entry['readouts'].items():
        if spec['quantity'] not in QUANTITIES:
            raise ValueError(f'{name}: unknown quantity {spec["quantity"]}')
        ref = spec['analyte']
        kind, _, value = ref.partition(':') if ':' in ref else ('', '', ref)
        if kind == 'drug':
            analyte = {'label': by_drug[value]['name'], 'id': by_drug[value]['id']}
        elif kind == 'target':
            target = by_target[value]
            analyte = {'label': target['symbol'] or target['label'], 'id': target['id']}
        elif kind == 'hgnc':
            analyte = {'label': value, 'id': hgnc(value)['id']}
        elif kind == 'cl':
            term = ols(value, 'cl')
            analyte = {'label': term['label'], 'id': term['id']}
        else:
            analyte = {'label': ref, 'id': None}
        matrix = None
        if spec['matrix']:
            term = ols(spec['matrix'], 'uberon')
            matrix = {'id': term['id'], 'label': term['label']}
        readouts[name] = {'analyte': analyte, 'quantity': spec['quantity'], 'matrix': matrix,
                          'compartment': spec['compartment'], 'ucum': spec['ucum']}
    return {
        'citations': [citation(d) for d in dois], 'context': entry['context'],
        'species': [ols(s, 'ncbitaxon') for s in entry['species']],
        'drugs': drugs, 'modalities': modalities, 'targets': targets,
        'indications': [ols(i, 'mondo') for i in entry['indications']],
        'routes': routes, 'readouts': readouts}


def build():
    sys.path.insert(0, str(ROOT))
    from qspquest_models import Library
    library = Library(ROOT)
    curation = json.loads(CURATION.read_text())['models']
    rows = {r['id']: r for r in library.list_models()}
    if set(curation) != set(rows):
        raise ValueError('Curation and catalog model identities differ: '
                         + ', '.join(sorted(set(curation) ^ set(rows))))
    models = {}
    for model_id in sorted(curation):
        models[model_id] = resolve_model(curation[model_id], source_dois(library.root, rows[model_id]))
        print(model_id, file=sys.stderr, flush=True)
    return {'schema': SCHEMA,
            'vocabularies': {'species': 'NCBITaxon', 'indications': 'MONDO', 'drugs': 'NCIt', 'routes': 'NCIt',
                             'modalities': 'NCIt', 'human_targets': 'HGNC', 'protein_targets': 'UniProt',
                             'small_molecule_targets': 'ChEBI', 'cells': 'CL', 'matrices': 'UBERON',
                             'units': 'UCUM', 'citations': 'Europe PMC, then Crossref'},
            'models': models}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Resolve again and fail if the stored file differs')
    args = parser.parse_args()
    value = build()
    if args.check:
        stored = json.loads(OUTPUT.read_text())
        stored.pop('generated', None)
        if stored != value:
            print('Stored discovery records differ from a fresh resolution', file=sys.stderr)
            raise SystemExit(1)
        print(f'{len(value["models"])} discovery records match')
        return
    value = {'schema': value['schema'], 'generated': date.today().isoformat(),
             **{k: v for k, v in value.items() if k != 'schema'}}
    OUTPUT.write_text(json.dumps(value, indent=1, ensure_ascii=False) + '\n')
    print(f'{len(value["models"])} discovery records written')


if __name__ == '__main__':
    main()
