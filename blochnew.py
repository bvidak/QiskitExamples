# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:14:24 2024

@author: Brani Vidakovic
"""
import matplotlib.pyplot as plt
from qiskit.visualization import plot_bloch_vector
plt.show(plot_bloch_vector([0,1,0], title="New Bloch Sphere"))
