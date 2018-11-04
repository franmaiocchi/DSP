# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 22:12:51 2018

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
    realizaciones = 200

    # guardaremos las señales creadas al ir poblando la siguiente matriz vacía
    power_densities = np.array([], dtype=np.float).reshape(N,0)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    variance = 2
    
    for i in range(realizaciones):
        
        aux = gen.generador_ruido(fs, N, mean = 0, variance = variance)
        spec_aux = tools.spectrum_analyzer(aux, fs, N, plot = False)
        psd = pow(1/N * np.abs(spec_aux), 2)
        power_densities = np.hstack([power_densities, psd.reshape(N,1)]) 
    
    psd_promedio = np.mean(power_densities, axis = 1)
    plt.plot(ff[0:int(N//2+1)], 2.0 * psd_promedio[0:int(N//2+1)])
    print(np.sum(psd_promedio))
    
    
testbench()