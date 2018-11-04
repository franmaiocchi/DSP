# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 15:49:59 2018

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

def barlett(N):
    
    k = np.linspace(0, (N-1), N)
    w = (2/(N-1))*((N-1)/2 - np.abs(k-(N-1)/2))
    return w

def testbench():
    
    fs = 1000
    R = 1
    K = 10      # Cantidad de bloques
    N = 1000    # Cantidad de muestras 
    overlap = 50    # Overlap en %
    L = int(N/K)    # Cantidad de muestras por bloque
    D = int(L * overlap/100) # Offset de los bloques
    cant_promedios = 1 + int((N-L)/D)   # Cantidad de promedios realizados
    
    df = fs/L
    ff = np.linspace(0, ((L-1)*df), int(L))
    
    f0 = fs/4
    a1 = 2
    
    mean = 0
    variance = 20
    
    window = barlett(L)
    window = window/LA.norm(window)
    
    for i in range(R):
        
        fr = gen.generador_ruido(fs, N, low = -1/2, high = 1/2, distribution = 'Uniform')
        noise = np.random.normal(mean, np.sqrt(variance), N)
        
        f1 = f0 + fr
        
        signal = gen.generador_senoidal(fs, f1, N, a1) + noise
    
        n1 = 0
        psd_average = 0
        for i in range(cant_promedios):
            noise_spectrum = fft(signal[n1:(n1+L)]*window, axis = 0)
            psd = pow((1/L)*np.abs(noise_spectrum), 2)
            psd_average = psd_average + psd/cant_promedios
            n1 = n1 + D
            
        psd_average = psd_average*L # NO TENGO IDEA DE DONDE SALE ESTE *L
        
        plt.figure()
        plt.stem(ff[0:int(L//2+1)], psd_average[0:int(L//2+1)])
    

    
testbench()