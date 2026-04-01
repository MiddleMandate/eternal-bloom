from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.providers.aer.noise import NoiseModel, thermal_relaxation_error
from qiskit.quantum_info import Statevector, partial_trace, entropy
import numpy as np

# CONFIGURATION
n_qubits = 6
entangling_depth = 3
phi_threshold = 1.5
num_steps = 5

# NOISE MODEL (Decoherence)
noise_model = NoiseModel()
relax_error = thermal_relaxation_error(t1=50, t2=30, time=0.1)
for i in range(n_qubits):
    noise_model.add_quantum_error(relax_error, ['id'], [i])

# DeltaPsi INTERACTION LAYER
def apply_delta_psi_layer(qc, depth):
    for d in range(depth):
        for i in range(0, n_qubits - 1, 2):
            qc.h(i)
            qc.cx(i, i + 1)
        for i in range(1, n_qubits - 1, 2):
            qc.h(i)
            qc.cx(i, i + 1)

# Phi CALCULATION FUNCTION
def compute_phi(statevec):
    max_phi = 0
    for i in range(1, n_qubits):
        traced_out = partial_trace(statevec, [i])
        entropy_s = entropy(traced_out)
        if entropy_s > max_phi:
            max_phi = entropy_s
    return max_phi

# SIMULATION LOOP
phi_log = []
for step in range(num_steps):
    qc = QuantumCircuit(n_qubits)
    qc.h(range(n_qubits))
    apply_delta_psi_layer(qc, step + 1)
    qc.barrier()

    backend = Aer.get_backend('statevector_simulator')
    compiled = transpile(qc, backend)
    result = execute(qc, backend, noise_model=noise_model).result()
    state = Statevector(result.get_statevector())

    phi_value = compute_phi(state)
    phi_log.append(phi_value)
    print(f"Step {step + 1}: Phi(t) = {phi_value:.3f}")

    if phi_value >= phi_threshold:
        print("Awareness threshold Phi_c crossed -- collapse triggered.")
        break
    else:
        print("...Phi below threshold. System remains probabilistic.")
