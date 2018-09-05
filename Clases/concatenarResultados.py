# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 16:54:18 2018

@author: Francisco
"""

import pdsmodulos.generador as gen
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def testbench():
#%% Definicion de los parametros
    
    frecuencias = (10, 20, 30, 40, 50)
    amplitudes = (1, 1, 1, 1, 1)
    fases = (0, 0, 0, 0, 0)
    
    fs = 8000
    N = 8000
    
    # guardaremos las señales creadas al ir poblando la siguiente matriz vacía
    resultados = np.array([], dtype=np.float).reshape(N,0)
    
#%% Creacion de las señales   
    
    for amp, freq, fase in zip(amplitudes, frecuencias, fases):
        tt, signal = gen.generador_senoidal(fs, freq, N, amp, fase)
        resultados = np.hstack([resultados, signal.reshape(N,1)])   # No entiendo porque hay que hacer el reshape. Pasa de (N,) a (N,1) dimensiones
    
#%% Presentación gráfica de los resultados
    
    plt.figure(1)
    line_hdls = plt.plot(tt, resultados)
    plt.title('Senoidales')
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')  
    plt.legend(frecuencias, loc = 'upper right')
    plt.show()

#%% Ejecucion del testbench
testbench()