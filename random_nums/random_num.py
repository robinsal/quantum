import projectq.setups.ibm
from projectq.backends import IBMBackend
from projectq import MainEngine
from projectq.ops import H, Measure

# this function theoretically will return a truly random number
# if connected to a quantum computer
def generate_random(engine):
	# generate a bit string length 20 with each bit equally likely to be 0 or 1
	bit_string = ''
	for i in range(20):
		qubit = engine.allocate_qubit()
		H | qubit	# the hadamard gate puts the qubit in superposition right
					# in between 0 and 1
		Measure | qubit
		bit_string += str(int(qubit))

	bin_to_int = int(bit_string, 2)
	max_int = int('1' * 20, 2)
	return bin_to_int / max_int # divide by max possibility to keep # in [0, 1]


# This engine is a quantum simulator, it is not actually going to produce a
# truly random number because it is run with a normal computer which cannot
# produce truly random numbers
eng = MainEngine()
print(generate_random(eng))
eng.flush()

# Now we will run it with a quantum computer backend. This number should in
# theory be truly random
