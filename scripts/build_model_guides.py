#!/usr/bin/env python3
"""Build browsable guides from released metadata without rewriting any archive.

SOURCE_REFERENCE.md preserves the previous card. Edit scientific metadata at its
source; edit presentation here. Run from any directory after updating a release.
"""
from pathlib import Path
import json
import re
import zipfile
import sys
import hashlib

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from qspquest_models import Library, load_archive
from qspquest_models.availability import load_records, project_catalog, project_source_families


def read(path):
    return json.loads(path.read_text())


def cell(value):
    return str(value).replace('|', '\\|').replace('\n', ' ')


def output_identity_rows(native, model):
    """Keep returned native units and archive labels distinct in identity tables."""
    units = {row['name']: row['unit'] for row in model.get('outputs', [])}
    result = []
    for name, entry in native.get('outputs', {}).items():
        if entry.get('analyte') is None:
            continue
        target = entry['native_name']
        if target not in units:
            raise ValueError('Declared output identity names an uncomputed output: ' + name)
        result.append({'readout': name, 'analyte': entry['analyte'],
                       'compartment': entry.get('compartment'),
                       'returned_unit': units[target], 'source_label': entry.get('unit')})
    return result


SOURCE_FOOTER = '[Scientific scope and attribution](SOURCE_REFERENCE.md) · [Source details](SOURCE_REPRODUCTION.json) · [Stored result evidence](evidence.json) · [Archive format](../../../tutorials/model-format.md)'


def curated_footer(card):
    """Retain manually curated scientific guidance after the generated footer."""
    for footer in [SOURCE_FOOTER, SOURCE_FOOTER.replace('Stored result evidence', 'Archive qualification record')]:
        if footer in card:
            return card.split(footer, 1)[1].strip()
    return ''


def source_only_candidate(evidence, index):
    if evidence.get('schema') != 'qspquest.models.source-preparation-evidence/v1':
        return False
    if (evidence.get('model_id') != index['model_id']
            or evidence.get('model_version') != index['model_version']
            or evidence.get('cases') != []
            or evidence.get('current_engine_qualification') != 'not_assessed'
            or evidence.get('numerical_qualification_accepted') is not False):
        raise ValueError('Source-only candidate cannot carry a qualified or mismatched execution record')
    return True


def cli_example(current, ident, version, scenario):
    if not current:
        return ['Use the checksum-pinned Python archive command above for this version. The library CLI selects the current default archive.', '']
    return ['The CLI uses the same selection (`--all-readouts` exports the complete table):', '', '```sh',
            f'python -m qspquest_models --library . --model {ident} --model-version {version} --scenario {scenario} --csv model-example-cli.csv', '```', '']


def reader_order(lines):
    """Put the runnable workflow first and retain audit details after its limits."""
    introduction, sections = [], []
    for line in lines:
        if line.startswith('## '):
            sections.append((line, [line]))
        elif sections:
            sections[-1][1].append(line)
        else:
            introduction.append(line)
    first = ['## Run an experiment', '## Inputs and outputs', '## Interpretation and limits']
    ordered = [section for title in first for heading, section in sections if heading == title]
    ordered += [section for heading, section in sections if heading not in first]
    for section in ordered:
        if section[0] in ('## Availability and qualification', '## Output identities'):
            title = section[0].removeprefix('## ')
            introduction += ['<details>', f'<summary>{title}</summary>', ''] + section[1:] + ['</details>', '']
        else:
            introduction += section
    return introduction


def topic(ident):
    if any(x in ident for x in ['diffdose', 'ubi_']):
        return 'Learning and synthetic mechanisms'
    if 'aav' in ident:
        return 'Gene delivery and antibody distribution'
    if any(x in ident for x in ['adalimumab', 'infliximab', 'vedolizumab', 'ustekinumab', 'risankizumab', 'secukinumab', 'certolizumab', 'dupilumab', 'dazukibart']):
        return 'Inflammation, skin and bowel disease'
    if any(x in ident for x in ['rituximab', 'erenumab', 'alemtuzumab', 'crenezumab', 'autotac', 'ravulizumab', 'gmg']):
        return 'Neurology and immune-cell dynamics'
    if any(x in ident for x in ['adc', 'vedotin', 'loncastuximab', 'inotuzumab', 'imgn529', 'skb264', 'aide']):
        return 'Antibody–drug conjugates and immunotoxins'
    if any(x in ident for x in ['nivolumab', 'atezolizumab', 'cemiplimab', 'envafolimab', 'bevacizumab', 'panitumumab', 'ramucirumab', 'pertuzumab', 'daratumumab', 'elranatamab', 'cd3x', 'crs', 'zenocutuzumab', 'protac']):
        return 'Oncology, binding and immune mechanisms'
    return 'Other pharmacology and protein distribution'



def build():
    records = load_records(ROOT / 'qspquest_models/availability.json')
    catalog = project_catalog(read(ROOT / 'catalog.json'), records)
    # Verify all versioned records before replacing the generated catalog.
    for record in records.values():
        archive = ROOT / 'models' / record.model_id / record.archive_version / 'model.omex'
        load_archive(archive, expected_sha256=record.archive_sha256, availability_record=record)
        if record.evidence_id != 'sha256:' + hashlib.sha256(archive.with_name('evidence.json').read_bytes()).hexdigest():
            raise ValueError('Availability evidence digest mismatch: ' + record.model_id)
    for row in catalog['models']:
        reproduction = read((ROOT / row['archive']).with_name('SOURCE_REPRODUCTION.json'))
        interpretation = reproduction.get('source_interpretations')
        if interpretation is not None:
            from qspquest_models import _source_interpretations
            row['source_interpretations'] = _source_interpretations(interpretation, row['id'], row['version'], row['omex_sha256'])
            row['limitations'] = 'Lymph binding uses local lymph coordinates rather than the plasma coordinates printed in supplementary equations 134-136 (page 32). This disclosed source interpretation is archive-bound in source_interpretations; author-code and physical-unit qualification remain open.'
        else:
            row.pop('source_interpretations', None)
        barrier = reproduction.get("barrier_parameters")
        if barrier:
            row["parameter_effects"] = barrier["parameters"]
            row["limitations"] = row.get("limitations", "") + " " + barrier["description"] + " " + barrier["limits"]
    source_catalog = project_source_families(read(ROOT / 'source-catalog.json'), catalog)
    (ROOT / 'catalog.json').write_text(json.dumps(catalog, indent=2) + '\n')
    (ROOT / 'source-catalog.json').write_text(json.dumps(source_catalog, indent=2) + '\n')
    library = Library(ROOT)
    selected = {row['id']: row for row in library.list_models()}
    cohort = library.availability_counts
    sources = {}
    source_by_id = {}
    for row in read(ROOT / 'source-catalog.json')['models']:
        omex = row.get('omex')
        if omex:
            sources[omex['archive']] = row
            source_by_id[omex['model_id']] = row
    summaries = read(ROOT / 'scripts/model_summaries.json')
    profiles = read(ROOT / 'qspquest_models/user_guides.json')
    listing = []
    for archive in sorted(ROOT.glob('models/*/*/model.omex')):
        folder = archive.parent
        preserved = curated_footer((folder / 'MODEL_CARD.md').read_text()) if (folder / 'MODEL_CARD.md').exists() else ''
        relative = archive.relative_to(ROOT).as_posix()
        with zipfile.ZipFile(archive) as z:
            index = json.loads(z.read('index.json'))
            native = index['native_execution']
            model = json.loads(z.read(native['model'])) if native.get('model') else {}
            requests = {sid: json.loads(z.read(path)) for sid, path in native['scenarios'].items()}
            scientific = {name: json.loads(z.read('scientific/' + name)) for name in ['model.json', 'equations.json', 'scenarios.json'] if 'scientific/' + name in z.namelist()}
            fitting = json.loads(z.read('fitting.json')) if 'fitting.json' in z.namelist() else {}
        ident, version = index['model_id'], index['model_version']
        source_only = source_only_candidate(read(folder / 'evidence.json'), index)
        row = selected[ident]
        availability = library.availability_records[ident + '/' + version]
        profile = {**profiles[ident + '/' + version], 'availability': availability.availability}
        assert profile['archive_sha256'] == read(folder / 'evidence.json')['omex_sha256'], 'stale guide archive pin'
        assert profile['starter'] in requests or not requests, (ident, version)
        source = sources.get(relative, {})
        if not source and scientific and ident in source_by_id:
            alternate = source_by_id[ident]
            if all(name in alternate.get('files', {}) for name in scientific):
                for name, value in scientific.items():
                    descriptor = alternate['files'][name]
                    path = ROOT / descriptor['path']
                    if hashlib.sha256(path.read_bytes()).hexdigest() != descriptor['sha256'] or read(path) != value:
                        raise ValueError('Alternate archive source context differs from its exact scientific documents')
                source = alternate
        source_model = read(ROOT / source['files']['model.json']['path']) if source else {}
        experiments = read(ROOT / source['files']['scenarios.json']['path']).get('scenarios', []) if source else []
        experiments = {s['id']: s for s in experiments}
        title = source_model.get('name') or row['name']
        description = source_model.get('description') or row.get('description') or model.get('description', '')
        reference = folder / 'SOURCE_REFERENCE.md'
        if not reference.exists():
            reference.write_text((folder / 'MODEL_CARD.md').read_text())
        reproduction = read(folder / 'SOURCE_REPRODUCTION.json')
        scenarios = list(requests)
        held = index.get('unavailable_scenario_ids', [])
        current = relative == row['archive']
        status = f'Runnable · {len(scenarios)} experiment' + ('s' if len(scenarios) != 1 else '') if scenarios else 'Inspection only · simulation unavailable'
        if profile['availability'] == 'source_replay':
            status = 'Source replay available; dynamic simulation unavailable'
        if held and scenarios:
            status += f' · {len(held)} unavailable'
        lines = [f'# {title}', '', '[Browse models](../../../MODEL_CATALOG.md) · [Setup](../../../README.md#setup) · [Python](../../../tutorials/python-quickstart.md) · [R](../../../tutorials/r-quickstart.md)', '', summaries[ident], '', f'**{status}.** Version {version}.', '']
        if not current:
            lines += [f'This is an alternate version. [Open the default version](../{row["version"]}/MODEL_CARD.md) for the standard quickstart.', '']
        lines += ['## Availability and qualification', '',
                  f'Execution: `{availability.availability}`. Publication review: `{availability.publication_review}`.',
                  f'Units: `{availability.unit_status}`. Current-engine qualification: `{availability.current_engine_qualification}`.',
                  f'Supported operations: {", ".join(availability.supported_operations)}.',
                  f'Fitting supported: `{str(availability.fitting_supported).lower()}`; fit ready: `{str(availability.fit_ready).lower()}`.',
                  f'Evidence identity: `{availability.evidence_id}`.', '',
                  'A runnable preset describes available execution. Stored evidence does not establish qualification for a different engine build.', '',
                  '## What you can explore', '']
        if current and availability.fit_ready:
            workflow = fitting['workflows'][0]['id']
            location = lines.index('## What you can explore')
            lines[location:location] = [
                '## Synthetic parameter recovery', '',
                'Complete the [fitting prerequisites](../../../tutorials/library-fitting.md#prerequisites-and-discovery) with the matching QSPQuest Python binding. The archive fixes synthetic observations, residual errors, parameter bounds, solver and convergence controls for each workflow.', '',
                '```python', 'from qspquest_models import Library',
                f"model = Library('.').load('{ident}', version='{version}')",
                "print([(w['id'], w['operation']) for w in model.fitting_workflows])",
                f"fit = model.fit_workflow('{workflow}')",
                "assert fit['checks']['passed'], fit['checks']", "print(fit['checks']['parameters'])", '```', '',
                'A successful fixture reports converged parameter recovery within its declared absolute limits. Retain the complete native result and diagnostics. A budget-limited or nonconverged result has failed checks; inspect those diagnostics before interpreting estimates.', '',
                'The six workflows cover three parameter starters under BDF and Rodas5P. Their scope is the exact archived synthetic recovery case. Source population reproduction, uncertainty coverage and clinical qualification require separate evidence.', '',
            ]
        if current and row.get('source_family'):
            family = row['source_family']
            canonical = family['canonical_model']
            family_members = next(f['members'] for f in catalog['source_families'] if f['family_id'] == family['family_id'])
            related = ', '.join(f"[{m['model_id']}](../../../models/{m['model_id']}/{m['version']}/MODEL_CARD.md) (`{m['model_fidelity']}`, `{m['version']}`)" for m in family_members)
            location = lines.index('## What you can explore')
            lines[location:location] = ['## Related representations', '', f"Declared representation: `{row['model_fidelity']}`. Source family: `{family['family_id']}`; paper: `{family['paper_id']}`.",
                f"Canonical full representation: [{canonical['model_id']}](../../../models/{canonical['model_id']}/{canonical['version']}/MODEL_CARD.md), version `{canonical['version']}`.",
                f'Related representations: {related}.',
                'This relationship does not establish physical units, publication reproduction or current-engine qualification.', '']
        questions = list(dict.fromkeys(q for sid in scenarios for q in experiments.get(sid, {}).get('scientific_questions', [])))
        if questions:
            lines += [f'- {q}' for q in questions[:6]] + ['']
        else:
            lines += [description, '']
        if reproduction.get('scenario_initialization'):
            contract = reproduction['scenario_initialization']
            lines += ['## Serotype initialization', '', contract['description'], '', contract['limitation'], '', contract['scope'], '']
        if reproduction.get('source_interpretations'):
            interpretation = reproduction['source_interpretations']
            lines += ['## Source equation interpretations', '', f"Archive SHA-256: `{interpretation['archive_sha256']}`. Coverage: selected disclosed choices; complete source qualification remains open.", '']
            for entry in interpretation['entries']:
                lines += [entry['source_locator'], '', entry['rationale'], '',
                          'Printed coordinates: ' + ', '.join(f'`{n}`' for n in entry['printed_coordinates']) + '.',
                          'Adopted coordinates: ' + ', '.join(f'`{n}`' for n in entry['adopted_coordinates']) + '.', '',
                          entry['conservation_implications'], '', entry['qualification_limits'], '']
        if reproduction.get("barrier_parameters"):
            barrier = reproduction["barrier_parameters"]
            lines += ["## Barrier inputs", "", barrier["description"], "", barrier["source_locator"], "", barrier["limits"], "", barrier["migration"], ""]
        if native.get('output_semantics'):
            semantics = native['output_semantics']
            lines += ['## Output identities', '', semantics['scope'], '',
                      semantics['unit_scope'], '', semantics['source_locator'], '',
                      '| Readout | Analyte identifier | Compartment identifier | Returned native unit | Archive source label |',
                      '| --- | --- | --- | --- | --- |']
            for identity in output_identity_rows(native, model):
                compartment = identity['compartment'] or 'undeclared'
                source_label = identity['source_label'] or 'undeclared'
                lines += [f"| `{cell(identity['readout'])}` | `{cell(identity['analyte'])}` | `{cell(compartment)}` | `{cell(identity['returned_unit'])}` | `{cell(source_label)}` |"]
            lines += ['', 'Inspect the same declarations using `model.output_semantics`. An undeclared identity is `None`; it is not inferred from the readout name.', '']
        if scenarios:
            first = profile['starter']
            lines += ['## Run an experiment', '', experiments.get(first, {}).get('description', ''), '', 'Complete [setup](../../../README.md#setup), then run this Python code from the library checkout:', '', '```python']
            if current:
                lines += ['from qspquest_models import Library', '', f"model = Library('.').load('{ident}', version='{version}')"]
            else:
                digest = read(folder / 'evidence.json')['omex_sha256']
                lines += ['from qspquest_models import load_archive', '', 'model = load_archive(', f"    '{relative}',", f"    expected_sha256='{digest}',", ')']
            lines += [f"result = model.run('{first}')", "model.write_csv(result, 'model-example-python.csv')", "print(len(result['times']), 'rows')", '```', '', '### Choose an experiment', '', 'A preset is a named experiment with fixed inputs. Summary/table replays expose retained', 'values; they are not new parameter fits or necessarily a changing biological trajectory.', '', '| Experiment ID (pass to `model.run`) | Purpose | Time range | Rows |', '| --- | --- | --- | ---: |']
            if len(scenarios) > 12:
                lines[-2:-2] = ['<details>', f'<summary>Browse all {len(scenarios)} runnable experiments</summary>', '']
            for sid, req in requests.items():
                exp = experiments.get(sid, {})
                label = exp.get('description') or exp.get('name') or sid.replace('_', ' ').replace('-', ' ').capitalize()
                regimen = req['regimen']
                start, end = regimen['start'], regimen['end']
                lines += [f"| `{sid}` | {cell(label)} | {start['value']:g}–{end['value']:g} {end['unit']} | {len(regimen['observations'])} |"]
            if len(scenarios) > 12:
                lines += ['', '</details>']
            req = requests[first]
            lines += ['', '## Inputs and outputs', '', 'Each experiment supplies the parameters, initial state, dosing schedule and sampling times.', '[Compare presets or change an input](../../../tutorials/change-inputs.md) when exploring another condition.', '', '`model-example-python.csv` contains `time`, `side` and the primary readouts below. `side` distinguishes', 'samples before (`pre`) and after (`post`) a dosing or other discrete event.', 'State columns use `state__`; retained constant source values use `source__`.', '', '| Primary column | Meaning | Archive unit label |', '| --- | --- | --- |']
            source_parameters = source_model.get('parameters', {})
            for output in profile['readouts']:
                kind, name = output['kind'], output['name']
                prefix = {'output': '', 'state': 'state__', 'source_parameter': 'source__'}[kind]
                unit = source_parameters[name]['unit'] if kind == 'source_parameter' else native[{'output': 'outputs', 'state': 'states'}[kind]][name]['unit']
                lines += [f"| `{prefix}{name}` | {cell(output['meaning'])} | `{unit}` |"]
            if profile['availability'] == 'source_replay':
                lines += ['', '**This starter is a source replay.** Its retained values are constant or short source checks.', 'No qualified dynamic simulation is available in this version. Zero drug states do not demonstrate a treatment response.']
            lines += ['', 'Python exports this small table by default. To export every output and biological state:', '', '```python', "model.write_csv(result, 'technical-trajectory.csv', all_readouts=True)", '```', '', *cli_example(current, ident, version, first), 'In R, `qspquest_data_frame(result)` returns the same primary columns.', 'Use `qspquest_data_frame(result, all_readouts = TRUE)` for the complete table.', '[R setup and examples](../../../tutorials/r-quickstart.md).', '', '<details>', f"<summary>Technical inventory: {len(native['outputs'])} outputs and {len(native['states'])} states</summary>", '', '| Technical column | Archive unit label |', '| --- | --- |']
            for kind, prefix in [('outputs', ''), ('states', 'state__')]:
                lines += [f"| `{prefix}{name}` | `{out['unit']}` |" for name, out in native[kind].items()]
            lines += ['', '</details>', '', 'The names retain the source conventions. A unit label of `1` means this execution profile', 'uses numerical source values; a unit-looking column name alone does not establish physical units.', '[How to interpret outputs](../../../tutorials/understand-results.md) explains this distinction.', '']
            preview_path = folder / 'starter-preview.json'
            if source_only:
                if preview_path.exists():
                    raise ValueError('Source-only candidate cannot reuse a numerical starter preview')
                lines += ['### Result qualification', '',
                          'No numerical reference is recorded for this archive version. The complete JSON retains its archive digest, model/request identity, time/side grid, output units and qualification scope.',
                          'Inspect those fields before interpreting a result; reproducible execution availability does not establish physical, biological, fitting or clinical qualification.', '']
            elif preview_path.exists():
                preview = read(preview_path)
                assert preview['scenario_id'] == first and preview['archive_sha256'] == read(folder / 'evidence.json')['omex_sha256']
                expected_names = [({'output': '', 'state': 'state__', 'source_parameter': 'source__'}[r['kind']] + r['name']) for r in profile['readouts']]
                assert [c['name'] for c in preview['columns']] == expected_names
                lines += ['### Check your result', '', f"The `{first}` starter has **{preview['rows']} rows**. Reference checkpoints:", '', '| Column | First row | Minimum (time, side) | Maximum (time, side) | Last row |', '| --- | ---: | --- | --- | ---: |']
                for column in preview['columns']:
                    low = f"{column['minimum']:.6g} ({column['minimum_time']:g} {preview['time_unit']}, {column['minimum_side']})"
                    high = f"{column['maximum']:.6g} ({column['maximum_time']:g} {preview['time_unit']}, {column['maximum_side']})"
                    lines += [f"| `{column['name']}` | {column['first']:.6g} | {low} | {high} | {column['last']:.6g} |"]
                lines += ['', 'These rounded values identify the expected trajectory; they are not numerical acceptance tolerances.', '[Starter reference and engine identity](starter-preview.json) records a fresh execution of the pinned archive.', 'The original stored CSV may omit states; the starter reference includes the primary readouts above.', '[Read the original stored result without installing the engine](../../../tutorials/understand-results.md#read-a-stored-result).', '']
            else:
                raise ValueError(f'Missing starter preview for {ident}; run scripts/validate_starters.py --write-previews')
        else:
            lines += ['No experiments in this version can currently run through the library loader.', 'The source files are available for inspection, but a simulation command would fail.', '', '[Choose a runnable model](../../../MODEL_CATALOG.md) or inspect the', '[unavailable experiment details](INTERCHANGE_AND_EXECUTION_HOLDS.json).', '']
        unit_limit = ('Only the PK dose and concentration coordinates described above carry explicit physical units. Other coordinates and complete model dimensions remain unqualified.' if native.get('dose_contracts') else 'Physical units have not been independently checked for this execution profile.')
        lines += ['## Interpretation and limits', '', 'These examples use fixed inputs. They do not perform population fitting or support clinical dosing decisions.', unit_limit, '']
        guards = list(dict.fromkeys(g for sid in scenarios for g in experiments.get(sid, {}).get('interpretation_guardrails', [])))
        lines += [f'- {g}' for g in guards[:6]]
        if len(guards) > 6:
            lines += ['', '<details>', '<summary>Additional experiment-specific interpretation notes</summary>', ''] + [f'- {g}' for g in guards[6:]] + ['', '</details>']
        for key in ['unit_scope', 'reproduced']:
            if reproduction.get(key):
                lines += ['', str(reproduction[key])]
        omitted = reproduction.get('not_reproduced', [])
        if omitted:
            lines += ['', 'Outside this version’s scope:', ''] + [f'- {x}' for x in omitted]
        if held:
            lines += ['', f'**{len(held)} experiments are unavailable for simulation.** See the [hold details](INTERCHANGE_AND_EXECUTION_HOLDS.json).']
        footer = SOURCE_FOOTER.replace('Stored result evidence', 'Archive qualification record') if source_only else SOURCE_FOOTER
        lines += ['', '## Sources and technical reference', '', footer, '']
        if preserved:
            lines += [preserved, '']
        (folder / 'MODEL_CARD.md').write_text(re.sub(r'\n{3,}', '\n\n', '\n'.join(reader_order(lines))))
        if current:
            listing.append((topic(ident), title, folder.relative_to(ROOT).as_posix(), summaries[ident], status))
    lines = ['# Choose a model', '', '[Start here](README.md) · [Python](tutorials/python-quickstart.md) · [R](tutorials/r-quickstart.md) · [Understand results](tutorials/understand-results.md)', '', f"Browse {cohort['selected_model_identities']} selected model identities below, grouped by topic. Use your browser’s Find command to search for a drug,", 'disease or mechanism. Each model guide lists its experiments, outputs and runnable status.', f"{cohort['selected_availability'].get('dynamic', 0)} selected identities offer dynamic starters; {cohort['selected_availability'].get('source_replay', 0)} offer source replays; {cohort['selected_availability'].get('inspection_only', 0)} are inspection only.", f"The archive inventory contains {cohort['versioned_archives']} versions; selected versions provide {cohort['selected_preset_requests']} preset requests and {cohort['selected_fit_ready']} fit-ready models.", '', '## Good places to start', '', '| Your question | Start with |', '| --- | --- |', f'| How do I run and plot a published PK/PD model? | [Rituximab and B-cell dynamics](models/qspquest_serkland_2025_rituximab_ms_pkpd/{selected["qspquest_serkland_2025_rituximab_ms_pkpd"]["version"]}/MODEL_CARD.md) |', '| How does local gating affect tumor versus systemic occupancy? | [Target-gated cargo walkthrough](tutorials/qsp-gated-cargo.md) |', '| How does exposure change biomarker turnover? | [Small turnover benchmark](models/qspquest_diffdose_2026_idr_benchmark/0.1.0/MODEL_CARD.md) |', '', 'PK describes drug exposure, PD describes drug effects, PBPK describes distribution through', 'physiological compartments, and QSP describes interacting biological mechanisms.', 'PopPK in a model name describes its source; these library examples run fixed parameters, not population fits.', '', '## Browse by topic', '']
    categories = sorted({entry[0] for entry in listing})
    for category in categories:
        anchor = re.sub(r'[^\w\s-]', '', category.lower()).replace(' ', '-')
        lines += [f'- [{category}](#{anchor})']
    for category in categories:
        lines += ['', f'## {category}', '', '| Model | What it describes | Availability |', '| --- | --- | --- |']
        for _, title, path, description, status in sorted(x for x in listing if x[0] == category):
            lines += [f'| [{cell(title)}]({path}/MODEL_CARD.md) | {cell(description)} | {status} |']
    lines += ['', '## Search from the terminal', '', '```sh', 'python -m qspquest_models --library . --search rituximab --runnable', '```', '', 'Use `--format json` for machine-readable discovery. [Technical reference](tutorials/model-format.md)', 'covers version selection and the underlying archive catalogs.', '']
    (ROOT / 'MODEL_CATALOG.md').write_text('\n'.join(lines))
    readme = ROOT / 'README.md'
    text = readme.read_text()
    start = text.index('The library contains ')
    end = text.index('\n\n## Setup', start)
    summary = (f"The library contains {cohort['selected_model_identities']} selected model identities: "
               f"{cohort['selected_availability'].get('dynamic', 0)} offer dynamic starters, "
               f"{cohort['selected_availability'].get('source_replay', 0)} offer source replays and "
               f"{cohort['selected_availability'].get('inspection_only', 0)} are inspection only.\n"
               f"Its {cohort['versioned_archives']} archived versions provide "
               f"{cohort['selected_preset_requests']} selected preset requests and "
               f"{cohort['selected_fit_ready']} fit-ready models.\n"
               "Counts describe execution availability. Physical units and current-engine scientific qualification\n"
               "remain separate; these examples use fixed parameters and do not support clinical dose selection.")
    readme.write_text(text[:start] + summary + text[end:])
    print(f'Wrote {len(listing)} catalog entries and {len(library.availability_records)} model guides.')


if __name__ == '__main__':
    build()
