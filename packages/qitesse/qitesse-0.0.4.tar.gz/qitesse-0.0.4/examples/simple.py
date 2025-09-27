from qitesse import Circuit, Gate

circuit = Circuit(gates = [
    Gate.h(0),
    Gate.crz(0, 1, 3.14/2),
    Gate.h(1),
    Gate.cnot(0, 1),
])
print(circuit.run(2))