# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 15:34:42 2018

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
#    Ns = np.arange(1024) + 1
#    Ns = np.array([10, 50, 100, 250, 500, 1000, 5000], dtype=np.float)
#   Ns = (2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096)    # Cantidad de muestras por realizacion
#    Ns = np.array([10000], dtype=np.float)
    N = np.linspace(10, 5000, 500)
    K = 10     # Cantidad de bloques
    
    
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
    
    
#%% Variamos N

    for n in N:
        
        L = int(n/K)
        real_bin_psd = variance/L
        
        noises = np.random.normal(mean, np.sqrt(variance), (int(L), K))
        
        noises_spectrum = fft(noises, axis = 0)
        psd = pow((1/L)*np.abs(noises_spectrum), 2)
        psd_average = np.average(psd, axis = 1)
        
        # Varianza del estimador periodograma
        bin_var = np.var(psd_average)*L**2    # Checkear si hay que multiplicar por L**2
        
        # Valor esperado de la PSD
        bin_PSD_esperado = np.average(psd_average)
        
        # Varianza de la señal, area del PSD
        varianza = np.sum(psd_average)
        
        sesgo = np.abs(real_bin_psd - bin_PSD_esperado)
        result_sesgo.append(sesgo)
        result_var.append(bin_var)
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(N, result_sesgo)
    plt.title("Sesgo en funcion de N")
    plt.xlabel("N")
    plt.ylabel("Sesgo")
    plt.yscale("log")
    plt.grid()
    
    plt.subplot(2,1,2)
    plt.plot(N, result_var)
    plt.title("Varianza en funcion de N")
    plt.xlabel("N")
    plt.ylabel("Varianza")
#    plt.yscale("log")
    plt.grid()
    
#    print("Varianza del bin promedio: " + str(bin_var))
#    print("Valor esperado del bin: " + str(bin_PSD_esperado))
#    print("Area: " + str(varianza))
#    print("Sesgo: " + str(result_sesgo))
  
#%% Variamos K
    
    K = np.array([1, 2, 5, 10, 20, 25, 40, 50, 100], dtype=np.float)
    K = np.linspace(1, 200, 200)
    N = 1000
    
    result_sesgo = []
    result_var = []
    
    df = []
    
    for k in K:
        
        L = int(N/k)
        real_bin_psd = variance/L
        
        df.append(fs/L)
        
        noises = np.random.normal(mean, np.sqrt(variance), (int(L), int(k)))
        
        noises_spectrum = fft(noises, axis = 0)
        psd = pow((1/L)*np.abs(noises_spectrum), 2)
        psd_average = np.average(psd, axis = 1)
        
        # Varianza del estimador periodograma
        bin_var = np.var(psd_average)*L**2    # Checkear si hay que multiplicar por L**2
        
        # Valor esperado de la PSD
        bin_PSD_esperado = np.average(psd_average)
        
        # Varianza de la señal, area del PSD
        varianza = np.sum(psd_average)
        
        sesgo = np.abs(real_bin_psd - bin_PSD_esperado)
        result_sesgo.append(sesgo)
        result_var.append(bin_var)
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(K, df)
    plt.title("Resolucion espectral en funcion de K")
    plt.xlabel("K")
    plt.ylabel("$\Delta f$")
#    plt.yscale("log")
    plt.grid()
    
    plt.subplot(2,1,2)
    plt.plot(K, result_var)
    plt.title("Varianza en funcion de K")
    plt.xlabel("K")
    plt.ylabel("Varianza")
    plt.yscale("log")
    plt.grid()
    
#    print("Varianza del bin promedio: " + str(bin_var))
#    print("Valor esperado del bin: " + str(bin_PSD_esperado))
#    print("Area: " + str(varianza))
#    print("Sesgo: " + str(result_sesgo))
    
    

testbench()