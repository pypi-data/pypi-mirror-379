# pyOutfit 1.0.0 – First Stable Release

_Tag: `v1.0.0` • Date: 2025-09-17_

High-performance Python bindings for the Rust **Outfit** engine delivering Gauss Initial Orbit Determination (IOD), multi-format observation ingestion, orbital element conversions, parallel batch processing, and observatory utilities — all with deterministic, typed, and well‑documented workflows.

---
## 🚀 Release Highlights
- First production/stable release (API considered stable; semantic versioning from here on).
- Complete reimplementation (Rust) of classic OrbFit Gauss IOD routines with structured result types.
- Unified Python interface exposing strongly‑typed orbital element families (Keplerian / Equinoctial / Cometary).
- High‑throughput ingestion of observations (MPC 80-column, ADES XML, in‑memory NumPy paths; Parquet architecture in place).
- Batch orbit estimation with optional **parallel** execution (Rayon) and reproducible seeded randomness (SplitMix64).
- Rich error taxonomy surfaced as Python `RuntimeError` messages for ergonomic `try/except` handling.
- Pandas accessor (`DataFrame.outfit`) enabling vectorized IOD from tabular data with schema remapping.
- Extensive tutorials + API reference generated via `mkdocstrings`.
- Type stubs (`.pyi`) and `py.typed` shipped for first‑class IDE & MyPy support.

---
## ✨ Why pyOutfit?
Traditional Fortran IOD tooling can be opaque, single‑threaded, and hard to integrate in modern Python data pipelines. **pyOutfit** brings:

| Dimension | Value |
|-----------|-------|
| Performance | Rust core, optional parallelism, zero / single conversion ingestion paths |
| Determinism | Seeded batch execution & reproducible randomized selection phases |
| Ergonomics | Builder pattern for `IODParams`, typed containers (`TrajectorySet`, `Observations`) |
| Extensibility | Modular readers; element conversion APIs; observer catalog integration |
| Documentation | Tutorials, API docs, examples executed in CI |
| Safety | Explicit error variants mapped cleanly to Python exceptions |

---
## 🧠 Core Functional Domains
### Initial Orbit Determination (Gauss)
- Robust solver with configurable tolerances & physical plausibility filters.
- Preliminary + (where feasible) corrected solutions represented via `GaussResult`.
- RMS filtering & acceptability control utilities in parameter builder.

### Orbital Element Representations
- Keplerian, Equinoctial, and Cometary element families with conversion routines.
- Consistent unit model (AU, radians, Modified Julian Date) across types.

### Observations & Trajectories
- In‑memory trajectory grouping; mapping style container for per‑object access.
- Multiple ingestion pathways (file, XML, NumPy arrays, future Parquet) with reproducible ordering.

### Parallel Execution & Reproducibility
- Opt‑in parallel batch estimation (`do_parallel`) using Rayon.
- Controlled seeding (SplitMix64) for consistent randomized triplet selection phases.

### Python Integration
- GIL released for compute‑heavy sections.
- `.pyi` stubs for all public classes and functions; `py.typed` included.
- Pandas accessor (`outfit`) for DataFrame‑centric workflows.

---
## 🔍 Public Python API (Condensed)
| Symbol | Purpose |
|--------|---------|
| `PyOutfit` | Global environment (ephemerides, observatory catalog, error model) |
| `Observer` | Observatory lookup / custom registration |
| `IODParams` (+ `builder()`) | Configurable IOD filters, tolerances, parallel mode |
| `TrajectorySet` | Batch container + `estimate_all_orbits` orchestration |
| `Observations` | Per‑trajectory access & estimation (`estimate_best_orbit`) |
| `GaussResult` | Structured orbit solution (stages + element extraction) |
| `KeplerianElements` / `EquinoctialElements` / `CometaryElements` | Element families |

---
## ⚙️ Performance Characteristics
- Hot loops implemented in Rust; Python overhead minimized.
- Zero‑copy ingestion path for radian arrays; single conversion pass for degree inputs.
- Fat LTO and single codegen unit in release builds for aggressive optimization.
- Parallel scaling tested across typical multi‑core workstation environments.

---
## 🧪 Quality & Testing
- Pytest suite covering API surface, element conversions, trajectory parsing, and IOD flows.
- Tutorial snippets executed in CI to avoid documentation drift.
- Structured error paths tested for clarity and stability.

---
## 🧭 Error Model
Representative failure cases exposed as descriptive `RuntimeError` messages (originating from Rust `OutfitError` variants) including: no feasible triplets, non‑finite scores, and RMS computation failures.

---
## 📦 Installation
Until wheels are published, build from source:
```bash
python3.12 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip maturin
maturin develop  # or: maturin build --release && pip install target/wheels/py_outfit-*.whl
```
Requirements: Python 3.12, Rust ≥ 1.82, a C toolchain (e.g. `build-essential`).

---
## 🏁 Quick Start
```python
from py_outfit import PyOutfit, IODParams

# Initialize environment (ephemerides + reference observatory)
env = PyOutfit("horizon:DE440", "VFCC17")

# Configure Gauss IOD parameters
params = IODParams.builder() \
    .max_triplets(500) \
    .do_parallel(False) \
    .finalize()

# Suppose you have a prepared TrajectorySet (see tutorials)
# results = trajectory_set.estimate_all_orbits(env, params, seed=1234)
```
See tutorials for full end‑to‑end examples (batch ingestion, pandas workflows, result inspection & export).

---
## 🔄 Changelog Summary (Diff vs. Pre‑Release State)
- Added: Full Gauss IOD implementation + result container.
- Added: Parameter builder with physical & numerical filter configuration.
- Added: Orbital element families and conversion utilities.
- Added: Observation ingestion & trajectory batch orchestration.
- Added: Parallel execution support with deterministic seeding.
- Added: Pandas integration accessor (`DataFrame.outfit`).
- Added: Python type stubs + `py.typed` for tooling.
- Added: Comprehensive tutorials & API docs.
- Added: CI examples execution to ensure documentation accuracy.

---
## 🧭 Roadmap (Post‑1.0.0 Ideas)
- Publish pre‑built wheels for common Python/Rust targets.
- Additional IOD / differential correction algorithms (Laplace, Väisälä, full least‑squares refinement).
- Parquet ingestion finalized + columnar performance benchmarks.
- Extended ephemeris provider abstraction and caching strategies.
- Optional logging/telemetry hooks for large batch runs.

(Items are prospective and may change — see project issues for the live roadmap.)

---
## 🙏 Acknowledgments
Inspired by the legacy Fortran **OrbFit** codebase; reimagined for modern, parallel, and typed scientific Python workflows via Rust. Thanks to early adopters and testers who provided feedback on ergonomics and performance expectations.

---
## 📄 Licensing & Citation
Licensed under **CeCILL-C** (see `LICENSE`). If this project contributes to published research, please cite it (a formal CITATION.cff will be added in a subsequent minor release).

Example citation (provisional):
```
Le Montagner, R. (2025). pyOutfit 1.0.0: Rust-powered Gauss Initial Orbit Determination for Python. https://github.com/FusRoman/pyOutfit
```

---
## ✅ Integrity Checklist (Release Artifacts)
- [x] Version synchronized (`Cargo.toml`, dynamic in `pyproject.toml`).
- [x] Changelog entry for 1.0.0.
- [x] Type stubs included (`py.typed`).
- [x] Documentation site builds locally.
- [x] Test suite passes (Python + Rust integration).

---
**Enjoy fast & reproducible orbit determination with pyOutfit. Feedback and issues welcome!**
