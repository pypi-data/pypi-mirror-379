from typing import List, Union
def check_bitwise_validity(qubits: Union[int, List[int]], num_qubits: int) -> None:
    qubits = [qubits] if isinstance(qubits, int) else qubits
    qubits_set = set(qubits)
    if len(qubits_set) != len(qubits):
        raise ValueError("Qubits should be unique.")
    for qubit in qubits:
        if qubit < 0 or qubit >= num_qubits:
            raise ValueError(f"Qubit index {qubit} is out of range for a circuit with {num_qubits} qubits.")