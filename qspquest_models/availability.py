"""Versioned model availability, independent of numerical execution evidence."""
from __future__ import annotations
from collections import Counter
from dataclasses import asdict, dataclass
import json
from pathlib import Path
import re

SCHEMA = 'qspquest.model-availability/v1'


@dataclass(frozen=True)
class Availability:
    model_id: str
    archive_version: str
    selected_version: str
    archive_sha256: str
    availability: str
    publication_review: str
    preset_ids: tuple[str, ...]
    unit_status: str
    fitting_supported: bool
    fit_ready: bool
    evidence_id: str
    current_engine_qualification: str

    @classmethod
    def parse(cls, value):
        if not isinstance(value, dict) or set(value) != set(cls.__dataclass_fields__):
            raise ValueError('Availability record has missing or unknown fields')
        strings = set(cls.__dataclass_fields__) - {'preset_ids', 'fitting_supported', 'fit_ready'}
        if any(not isinstance(value[key], str) or not value[key] for key in strings):
            raise ValueError('Availability identity and status fields must be nonempty strings')
        ids = value['preset_ids']
        if not isinstance(ids, list) or any(not isinstance(s, str) or not s for s in ids) or ids != sorted(set(ids)):
            raise ValueError('Availability preset IDs must be sorted unique strings')
        if any(type(value[key]) is not bool for key in ('fitting_supported', 'fit_ready')):
            raise ValueError('Availability fitting flags must be boolean')
        if not re.fullmatch('[0-9a-f]{64}', value['archive_sha256']) or not re.fullmatch('sha256:[0-9a-f]{64}', value['evidence_id']):
            raise ValueError('Availability requires SHA-256 archive and evidence identities')
        if value['availability'] not in ('dynamic', 'source_replay', 'inspection_only'):
            raise ValueError('Unsupported availability class')
        if value['publication_review'] not in ('pending', 'unrecorded', 'approved'):
            raise ValueError('Unsupported publication review state')
        if value['unit_status'] not in ('physically_qualified', 'source_scale_unqualified', 'unqualified'):
            raise ValueError('Unsupported unit status')
        # Qualification requires an engine/operation-specific receipt, not an archive label.
        if value['current_engine_qualification'] != 'not_assessed':
            raise ValueError('Archive availability cannot assert current-engine qualification')
        if (value['availability'] == 'inspection_only') != (not ids):
            raise ValueError('Availability class contradicts preset execution')
        if value['fit_ready'] and not value['fitting_supported']:
            raise ValueError('Fit readiness requires fitting support')
        if value['fitting_supported'] and value['availability'] != 'dynamic':
            raise ValueError('Fitting requires a dynamic execution contract')
        return cls(**{**value, 'preset_ids': tuple(ids)})

    @property
    def selected(self):
        return self.archive_version == self.selected_version

    @property
    def supported_operations(self):
        operations = ['inspect']
        if self.availability != 'inspection_only':
            operations.append('run_preset')
        if self.availability == 'dynamic':
            operations.append('exploratory_simulation')
        if self.fitting_supported:
            operations.append('fit')
        return operations

    @property
    def blockers(self):
        values = ['current_engine_qualification_not_assessed']
        if self.publication_review != 'approved':
            values.append('publication_review_' + self.publication_review)
        if self.unit_status != 'physically_qualified':
            values.append('physical_units_not_qualified')
        if not self.fitting_supported:
            values.append('fitting_not_supported')
        if self.availability == 'inspection_only':
            values.append('simulation_unavailable')
        if self.availability == 'source_replay':
            values.append('dynamic_simulation_not_qualified')
        return values

    def describe(self):
        return {**asdict(self), 'preset_ids': list(self.preset_ids), 'schema': SCHEMA,
                'selected': self.selected, 'supported_operations': self.supported_operations,
                'blockers': self.blockers}

    def verify_archive(self, index, digest, fitting):
        native = index['native_execution']
        if (index['model_id'], index['model_version'], digest) != (self.model_id, self.archive_version, self.archive_sha256):
            raise ValueError('Availability identity or archive digest mismatch')
        if tuple(sorted(native['scenarios'])) != self.preset_ids:
            raise ValueError('Availability preset inventory differs from archive')
        if (not native.get('model')) != (self.availability == 'inspection_only'):
            raise ValueError('Availability execution differs from native model')
        unit = ('physically_qualified' if native.get('dimensional_qualification') is True else
                'source_scale_unqualified' if native.get('coordinates') == 'unchanged_source_numeric_values' else 'unqualified')
        if unit != self.unit_status:
            raise ValueError('Availability unit status differs from archive')
        flags = (fitting.get('fitting_supported', False), fitting.get('fit_ready', False))
        if any(type(flag) is not bool for flag in flags) or flags != (self.fitting_supported, self.fit_ready):
            raise ValueError('Availability fitting flags differ from archive contract')


def load_records(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate availability key: ' + key)
            result[key] = value
        return result
    data = json.loads(Path(path).read_bytes(), object_pairs_hook=unique)
    if set(data) != {'schema', 'records'} or data['schema'] != SCHEMA or not isinstance(data['records'], dict):
        raise ValueError('Unsupported availability registry')
    records = {key: Availability.parse(value) for key, value in data['records'].items()}
    for key, record in records.items():
        if key != record.model_id + '/' + record.archive_version:
            raise ValueError('Availability key differs from model/version')
    return records



SOURCE_FAMILY_SCHEMA = 'qspquest.source-families/v1'


def _bounded(value, maximum):
    return (isinstance(value, str) and bool(value.strip())
            and len(value.encode('utf-8')) <= maximum
            and not any(ord(c) < 32 or 127 <= ord(c) <= 159 for c in value))


@dataclass(frozen=True)
class FamilyMember:
    model_id: str
    version: str
    archive_sha256: str
    model_fidelity: str

    @classmethod
    def parse(cls, value):
        if not isinstance(value, dict) or set(value) != set(cls.__dataclass_fields__):
            raise ValueError('Source-family member has missing or unknown fields')
        if not all(_bounded(value[k], 128) for k in ('model_id', 'version')):
            raise ValueError('Source-family member needs bounded model/version identifiers')
        if not isinstance(value['archive_sha256'], str) or not re.fullmatch('[0-9a-f]{64}', value['archive_sha256']):
            raise ValueError('Source-family member requires an archive SHA-256 pin')
        if value['model_fidelity'] not in ('full', 'reduced', 'synthetic', 'unrecorded'):
            raise ValueError('Unsupported declared model fidelity')
        return cls(**value)


@dataclass(frozen=True)
class SourceFamily:
    family_id: str
    paper_id: str
    canonical_model: tuple[str, str]
    members: tuple[FamilyMember, ...]

    @classmethod
    def parse(cls, value, records):
        if not isinstance(value, dict) or set(value) != set(cls.__dataclass_fields__):
            raise ValueError('Source family has missing or unknown fields')
        if not _bounded(value['family_id'], 128) or not _bounded(value['paper_id'], 512):
            raise ValueError('Source family needs bounded family/paper identifiers')
        canonical = value['canonical_model']
        if (not isinstance(canonical, dict) or set(canonical) != {'model_id', 'version'}
                or not all(_bounded(canonical[k], 128) for k in ('model_id', 'version'))):
            raise ValueError('Source family needs an exact canonical model/version')
        if not isinstance(value['members'], list) or not 1 <= len(value['members']) <= 32:
            raise ValueError('Source family needs between one and 32 declared members')
        members = tuple(FamilyMember.parse(v) for v in value['members'])
        refs = [(m.model_id, m.version) for m in members]
        if len(set(refs)) != len(refs):
            raise ValueError('Source-family model/version members must be unique')
        for member in members:
            record = records.get(member.model_id + '/' + member.version)
            if not record or not record.selected or record.archive_sha256 != member.archive_sha256:
                raise ValueError('Source-family member pin differs from selected archive: ' + member.model_id)
        canonical_ref = (canonical['model_id'], canonical['version'])
        full = [m for m in members if (m.model_id, m.version) == canonical_ref and m.model_fidelity == 'full']
        if len(full) != 1 or records[full[0].model_id + '/' + full[0].version].availability == 'inspection_only':
            raise ValueError('Canonical source-family reference must resolve to one executable full member')
        return cls(value['family_id'], value['paper_id'], canonical_ref, members)

    @property
    def declaration(self):
        return {'family_id': self.family_id, 'paper_id': self.paper_id,
                'canonical_model': {'model_id': self.canonical_model[0], 'version': self.canonical_model[1]}}


def family_projections(catalog, records):
    """Validate explicit pinned relationships; absent declarations remain unrecorded."""
    if 'source_families' not in catalog and 'source_family_schema' not in catalog:
        return {}
    if (catalog.get('source_family_schema') != SOURCE_FAMILY_SCHEMA
            or not isinstance(catalog.get('source_families'), list)):
        raise ValueError('Unsupported source-family registry')
    projected, identifiers = {}, set()
    for value in catalog['source_families']:
        family = SourceFamily.parse(value, records)
        if family.family_id in identifiers:
            raise ValueError('Duplicate source-family identifier')
        identifiers.add(family.family_id)
        for member in family.members:
            if member.model_id in projected:
                raise ValueError('A selected model may belong to only one declared source family')
            projected[member.model_id] = {'source_family': family.declaration,
                                          'model_fidelity': member.model_fidelity}
    return projected


def project_source_families(source_catalog, catalog):
    """Generate source-record relationships from their exact selected OMEX identity."""
    if (not isinstance(source_catalog, dict) or not isinstance(source_catalog.get('models'), list)
            or any(not isinstance(row, dict) for row in source_catalog['models'])):
        raise ValueError('Source catalog needs a models array of records')
    selected = {(r['id'], r['version']): r for r in catalog['models']}
    result = {**source_catalog, 'models': []}
    for row in source_catalog['models']:
        result_row = {k: v for k, v in row.items() if k not in ('source_family', 'model_fidelity')}
        omex = row.get('omex')
        if omex is None:
            omex = {}
        if not isinstance(omex, dict):
            raise ValueError('Source OMEX descriptor must be an object or null')
        target = selected.get((omex.get('model_id'), omex.get('version')))
        if target and target.get('source_family'):
            if omex.get('omex_sha256') != target['omex_sha256']:
                raise ValueError('Source record archive digest differs from family member')
            result_row.update({k: target[k] for k in ('source_family', 'model_fidelity')})
        result['models'].append(result_row)
    return result


def verify_source_families(source_catalog, catalog):
    if project_source_families(source_catalog, catalog) != source_catalog:
        raise ValueError('Source catalog family fields differ from the exact selected archive')


def project_catalog(catalog, records):
    """Generate availability fields while retaining descriptive catalog metadata."""
    selected = {r.model_id: r for r in records.values() if r.selected}
    if len(selected) != len(catalog['models']) or set(selected) != {row['id'] for row in catalog['models']}:
        raise ValueError('Availability and descriptive catalog identities differ')
    result = {**catalog, 'availability_schema': SCHEMA, 'models': []}
    for row in catalog['models']:
        record = selected[row['id']]
        presets = row['scenario_ids'] if set(row['scenario_ids']) == set(record.preset_ids) and len(row['scenario_ids']) == len(record.preset_ids) else list(record.preset_ids)
        result['models'].append({**row, 'version': record.archive_version,
            'archive': f'models/{record.model_id}/{record.archive_version}/model.omex',
            'omex_sha256': record.archive_sha256, 'scenario_ids': presets,
            'publication_status': record.publication_review,
            'fitting_supported': record.fitting_supported, 'fit_ready': record.fit_ready})
    families = family_projections(result, records)
    for row in result['models']:
        if row['id'] in families:
            row.update(families[row['id']])
        elif 'source_family' in row:
            raise ValueError('Catalog family declaration has no authoritative registry member')
    verify_catalog(result, records)
    return result

def verify_catalog(catalog, records):
    families = family_projections(catalog, records)
    rows = catalog['models']
    selected = [r for r in records.values() if r.selected]
    if len({row['id'] for row in rows}) != len(rows) or len(selected) != len(rows):
        raise ValueError('Availability selected identity inventory differs from catalog')
    for row in rows:
        record = records.get(row['id'] + '/' + row['version'])
        if not record or not record.selected or record.archive_sha256 != row['omex_sha256']:
            raise ValueError('Catalog selected version or digest differs from availability')
        if sorted(row['scenario_ids']) != list(record.preset_ids) or len(set(row['scenario_ids'])) != len(row['scenario_ids']):
            raise ValueError('Catalog preset inventory differs from availability')
        if any(type(row.get(key)) is not bool or row[key] != getattr(record, key) for key in ('fitting_supported', 'fit_ready')):
            raise ValueError('Catalog fitting flags differ from availability')
        if row.get('publication_status') != record.publication_review:
            raise ValueError('Catalog publication review differs from availability')
        expected_family = families.get(row['id'])
        if expected_family:
            if any(row.get(k) != v for k, v in expected_family.items()):
                raise ValueError('Catalog source-family fields differ from the pinned registry')
        elif 'source_family' in row:
            raise ValueError('Catalog source-family declaration is unrecorded in the registry')
        if 'model_fidelity' in row and row['model_fidelity'] not in ('full', 'reduced', 'synthetic', 'unrecorded'):
            raise ValueError('Unsupported declared model fidelity')
    versions = {row['id']: row['version'] for row in rows}
    if any(versions.get(r.model_id) != r.selected_version for r in records.values()):
        raise ValueError('Availability alternate version has a contradictory selected version')


def counts(records):
    current = [record for record in records.values() if record.selected]
    return {'selected_model_identities': len(current), 'versioned_archives': len(records),
            'selected_preset_requests': sum(len(r.preset_ids) for r in current),
            'all_archive_preset_requests': sum(len(r.preset_ids) for r in records.values()),
            'selected_availability': dict(sorted(Counter(r.availability for r in current).items())),
            'selected_fitting_supported': sum(r.fitting_supported for r in current),
            'selected_fit_ready': sum(r.fit_ready for r in current)}


def require_publication_review(records):
    unresolved = [key for key, record in records.items() if record.publication_review != 'approved']
    if not records:
        raise ValueError("Publication requires an availability registry")
    if unresolved:
        raise ValueError('Unresolved publication review: ' + ', '.join(unresolved))
