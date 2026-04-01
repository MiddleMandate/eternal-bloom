# UFT-EB -- Covariant Tau-Lock Ansatz v0.1 (Updated)

**Scope:** Minimal covariant tau-lock collapse formulation with light-cone-localized stochastic coupling, threshold condition, no-signaling argument, and conservation in expectation. This updated version includes a visual schematic.

---

## 1. State Evolution Framework

- **Spacetime:** (M, g_uv); flat case g_uv = eta_uv.
- **State on hypersurface Sigma:** |Psi(Sigma)>.
- **Microcausality:** [Phi_a(x), Phi_b(y)] = 0 if (x-y)^2 < 0.

Deterministic Tomonaga-Schwinger evolution (no collapse):
i*hbar delta|Psi(Sigma)> = integral_Sigma d*sigma_u(x) n^u(x) H_int(x) |Psi(Sigma)>.

---

## 2. Collapse Generator & Light-Cone Noise

- **Local collapse operator:** L(x) (e.g., smeared energy density).
- **Stochastic update:**
d|Psi(Sigma)> = integral_Sigma d*sigma_u(x) n^u(x) [ sqrt(gamma)(L(x) - <L(x)>) dW_x - gamma/2 (L(x) - <L(x)>)^2 d^4x ] |Psi(Sigma)>.

- **Noise field covariance:**
E[dW_x dW_y] = K_ell(x-y) d^4x d^4y
with K_ell peaked near null separation sigma(x-y) ~ 0 (light cone).

---

## 3. Tau-Lock Threshold Condition

Define information-flux density phi(x) and integrated scalar:
Phi[Sigma; O] = integral_{O cap J^-(Sigma)} d^4y w_tau(Sigma,y) phi(y).

**Collapse trigger:** First Sigma* where Phi[Sigma*; O] >= Phi_c(n(O))
with n = complexity index; Phi_c increasing in n.

---

## 4. No-Signaling & Conservation

- **No-signaling:** Expectation values evolve independently of spacelike-separated operations by microcausality + null-localized kernel.
- **Conservation:** Chosen L and drift ensure div E[T^uv] = 0 up to vanishing smearing errors.

---

## 5. GR Overlay

G_uv[E(g)] = (8*pi*G/c^4) * (E[T_uv] + lambda * Xi_uv[phi, Phi]).

---

## Visual Schematic

Below: tau-lock collapse event localized near the light cone.

![tau-lock schematic](tau_lock_light_cone_schematic.png)

---

**Checklist (Task 1)**
- [x] Covariant tau-lock trigger
- [x] Light-cone noise kernel
- [x] No-signaling argument
- [x] Conservation condition
- [x] Assumptions documented
