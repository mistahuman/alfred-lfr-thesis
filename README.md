# Thesis, Slides & Paper - Marco Lanconelli's Degree

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Alma Mater Studiorum, Università di Bologna**  
Corso di Laurea Magistrale in Ingegneria Energetica — A.A. 2018/2019

> *Modellazione di un reattore nucleare LFR e implementazione su piattaforma con accoppiamento neutronico-termoidraulico*  
> (Modelling of a Lead-cooled Fast Reactor and implementation on a multi-physics platform with neutronics-thermohydraulics coupling)

---

## Abstract

This work presents the modelling and simulation of a Generation-IV Lead-cooled Fast Reactor (LFR) inspired by the **ALFRED** (Advanced Lead Fast Reactor European Demonstrator) concept design. The focus is on the coupling between neutronics and thermohydraulics on the **FEMuS** multi-physics platform. Neutronic calculations were performed with **DRAGON5/DONJON5** to generate homogenised cross-section libraries feeding a coupled full-core steady-state solver.

**Key topics:** neutron transport, multi-group cross-section generation, nodal diffusion, FEM thermal-hydraulics, neutronics–thermohydraulics coupling, LFR safety parameters.

---

## Documents

| Document | PDF |
|----------|-----|
| Master's thesis | [thesis_lanconelli.pdf](thesis/thesis_lanconelli.pdf) |
| Defence presentation | [slides_lanconelli.pdf](slides-thesis/main/slides_lanconelli.pdf) |
| Conference presentation | [slides_conference.pdf](slides-conference/main/slides_conference.pdf) |
| Conference paper | [a_multiphysics_approach_to_lfr_analysis_final.pdf](paper/a_multiphysics_approach_to_lfr_analysis_final.pdf) |

### Related publications

The conference paper was presented at the **IAEA Technical Meeting on Small Modular Fast Reactors** and published in:

> M. Lanconelli, M. Sumini, S. Manservisi — *"A Multiphysics Approach to LFR Analysis"*  
> in *Benefits and Challenges of Small Modular Fast Reactors*, IAEA-TECDOC-1972, Wien, 2021, pp. 280–291

- [IAEA TECDOC-1972 (full volume)](https://www-pub.iaea.org/MTCD/Publications/PDF/TE-1972web.pdf)
- [Conference presentation slides](https://conferences.iaea.org/event/204/contributions/15892/attachments/8238/10876/09-presentation_sumini_26_9.pdf)
- [UniBo CRIS record](https://cris.unibo.it/handle/11585/906623?mode=simple)

---

## Computational workflow

The simulation is a four-step pipeline:

```
┌─────────────────────────────────────────────────────────────────┐
│  STEP 0 — Mesh generation (SALOME)                              │
│  code/med/Esagoni.py  →  esagoni10.med                          │
│  3D hexagonal core mesh for the FEM thermal-hydraulics solver   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  STEP 1 — Lattice transport (DRAGON5)                           │
│  Input: JEFF 3.1.2 nuclear data library (315 energy groups)     │
│                                                                 │
│  smr_fissile.x2m    →  ACOMPO1  (inner fissile assembly, MOX)   │
│  smr_fissile_ex.x2m →  ACOMPO3  (outer fissile assembly)        │
│  smr_solide33.x2m   →  ACOMPO4  (structural/reflector)          │
│                                                                 │
│  Each run: self-shielding → flux (B1) → homogenisation          │
│  + condensation 315 → 33 groups, over a burnup/temperature grid │
│  Output: multi-parameter COMPO tables in code/compo/SMRcompo33/ │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  STEP 2 — Full-core neutronics (DONJON5)                        │
│  Input: ACOMPO1, ACOMPO2 (=ACOMPO1), ACOMPO3, ACOMPO4           │
│                                                                 │
│  smr_core.x2m with procedures:                                  │
│    GeoCo.c2m       — hexagonal core geometry (9 rings)          │
│    SetFuelMap.c2m  — assembly-type map                          │
│    SetParam.c2m    — burnup/temperature parameters              │
│    alf_N_Pb.c2m    — lead density from temperature              │
│                                                                 │
│  Method: nodal diffusion, SPN-3, Raviart-Thomas-Schneider       │
│  Cases: rods extracted (TBE) / inserted (TBI) / half (THALF)    │
│  Output: k_effective, 3D power distribution                     │
└───────────────────────────┬─────────────────────────────────────┘
                            │
┌───────────────────────────▼─────────────────────────────────────┐
│  STEP 3 — Neutronics–thermohydraulics coupling (FEMuS)          │
│  Input: power map (DONJON5) + mesh (SALOME)                     │
│                                                                 │
│  IniPowCompo.c2m   — initialise coupled power component         │
│  PowComponent.c2m  — DONJON5 side of the coupling interface     │
│                                                                 │
│  Iterative loop until convergence:                              │
│    DONJON5  →  power distribution  →  FEMuS (FEM heat solver)   │
│    FEMuS    →  temperature/density fields  →  DONJON5           │
│  Output: converged steady-state neutronics + temperature fields │
└─────────────────────────────────────────────────────────────────┘
```

---

## Code

### Disclaimer and credits

This code was developed as part of my Master's thesis at the
**Laboratorio di Montecuccolino** (LABO — Nuclear Engineering Laboratory,
Università di Bologna) under the supervision of:

- Prof. Sandro Manservisi
- Prof. Marco Sumini
- Prof. Ruben Scardovelli
- Ing. Valentina Giovacchini
- Ing. Andrea Chierici
- Ing. Leonardo Chirco

Several scripts were developed collaboratively within the lab and build
on existing tools and procedures from the DRAGON5/DONJON5 ecosystem.
Credit belongs to everyone involved — I am publishing this purely as
an archive of the work done, not as a claim of sole authorship.

**A note on reproducibility:** this work was completed in 2018–2019 and
several years have passed since. I no longer have detailed memory of
every implementation choice, and I cannot guarantee the code runs
out of the box even with all the required tools in place.

The code is **not self-contained** and cannot be run without:

- **DRAGON5 / DONJON5** — licensed from École Polytechnique de Montréal
- **JEFF 3.1.2 nuclear data library** — distributed by OECD/NEA (large binary files, not included in this repository)
- **FEMuS** multi-physics platform — with HPC dependencies (PETSc, libMesh, HDF5, SALOME MEDCoupling)
- **SALOME** — open source, required only to regenerate the mesh

The pre-computed libraries in `code/compo/` allow running DONJON5 (Step 2)
without re-running the DRAGON5 lattice calculations (Step 1).

---

### `code/dragon/` — DRAGON5 lattice transport

Lattice-level neutron transport calculations for each assembly type.
Each produces a multi-parameter cross-section library (COMPO) as output.

| File | Assembly type | Output |
|------|--------------|--------|
| `smr_fissile.x2m` | Inner fissile (MOX fuel, standard enrichment) | `ACOMPO1` |
| `smr_fissile_ex.x2m` | Outer fissile (MOX fuel, extended enrichment) | `ACOMPO3` |
| `smr_solide33.x2m` | Structural / reflector assemblies | `ACOMPO4` |

Each run: pin-cell geometry (7 radial zones) → self-shielding → flux (B1) →
homogenisation + condensation 315 → 33 groups, over a grid of burnup steps
(0–1095 days), fuel temperatures (400–1000 °C), and lead coolant density.

The `.access` files are shell scripts that set up the run directory before
launching DRAGON5. `smr_proc/` contains shared CLE-2000 procedures
(geometry, cross-section composition, library initialisation, interpolation).

---

### `code/donjon/` — DONJON5 full-core neutronics

**Main script:** `smr_core.x2m` — reads ACOMPO1–4, constructs the full
hexagonal core (9 rings), runs steady-state nodal diffusion (SPN-3,
Raviart-Thomas-Schneider, 33 groups), outputs k_effective and 3D power
distribution. Three rod configurations: TBE (extracted), TBI (inserted),
THALF (half inserted).

**Procedures in `smr_core_proc/`:**

| Procedure | Purpose |
|-----------|---------|
| `GeoCo.c2m` | Hexagonal full-core geometry (assembly-level mesh) |
| `SetFuelMap.c2m` | Fuel assembly type map over the core |
| `SetParam.c2m` | Burnup and temperature parameters in the fuel map |
| `alf_N_Pb.c2m` | Lead density from coolant temperature |
| `IniPowCompo.c2m` | Initialises the power component for the coupled FEMuS run |
| `PowComponent.c2m` | DONJON5 reactor physics component used in the coupling loop |

---

### `code/compo/` — Pre-computed cross-section libraries

Binary COMPO files output by DRAGON5, used as input to DONJON5.

| Directory | Groups | Notes |
|-----------|--------|-------|
| `SMRcompo33/` | 33 | Used in the thesis calculations |
| `SMRcompo5/` | 5 | Further condensed — used for faster test runs |

Within `SMRcompo33/`: `ACOMPO1` (fissile inner), `ACOMPO3` (fissile extended),
`ACOMPO4` (structural/reflector), `ABURNUP` (burnup data).
`B/` and `N/` are variants with control rods inserted (TBI) and neutron
absorber rods respectively.

---

### `code/med/` — SALOME geometry and mesh

| File | Purpose |
|------|---------|
| `Esagoni.py` | SALOME v9.2.0 script — builds the 3D hexagonal core geometry and generates the structured hexahedral mesh via axial extrusion |
| `esagoni10.med` | Pre-generated MED mesh file — used directly by FEMuS |

9 rings of hexagonal assemblies, 15 axial planes, total height 350 cm.
Quadratic elements for the FEM thermal solver.

---

## Building the documents

```bash
bash install.sh   # install LaTeX dependencies (Ubuntu/Debian)
make              # compile all documents
make thesis       # → thesis/thesis_lanconelli.pdf
make slides-thesis      # → slides-thesis/main/slides_lanconelli.pdf
make slides-conference  # → slides-conference/main/slides_conference.pdf
make clean        # remove auxiliary files, keep PDFs
make cleanall     # remove auxiliary files and PDFs
```

---

## Tools

| Tool | Purpose |
|------|---------|
| [DRAGON5](https://www.polymtl.ca/merlin/) | Lattice neutron transport — cross-section generation |
| [DONJON5](https://www.polymtl.ca/merlin/) | Full-core nodal diffusion solver |
| FEMuS | Multi-physics FEM platform (thermohydraulics + coupling) — internal tool, Università di Bologna |
| [SALOME](https://www.salome-platform.org/) | 3D geometry and mesh generation |
| LaTeX / pdflatex | Document typesetting |

---

*This README was written with the assistance of [Claude](https://claude.ai) (Anthropic).*
