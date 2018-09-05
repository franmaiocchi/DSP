# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 20:42:58 2018

@author: Francisco
"""

from scipy.fftpack import fft
import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def testbench():
    
    fs = 1000
    N = 1000
    
    a0 = 1
    f0 = 10
    
    tiempo, señal1 = gen.generador_senoidal(fs, f0, N, a0)
    tools.spectrum_analyzer(señal1, fs, N)
    
    tiempo, señal2 = gen.generador_ruido(fs, N, mean = 0, variance = 5)
    tools.spectrum_analyzer(señal2, fs, N)
    
    tiempo, señal3 = gen.generador_ruido(fs, N, distribution = 'Uniform', high = 2, low = -2)
    tools.spectrum_analyzer(señal3, fs, N)
    
    tiempo, señal4 = gen.generador_ruido(fs, N, distribution = 'Triangular')
    tools.spectrum_analyzer(señal4, fs, N)
    
    plt.figure()
    plt.subplot(4,1,1)
    plt.hist(señal1, bins=10)  # arguments are passed to np.histogram
    plt.subplot(4,1,2)
    plt.hist(señal2, bins=10)  # arguments are passed to np.histogram
    plt.subplot(4,1,3)
    plt.hist(señal3, bins=10)  # arguments are passed to np.histogram
    plt.subplot(4,1,4)
    plt.hist(señal4, bins=10)  # arguments are passed to np.histogram
    

testbench()

