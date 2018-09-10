# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 17:25:01 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def zero_padding_testbench():
    
    fs = 1000   # Frecuencia de muestreo
    N = 1000    # Cantidad de muestras
    resultados = []
    frecuencias = []

    
    M = (0, N/10, N, 10*N) # Cantidad de ceros que se agregan
    
    fd = (0, 0.01, 0.25, 0.5)   # Offsets respecto al bin
    
    f0 = fs/4 + fd[2] # Frecuencia de la señal
    
    for zero_padding in M:
        tt, signal = gen.generador_senoidal(fs, f0, N + zero_padding)
        ff, spectrum = tools.spectrum_analyzer(signal, fs, N + zero_padding, plot = False)
        resultados.append(2.0/(N + zero_padding) * np.abs(spectrum[0:int((N + zero_padding)//2+1)]))
        frecuencias.append(ff[0:int((N + zero_padding)//2+1)])
    
    for res, freq, i, zp in zip(resultados, frecuencias, range(1,5), M):
        plt.subplot(2,2,i)
        plt.title('zero padding de ' + str(zp) + ' ceros')
        plt.stem(freq, res)
        
    plt.suptitle('Senoidal de ' + str(f0) + ' Hz', fontsize=16)
    
    

zero_padding_testbench()
    