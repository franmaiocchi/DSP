# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 18:23:19 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal
from scipy.fftpack import fft

def testbench():

    fs = 1000   # Frecuencia de muestreo
#    Ns = np.array([10, 50, 100, 250, 500, 1000, 5000], dtype=np.float)
#    Ns = np.arange(1024) + 1
    Ns = np.array([10000], dtype=np.float)
    
#    # Vector de tiempos
#    tt = np.linspace(0, (N-1)/fs, N)
#    
#    # Vector de frecuencias
#    df = fs/N
#    ff = np.linspace(0, ((N-1)*df), int(N))
    
    # Parametros del ruido blanco gaussiano
    mean = 0
    variance = 2
    
    result_sesgo = []
    result_var = []
#%% 

    for N in Ns:
        
        real_bin_psd = variance/N
        noises = np.random.normal(mean, np.sqrt(variance), int(N))
        
        noises_spectrum = fft(noises, axis = 0)
        psd = pow((1/N)*np.abs(noises_spectrum), 2)
        
        # Varianza del estimador periodograma
        bin_var = np.var(psd)*N**2    # Checkear si hay que multiplicar por N**2
        
        # Valor esperado de la PSD
        bin_PSD_esperado = np.average(psd)
        
        # Varianza de la señal, area del PSD
        varianza = np.sum(psd)
        
        sesgo = np.abs(real_bin_psd - bin_PSD_esperado)
        result_sesgo.append(sesgo)
        result_var.append(bin_var)
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(Ns, result_sesgo)
    plt.title("Sesgo en funcion de N")
    plt.xlabel("N")
    plt.ylabel("Sesgo")
    plt.yscale("log")
    plt.grid()
    
    plt.subplot(2,1,2)
    plt.plot(Ns, result_var)
    plt.title("Varianza en funcion de N")
    plt.xlabel("N")
    plt.ylabel("Varianza")
    plt.yscale("log")
    plt.grid()
    
    print(result_sesgo)
    print(result_var)

testbench()