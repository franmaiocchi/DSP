# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 20:53:17 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def testbench():
    
    fs = 1024
    N = 1024
    
    a1 = 1
    a2 = pow(10, -2)*a1
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    f01 = fs/4
    f02 = f01 + 10*fs/(2*N)
    
    print("La frecuencia 1 es" + str(f01) + " y la frecuencia 2 es " + str(f02))
    
    tt, x1 = gen.generador_senoidal(fs, f01, N, a1)
    tt, x2 = gen.generador_senoidal(fs, f02, N, a2)
    
    signal = x1 + x2
    plt.plot(tt, signal)
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.figure()
    plt.xlabel('f')
    plt.title('Espectro en frecuencia')
    plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [V]')
    plt.xlim((156,356))
    plt.grid()
    plt.suptitle("Ejercicio 2a")
    
    # El 2b es 300 dB aprox -> puedo bajar 260 dB
    
    signal = signal/np.max(signal)
    signal_q = tools.quantizer(signal, 16, 2)
    spectrum = tools.spectrum_analyzer(signal_q, fs, N, plot = False)
    
    plt.figure()
    plt.xlabel('f')
    plt.title('Espectro en frecuencia')
    plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.ylabel('Magnitud [V]')
    plt.xlim((156,356))
    plt.grid()
    plt.suptitle("Ejercicio 2b - Cuantizado")
    
    d1=(0, 0.01, 0.25, 0.5)
    
    for freq_offset in d1:
        tt, x1 = gen.generador_senoidal(fs, f01 + freq_offset*fs/N, N, a1)
        tt, x2 = gen.generador_senoidal(fs, f02, N, a2)
        signal = x1 + x2
        spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
        plt.figure()
        plt.xlabel('f')
        plt.title('Espectro en frecuencia')
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [V]')
        plt.xlim((156,356))
        plt.grid()
        plt.suptitle("Frecuencia del tono principal de " + str(f01+freq_offset) + " Hz")        
  
    bartlett = np.bartlett(N)
    blackman = np.blackman(N)
    hamming = np.hamming(N)
    hanning = np.hanning(N)    
    
    ventanas = [bartlett, blackman, hamming, hanning]
    
    for window, i in zip(ventanas, range(1, 5)):
        spectrum = tools.spectrum_analyzer(signal*window, fs, N, plot = False)
        plt.subplot(2,2,i)
        plt.title(str(i))
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [V]')
        plt.xlim((156,356))
        plt.grid()
        plt.ylim((-100, 0))
        
    
testbench()