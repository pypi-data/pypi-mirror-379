# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.

"""qdk bundling meta-package.

Design goals:
    * Provide a single import root `qdk` that exposes bundled quantum tooling as
        submodules (`qdk.qsharp`, `qdk.widgets`, etc.).

Optional extras:
    azure   -> installs `azure-quantum`, available as `qdk.azure`.
    qiskit  -> installs `qiskit`, available as `qdk.qiskit`.
    jupyter -> installs `qsharp-widgets` + `qsharp-jupyterlab`; exposes `qdk.widgets`.

"""

# Optional: use telemetry hook if present (skipped in stub/mock envs)
try:
    import qsharp.telemetry_events.on_qdk_import

    qsharp.telemetry_events.on_qdk_import()
except Exception:
    pass

# Some common utilities are lifted to the qdk root.
from qsharp import code
from qsharp import (
    set_quantum_seed,
    set_classical_seed,
    dump_machine,
    dump_circuit,
    init,
    Result,
    TargetProfile,
    StateDump,
    ShotResult,
    PauliNoise,
    DepolarizingNoise,
    BitFlipNoise,
    PhaseFlipNoise,
)

# utilities lifted from qsharp
__all__ = [
    "code",
    "set_quantum_seed",
    "set_classical_seed",
    "dump_machine",
    "dump_circuit",
    "init",
    "Result",
    "TargetProfile",
    "StateDump",
    "ShotResult",
    "PauliNoise",
    "DepolarizingNoise",
    "BitFlipNoise",
    "PhaseFlipNoise",
]
