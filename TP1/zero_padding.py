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
    L = 1000    # Cantidad de muestras
    resultados = []
    frecuencias = []
    
    M = (0, L/10, L, 10*L) # Cantidad de ceros que se agregan
    
    fd = (0, 0.01, 0.25, 0.5)   # Offsets respecto al bin
    
    f0 = fs/4 + fd[0] # Frecuencia de la señal
    
    for zero_padding in M:
        tt, sen = gen.generador_senoidal(fs, f0, L)
        signal = np.concatenate((sen, np.zeros(int(zero_padding))))
        N = L + zero_padding
        df = fs/N
        ff = np.linspace(0, int((N-1)*df), int(N))
        spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
        resultados.append(2.0/(L) * np.abs(spectrum[0:int((N)//2+1)]))
        frecuencias.append(ff[0:int((N)//2+1)])
    
    for res, freq, i, zp in zip(resultados, frecuencias, range(1,5), M):
        plt.subplot(2,2,i)
        plt.title('zero padding de ' + str(zp) + ' ceros')
        plt.stem(freq, res)
        plt.xlim((225,275))
        
    plt.suptitle('Senoidal de ' + str(f0) + ' Hz', fontsize=16)
    
zero_padding_testbench()
    