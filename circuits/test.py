from projectq.backends import CircuitDrawer
from projectq import MainEngine
from projectq.ops import H, CNOT, X, Y

circuit_backend = CircuitDrawer()
eng = MainEngine(circuit_backend)
q1 = eng.allocate_qubit()
q2 = eng.allocate_qubit()
H | q1
CNOT | (q1, q2)
X | q2
Y | q1
eng.flush()


print(circuit_backend.get_latex())
