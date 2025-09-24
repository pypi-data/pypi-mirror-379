from tgqSim.circuit.quantum_circuit import QuantumCircuit
from tgqSim.gate.single_gate import *
from tgqSim.gate.double_gate import *
from tgqSim.sim.QuantumSimulator_v2 import QuantumSimulator
from tgqSim.circuit.decompose.compiler.transpiler import transpile

import numpy as np

if __name__ == '__main__':

    num_qubits = 3
    circuit = QuantumCircuit(num_qubits=num_qubits)
    circuit.h(0)
    circuit.append(H(1))
    circuit.cnot(0, 2)
    circuit.append(CP(1, 2, np.pi / 4))
    circuit.ccx(0, 1, 2)

    print(circuit)

    print("cpu simulator...")
    sim = QuantumSimulator()
    state = sim.run_statevector(circuit=circuit)
    print(state)

    # print("gpu simulator....")
    # sim = QuantumSimulator(device="gpu")
    # state = sim.run_statevector(circuit=circuit)
    # print(state)

    print("decompose quantum circuit...")
    # 芯片拓扑结构
    chip_topology = np.ones(shape=(circuit.num_qubits, circuit.num_qubits), dtype=np.int8)
    transpiled_circuit, _, _ = transpile(
            circuit=circuit,
            basis_double_qubit_gate=["cz"],
            basis_single_qubit_gate=["x", "y", "rx", "ry", "rz", "sx"],
            chip_topology=chip_topology,
            starting_physical_qubit_num=circuit.num_qubits
        )
    print(transpiled_circuit)