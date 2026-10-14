"""Inspect scoped archive assessment axes without qualifying a current run."""
from copy import deepcopy
import hashlib,json
from .tables import _scientific_assessment

def validate(declaration,index,archive_sha256,members):
    if declaration is None:return None
    if not isinstance(declaration,dict) or set(declaration)!={'file_sha256','manifest'} or not isinstance(declaration['manifest'],dict):
        raise ValueError('Scientific assessment declaration has missing or unknown fields')
    native_path=index['native_execution'].get('model')
    if not native_path or native_path not in members:raise ValueError('Scientific assessments require an executable native model')
    if declaration['manifest'].get('native_model_sha256')!=hashlib.sha256(members[native_path]).hexdigest():
        raise ValueError('Scientific assessment native model SHA-256 mismatch')
    m={'schema':'qspquest.mcp-scientific-assessment/v1','declaration':declaration,'effective_source_matches_archive':True,'request_matches_stored_preset':None,'current_engine_and_request':'not_assessed','notice':'Scoped archive declaration; no current engine or request qualification.'}
    _scientific_assessment({'scientific_assessment':m,'model':{'id':index['model_id'],'version':index['model_version'],'archive_sha256':archive_sha256,'provenance':{'metadata':{'scientific_assessments':{'sha256':declaration['file_sha256']},'scientific_assessment_contract':declaration}}},'inputs':{}})
    native=json.loads(members[native_path]);symbols={x['name'] for key in ['parameters','covariates','individual','definitions','states','outputs'] for x in native.get(key,[])}
    for a in declaration['manifest']['assessments']:
        for f in a['findings']:
            if not set(f['native_symbols'])<=symbols:raise ValueError('Scientific assessment finding refers to unknown native symbols')
    return deepcopy(declaration)
