# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 15:36:14 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def cuantizador_testbench():
    
    fs = 1000   # Frecuencia de muestreo
    N = 1000    # Cantidad de muestras
    a0 = np.sqrt(2)      # Amplitud de la senoidal
    f0 = 10     # Frecuencia de la senoidal
    cantidad_bits = (4, 8, 16)  # Cantidad de bits de los cuantizadores
    rango = 2   # Rango del cuantizador
    energia_total_q = []    # Lista donde guardo la energia total de la señal cuantizada
    energia_total_e = []    # Lista donde guardo la energia total del error
    errores = []    # Lista donde guardo los errores
    signals_q = []  # Lista donde guardo las señales cuantizadas
    
    df = fs/N   # Resolucion espectral
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    tt, s = gen.generador_senoidal(fs, f0, N, a0)
    tt, n = gen.generador_ruido(fs, N, mean = 0, variance = 0.1, distribution = 'Normal')
    print("La energia de la señal es " + str(tools.energy(s, domain = 'time')))
    print("La energia del ruido es " + str(tools.energy(n, domain = 'time'))) 
    s_real = s + n
    
    # Normalizo en amplitud para que no sature el cuantizador
    s_real = s_real / np.max(np.abs(s_real))
    s = s / np.max(np.abs(s))

    
    energia_total = tools.energy(tools.spectrum_analyzer(s_real, fs, N, plot = False))
 
    for b in cantidad_bits:
        
        s_q = tools.quantizer(s, b, rango)
        spectrum = tools.spectrum_analyzer(s_q, fs, N, plot = False)
        e = s_q - s
        
        signals_q.append(s_q)
        errores.append(e)
        energia_total_q.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
        energia_total_e.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
        
        plt.figure()
        plt.suptitle("Cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
        plt.subplot(3,1,1)
        plt.xlabel('Tiempo [Seg]')
        plt.ylabel('Amplitud [V]')
        plt.xlim(0, 0.1)
        plt.stem(tt, s_q, 'b', label=r'Señal cuantizada')
        plt.hold
        plt.plot(tt, s, 'r', label=r'Señal real')
        plt.legend()
        plt.subplot(3,1,2)
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [dB]')
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        plt.subplot(3,1,3)
        e_normalizado = e/(rango/(pow(2, b) -2))
        plt.hist(e_normalizado, bins = 15)
    
    for b in cantidad_bits:
        
        s_q = tools.quantizer(s_real, b, rango)
        spectrum = tools.spectrum_analyzer(s_q, fs, N, plot = False)
        e = s_q - s_real
        
        signals_q.append(s_q)
        errores.append(e)
        energia_total_q.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
        energia_total_e.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
        
        plt.figure()
        plt.suptitle("Cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
        plt.subplot(3,1,1)
        plt.xlabel('Tiempo [Seg]')
        plt.ylabel('Amplitud [V]')
        plt.xlim(0, 0.1)
        plt.stem(tt, s_q, 'b', label=r'Señal cuantizada')
        plt.hold
        plt.plot(tt, s_real, 'r', label=r'Señal real')
        plt.legend()
        plt.subplot(3,1,2)
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [dB]')
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        plt.subplot(3,1,3)
        e_normalizado = e/(rango/(pow(2, b) -2))
        plt.hist(e_normalizado, bins = 15)
    

        

    

#    plt.figure()
#    plt.subplot(2,1,1)
#    plt.xlabel('Tiempo [Seg]')
#    plt.ylabel('Amplitud [V]')
#    plt.xlim(0, 0.1)
#    plt.plot(tt, s_q, 'b', label=r'Señal cuantizada')
#    plt.hold
#    plt.plot(tt, s_real, 'r', label=r'Señal real')
#    plt.legend()
#    plt.subplot(2,1,2)
#    plt.hist(e, bins = 10)
#    
#    s_q = tools.quantizer(s, cantidad_bits, rango)
#    e = s_q - s
#    
#    plt.figure()
#    plt.subplot(2,1,1)
#    plt.xlabel('Tiempo [Seg]')
#    plt.ylabel('Amplitud [V]')
#    plt.xlim(0, 0.1)
#    plt.plot(tt, s_q, 'b', label=r'Señal cuantizada')
#    plt.hold
#    plt.plot(tt, s, 'r', label=r'Señal ideal')
#    plt.legend()
#    plt.subplot(2,1,2)
#    plt.hist(e, bins = 10)
    
cuantizador_testbench()