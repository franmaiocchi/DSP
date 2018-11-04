# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:31:03 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal

def testbench():
    
    fs = 1024
    N = 1024
    prueba = (10, 100, 1000, 10000)
    ruidos = []
    power_density = []
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    variance = 2
    
    for realizaciones in prueba:
        
        power_density = []
        ruidos = []
        for i in range(realizaciones):
            
            aux = gen.generador_ruido(fs, N, mean = 0, variance = variance)
            spec_aux = tools.spectrum_analyzer(aux, fs, N, plot = False)
            power_density.append(tools.energy_2(spec_aux))
            ruidos.append(aux)
        
        print("Con " + str(realizaciones) + " realizaciones la energía es " + str(np.average(power_density)))
    
testbench()