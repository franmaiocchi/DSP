# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 21:00:13 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def cuantizador_testbench():
    
    fs = 1000
    N = 1000
    a0 = 1
    noise_amp = (a0)/20
    f0 = 100
    cantidad_bits = (4, 8, 16)
    rango = 2.1
    energia_total_q = []
    energia_total_e = []
    errores = []
    
    tt, s = gen.generador_senoidal(fs, f0, N, a0)
    tt, n = gen.generador_ruido(fs, N, low = -noise_amp, high = noise_amp, distribution = 'Uniform')
    
    s_real = s + n
    
    energia_total = tools.energy(tools.spectrum_analyzer(s_real, fs, N, plot = False))
    
    for b in cantidad_bits:
        s_q = tools.quantizer(s_real, b, rango)
        e = s_q - s_real
        errores.append(e)
        energia_total_q.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
        energia_total_e.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
    
    print(energia_total)
    print(energia_total_q)
    print(energia_total_e)
    
    for error, b in zip(errores, cantidad_bits):
        plt.figure(figsize = (12, 6))
        plt.title('Cuantizador de ' + str(b) + ' bits')
        plt.hist(error, bins = 10)
    

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