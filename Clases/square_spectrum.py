# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 20:34:59 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def testbench():
    
    fs = 1200
    N = 1200
    f0 = 170
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    tt = np.linspace(0, (N-1)/fs, N)
    signal = gen.generador_cuadrada(1,f0, fs, N, 0.5)
        
    plt.figure()
    plt.plot(tt, signal)
    
    tools.spectrum_analyzer(signal, fs, N)
    
testbench()
