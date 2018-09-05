# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 16:05:29 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def leakage_testbench():
    
    fd=(0, 0.01, 0.25, 0.5)
    N  = 1000 # muestras
    fs = 1000 # Hz
    resultados = np.array([], dtype=np.float).reshape(N,0)
    resto_frecuencias = []
    
    for i in range(len(fd)):
        resto_frecuencias.append(0)
    
    for freq_offset in fd:
        tt, signal = gen.generador_senoidal(fs, fs/4 + freq_offset, N)
        ff, spectrum = tools.spectrum_analyzer(signal, fs, N)
        resultados = np.hstack([resultados, spectrum.reshape(N,1)])
    
    df = ff[1]
    m_f0 = int((fs/4)/df)
    
    print(2.0/N *np.abs(resultados[m_f0,0]))
    print(2.0/N *np.abs(resultados[m_f0,1]))
    print(2.0/N *np.abs(resultados[m_f0,2]))
    print(2.0/N *np.abs(resultados[m_f0,3]))
    print(2.0/N *np.abs(resultados[m_f0+1,0]))
    print(2.0/N *np.abs(resultados[m_f0+1,1]))
    print(2.0/N *np.abs(resultados[m_f0+1,2]))
    print(2.0/N *np.abs(resultados[m_f0+1,3]))
    
    for freq in ff[0:(N//2-1)]:
        if freq != fs/4:
            for i in range(len(fd)):
                resto_frecuencias[i] = resto_frecuencias[i] + pow((2.0/N *np.abs(resultados[int(freq),i])),2)
    
    print(resto_frecuencias)
            
        
    
    

leakage_testbench()