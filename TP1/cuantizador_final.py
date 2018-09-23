# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 12:30:38 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def cuantizador_testbench():
    
    fs = 1000                   # Frecuencia de muestreo
    N = 1000                    # Cantidad de muestras
    a0 = np.sqrt(2)             # Amplitud de la senoidal
    f0 = 5                      # Frecuencia de la senoidal
    cantidad_bits = (4, 8, 16)  # Cantidad de bits de los cuantizadores
    rango = 2                   # Rango del cuantizador
    energia_total_q_real = []   # Lista donde guardo la energia total de la señal cuantizada real
    energia_total_q = []        # Lista donde guardo la energia total de la señal cuantizada ideal
    energia_total_e_real = []   # Lista donde guardo la energia total del error de la señal real
    energia_total_e = []        # Lista donde guardo la energia total del error de la señal ideal
    errores_real = []           # Lista donde guardo los errores de la señal real
    errores = []                # Lista donde guardo los errores de la señal ideal
    signals_q_real = []         # Lista donde guardo las señales cuantizadas reales
    signals_q = []              # Lista donde guardo las señales cuantizadas ideales
    
    df = fs/N   # Resolucion espectral
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    tt, s = gen.generador_senoidal(fs, f0, N, a0)
    tt, n = gen.generador_ruido(fs, N, mean = 0, variance = 0.1, distribution = 'Normal')
    s_real = s + n
    
    # Normalizo en amplitud para que no sature el cuantizador
    s_real = s_real / np.max(np.abs(s_real))
    s = s / np.max(np.abs(s))

    
    energia_total = tools.energy(tools.spectrum_analyzer(s_real, fs, N, plot = False))
 
    for b in cantidad_bits:
        
        # Cuantizacion de señal ideal
        s_q = tools.quantizer(s, b, rango)
        signals_q.append(s_q)
        energia_total_q.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
        e = s_q - s
        errores.append(e)
        energia_total_e.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
        
        # Cuantizacion de señal real
        s_q = tools.quantizer(s_real, b, rango)
        signals_q_real.append(s_q)
        e = s_q - s_real
        errores_real.append(e)
        energia_total_q_real.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
        energia_total_e_real.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
    
    # Ploteo de señales
    for b, i in zip(cantidad_bits, range(3)):
        
        plt.figure()
        plt.suptitle("Señal de error con cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
        
        # Ploteo de la señal de error ideal
        plt.subplot(1,2,1)
        plt.title("Error de señal ideal (sin ruido)")
        plt.xlabel('Tiempo [Seg]')
        plt.ylabel('Amplitud [V]')
        plt.xlim(0, 0.4)
        plt.grid()
        plt.plot(tt, errores[i])
        
        # Ploteo de la señal de error real
        plt.subplot(1,2,2)
        plt.title("Error de señal real")
        plt.xlabel('Tiempo [Seg]')
        plt.ylabel('Amplitud [V]')
        plt.xlim(0, 0.4)
        plt.grid()
        plt.plot(tt, errores_real[i])
    
    # Ploteo de espectros    
    for b, i in zip(cantidad_bits, range(3)):
        
        plt.figure()
        plt.suptitle("Espectro de error con cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
        
        # Ploteo del espectro ideal
        plt.subplot(1,2,1)
        plt.title("Error de señal ideal")
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [dB]')
        plt.xlim(0, 100)
        plt.grid()
        spectrum = tools.spectrum_analyzer(errores[i], fs, N, plot = False)
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        
        # Ploteo del espectro real
        plt.subplot(1,2,2)
        plt.title("Error de señal real")
        plt.xlabel('Frecuencia [Hz]')
        plt.ylabel('Magnitud [dB]')
        plt.xlim(0, 100)
        plt.grid()
        spectrum = tools.spectrum_analyzer(errores_real[i], fs, N, plot = False)
        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
        
    for b, i in zip(cantidad_bits, range(3)):
        
        plt.figure()
        plt.suptitle("Histograma del error con cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
        
        # Histograma la señal de error ideal
        plt.subplot(1,2,1)
        plt.title("Histograma señal ideal (sin ruido)")
        plt.xlabel('Cuentas')
        e_normalizado = errores[i]/(rango/(pow(2, b) -2))
        plt.hist(e_normalizado, bins = 10)
        
        # Histograma de la señal de error real
        plt.subplot(1,2,2)
        plt.title("Histograma señal real")
        plt.xlabel('Cuentas')
        plt.ylabel('Veces')
        e_normalizado = errores_real[i]/(rango/(pow(2, b) -2))
        plt.hist(e_normalizado, bins = 10)
        
#        plt.figure()
#        plt.suptitle("Cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
#        plt.subplot(3,1,1)
#        plt.xlabel('Tiempo [Seg]')
#        plt.ylabel('Amplitud [V]')
#        plt.xlim(0, 0.1)
#        plt.stem(tt, s_q, 'b', label=r'Señal cuantizada')
#        plt.hold
#        plt.plot(tt, s, 'r', label=r'Señal real')
#        plt.legend()
#        plt.subplot(3,1,2)
#        plt.xlabel('Frecuencia [Hz]')
#        plt.ylabel('Magnitud [dB]')
#        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
#        plt.subplot(3,1,3)
#        e_normalizado = e/(rango/(pow(2, b) -2))
#        plt.hist(e_normalizado, bins = 15)
#    
#    for b in cantidad_bits:
#        
#        s_q = tools.quantizer(s_real, b, rango)
#        spectrum = tools.spectrum_analyzer(s_q, fs, N, plot = False)
#        e = s_q - s_real
#        
#        signals_q.append(s_q)
#        errores.append(e)
#        energia_total_q.append(tools.energy(tools.spectrum_analyzer(s_q, fs, N, plot = False)))
#        energia_total_e.append(tools.energy(tools.spectrum_analyzer(e, fs, N, plot = False)))
#        
#        plt.figure()
#        plt.suptitle("Cuantificador de " + str(b) + ' bits con q = ' + str(rango/(pow(2, b) -2)))
#        plt.subplot(3,1,1)
#        plt.xlabel('Tiempo [Seg]')
#        plt.ylabel('Amplitud [V]')
#        plt.xlim(0, 0.1)
#        plt.stem(tt, s_q, 'b', label=r'Señal cuantizada')
#        plt.hold
#        plt.plot(tt, s_real, 'r', label=r'Señal real')
#        plt.legend()
#        plt.subplot(3,1,2)
#        plt.xlabel('Frecuencia [Hz]')
#        plt.ylabel('Magnitud [dB]')
#        plt.plot(ff[0:int(N//2+1)], 20*np.log10(2.0/N * np.abs(spectrum[0:int(N//2+1)])))
#        plt.subplot(3,1,3)
#        e_normalizado = e/(rango/(pow(2, b) -2))
#        plt.hist(e_normalizado, bins = 15)
#    

        

    

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