# Quantum Programming Examples

## Random Number Generation
An interesting application of quantum computing is that it can theoretically produce truly random numbers. To understand why,
we need to understand what quantum computers are. Without going deeply into it, quantum computers basically have chips so
small, that the transistors begin to exhibit phenomena of quantum mechanics (I am not an expert, and it is possible that this
is a flawed explanation).

In quantum computing, instead of bits (0 **OR** 1), there are qubits, a probabilistic value that will either turn into 0
or 1. In other words, a qubit is somewhere in *superposition*, or in between 0 and 1, and when it is observed it will 
*collapse* into 0 or 1, with the probability of the result depending on its superposition. If its superposition is such
that it is equally likely to collapse into 0 or 1, it is theoretically completely random which one it'll collapse to. 

Using this, we can create a truly random number generator. Unfortunately, my 'truly random' number generator actually relies
on a quantum simulator, instead of an actual quantum computer, so it is actually a simulated truly random number generator.

It works like so:
  Generate a qubit. Put it into perfect superposition between 0 and 1 with what's known as a Hadamard gate. Measure it
  (so that it collapses to either 0 or 1) and append it to a bit string. Do this 20 times to get a 20-bit bit string.
  Convert that string to an integer and divide by the maximum possibility ('11111...111').
  
The results:
  This will produce an integer from [0, 2^20] with each possiblity equally likely. It then divides it by 2^20 resulting in
  a float in [0, 1]. However, it is a discrete set of floats. For a bit string of length n, the generated number is of the
  set: [0, 1/(2^n - 1), 2/(2^n - 1), ... , (2^n - 2)/(2^n - 1), 1]. So therefore, since this generates 20 qubits to create the
  bit string the total number of possible outcomes is actually 1,048,576 or 2^20.
  
There very well may be better algorithms to generate random numbers with quantum computers, but this is the solution I came
up with.
