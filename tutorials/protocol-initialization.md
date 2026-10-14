# Inspect initialization and normalization

Use this workflow to inspect when a source protocol starts and how percentage
readouts are defined before modifying a scenario. It requires Python 3.10 or
later and the model-library source distribution. From the distribution root,
run the included complete example:

```sh
PYTHONPATH=. python3 tutorials/protocol_initialization.py
```

The example uses the supplied model archive and catalog. It does not require an
engine executable or network access. Expected output is the verified declaration
followed by `Verified 13 archived initialization clocks and 4 explicit reference
denominators; equilibrium and physical qualification are not asserted.`

`model.protocol_initialization` returns a copy of the hash-bound source
declaration. The catalog pins its file bytes; the SDK checks model/version,
archive/native-model identity, the exact scenario inventory, original start
quantities and initial override counts, and each normalization's native readout
expression. An absent declaration returns `None`; it does not establish a policy
from output names. A changed checksum or scenario must be resolved before loading.

The selected ICM AAV scenario starts at −1000 h and administers its first dose
at 0 h. Starting parameter changes apply from initialization; a change intended
only at dosing belongs at that boundary. The declared no-dose target scenario
starts at −504 h and has `intervention_time: null`. A negative clock or a scenario
name does not establish equilibrium: convergence needs separate evidence.

The four TargetX percentage readouts divide 100 times the indicated free-target
state by a named baseline parameter. Their `declared_reference_input` basis
uses that input, including explicit overrides. Transport changes alone do not
automatically redefine the denominator from a trajectory sample. Native unit
`1` remains a source coordinate; friendly labels do not qualify physical units.

Literal initial states are independently declared inputs. Changing a receptor
total parameter alone does not recompute the corresponding free-receptor initial
value. Choose a coupled stored scenario or provide the intended initials
explicitly. After modifying a protocol, inspect the engine's prepared initial
values and actual input phases as well as this original source declaration.
Historical preset evidence does not qualify the modified request.
