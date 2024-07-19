# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 13:09:54 2023

@author: Brani Vidakovic
"""
from qiskit import QuantumCircuit, transpile
from qiskit.providers.basic_provider import BasicSimulator
from qiskit.visualization import *

import matplotlib.pyplot as plt

secretnumber = '101001'

circuit = QuantumCircuit(len(secretnumber)+1,len(secretnumber))
circuit.draw("mpl")
 
 
circuit.h(range(len(secretnumber)))
circuit.x(len(secretnumber))
circuit.h(len(secretnumber))

circuit.barrier()
circuit.draw("mpl")

for ii,yesno in enumerate(reversed(secretnumber)):
    if yesno == '1':
        circuit.cx(ii, len(secretnumber))

circuit.barrier()
circuit.draw("mpl")
 
    
circuit.h(range(len(secretnumber)))

circuit.barrier()

circuit.measure(range(len(secretnumber)),range(len(secretnumber)))

plt.show(circuit.draw("mpl"))
 


sim_backend = BasicSimulator()
job = sim_backend.run(transpile(circuit, sim_backend), shots=1024)
result = job.result()
print("Basic simulator : ")
 
counts = result.get_counts()

plt.show(plot_histogram(counts))

print(counts)


