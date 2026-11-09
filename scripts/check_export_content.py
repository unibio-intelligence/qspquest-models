"""Refuse source-acquisition bookkeeping in the selected archives.

Model archives describe a paper's model, study and results. Values that record
how the paper was found or retrieved (queue ranks, citation counts, PMID or
PMCID numbers, publication year and pages, fetch, availability, blocked and
placeholder flags, licence flags, preprint searches, document file counts and
digitization artifacts) are not model content. Bibliographic identifiers belong
in the catalog's discovery fields.

The check reads every symbol name of the selected archives (parameters,
definitions, states, covariates and outputs), the scenario names and
descriptions, and the generated model cards. Reviewed exceptions are listed in
``export_content_exceptions.json``; the replay token ``validation_run_nonce``
and run/replay tokens are refused in archive members, source snapshots, sidecars
and compressed result tables. Use --model ID for a focused authoring check.
"""
from __future__ import annotations

import argparse
import gzip
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXCEPTIONS = Path(__file__).with_name('export_content_exceptions.json')
RUNTIME = 'validation_run_nonce'
REPLAY = re.compile(r'(?i)validation[_ -]run[_ -]nonce|(?:run|replay)[_ -](?:nonce|token)|cache[_ -]buster')

NAME = re.compile(
    r'(?i)(^|_)('
    r'citation_rank|cited_by|citedby|queue|refined_rank|title_model_rank|priority_score'
    r'|pmid|pmcid|doi|fetched|fetch|blocked|cloudflare|recaptcha|captcha|placeholders?|paywall'
    r'|crossref|europepmc|pmc|jats|oup|springer|frontiers|mdpi|wiley|elsevier'
    r'|license|licence|cc_by|preprint|biorxiv|medrxiv|publication_year|paper_year|citation_year'
    r'|pdf|html|xml|docx|tgz|emf|eps|digitization|pixel|raster|quarantined'
    r'|page_start|page_end|page_count|pages_n|article_pages|figure_assets'
    r'|(supplement|supplementary_information|full_text|figure_images?)_(available|expected|found|count|pages|media'
    r'|links|indexed|tables|figures|binary)'
    r'|(main_)?(table|figure|figure_image|extracted_table)_count'
    r')(_|$)')
TEXT = re.compile(
    r'(?i)\b(citation rank|cited[- ]by count|queue (row|rank)|fetched|cloudflare|recaptcha|captcha'
    r'|proof-of-work|placeholder|source packet|source[- ]status|retrieval|route[- ]audit|source[- ]audit)\b')


def exceptions():
    value = json.loads(EXCEPTIONS.read_text())
    return {(e['model_id'], e['name']) for e in value['exceptions']}


def _names(record):
    for group in ('states', 'parameters', 'covariates', 'definitions', 'switches', 'outputs'):
        for row in record.get(group, []):
            yield group, row.get('source_name') or row['native_name']


def _scientific_names(model, equations):
    for group in ('states', 'parameters', 'covariates'):
        for name in model.get(group) or {}:
            yield group, name
    for group in ('definitions', 'derived_outputs'):
        for name in equations.get(group) or {}:
            yield group, name


def findings(library, *, allowed=None, model_ids=None):
    """(model_id, where, name) for every refused name or phrase; and runtime-token holders."""
    allowed = exceptions() if allowed is None else allowed
    refused, runtime = [], []
    rows = library.list_models()
    if model_ids is not None:
        requested = set(model_ids)
        unknown = requested - {r['id'] for r in rows}
        if not requested or unknown:
            raise ValueError('Select existing model ids: ' + ', '.join(sorted(unknown)))
        rows = [r for r in rows if r['id'] in requested]
    ids = {r['id'] for r in rows}
    sources = {}
    for source in library.list_source_models():
        mid = (source.get('omex') or {}).get('model_id')
        if mid in ids:
            sources.setdefault(mid, []).append(source)
    for row in rows:
        model = library.load(row['id'])
        archive = library.root / row['archive']
        record = library.parameter_metadata(row['id'])
        names = list(_names(record)) if record else []
        members = model.members
        if 'scientific/model.json' in members:
            scientific = json.loads(members['scientific/model.json'])
            equations = json.loads(members['scientific/equations.json'])
            names += list(_scientific_names(scientific, equations))
            for scenario in json.loads(members['scientific/scenarios.json']).get('scenarios', []):
                for field in ('id', 'name', 'description'):
                    text = str(scenario.get(field) or '')
                    if (field == 'id' and NAME.search(text.replace('-', '_'))) or TEXT.search(text):
                        if (row['id'], scenario['id']) not in allowed:
                            refused.append((row['id'], 'scenario ' + field, text))
        for source in sources.get(row['id'], []):
            documents = library.load_source_model(source['id'])
            names += list(_scientific_names(documents['model.json'], documents['equations.json']))
            for name, document in documents.items():
                if REPLAY.search(json.dumps(document)):
                    refused.append((row['id'], 'source ' + name, 'replay token'))
                    runtime.append(row['id'])
        seen = set()
        for where, name in names:
            if name in seen:
                continue
            seen.add(name)
            if REPLAY.search(name):
                runtime.append(row['id'])
                refused.append((row['id'], where, name))
            elif NAME.search(name) and (row['id'], name) not in allowed:
                refused.append((row['id'], where, name))
        revision = model.index.get('source_revision') or {}
        if set(revision) - {'source_version'}:
            refused.append((row['id'], 'source_revision', 'revision bookkeeping'))
        # Also inspect metadata and non-executable members, not just live symbols.
        for name, raw in members.items():
            if REPLAY.search(raw.decode('utf-8', 'replace')):
                refused.append((row['id'], name, RUNTIME))
                runtime.append(row['id'])
        card = archive.with_name('MODEL_CARD.md')
        if card.is_file():
            for match in TEXT.finditer(card.read_text()):
                if (row['id'], match.group(0).lower()) not in allowed:
                    refused.append((row['id'], 'MODEL_CARD.md', match.group(0)))
    selected = {str((library.root / r['archive']).parent.relative_to(library.root)) for r in rows}
    distributed = {str(p.relative_to(library.root)) for p in library.root.glob('models/*/*') if p.is_dir() and (model_ids is None or p.parent.name in ids)}
    for folder in sorted(distributed - selected):
        refused.append((folder, 'archive', 'unselected version'))
    for folder in selected:
        for asset in (library.root / folder).rglob('*'):
            if not asset.is_file():
                continue
            if asset.name.endswith('.csv.gz'):
                raw = gzip.decompress(asset.read_bytes())
            elif asset.suffix in ('.json', '.md', '.csv'):
                raw = asset.read_bytes()
            else:
                continue
            if REPLAY.search(raw.decode('utf-8', 'replace')):
                refused.append((folder, asset.name, 'replay token'))
                runtime.append(Path(folder).parts[1])
    return sorted(set(refused)), sorted(set(runtime))


def main():
    sys.path.insert(0, str(ROOT))
    from qspquest_models import Library
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--model', action='append', help='Check only this selected model; repeat for several models')
    args = parser.parse_args()
    refused, runtime = findings(Library(ROOT), model_ids=args.model)
    for model_id, where, name in refused:
        print(f'{model_id}: {where}: {name}')
    print(f'{len(refused)} refused; {len(runtime)} models still carry replay tokens')
    raise SystemExit(1 if refused else 0)


if __name__ == '__main__':
    main()
