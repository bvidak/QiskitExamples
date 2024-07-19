# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:07:54 2023

@author: Brani Vidakovic
"""

#import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_histogram



# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

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