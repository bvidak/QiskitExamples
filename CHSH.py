import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
#from qiskit_aer.primitives import Sampler
#from qiskit_ibm_runtime import SamplerV2 as Sampler
from qiskit.providers.basic_provider import BasicSimulator 
from qiskit.visualization import *
from numpy.random import randint
import numpy as np

def chsh_game(strategy):
 
    # Referee chooses x and y randomly
    x, y = randint(0, 2), randint(0, 2)

    # Use strategy to choose a and b
    a, b = strategy(x, y)

    # Referee decides if Alice and Bob win or lose
    if (a != b) == (x & y):
        return 1  # Win
    return 0  # Lose

def chsh_circuit(x, y):
    qc = QuantumCircuit(2,  2)
    qc.h(0)
    qc.cx(0, 1)
    qc.barrier()

    # Alice
    if x == 0:
        qc.ry(0, 0)
    else:
        qc.ry(-np.pi / 2, 0)
    qc.measure(0, 0)

    # Bob
    if y == 0:
        qc.ry(-np.pi / 4, 1)
    else:
        qc.ry(np.pi / 4, 1)
    qc.measure(1, 1)

    return qc


print("(x,y) = (0,0)")
plt.show(chsh_circuit(0, 0).draw(output='mpl', style='iqp'))

print("(x,y) = (0,1)")
plt.show(chsh_circuit(0, 1).draw(output='mpl', style='iqp'))

print("(x,y) = (1,0)")
plt.show(chsh_circuit(1, 0).draw(output='mpl', style='iqp'))

print("(x,y) = (1,1)")
plt.show(chsh_circuit(1, 1).draw(output='mpl', style='iqp'))


#sampler = Sampler()
sim_backend = BasicSimulator()

def quantum_strategy(x, y):
    # `shots=1` runs the circuit once
    result = sim_backend.run(chsh_circuit(x, y), shots=100).result()
    #statistics = result.quasi_dists[0].binary_probabilities()
    #bits = list(statistics.keys())[0]
    #a, b = bits[0], bits[1]
    #return a, b
    return result.get_counts()


print(quantum_strategy(1,1))

plt.show(plot_histogram(quantum_strategy(1,1)))

"""
sim_backend = BasicSimulator()
job = sim_backend.run(transpile(circuit, sim_backend), shots=1024)
result = job.result()
print("Basic simulator : ")
 
counts = result.get_counts()
 

plt.show(plot_histogram(counts))
 

NUM_GAMES = 10000
TOTAL_SCORE = 0

for _ in range(NUM_GAMES):
    TOTAL_SCORE += chsh_game(quantum_strategy)

print("Fraction of games won:", TOTAL_SCORE / NUM_GAMES)



"""