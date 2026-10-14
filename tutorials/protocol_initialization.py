"""Inspect verified initialization clocks and denominators without running a model."""
import json
from qspquest_models import Library

model = Library().load('qspquest_liu_2026_aav_mab_targetx_rat_brain_full_qsp', version='2.1.2')
declaration = model.protocol_initialization
assert declaration is not None
manifest = declaration['manifest']
assert len(manifest['scenarios']) == 13 and len(manifest['normalizations']) == 4
print(json.dumps(declaration, indent=2))
print('Verified 13 archived initialization clocks and 4 explicit reference denominators; equilibrium and physical qualification are not asserted.')
