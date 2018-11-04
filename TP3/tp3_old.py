# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:43:13 2018

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
    N = 4096    # Cantidad de muestras por realizacion
    L = 200     # Cantidad de realizaciones
    
    # Vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    
    # Vector de frecuencias
    df = fs/N
    ff = np.linspace(0, ((N-1)*df), int(N))
    
    # Parametros del ruido blanco gaussiano
    mean = 0
    variance = 2
#%% 
    noises = np.random.normal(mean, np.sqrt(variance), (N, L))
    
    noises_spectrum = fft(noises, axis = 0)
    psd = pow((1/N)*np.abs(noises_spectrum), 2)
    
    psd_average = np.average(psd, axis = 1)
    
    # Varianza del estimador periodograma
    bin_var = np.var(psd_average)*N**2    # Checkear si hay que multiplicar por N**2
    
    # Valor esperado de la PSD
    bin_PSD_esperado = np.average(psd_average)
    
    # Varianza de la señal, area del PSD
    varianza = np.sum(psd_average)
    


testbench()