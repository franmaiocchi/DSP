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
import spectrum as sp

def barlett(N):
    
    k = np.linspace(0, (N-1), N)
    w = (2/(N-1))*((N-1)/2 - np.abs(k-(N-1)/2))
    return w

def testbench():
    
    fs = 1000
    R = 200       # Cantidad de realizaciones
    K = 10      # Cantidad de bloques
    N = 1000    # Cantidad de muestras 
    overlap = 50    # Overlap en %
    L = int(N/K)    # Cantidad de muestras por bloque
    D = int(L * overlap/100) # Offset de los bloques
    cant_promedios = 1 + int((N-L)/D)   # Cantidad de promedios realizados
    freqs = np.array([], dtype=np.float).reshape(R,0)
    freqs_BT = np.array([], dtype=np.float).reshape(R,0)
    
    df = fs/L
    ff = np.linspace(0, ((L-1)*df), int(L))
    
    f0 = fs/4
    a1 = 2
    
    SNR = np.array([3, 10], dtype=np.float)
    
    mean = 0
    
    window = barlett(L)
    window = window/LA.norm(window)
    
    for snr in SNR:
        
        variance = N*pow(a1, 2)*pow(10, (-snr)/10)/2
        aux = np.array([], dtype = np.float)
        aux2 = np.array([], dtype = np.float)
    
        for i in range(R):
            
            fr = gen.generador_ruido(fs, N, low = -1/2, high = 1/2, distribution = 'Uniform')
            noise = gen.generador_ruido(fs, N, mean, variance, distribution = 'Normal')
            
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
            
            psd_BT = sp.CORRELOGRAMPSD(signal, NFFT = L, lag=int(np.round(L/5)), window='hamming')
#            plt.figure()
#            plt.stem(ff[0:int(L//2+1)], psd_BT[0:int(L//2+1)])
            
            indice = np.where(psd_average[0:int(L//2+1)] == np.max(psd_average[0:int(L//2+1)]))
            aux = np.append(aux, ff[indice])
            indice = np.where(psd_BT[0:int(L//2+1)] == np.max(psd_BT[0:int(L//2+1)]))
            aux2 = np.append(aux2, ff[indice])
            
            
            
            
    #        plt.figure()
    #        plt.stem(ff[0:int(L//2+1)], psd_average[0:int(L//2+1)])
        freqs = np.hstack([freqs, aux.reshape(R,1)] )
        freqs_BT = np.hstack([freqs_BT, aux2.reshape(R,1)] )
    plt.plot(freqs)
    var = np.var(freqs, axis = 0)
    var_BT = np.var(freqs_BT, axis = 0)
    
    print("La varianza de welch con SNR 3dB es: " + str(var[0]))
    print("La varianza de welch con SNR 10dB es: " + str(var[1]))
    print("La varianza de BT con SNR 3dB es: " + str(var_BT[0]))
    print("La varianza de BT con SNR 10dB es: " + str(var_BT[1]))
    
    
    
testbench()