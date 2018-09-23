# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 17:14:22 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def parseval_testbench():
    
    fs = 1024   # Frecuencia de muestreo
    N = 1024    # Cantidad de muestras
    a0 = np.sqrt(2)     # Amplitud de la senoidal
    f0 = 10     # Frecuencia de la senoidal
    energia_n = 0
    energia_f = 0
    
    df = fs/N   # Resolucion espectral
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    tt, s = gen.generador_senoidal(fs, f0, N, a0)
    
    spectrum = tools.spectrum_analyzer(s, fs, N, plot = False)
    
    for x in s:
        energia_n = energia_n + pow(x, 2)/N
    

    
    for i in range(N//2+1):
        energia_f = energia_f + pow(2.0/N * np.abs(spectrum[i]), 2)/2
    
    print('Energia antes de la DFT ' + str(energia_n))
    print('Energia despues de la DFT ' + str(energia_f))
    print(np.sqrt(np.mean(np.square(s))))
    
    
    
parseval_testbench()