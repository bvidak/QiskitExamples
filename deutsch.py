# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 13:10:30 2023

@author: Brani Vidakovic
"""

'''
    Deutsch-Jozsa Algorithm

    Consider a function f(x) that takes as input n-bit strings x and returns 0 or 1. Suppose we are
    promised that f(x) is either a constant function that takes the same value c in {0,1} on all
    inputs x, or a balanced function that takes each value 0 and 1 on exactly half of the inputs. 
    The goal is to decide whether f is constant or balanced by making as few function evaluations 
    as possible. Classically, it requires 2^{n-1}+1 function evaluations in the worst case. Using 
    the Deutsch-Jozsa algorithm, the question can be answered with just one function evaluation.
    
    Deutsch's algorithm is the simpler case of Deutsch-Jozsa Algorithm which has a function f(x) 
    which takes 1-bit as input.

    Source: https://github.com/Qiskit/ibmqx-user-guides/blob/master/rst/full-user-guide/004-Quantum_Algorithms/080-Deutsch-Jozsa_Algorithm.rst

'''

import matplotlib.pyplot as plt
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit 
from qiskit.visualization import plot_histogram



qr = QuantumRegister(2)  # Initialize two qubits
cr = ClassicalRegister(2)  # Initialize two bits for record measurements
circuit = QuantumCircuit(qr, cr)

circuit.x(qr[1])  # initialize the ancilla qubit in the |1> state

circuit.barrier()

# First step of quantum algorithms - Prepare the superposition
# For superposition, we apply the Hadamard gate on both qubits
circuit.h(qr[0])
circuit.h(qr[1])

circuit.barrier()

# Oracle function for ballanced f(0) != f(1)
circuit.cx(qr[0], qr[1])
# Oracle function for unballanced or constant f(0)= f(1)
#circuit.x(qr[1])

circuit.barrier()



# Apply Hadamard gates after querying oracle function
circuit.h(qr[0])
circuit.h(qr[1])

circuit.barrier()

# Measure qubit
circuit.measure(qr[0], cr[0])


from qiskit.providers.basic_provider import BasicSimulator

backend = BasicSimulator()

# If you do not specify the number of shots, the default is 1024
result = backend.run(circuit, shots=2000).result()   

# Extract the counts of 0 and 1 measurements
counts = result.get_counts()                    
plt.show(plot_histogram(counts))
# Execute the circuit on the qasm simulator
# Draw the circuit
circuit.draw()
print(circuit)
# Plot a histogram
 
print(counts)

print("Simulator result")
for c1c0 in counts:
    print(f'c0 = {c1c0[1]} ({counts[c1c0]} shots)')
# C0 observed as 1
# It indicates f(0) != f(1)  balanced
# C0 observed as 0 
# It indicates f(0) = f(1)  unbalanced or constant

 
