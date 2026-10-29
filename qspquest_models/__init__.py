"""Named model-library simulations using only the standalone QSPQuest engine."""

from __future__ import annotations
from dataclasses import dataclass, field
import hashlib, io, json, math, os, posixpath, shutil, stat, subprocess, tempfile, zipfile
from pathlib import Path
from .availability import SCHEMA, counts, load_records, verify_catalog
from .tables import read_table
from .input_bindings import (InputBindingError, build as _input_bindings,
                             check as _check_input_bindings, resolve as _resolve_input_alias)

__version__ = "0.1.0rc1"


def _json(data):
    def unique(pairs):
        obj = {}
        for k, v in pairs:
            if k in obj:
                raise ValueError("duplicate JSON key: " + k)
            obj[k] = v
        return obj

    def reject(x):
        raise ValueError("nonfinite JSON constant: " + x)

    return json.loads(data, object_pairs_hook=unique, parse_constant=reject)


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def _members(raw):
    if len(raw) > 50_000_000:
        raise ValueError("archive exceeds 50 MB")
    result = {}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        infos = z.infolist()
        if len(infos) > 5000 or sum(i.file_size for i in infos) > 200_000_000:
            raise ValueError("archive expansion budget exceeded")
        for i in infos:
            n = i.filename
            if (
                n in result
                or n.startswith("/")
                or "\\" in n
                or ".." in n.split("/")
                or posixpath.normpath(n) != n
                or stat.S_ISLNK(i.external_attr >> 16)
                or i.flag_bits & 1
                or i.file_size > 10_000_000
            ):
                raise ValueError("unsafe archive member")
            result[n] = z.read(i)
    index = _json(result["index.json"])
    if index.get("profile") != "ubi.omex.rust-ode/v1":
        raise ValueError("unsupported OMEX profile")
    if set(result) != set(index["members"]) | {"index.json", "manifest.xml"}:
        raise ValueError("archive inventory mismatch")
    for n, h in index["members"].items():
        if _sha(result[n]) != h:
            raise ValueError("member digest mismatch: " + n)
    from xml.etree import ElementTree as E

    xml = result["manifest.xml"]
    if b"<!DOCTYPE" in xml.upper() or b"<!ENTITY" in xml.upper():
        raise ValueError("XML entities prohibited")
    locations = [e.attrib["location"] for e in E.fromstring(xml)]
    if len(locations) != len(set(locations)) or set(locations) != {"."} | {
        "./" + n for n in result if n != "manifest.xml"
    }:
        raise ValueError("OMEX manifest mismatch")
    native = index.get("native_execution", {})
    if native.get("schema") != "qspquest.models.native-execution/v1":
        raise ValueError("archive lacks standalone QSPQuest execution projection")
    ids = [s["scenario_id"] for s in index["scenarios"]]
    if len(ids) != len(set(ids)) or set(ids) != set(native["scenarios"]):
        raise ValueError("scenario inventory mismatch")
    return result, index


def _source_interpretations(record, model_id, version, archive_hash, members=None):
    """Validate optional scientific choices against their exact execution identity."""
    if record is None:
        return None
    fields = {'schema', 'model_id', 'model_version', 'archive_sha256', 'native_model_sha256',
              'coverage', 'author_code_qualification', 'dimensional_qualification', 'entries'}
    if not isinstance(record, dict) or set(record) != fields:
        raise ValueError('Source interpretations require the closed v1 record')
    if (record['schema'] != 'qspquest.source-interpretations/v1'
            or record['model_id'] != model_id or record['model_version'] != version
            or record['archive_sha256'] != archive_hash):
        raise ValueError('Source interpretation identity differs from the selected archive')
    digest = record['native_model_sha256']
    if not isinstance(digest, str) or len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
        raise ValueError('Source interpretations need a native model SHA-256')
    if (record['coverage'] != 'selected_structural_interpretations'
            or record['author_code_qualification'] != 'not_assessed'
            or record['dimensional_qualification'] is not False):
        raise ValueError('Source interpretations do not establish complete scientific qualification')
    entries = record['entries']
    if not isinstance(entries, list) or not 1 <= len(entries) <= 32:
        raise ValueError('Source interpretations need 1 to 32 entries')
    text_fields = {'id', 'source_locator', 'rationale', 'conservation_implications', 'qualification_limits'}
    list_fields = {'printed_coordinates', 'adopted_coordinates', 'source_definitions', 'native_definitions'}
    def text(value):
        return isinstance(value, str) and 0 < len(value) <= 2000 and not any(ord(c) < 32 for c in value)
    ids = set()
    for entry in entries:
        if (not isinstance(entry, dict) or set(entry) != text_fields | list_fields
                or not all(text(entry[k]) for k in text_fields)):
            raise ValueError('Invalid source interpretation entry')
        for key in list_fields:
            values = entry[key]
            if (not isinstance(values, list) or not 1 <= len(values) <= 32
                    or not all(text(v) for v in values) or len(set(values)) != len(values)):
                raise ValueError('Invalid source interpretation coordinate or definition list')
        if entry['id'] in ids or len(entry['source_definitions']) != len(entry['native_definitions']):
            raise ValueError('Ambiguous source interpretation definitions')
        ids.add(entry['id'])
    if len(json.dumps(record)) > 16000:
        raise ValueError('Source interpretation record exceeds 16 KB')
    if members is not None:
        if _sha(members['native/model.json']) != digest:
            raise ValueError('Source interpretation native model hash mismatch')
        native = _json(members['native/model.json'])
        definitions = {d['name']: d['expression'] for d in native['definitions']}
        state_names = {s['name'] for s in native['states']}
        index = _json(members['index.json'])
        readouts = {o['name']: o['expression'].get('name') for o in native['outputs']}
        def symbols(value):
            if isinstance(value, dict):
                return ({value['name']} if value.get('kind') == 'symbol' else set()) | set().union(*(symbols(v) for v in value.values()))
            if isinstance(value, list):
                return set().union(*(symbols(v) for v in value))
            return set()
        from xml.etree import ElementTree as ET
        source_definitions = {n.attrib['variable']: n for n in ET.fromstring(members['model.xml']).iter()
                              if n.tag.endswith('}assignmentRule')}
        for entry in entries:
            if (not set(entry['native_definitions']) <= set(definitions)
                    or not set(entry['source_definitions']) <= set(source_definitions)):
                raise ValueError('Source interpretation refers to absent equation definitions')
            coordinates = set(entry['adopted_coordinates'])
            if not coordinates <= set(index['native_execution']['states']):
                raise ValueError('Source interpretation refers to absent adopted coordinates')
            aliases = {readouts[index['native_execution']['states'][name]['native_name']] for name in coordinates}
            for source_name, native_name in zip(entry['source_definitions'], entry['native_definitions']):
                source_symbols = {n.text.strip() for n in source_definitions[source_name].iter() if n.tag.endswith('}ci')}
                if (source_symbols & set(index['native_execution']['states']) != coordinates
                        or symbols(definitions[native_name]) & state_names != aliases):
                    raise ValueError('Source interpretation coordinates differ from its equation definitions')
    return _json(json.dumps(record))


def _finite_number(value):
    return type(value) in (int, float) and math.isfinite(value)


def _time_value(quantity, unit):
    """Convert the standard time units used by library requests."""
    from fractions import Fraction
    scales = {'ns': Fraction(1, 1000000000), 'us': Fraction(1, 1000000),
              'ms': Fraction(1, 1000), 's': 1, 'min': 60, 'h': 3600,
              'd': 86400, 'wk': 604800}
    value, source = quantity.get('value'), quantity.get('unit')
    if not _finite_number(value):
        raise ValueError('Request time must be a finite number')
    if source == unit:
        return value
    if source not in scales or unit not in scales:
        raise ValueError('Use the model time unit or a standard time unit (ns, us, ms, s, min, h, d, wk)')
    return value * float(Fraction(scales[source]) / Fraction(scales[unit]))


def _validate_native_result(result, model, request):
    """Reject incomplete native results before aliases or readouts are selected."""
    outputs = result.get('outputs')
    expected = {o['name']: o['unit'] for o in model['outputs']}
    if (result.get('schema') != 'qspquest.result/v0.1'
            or result.get('model_id') != model['model_id']
            or result.get('time_unit') != model['time_unit']
            or not isinstance(outputs, list) or not outputs
            or any(not isinstance(o, dict) or not isinstance(o.get('name'), str) for o in outputs)):
        raise ValueError('Native result identity, time unit or readouts differ from archived model')
    columns = {o['name']: o for o in outputs}
    if (len(columns) != len(outputs) or set(columns) != set(expected)
            or any(columns[n].get('unit') != u for n, u in expected.items())):
        raise ValueError('Native result has duplicate, missing or unexpected readouts or units')
    times, sides = result.get('times'), result.get('sides')
    if (not isinstance(times, list) or not times or not all(_finite_number(t) for t in times)
            or not isinstance(sides, list) or len(sides) != len(times)
            or any(side not in ('pre', 'post') for side in sides)
            or any(not isinstance(c.get('values'), list) or len(c['values']) != len(times)
                   or not all(_finite_number(v) for v in c['values']) for c in outputs)):
        raise ValueError('Nonfinite, empty or incomplete native result')
    regimen = request['regimen']
    points = regimen.get('observations')
    if points is not None:
        expected_times = [_time_value(p['time'], model['time_unit']) for p in points]
        if times != expected_times or sides != [p.get('side', 'post') for p in points]:
            raise ValueError('Native result differs from requested observation times or sides')
    else:
        # Trajectories also include event boundaries; preserve these legitimate rows.
        required = [regimen['start'], *regimen.get('samples', []), regimen['end']]
        required = [_time_value(t, model['time_unit']) for t in required]
        if (not set(required).issubset(times) or min(times) != required[0]
                or max(times) != required[-1] or times != sorted(times)):
            raise ValueError('Native trajectory omits requested times or exceeds its interval')
    return columns


@dataclass
class ModelArchive:
    """Verified curated archive, preserving its exact named conditions.

    Native JSON is generated from the validated SBML at authoring time and bound
    into this archive by digest. This is a curated execution profile, not a
    general-purpose SBML/SED-ML interpreter. Fitting requires a separately
    verified synthetic workflow declaration.
    """

    members: dict
    index: dict
    archive_sha256: str
    executable: str | None = None
    guide: dict | None = None
    availability: dict | None = None
    source_interpretations: dict | None = None
    _precision_profiles: dict | None = None
    _protocol_initialization: dict | None = None
    _scientific_assessments: dict | None = None

    @property
    def model_id(self):
        return self.index["model_id"]

    @property
    def scenario_ids(self):
        return tuple(self.index["native_execution"]["scenarios"])

    def run(self, scenario_id, *, precision_profile_id=None):
        """Run an archived scenario with one complete named parameter convention."""
        if precision_profile_id is not None:
            return self.research_copy(scenario_id, precision_profile_id=precision_profile_id).run()
        return self._run_request(scenario_id)

    @property
    def fitting_contract(self):
        """Complete verified synthetic fitting scope; an empty object means unavailable."""
        from .fitting import validate, _member
        declaration = (_member({'path': 'fitting.json', 'sha256': self.index['members']['fitting.json']},
                               self.index, self.members) if 'fitting.json' in self.members else {})
        return validate(declaration, self.index, self.members, self.availability)

    @property
    def fitting_workflows(self):
        """Defensive copies of declared workflows, including explicit qualification status."""
        return self.fitting_contract.get('workflows', [])

    def fit_workflow(self, workflow_id):
        """Execute one exact passed synthetic workflow and retain full diagnostics.

        Inputs cannot be edited through this interface. Inspect checks.passed and
        native_result: a returned nonconverged fit remains a failed recovery.
        Archive evidence does not qualify the currently installed engine.
        Requires the matching QSPQuest Python wheel.
        """
        from .fitting import select, _number, _member, _pieces, _check_result_numbers
        workflow = select(self.fitting_contract, workflow_id)
        from qspquest import CompiledModel, CompiledSensitivities
        model = _json(self.members[self.index['native_execution']['model']])
        request = workflow['native_request']
        names = [p['native_name'] for p in workflow['parameters']]
        if workflow['operation'] == 'fit_scalar':
            compiled = CompiledModel(model)
            result = compiled.fit_scalar(request)
            fit = result
            expected_schema = 'qspquest.scalar-fit-result/v0.1'
        else:
            compiled = CompiledSensitivities(model, names)
            result = compiled.fit(request)
            fit = result.get('fit')
            expected_schema = 'qspquest.fit-result/v0.1'
        if result.get('schema') != expected_schema or not isinstance(fit, dict) or result.get('population') is not None:
            raise ValueError('Native fitting result differs from the archived operation')
        identity = fit.get('objective', {}).get('identity', {})
        from qspquest import fitting_identity
        canonical = fitting_identity(model, request, workflow['operation'], result=result)
        evidence = _member(workflow['qualification']['evidence'], self.index, self.members)
        _check_result_numbers(fit, workflow['parameters'], len(_pieces(workflow)[1]),
                              workflow['operation'], evidence['fit_request_hash'])
        if identity.get('model_content_hash') != canonical['model_content_hash']:
            raise ValueError('Native fitting result model identity differs')
        checks = {}
        for role in workflow['parameters']:
            estimate = fit.get('parameters', {}).get(role['native_name'], {})
            value = _number(estimate.get('value'))
            checks[role['native_name']] = {'estimate': value, 'truth': role['synthetic_truth'],
                'unit': role['unit'], 'absolute_limit': role['recovery_absolute_tolerance'],
                'passed': estimate.get('unit') == role['unit'] and abs(value - role['synthetic_truth']) <= role['recovery_absolute_tolerance']}
        gradient_passed = True
        if workflow['operation'] == 'fit_individual':
            gradient = _number(fit.get('projected_gradient_norm'))
            gradient_passed = 0 <= gradient <= request['problem']['request']['gradient_tolerance']
        return {'native_result': result, 'effective_request': request, 'workflow_id': workflow_id,
                'operation': workflow['operation'], 'model_id': self.model_id,
                'model_version': self.index['model_version'], 'archive_sha256': self.archive_sha256,
                'native_model_sha256': self.fitting_contract['native_model_sha256'],
                'native_request_sha256': canonical['native_request_sha256'],
                'checks': {'passed': fit.get('status') == 'converged' and gradient_passed and all(c['passed'] for c in checks.values()),
                           'fit_status': fit.get('status'), 'parameters': checks, 'gradient_passed': gradient_passed},
                'current_engine_qualification': 'not_assessed',
                'source_population_reproduction': False,
                'scope': 'Exact synthetic recovery only; no physical, clinical or source population qualification',
                'limitations': workflow['limitations']}

    @property
    def precision_profiles(self):
        """Complete archive-bound conventions; None means none declared.

        The default matches archived scalar inputs. Source rounding choices do
        not qualify biology, physical dimensions or population inference.
        """
        from .precision_profiles import validate
        return validate(self._precision_profiles, self.index, self.archive_sha256, self.members)

    @property
    def protocol_initialization(self):
        """Hash-bound source clock and denominator declarations; None means undeclared."""
        from .protocol_initialization import validate
        return validate(self._protocol_initialization, self.index, self.archive_sha256, self.members)

    @property
    def scientific_assessments(self):
        """Separate pinned archive assessment axes; None means undeclared."""
        from .scientific_assessments import validate
        return validate(self._scientific_assessments, self.index, self.archive_sha256, self.members)

    @property
    def starter_scenario(self):
        return self.guide.get('starter') if self.guide else None

    @property
    def parameter_effects(self):
        """Archive-declared modality effects; source qualification remains separate."""
        from copy import deepcopy
        return deepcopy(self.index["native_execution"].get("parameter_effects", {}))

    @property
    def dose_contracts(self):
        """Archive-declared dose coordinates and source units; empty if undeclared.

        These declarations do not convert a dose or qualify unrelated equations.
        The returned mapping can be edited without modifying the archive.
        """
        from copy import deepcopy
        return deepcopy(self.index["native_execution"].get("dose_contracts", {}))

    @property
    def output_semantics(self):
        """Declared identities and actual native units; None means undeclared.

        Labels do not convert quantities or establish scientific qualification.
        The returned mapping can be edited without modifying the archive.
        """
        native = self.index["native_execution"]
        if not native.get("model"):
            return {}
        units = {row["name"]: row["unit"] for row in
                 _json(self.members[native["model"]])["outputs"]}
        return {name: {"analyte": row.get("analyte"),
                       "compartment": row.get("compartment"),
                       "returned_unit": units[row["native_name"]],
                       "description": row.get("description")}
                for name, row in native["outputs"].items()}

    @property
    def input_bindings(self):
        """Version-bound canonical names, declared aliases, units and defaults.

        Source labels remain separate from native units. This registry does not
        evaluate derived initial values or establish scientific qualification.
        Its hash is distinct from the MCP inspection hash.
        """
        return _input_bindings(self.members, self.index, self.archive_sha256)

    def resolve_input_alias(self, group, name, *, expected_input_binding_hash=None):
        """Resolve one exact alias; stale contexts require explicit migration."""
        return _resolve_input_alias(self.input_bindings, group, name, expected_input_binding_hash)

    def research_copy(self, scenario_id, *, expected_input_binding_hash=None, precision_profile_id=None):
        """Copy verified inputs for an exploratory run; the archive stays intact."""
        native = self.index['native_execution']
        if scenario_id not in native['scenarios']:
            raise ValueError('unknown or unavailable scenario: ' + str(scenario_id))
        if self.guide and self.guide['availability'] == 'source_replay':
            raise ValueError('Source replay available; dynamic simulation unavailable. Choose a dynamic model for research copies')
        _check_input_bindings(self.input_bindings, expected_input_binding_hash)
        copied = ResearchCopy(self, scenario_id, _json(self.members[native['scenarios'][scenario_id]]))
        if precision_profile_id is not None:
            copied.set_precision_profile(precision_profile_id)
        return copied

    def _run_request(self, scenario_id, edited_request=None, precision_profile_id=None):
        native = self.index["native_execution"]
        if scenario_id in self.index.get("unavailable_scenario_ids", []):
            raise ValueError(
                "scenario has no qualified execution; inspect INTERCHANGE_AND_EXECUTION_HOLDS.json: "
                + str(scenario_id)
            )
        if scenario_id not in native["scenarios"]:
            raise ValueError("unknown scenario: " + str(scenario_id))
        model = _json(self.members[native["model"]])
        request = edited_request if edited_request is not None else _json(self.members[native["scenarios"][scenario_id]])
        from .precision_profiles import receipt
        precision = receipt(self.precision_profiles, self.index, self.members, request,
                            scenario_id, precision_profile_id)
        if model["model_id"] != self.model_id:
            raise ValueError("native model identity mismatch")
        if self.executable or os.environ.get("QSPQUEST_EXECUTABLE"):
            result = self._cli(model, request)
        else:
            try:
                from qspquest import CompiledModel
            except ImportError:
                result = self._cli(model, request)
            else:
                result = CompiledModel(model).run(request)
        columns = _validate_native_result(result, model, request)

        def readouts(mapping):
            return [
                {
                    "name": name,
                    "unit": columns[row["native_name"]]["unit"],
                    "declared_source_unit": row.get('source_unit', row.get('unit')),
                    "native_name": row["native_name"],
                    "values": columns[row["native_name"]]["values"],
                }
                for name, row in mapping.items()
            ]

        mapped = {
            **result,
            "outputs": readouts(native["outputs"]),
            "states": readouts(native["states"]),
            "scenario_id": scenario_id,
            "archive_sha256": self.archive_sha256,
            "model_version": self.index["model_version"],
            "effective_request": _json(json.dumps(request, allow_nan=False)),
            "effective_outputs": [o["name"] for o in result["outputs"]],
            "research_copy": edited_request is not None,
            "model_provenance": {"origin": "verified_archive",
                                 "native_model_sha256": _sha(self.members[native["model"]]),
                                 "execution_pin": self.index.get("execution_pin")},
            "coordinates": native["coordinates"],
            "dimensional_qualification": native.get("dimensional_qualification", False),
            "availability": self.availability,
        }
        if precision is not None:
            mapped['precision_profile'] = precision
            mapped['model_provenance']['precision_profile'] = precision
        if self.source_interpretations is not None:
            mapped['model_provenance']['source_interpretations'] = _json(json.dumps(self.source_interpretations))
        if self.guide:
            mapped['primary_readouts'] = self.guide.get('scenarios', {}).get(scenario_id, self.guide['readouts'])
            source_readouts = [r for r in mapped['primary_readouts'] if r['kind'] == 'source_parameter']
            if source_readouts:
                if edited_request is not None:
                    raise ValueError('Source replay values do not describe edited inputs; choose a dynamic model for research copies')
                scientific = _json(self.members['scientific/model.json'])
                experiments = _json(self.members['scientific/scenarios.json'])['scenarios']
                overrides = next(s for s in experiments if s['id'] == scenario_id).get('parameters', {})
                mapped['source_values'] = [
                    {'name': r['name'], 'unit': scientific['parameters'][r['name']]['unit'],
                     'values': [overrides.get(r['name'], scientific['parameters'][r['name']]['default'])] * len(mapped['times'])}
                    for r in source_readouts
                ]
        if edited_request is not None:
            mapped['research_copy'] = True
            mapped['base_scenario_id'] = scenario_id
            mapped['request_sha256'] = _sha(json.dumps(request, sort_keys=True, allow_nan=False).encode())
        return mapped

    def _cli(self, model, request):
        exe = (
            self.executable
            or os.environ.get("QSPQUEST_EXECUTABLE")
            or shutil.which("qspquest")
        )
        if not exe:
            raise RuntimeError(
                "Install QSPQuest (Python package or CLI); see the quickstart. The library has no alternate solver."
            )
        if shutil.which(str(exe)) is None:
            raise FileNotFoundError(f"QSPQuest executable is unavailable: {exe}")
        with tempfile.TemporaryDirectory(prefix="qspquest-model-") as tmp:
            m = Path(tmp) / "model.json"
            r = Path(tmp) / "request.json"
            m.write_text(json.dumps(model, allow_nan=False))
            r.write_text(json.dumps(request, allow_nan=False))
            process = subprocess.run(
                [str(exe), "run", str(m), str(r)],
                capture_output=True,
                text=True,
                timeout=900,
            )
        if process.returncode:
            raise RuntimeError("QSPQuest execution failed: " + process.stderr.strip())
        return _json(process.stdout)

    @staticmethod
    def write_csv(result, path, include_states=False, *, all_readouts=False):
        """Create CSV plus .manifest.json with units and provenance; never overwrite.

        Returns the manifest. Use read_table(path) to validate and reimport the
        pair. Missing context in manually assembled results is explicitly null.
        """
        from .tables import write_table
        outputs = result_columns(result, all_readouts=all_readouts or include_states)
        return write_table(result, path, outputs)


def result_columns(result, *, all_readouts=False):
    """Use identical column names in Python, CLI and R (state__/source__ prefixes)."""
    lookup = {}
    for kind, key, prefix in [('output', 'outputs', ''), ('state', 'states', 'state__'),
                              ('source_parameter', 'source_values', 'source__')]:
        for column in result.get(key, []):
            if (kind, column['name']) in lookup:
                raise ValueError('Duplicate result readout: ' + column['name'])
            lookup[(kind, column['name'])] = {**column, 'name': prefix + column['name'], 'kind': kind}
    selection = result.get('primary_readouts')
    if all_readouts or selection is None:
        return list(lookup.values())
    return [{**lookup[(r['kind'], r['name'])], 'meaning': r['meaning']} for r in selection]


@dataclass
class ResearchCopy:
    model: ModelArchive
    scenario_id: str
    request: dict
    _inspected_input_binding_hash: str = field(init=False, repr=False)
    _precision_profile_id: str | None = field(default=None, init=False, repr=False)
    _inspected_precision_profile_hash: str | None = field(default=None, init=False, repr=False)

    def __post_init__(self):
        self._inspected_input_binding_hash = self.model.input_bindings['context']['input_binding_hash']
        from .precision_profiles import digest
        manifest = self.model.precision_profiles
        self._inspected_precision_profile_hash = digest(manifest) if manifest else None

    @property
    def input_binding_hash(self):
        """Binding context retained when this research copy was created."""
        return self._inspected_input_binding_hash

    def _check_bindings(self, expected=None):
        from .precision_profiles import digest
        manifest = self.model.precision_profiles
        if (digest(manifest) if manifest else None) != self._inspected_precision_profile_hash:
            raise ValueError('Precision profile manifest changed; create a fresh research copy after inspection')
        bindings = self.model.input_bindings
        _check_input_bindings(bindings, self._inspected_input_binding_hash)
        _check_input_bindings(bindings, expected)
        return bindings

    @property
    def parameters(self):
        """Mutable native inputs with their effective values and archived units.

        Unit ``1`` retains the source numerical scale. A parameter edit does
        not recompute coupled initial states or grant scientific qualification.
        """
        from copy import deepcopy
        self._check_bindings()
        native = _json(self.model.members[self.model.index['native_execution']['model']])
        return {p['name']: deepcopy(self.request['parameters'].get(p['name'], p['default']))
                for p in native['parameters'] if not p.get('fixed', False)}

    @property
    def precision_profile(self):
        """Selected whole parameter convention and any subsequent modifications."""
        self._check_bindings()
        from .precision_profiles import receipt
        return receipt(self.model.precision_profiles, self.model.index, self.model.members,
                       self.request, self.scenario_id, self._precision_profile_id)

    def set_precision_profile(self, profile_id):
        """Replace all mutable scalar inputs; retain states, doses and protocol."""
        self._check_bindings()
        from .precision_profiles import select
        profile = select(self.model.precision_profiles, self.scenario_id, profile_id)
        if profile is None:
            raise ValueError('No precision profiles declared for this archive')
        self.request['parameters'] = profile['scenarios'][self.scenario_id]['parameters']
        self._precision_profile_id = profile['id']
        return self

    def set_parameter(self, name, value, *, expected_input_binding_hash=None):
        """Set a mutable input by alias in its actual native unit; check bounds."""
        bindings = self._check_bindings(expected_input_binding_hash)
        binding = _resolve_input_alias(bindings, 'parameters', name)
        name = binding['native_name']
        if binding['fixed']:
            raise ValueError('fixed parameter: ' + name + '; inspect copy.parameters for mutable inputs')
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('parameter value must be finite')
        native = _json(self.model.members[self.model.index['native_execution']['model']])
        parameter = next(p for p in native['parameters'] if p['name'] == name)
        unit = parameter['default']['unit']
        bounds = parameter.get('bounds')
        if bounds is not None:
            if any(q['unit'] != unit for q in bounds):
                raise ValueError('parameter bounds use a different unit; inspect the archived model')
            if not bounds[0]['value'] <= value <= bounds[1]['value']:
                raise ValueError('parameter ' + name + ' must be between ' + str(bounds[0]['value']) + ' and ' + str(bounds[1]['value']) + ' ' + unit)
        self.request['parameters'][name] = {'value': float(value), 'unit': unit}
        return self

    @property
    def doses(self):
        """Inspect zero-based dose indexes, amounts, units and administration times."""
        from copy import deepcopy
        return deepcopy(self.request['regimen']['administrations'])

    def set_dose(self, index, amount):
        """Change one scheduled amount, retaining its archived numerical unit."""
        self._check_bindings()
        doses = self.request['regimen']['administrations']
        if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < len(doses):
            raise ValueError('dose index is unavailable; inspect copy.doses. Some models encode exposure in initial states')
        if isinstance(amount, bool) or not isinstance(amount, (int, float)) or not math.isfinite(amount) or amount < 0:
            raise ValueError('dose amount must be finite and nonnegative')
        doses[index]['amount']['value'] = float(amount)
        return self

    @property
    def initial_states(self):
        """Retained explicit starting quantities keyed by biological state aliases.

        Coupled initial expressions are available in model.input_bindings;
        this accessor does not evaluate or replace them.
        """
        bindings = self._check_bindings()['initial_states']
        native = self.model.index['native_execution']
        names = native.get('states') or bindings
        retained = self.request.get('initial_states', {})
        return {name: dict(retained[bindings[name]['native_name']])
                for name in names if name in bindings and bindings[name]['native_name'] in retained}

    def set_initial_state(self, name, value, *, expected_input_binding_hash=None):
        """Set one initial state by canonical name or alias in its native unit."""
        bindings = self._check_bindings(expected_input_binding_hash)
        binding = _resolve_input_alias(bindings, 'initial_states', name)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
            raise ValueError('initial value must be finite')
        self.request.setdefault('initial_states', {})[binding['native_name']] = {
            'value': float(value), 'unit': binding['unit']}
        return self

    def run(self):
        self._check_bindings()
        return self.model._run_request(self.scenario_id, self.request, self._precision_profile_id)

    def save(self, directory):
        """Save reproducible native inputs and base archive identity to a new directory."""
        bindings = self._check_bindings()
        folder = Path(directory)
        folder.mkdir(parents=True, exist_ok=False)
        folder.joinpath('model.json').write_bytes(self.model.members[self.model.index['native_execution']['model']])
        folder.joinpath('request.json').write_text(json.dumps(self.request, indent=2, allow_nan=False))
        folder.joinpath('input-bindings.json').write_text(json.dumps(bindings, indent=2, allow_nan=False))
        if self.precision_profile is not None:
            folder.joinpath('precision-profile.json').write_text(json.dumps(self.precision_profile, indent=2, allow_nan=False))
        folder.joinpath('provenance.json').write_text(json.dumps({
            'input_binding_hash': self.input_binding_hash,
            'precision_profile': self.precision_profile,
            'research_copy': True, 'model_id': self.model.model_id,
            'model_version': self.model.index['model_version'], 'base_scenario_id': self.scenario_id,
            'archive_sha256': self.model.archive_sha256,
            'request_sha256': _sha(json.dumps(self.request, sort_keys=True, allow_nan=False).encode()),
        }, indent=2))
        return folder


def load_archive(path, *, expected_sha256, executable=None, availability_record=None, source_interpretations=None, precision_profiles=None, protocol_initialization=None, scientific_assessments=None):
    """Require an external SHA-256 pin; consume exactly the bytes verified."""
    raw = Path(path).read_bytes()
    if _sha(raw) != expected_sha256:
        raise ValueError("archive SHA-256 differs from expected pin")
    members, index = _members(raw)
    profiles = _json(Path(__file__).with_name('user_guides.json').read_bytes())
    key = index['model_id'] + '/' + index['model_version']
    guide = profiles.get(key)
    if availability_record is None:
        record = load_records(Path(__file__).with_name('availability.json')).get(key)
        availability_record = record if record and record.archive_sha256 == expected_sha256 else None
    if availability_record:
        availability_record.verify_archive(index, expected_sha256, _json(members.get('fitting.json', b'{}')))
    from .fitting import validate as validate_fitting
    validate_fitting(_json(members.get('fitting.json', b'{}')), index, members,
                     availability_record.describe() if availability_record else None,
                     native_identity=False)
    if guide and availability_record:
        guide = {**guide, 'availability': availability_record.availability}
    else:
        guide = None
    if guide and guide.get('archive_sha256') != expected_sha256:
        guide = None
    if guide and (guide['starter'] not in index['native_execution']['scenarios'] and guide['starter'] is not None):
        raise ValueError('starter guide does not match archive experiments')
    interpretation = _source_interpretations(source_interpretations, index['model_id'],
                                              index['model_version'], expected_sha256, members)
    from .precision_profiles import validate
    precision = validate(precision_profiles, index, expected_sha256, members)
    from .protocol_initialization import validate as validate_protocol
    protocol = validate_protocol(protocol_initialization, index, expected_sha256, members)
    from .scientific_assessments import validate as validate_scientific
    scientific = validate_scientific(scientific_assessments, index, expected_sha256, members)
    return ModelArchive(members, index, expected_sha256, executable, guide,
                        availability_record.describe() if availability_record else None, interpretation, precision, protocol, scientific)


class Library:
    def __init__(self, root=None, *, executable=None):
        bundled = Path(__file__).resolve().parent / '_library'
        self.root = Path(root) if root else (bundled if (bundled / 'catalog.json').is_file()
                                           else Path(__file__).resolve().parents[1])
        self.catalog = _json((self.root / "catalog.json").read_bytes())
        self.executable = executable
        for row in self.catalog['models']:
            _source_interpretations(row.get('source_interpretations'), row['id'], row['version'], row['omex_sha256'])
        self.availability_records = {}
        if 'availability_schema' in self.catalog:
            if self.catalog['availability_schema'] != SCHEMA:
                raise ValueError('Unsupported catalog availability schema')
            registry = (Path(__file__).with_name('availability.json') if self.root == bundled
                        else self.root / 'qspquest_models/availability.json')
            self.availability_records = load_records(registry)
            verify_catalog(self.catalog, self.availability_records)
            source_catalog = self.root / 'source-catalog.json'
            if source_catalog.is_file():
                from .availability import verify_source_families
                verify_source_families(_json(source_catalog.read_bytes()), self.catalog)
        elif (any(k in self.catalog for k in ('source_family_schema', 'source_families'))
              or any('source_family' in row for row in self.catalog['models'])):
            raise ValueError('Source-family declarations require the versioned availability registry')

    @property
    def availability_counts(self):
        return counts(self.availability_records)

    def list_models(self):
        return [{**row, 'availability': self.availability_records[row['id'] + '/' + row['version']].describe()}
                for row in self.catalog['models']] if self.availability_records else list(self.catalog['models'])

    def search(self, query):
        """Search the displayed browsing summaries and retained source descriptions."""
        summaries_path = self.root / 'scripts/model_summaries.json'
        summaries = _json(summaries_path.read_bytes()) if summaries_path.is_file() else {}
        descriptions = {}
        if (self.root / 'source-catalog.json').is_file():
            for source in self.list_source_models():
                if source.get('format') == 'scientific_json' and source.get('omex'):
                    descriptions[source['omex']['model_id']] = self.load_source_model(source['id'])['model.json'].get('description', '')
        # Users commonly paste a typographic dash or a regular hyphen.
        def normalize(value):
            import re
            return re.sub(r'[-–—]', ' ', value.casefold())
        query = normalize(query)
        return [row for row in self.list_models() if query in normalize(' '.join([
            *(str(row.get(k, '')) for k in ['id', 'name', 'description']),
            summaries.get(row['id'], ''), descriptions.get(row['id'], ''),
        ]))]

    def list_source_models(self):
        """List scientific-source models, including explicit rights holds."""
        from .sources import list_sources

        return list_sources(self.root)

    def load_source_model(self, model_id):
        """Inspect a scientific source model. Runtime readiness is separate."""
        from .sources import load_source

        return load_source(self.root, model_id)

    def load_source_execution(self, model_id):
        """Load the selected scientific-source OMEX through the standalone route."""
        rows = [r for r in self.list_source_models() if r["id"] == model_id]
        if len(rows) != 1 or not rows[0].get("omex"):
            raise PermissionError(
                "Source is metadata only; no releasable implementation"
            )
        record = rows[0]["omex"]
        from .sources import execution_status
        execution_status(self.root, rows[0], self.availability_records.get(
            record['model_id'] + '/' + record['version']))
        self.load_source_model(model_id)
        relative = Path(record["archive"])
        if relative.is_absolute() or ".." in relative.parts:
            raise ValueError("unsafe source archive path")
        path = self.root / relative
        if any(p.is_symlink() for p in (path, *path.parents)):
            raise ValueError("source archive symlink prohibited")
        return load_archive(
            path, expected_sha256=record["omex_sha256"], executable=self.executable,
            availability_record=self.availability_records.get(record['model_id'] + '/' + record['version']),
            source_interpretations=next((r.get('source_interpretations') for r in self.catalog['models']
                                         if r['id'] == record['model_id'] and r['version'] == record['version']), None),
        )

    def list_source_executions(self):
        """Discover exact execution identities, availability and stored evidence scope.

        ``version`` identifies the scientific source snapshot. The selected
        archive has its own ``execution_version`` and SHA-256 identity.
        """
        from .sources import execution_status
        return [execution_status(self.root, row, self.availability_records.get(
            row['omex']['model_id'] + '/' + row['omex']['version']))
                for row in self.list_source_models() if row.get('omex')]

    def load(self, model_id, *, version=None):
        """Load one verified archive; an explicit version never selects a replacement."""
        if version is not None and (not isinstance(version, str) or not version):
            raise ValueError('version must be a nonempty exact model-version string')
        available = [r for r in self.catalog["models"] if r["id"] == model_id]
        rows = [r for r in available if version is None or r['version'] == version]
        if not rows and version is not None:
            raise InputBindingError({'code': 'model_version_unavailable',
                'message': 'Selected model version is unavailable. Inspect library.list_models() and explicitly migrate before choosing another version.',
                'model_id': str(model_id)[:128], 'requested_version': version[:128],
                'available_versions': sorted({r['version'] for r in available})[:32],
                'migration': 'inspect_current_bindings'})
        if len(rows) != 1:
            raise ValueError("unknown or duplicate model: " + str(model_id))
        row = rows[0]
        path = Path(row["archive"])
        if path.is_absolute() or ".." in path.parts:
            raise ValueError("unsafe catalog path")
        precision = None
        descriptor = row.get('precision_profiles')
        if descriptor is not None:
            if not isinstance(descriptor, dict) or set(descriptor) != {'path', 'sha256'}:
                raise ValueError('Precision profile descriptor requires path and sha256')
            supplied_path = descriptor['path']
            if (not isinstance(supplied_path, str) or '\\' in supplied_path or ':' in supplied_path
                    or any(part in ('', '.', '..') for part in supplied_path.split('/'))):
                raise ValueError('Unsafe precision profile path')
            relative = Path(supplied_path)
            resolved = (self.root / relative).resolve()
            if not resolved.is_relative_to(self.root.resolve()):
                raise ValueError('Precision profile path escapes library')
            if resolved.stat().st_size > 4_000_000:
                raise ValueError('Precision profile file exceeds 4 MB')
            raw = resolved.read_bytes()
            if _sha(raw) != descriptor['sha256']:
                raise ValueError('Precision profile SHA-256 differs from catalog')
            precision = _json(raw)
        protocol = None
        descriptor = row.get('protocol_initialization')
        if descriptor is not None:
            if not isinstance(descriptor, dict) or set(descriptor) != {'path', 'sha256'}:
                raise ValueError('Protocol initialization descriptor requires path and sha256')
            supplied_path = descriptor['path']
            if (not isinstance(supplied_path, str) or '\\' in supplied_path or ':' in supplied_path
                    or any(part in ('', '.', '..') for part in supplied_path.split('/'))):
                raise ValueError('Unsafe protocol initialization path')
            resolved = (self.root / supplied_path).resolve()
            if not resolved.is_relative_to(self.root.resolve()):
                raise ValueError('Protocol initialization path escapes library')
            if resolved.stat().st_size > 1_000_000:
                raise ValueError('Protocol initialization file exceeds 1 MB')
            raw = resolved.read_bytes()
            if _sha(raw) != descriptor['sha256']:
                raise ValueError('Protocol initialization SHA-256 differs from catalog')
            protocol = {'file_sha256': descriptor['sha256'], 'manifest': _json(raw)}
        scientific = None
        descriptor = row.get('scientific_assessments')
        if descriptor is not None:
            if not isinstance(descriptor, dict) or set(descriptor) != {'path', 'sha256'}:
                raise ValueError('Scientific assessment descriptor requires path and sha256')
            supplied_path = descriptor['path']
            if (not isinstance(supplied_path, str) or '\\' in supplied_path or ':' in supplied_path
                    or any(part in ('', '.', '..') for part in supplied_path.split('/'))):
                raise ValueError('Unsafe scientific assessment path')
            resolved = (self.root / supplied_path).resolve()
            if not resolved.is_relative_to(self.root.resolve()):
                raise ValueError('Scientific assessment path escapes library')
            if resolved.stat().st_size > 24_000:
                raise ValueError('Scientific assessment file exceeds 24 KB')
            raw = resolved.read_bytes()
            if _sha(raw) != descriptor['sha256']:
                raise ValueError('Scientific assessment SHA-256 differs from catalog')
            scientific = {'file_sha256': descriptor['sha256'], 'manifest': _json(raw)}
        model = load_archive(
            self.root / path,
            expected_sha256=row["omex_sha256"],
            executable=self.executable,
            availability_record=self.availability_records.get(model_id + '/' + row['version']),
            source_interpretations=row.get('source_interpretations'),
            precision_profiles=precision,
            protocol_initialization=protocol,
            scientific_assessments=scientific,
        )
        if (model.model_id != model_id or model.index['model_version'] != row['version']
                or set(model.scenario_ids) != set(row['scenario_ids'])):
            raise ValueError("catalog/archive mismatch")
        return model
