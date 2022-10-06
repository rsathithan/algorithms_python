"""
Build the quantum full adder (QFA) for any sum of
two quantum registers and one carry in. This circuit
is designed using the Qiskit framework. This
experiment run in IBM Q simulator with 1000 shots.
.
References:
https://www.quantum-inspire.com/kbase/full-adder/
"""

import qiskit
from qiskit import Aer, ClassicalRegister, QuantumCircuit, QuantumRegister, execute


def q_full_adder(
    inp_1: int = 1, inp_2: int = 1, cin: int = 1
) -> qiskit.result.counts.Counts:
    """
    # >>> q_full_adder(inp_1, inp_2, cin)
    # the inputs can be 0/1 for qubits in define
    # values, or can be in a superposition of both
    # states with hadamard gate using the input value 2.
    # result for default values: {11: 1000}
    qr_0: ──■────■──────────────■──
            │  ┌─┴─┐          ┌─┴─┐
    qr_1: ──■──┤ X ├──■────■──┤ X ├
            │  └───┘  │  ┌─┴─┐└───┘
    qr_2: ──┼─────────■──┤ X ├─────
          ┌─┴─┐     ┌─┴─┐└───┘
    qr_3: ┤ X ├─────┤ X ├──────────
          └───┘     └───┘
    cr: 2/═════════════════════════
    Args:
        inp_1: input 1 for the circuit.
        inp_2: input 2 for the circuit.
        cin: carry in for the circuit.
    Returns:
        qiskit.result.counts.Counts: sum result counts.
    """
    # build registers
    qr = QuantumRegister(4, "qr")
    cr = ClassicalRegister(2, "cr")
    # list the entries
    entry = [inp_1, inp_2, cin]

    quantum_circuit = QuantumCircuit(qr, cr)

    for i in range(0, 3):
        if entry[i] == 2:
            quantum_circuit.h(i)  # for hadamard entries
        elif entry[i] == 1:
            quantum_circuit.x(i)  # for 1 entries
        else:
            quantum_circuit.i(i)  # for 0 entries

    # build the circuit
    quantum_circuit.ccx(0, 1, 3)  # ccx = toffoli gate
    quantum_circuit.cx(0, 1)
    quantum_circuit.ccx(1, 2, 3)
    quantum_circuit.cx(1, 2)
    quantum_circuit.cx(0, 1)

    quantum_circuit.measure([2, 3], cr)  # measure the last two qbits

    backend = Aer.get_backend("qasm_simulator")
    job = execute(quantum_circuit, backend, shots=1000)

    return job.result().get_counts(quantum_circuit)


if __name__ == "__main__":
    print(f"Total sum count for state is: {q_full_adder()}")
