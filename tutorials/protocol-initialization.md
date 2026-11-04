# Inspect initialization and normalization

Use this workflow to inspect when a source protocol starts and how percentage
readouts are defined before modifying a scenario. It requires Python 3.10 or
later and the model-library source distribution. From the distribution root,
run the included complete example:

```sh
PYTHONPATH=. python3 tutorials/protocol_initialization.py
```

It needs no engine or network access. It prints the declaration and ends with
`Verified 13 archived initialization clocks and 4 explicit reference
denominators; equilibrium and physical qualification are not asserted.`

`model.protocol_initialization` returns the source's declared start times and
percentage definitions, after checking that they match the model. If nothing is
declared it returns `None`; do not guess the policy from output names.

The ICM AAV scenario starts at −1000 h and gives its first dose at 0 h. A
parameter change made at the start applies from −1000 h; to change something only
at dosing, apply it at 0 h. The no-dose target scenario starts at −504 h and has
`intervention_time: null`. Starting early does not guarantee that the system has
reached steady state; that needs a separate check.

The four TargetX percentage readouts are 100 × free target ÷ a named baseline
parameter; this `declared_reference_input` basis follows any override of that
parameter. Changing transport does not recompute it from the simulation. Unit
`1` is not a checked physical unit, whatever the label says.

Starting states are separate inputs. Changing a receptor-total parameter alone
does not recompute the free-receptor starting value. Use a stored scenario that
sets both, or set the starting values yourself. After changing a protocol, check
the starting values and input timing the engine actually used. Stored results
for the original preset do not cover your change.
