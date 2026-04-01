# UFT‑EB — Covariant τ‑Lock Ansatz v0.1

**Scope:** Minimal covariant formulation of τ‑lock collapse with light‑cone–localized stochasticity, no‑signaling in expectation, and conservation properties. Assumptions are explicit and limited to flat background for clarity (curved background notes included).

---

## 1. Kinematics and States (Tomonaga–Schwinger Form)

- Spacetime $(\mathcal{M}, g_{\mu\nu})$; in flat case, $g_{\mu\nu}=\eta_{\mu\nu}$.
- Quantum state is assigned to a spacelike hypersurface $\Sigma$: $\lvert \Psi(\Sigma)\rangle$ (Tomonaga–Schwinger picture).
- Local fields $\hat{\Phi}_a(x)$ with microcausality: $[\hat{\Phi}_a(x), \hat{\Phi}_b(y)]=0$ if $(x-y)^2<0$.

Deterministic evolution (no collapse) is:

$$i\hbar\,\delta \lvert \Psi(\Sigma)\rangle = \int_{\Sigma} d\sigma_\mu(x)\, n^\mu(x)\,\hat{\mathcal{H}}_{\text{int}}(x)\,\lvert \Psi(\Sigma)\rangle$$

where $n^\mu$ is the future‑directed unit normal to $\Sigma$.

---

## 2. Local Collapse Generator and Noise (Relativistic CSL-style, Light-Cone Localized)

Introduce a **local collapse density** $\hat{L}(x)$ (Hermitian scalar operator built from local field densities; examples: smeared mass/number/energy density).

Stochastic state update on an infinitesimal deformation of $\Sigma$ at $x$:

$$d\lvert \Psi(\Sigma)\rangle = \int_{\Sigma} d\sigma_\mu(x)\, n^\mu(x)\, \Big\{ \sqrt{\gamma}\, \big(\hat{L}(x) - \langle \hat{L}(x)\rangle_\Sigma\big)\, dW_x -\tfrac{\gamma}{2}\, \big(\hat{L}(x)-\langle \hat{L}(x)\rangle_\Sigma\big)^2 d^4x \Big\} \lvert \Psi(\Sigma)\rangle$$

with coupling $\gamma>0$.

**Noise field $dW_x$**:
- Zero mean, Lorentz-invariant covariance with light-cone-localized kernel:

$$\mathbb{E}[\,dW_x\, dW_y\,] = K_\ell(x-y)\, d^4x\, d^4y$$

$$K_\ell(z) = \frac{1}{\mathcal{N}_\ell}\, f\!\big(\sigma(z)/\ell^2\big)$$

where $\sigma(z)=g_{\mu\nu}z^\mu z^\nu$ and $f$ is sharply peaked on $\sigma\approx 0$ (null-separation) and decays rapidly outside the light cone; $\ell$ is an invariant correlation length; $\mathcal{N}_\ell$ normalizes $K_\ell$.

> **Note:** In curved spacetime, replace $K_\ell(x-y)$ by the Hadamard parametrix $K_\ell(x,y)$ constructed from Synge's world function and parallel transport, preserving local covariance.

---

## 3. τ-Lock Trigger (Observer-Independent Threshold)

Define a **local information-flux density** $\varphi(x)$ and an **integrated scalar** $\Phi[\Sigma; \mathcal{O}]$:

$$\varphi(x) \equiv \alpha_1\, \dot{S}(x) + \alpha_2\, \mathcal{I}_F(x) + \alpha_3\, \Vert \nabla \rho(x)\Vert^2 + \cdots$$

$$\Phi[\Sigma;\mathcal{O}] \equiv \int_{\mathcal{O}\cap J^-(\Sigma)} d^4y\, w_\tau(\Sigma,y)\, \varphi(y)$$

The **τ-lock condition** is: **Collapse at the earliest hypersurface** $\Sigma^\star$ for which $\Phi[\Sigma^\star;\mathcal{O}] \ge \Phi_c\big(n(\mathcal{O})\big)$, with threshold scaling $\Phi_c(n)$ monotonically increasing in complexity $n$.

---

## 4. No-Signaling (Expectation-Value Argument, Sketch)

For any local observable $\hat{A}(x)$ and any choice of spacelike-separated operation $\hat{\mathcal{O}}(y)$, $x \nsim y$:

$$\partial_\Sigma \,\mathbb{E}\big[\langle \hat{A}(x) \rangle\big] =\mathbb{E}\Big[\tfrac{i}{\hbar}\langle [\hat{\mathcal{H}}_{\text{int}}(x),\hat{A}(x)]\rangle + \gamma\, \mathcal{D}_{\hat{L}_\ell(x)}[\hat{A}(x)]\Big]$$

By microcausality and the support of $K_\ell$ on/null to $x$, **spacelike operations at $y$ do not alter the marginal evolution of $\langle \hat{A}(x)\rangle$**. Hence **no superluminal signaling in expectation**.

---

## 5. Conservation in Expectation & Born Rule

- Define renormalized stress-energy $\hat{T}^{\mu\nu}(x)$ and require conservation under the stochastic dynamics.
- Choose $\hat{L}(x)$ and counter-drift such that:

$$\nabla_\mu \,\mathbb{E}\big[T^{\mu\nu}(x)\big]=0 + \mathcal{O}(e^{-\ell^{-1}\,\mathrm{dist}})$$

i.e., conserved up to exponentially suppressed smearing errors.

- **Born rule:** The nonlinear drift is the Girsanov correction that ensures the state-norm is a martingale; standard arguments then yield Born probabilities for outcomes of $\hat{L}$-compatible POVMs on $\Sigma$.

---

## 6. Entropy-Curvature Coupling (GR Overlay)

$$G_{\mu\nu}[\mathbb{E}(g)] = \frac{8\pi G}{c^4}\,\Big(\mathbb{E}[T_{\mu\nu}] + \lambda\, \Xi_{\mu\nu}[\varphi,\Phi]\Big)$$

where $\Xi_{\mu\nu}$ is a symmetric, divergence-free functional of information densities, and $\lambda$ sets coupling strength. In the no-collapse/low-info limit, $\Xi_{\mu\nu}\to 0$ and **GR is recovered**.

---

## 7. Boundary Conditions & Parameters

- Smearing scale $\ell$ (invariant), τ-window kernel $w_\tau$, collapse rate $\gamma$, and threshold law $\Phi_c(n)$.
- Flat background for Sections 2-5; curved generalization via Hadamard kernels and local tetrads.
- Microcausality assumed for the underlying QFT algebra.

---

## 8. Aeondex Event Record (for Objectivity & Audits)

On each τ-lock: record tuple $\mathcal{E} = (x^{\star\mu}, \Sigma\text{-ID}, \text{mode/eigenlabel of }\hat{L}, \Delta S, \Phi, \text{Reverb }R, \text{hash/state digest})$.

Aeondex is append-only and covariant (coordinates replaced by invariant identifiers in curved backgrounds).

---

## 9. Checklist Status (Task 1)

- [x] Define τ-lock trigger in covariant form
- [x] Light-cone localized noise term (invariant kernel $K_\ell$)
- [x] No-signaling argument in expectation (sketch)
- [x] Stress-energy conservation in expectation (conditions)
- [x] Assumptions & boundary conditions documented

**Next:** integrate these axioms into the "Minimal Field Axioms" document and implement the 1+1D toy lattice to visualize causal cones and conservation diagnostics.
