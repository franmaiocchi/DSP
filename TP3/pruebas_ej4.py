# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 16:36:36 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal
from scipy.fftpack import fft
from numpy import linalg as LA

def testbench():
    
    fs = 1000
    R = 1
    N = 1000    # Cantidad de muestras 
    
    df = fs/N
    ff = np.linspace(0, ((N-1)*df), int(N))
    
    f0 = fs/4
    a1 = 1
    
    att = -3
    
    mean = 0
    variance = ((a1**2)/2)*10**(att/10)*N    
#    variance = 2
    for i in range(R):
        
        fr = gen.generador_ruido(fs, N, low = -1/2, high = 1/2, distribution = 'Uniform')
        noise = np.random.normal(mean, np.sqrt(variance), N)
        
        f1 = f0
  
        signal = gen.generador_senoidal(fs, f1, N, a1) + noise
    
        spectrum = fft(signal, axis = 0)
        psd = pow((1/N)*np.abs(spectrum), 2)
        
        plt.figure()
        plt.plot(ff[0:int(N//2+1)], 10*np.log10(np.abs(psd[0:int(N//2+1)])/np.max((psd))))
#        plt.plot(ff[0:int(N//2+1)], 10*np.log10(np.abs(spectrum[0:int(N//2+1)])/np.max(np.abs(spectrum))))
        plt.grid()
    

    
testbench()