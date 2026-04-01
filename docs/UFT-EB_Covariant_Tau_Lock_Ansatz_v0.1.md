# UFT-EB -- Covariant Tau-Lock Ansatz v0.1

**Scope:** Minimal covariant formulation of tau-lock collapse with light-cone-localized stochasticity, no-signaling in expectation, and conservation properties.

---

## 1. Kinematics and States (Tomonaga-Schwinger Form)

- Spacetime (M, g_uv); in flat case, g_uv = eta_uv.
- Quantum state assigned to spacelike hypersurface Sigma: |Psi(Sigma)> (Tomonaga-Schwinger picture).
- Local fields with microcausality: [Phi_a(x), Phi_b(y)] = 0 if (x-y)^2 < 0.

Deterministic evolution (no collapse):
i*hbar * delta|Psi(Sigma)> = integral_Sigma d*sigma_u(x) n^u(x) H_int(x) |Psi(Sigma)>

---

## 2. Local Collapse Generator and Noise (Relativistic CSL-style, Light-Cone Localized)

Introduce a local collapse density L(x) (Hermitian scalar operator built from local field densities).

Stochastic state update on infinitesimal deformation of Sigma at x:
d|Psi(Sigma)> = integral_Sigma d*sigma_u(x) n^u(x) { sqrt(gamma) (L(x) - <L(x)>) dW_x - gamma/2 (L(x) - <L(x)>)^2 d^4x } |Psi(Sigma)>

Noise field dW_x: Zero mean, Lorentz-invariant covariance with light-cone-localized kernel:
E[dW_x dW_y] = K_ell(x-y) d^4x d^4y
K_ell(z) = (1/N_ell) f(sigma(z)/ell^2)

where sigma(z) = g_uv z^u z^v and f is sharply peaked on sigma ~ 0 (null-separation).

> **Note:** In curved spacetime, replace K_ell(x-y) by the Hadamard parametrix K_ell(x,y).

---

## 3. Tau-Lock Trigger (Observer-Independent Threshold)

Define local information-flux density phi(x) and integrated scalar Phi[Sigma; O]:
phi(x) = alpha_1 S_dot(x) + alpha_2 I_F(x) + alpha_3 ||grad rho(x)||^2 + ...
Phi[Sigma; O] = integral_{O cap J^-(Sigma)} d^4y w_tau(Sigma,y) phi(y)

**Tau-lock condition:** Collapse at earliest hypersurface Sigma* for which Phi[Sigma*; O] >= Phi_c(n(O)), with threshold scaling Phi_c(n) monotonically increasing in complexity n.

---

## 4. No-Signaling (Expectation-Value Argument, Sketch)

By microcausality and the support of K_ell on/null to x, spacelike operations at y do not alter the marginal evolution of <A(x)>. Hence no superluminal signaling in expectation.

---

## 5. Conservation in Expectation & Born Rule

- Conserved up to exponentially suppressed smearing errors: div E[T^uv(x)] = 0 + O(exp(-ell^-1 * dist))
- Born rule: The nonlinear drift is the Girsanov correction ensuring state-norm is a martingale.

---

## 6. Entropy-Curvature Coupling (GR Overlay)

G_uv[E(g)] = (8*pi*G/c^4) * (E[T_uv] + lambda * Xi_uv[phi, Phi])

where Xi_uv is a symmetric, divergence-free functional of information densities. In the no-collapse/low-info limit, Xi_uv -> 0 and GR is recovered.

---

## 7. Boundary Conditions & Parameters

- Smearing scale ell (invariant), tau-window kernel w_tau, collapse rate gamma, threshold law Phi_c(n)
- Flat background for Sections 2-5; curved generalization via Hadamard kernels and local tetrads
- Microcausality assumed for the underlying QFT algebra

---

## 8. Aeondex Event Record

On each tau-lock: record tuple E = (x*^u, Sigma-ID, mode/eigenlabel of L, Delta S, Phi, Reverb R, hash/state digest). Append-only and covariant.

---

## 9. Checklist Status

- [x] Define tau-lock trigger in covariant form
- [x] Light-cone localized noise term (invariant kernel K_ell)
- [x] No-signaling argument in expectation (sketch)
- [x] Stress-energy conservation in expectation (conditions)
- [x] Assumptions & boundary conditions documented

**Next:** Integrate these axioms into the Minimal Field Axioms document and implement the 1+1D toy lattice.
