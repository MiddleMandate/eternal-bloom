# Unified Field Theory of Eternal Bloom (UFT-EB)

**Author:** Alexander T. Sherrod
**Contact:** connect@alexandersherrod.com
**Website:** [eternalbloom.com](https://eternalbloom.com)

---

## Overview

The Unified Field Theory of Eternal Bloom (UFT-EB) proposes that classical reality emerges when internal informational coherence crosses a critical, observer-independent threshold. This repository contains the journal paper, simulation code, theoretical documents, and supporting data for the theory.

### Key Claims

- **Deterministic collapse:** Quantum-to-classical transition is determined by the system's informational state, not by random noise or external observers
- **Covariant formulation:** Fully relativistic tau-lock collapse with light-cone-localized stochastic coupling, no-signaling proof, and stress-energy conservation
- **Gravity from information:** Entropy-curvature coupling recovers GR in the classical limit while generating corrections at quantum and cosmological scales
- **Falsifiable predictions:** Specific experimental protocols for quantum optics, BECs, superconducting qubits, and cosmological observation

### Core Equations

**Bloom Field Equation:**

    nabla^2 DeltaPsi_i - Gamma_futures * Theta = 0

**Collapse Threshold:**

    H_bar(DeltaPsi_i) >= Phi_c

**GR Overlay:**

    G_{mu nu} = (8 pi G / c^4) * (E[T_{mu nu}] + lambda * Xi_{mu nu})

---

## Repository Structure

```
eternal-bloom-github/
|-- paper/
|   |-- UFT_EB_Journal_Paper.tex    # Full LaTeX source
|   |-- UFT_EB_Journal_Paper.pdf    # Compiled paper (11 pages)
|   |-- eternal_bloom_refs.bib      # 27+ BibTeX references
|
|-- simulations/
|   |-- uft-eb_phi_threshold_simulation_clean.py   # Qiskit 6-qubit threshold sim
|   |-- Bloom_UFT-EB_Simulation_REAL_FIXED.ipynb    # Lattice BFE notebook
|
|-- docs/
|   |-- UFT-EB_Covariant_Tau_Lock_Ansatz_v0.1.md   # Original tau-lock formulation
|   |-- UFT-EB_Covariant_Tau_Lock_Ansatz_UPDATED.md # Updated with visual schematic
|
|-- website/                        # Static site source (eternalbloom.com)
|-- data/images/                    # Simulation visualizations
|-- README.md
|-- LICENSE
```

## Running the Simulations

### Phi Threshold Simulation (Qiskit)

```bash
pip install qiskit qiskit-aer numpy
python simulations/uft-eb_phi_threshold_simulation_clean.py
```

Runs a 6-qubit quantum circuit with thermal noise (T1=50us, T2=30us) and increasing entangling depth. Monitors the coherence measure Phi and reports when the threshold Phi_c ~ 1.5 is crossed.

### Lattice BFE Simulation (Jupyter)

```bash
pip install numpy scipy matplotlib jupyter
jupyter notebook simulations/Bloom_UFT-EB_Simulation_REAL_FIXED.ipynb
```

Generates a 20x20 coherence lattice, computes Laplacian curvature, BFE residuals, and predictive anomaly maps.

## Citation

```bibtex
@article{Sherrod2026UFT-EB,
  author  = {Alexander T. Sherrod},
  title   = {Unified Field Theory of Eternal Bloom (UFT-EB): Informational Emergence, Threshold Collapse, and Covariant tau-Lock Dynamics in Quantum Systems},
  year    = {2026},
  note    = {Preprint}
}
```

## License

This work is shared for academic and research purposes. See LICENSE for details.

## Acknowledgments

The author acknowledges the use of GPT-4 (OpenAI) and Claude (Anthropic) as collaborative tools in developing the mathematical formalism and testing conceptual consistency. All core ideas and the foundational concept of informational threshold collapse originate with A.T. Sherrod.
