# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 19:48:41 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools

def signal_1():
   
    fs = 1000
    N = 1000
    f0 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N, a0)
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])    
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))    
    
def signal_2():
    
    fs = 1000
    N = 1000
    f0 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N, a0)
    signal[int(fs/f0):] = 0
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))   
    
    
def signal_3():
    
    fs = 1000
    N = 1000
    f0 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N, a0)
    signal[:int(2*fs/f0)+1] = 0
    signal[int(3*fs/f0):] = 0
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
    
def signal_4():
 
    fs = 1000
    N = 1000
    f01 = 9*fs/N
    f02 = 8*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f01 = int(N*(f01)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f01, int(N/4), a0)
    sen1[int(fs/f01):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
    sen2[int(fs/f02):] = 0
    
    signal = np.concatenate((sen1, sen2))
    tt = np.linspace(0, (N-1)/fs, N)
    
    plt.figure(figsize = (12, 12))
    plt.subplot(3,1,1)
    plt.plot(tt, signal, label = str(f01) + " Hz y " + str(f02) + ' Hz')
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(3,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    plt.subplot(3,1,3)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum[0:int(N//2+1)]),np.real(spectrum[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f01]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
    
    
def signal_5():
 
    fs = 1000
    N = 1000
    
    f01 = 8*fs/N
    f02 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f01 = int(N*(f01)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f01, int(N/4), a0)
    sen1[int(fs/f01):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
    sen2[int(fs/f02):] = 0
    signal = np.concatenate((sen1, sen2))
    tt = np.linspace(0, (N-1)/fs, N)
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f01) + " Hz y " + str(f02) + ' Hz')
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f01]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
    
def signal_6():

    fs = 1000
    N = 1000
    f0 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N, a0)
    signal[int(3*fs/f0):] = 0
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))   
    
def signal_7():

    fs = 1000
    N = 1000
    
    f0 = 9*fs/N
    a1 = np.sqrt(2) 
    a2 = np.sqrt(2)*np.sqrt(100)
    a3 = np.sqrt(2)*np.sqrt(10)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f0, N, a0 = a1)
    sen1[int(fs/f0):] = 0
#    plt.subplot(4,1,1) 
#    plt.stem(sen1)
    
    tt, sen2 = gen.generador_senoidal(fs, f0, N, a0 = a2)
    sen2[:(int(fs/f0))] = 0
    sen2[int(2*fs/f0):] = 0
#    plt.subplot(4,1,2) 
#    plt.stem(sen2)
    
    tt, sen3 = gen.generador_senoidal(fs, f0, N, a0 = a3)
    sen3[:(int(2*fs/f0))] = 0
    sen3[int(3*fs/f0):] = 0
#    plt.subplot(4,1,3) 
#    plt.stem(sen3)
    
    signal = sen1 + sen2 + sen3
    tt = np.linspace(0, (N-1)/fs, N)
#    plt.subplot(4,1,4)
#    plt.stem(tt, signal)
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
    
#def signal_8():
#
#    fs = 1000
#    N = 1000
#    
#    f0 = 9*fs/N
##    a1 = np.sqrt(2) 
##    a2 = np.sqrt(2)*np.sqrt(100)
##    a3 = np.sqrt(2)*np.sqrt(10)
#    a1 = 1
#    a2 = 1
#    a3 = 1
#    
#    df = fs/N
#    ff = np.linspace(0, int((N-1)*df), int(N))
#    
#    m_f0 = int(N*(f0)/fs)
#    
#    tt, sen1 = gen.generador_senoidal(fs, f0, int(3*fs/f0), a0 = a1)
#    sen1[int(fs/f0):] = 0
#    
#    tt, sen2 = gen.generador_senoidal(fs, f0, int(3*fs/f0), a0 = a2)
#    sen2[:(int(fs/f0))] = 0
#    sen2[int(2*fs/f0):] = 0
#    
#    tt, sen3 = gen.generador_senoidal(fs, f0, int(3*fs/f0), a0 = a3)
#    sen3[:(int(2*fs/f0))] = 0
#    sen3[int(3*fs/f0)+1:] = 0
#    
#    aux = sen1 + sen2 + sen3
#    signal = np.concatenate((aux, aux, aux, np.array([0])))
##    plt.subplot(4,1,4)
#    tt = np.linspace(0, (N-1)/fs, N)
#    
#    plt.figure(figsize = (12, 12))
#    plt.subplot(2,1,1)
#    plt.plot(tt, signal, label = str(f0) + " Hz")
#    plt.grid()
#    plt.xlabel('Tiempo [segundos]')
#    plt.ylabel('Amplitud [V]')
#    plt.title('Señal en el tiempo')
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')
#    
#    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
#    
#    plt.subplot(2,1,2)
#    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
#    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,100))
#    plt.grid()
#    plt.ylabel('Magnitud [V]')
#    plt.title('Espectro de la señal') 
#    
#    energia_total = tools.energy(spectrum)
#    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
#    
#    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
#    print(imax)
#    print(ff[imax])  
#    
#    print('La energia total es ' + str(energia_total))
#    print('La energia en f0 es ' + str(energia_f0))  
    
def signal_8():

    fs = 1000
    N = 1000
    
    f0 = 9*fs/N
    a1 = np.sqrt(2) 
    a2 = np.sqrt(2)*np.sqrt(100)
    a3 = np.sqrt(2)*np.sqrt(10)

    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f0, N, a0 = a1)
    sen1[int(fs/f0):int(3*fs/f0)] = 0
    sen1[int(4*fs/f0):int(6*fs/f0)] = 0
    sen1[int(7*fs/f0):] = 0
#    plt.plot(tt, sen1)
    
    tt, sen2 = gen.generador_senoidal(fs, f0, N, a0 = a2)
    sen2[:(int(fs/f0))] = 0
    sen2[int(2*fs/f0):int(4*fs/f0)] = 0
    sen2[int(5*fs/f0):int(7*fs/f0)] = 0
    sen2[int(8*fs/f0):] = 0
#    plt.plot(tt, sen2)
    
    tt, sen3 = gen.generador_senoidal(fs, f0, N, a0 = a3)
    sen3[:(int(2*fs/f0))] = 0
    sen3[int(3*fs/f0):int(5*fs/f0)] = 0
    sen3[int(6*fs/f0):int(8*fs/f0)] = 0
#    plt.plot(tt, sen3)
    
    signal = sen1 + sen2 + sen3
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal') 
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
    
def signal_9():

    fs = 1000
    N = 1000   
    
    f0 = 9*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f0, N, a0)
    sen1[int(fs/f0):] = 0
    
    tt, sen2 = gen.generador_senoidal(fs, f0, N, a0, p0 = np.pi)
    sen2[:(int(fs/f0))] = 0
    sen2[int(2*fs/f0):] = 0
    
    signal = sen1 + sen2
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal') 
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))  
 
def signal_prueba1():
    
    fs = 1000
    N = 1000
    f0 = 5
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f0 = int(N*(f0)/fs)
    
    tt, signal = gen.generador_senoidal(fs, f0, N, a0)
    cuadrada = np.ones(N)
#    signal[int(fs/f0):] = 0
#    signal[int(fs/f0):] = 0
    signal[int(1*fs/f0):] = 0
    cuadrada[int(1*fs/f0):] = 0
#    signal[int(25*fs/f0):] = 0
#    signal[int(50*fs/f0):] = 0
#    signal[int(125*fs/f0):] = 0
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, signal, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))   
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, cuadrada, label = str(f0) + " Hz")
    plt.grid()
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.title('Señal en el tiempo')
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')
    
    spectrum = tools.spectrum_analyzer(cuadrada, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,100))
    plt.grid()
    plt.ylabel('Magnitud [V]')
    plt.title('Espectro de la señal')
    
    energia_total = tools.energy(spectrum)
    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f0]),2)/2
    
    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
    print(imax)
    print(ff[imax])  
    
    print('La energia total es ' + str(energia_total))
    print('La energia en f0 es ' + str(energia_f0))   
  
def signal_prueba2():
    
    fs = 1000
    N = 1000
    f01 = 9*fs/N
    f02 = 8*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f01 = int(N*(f01)/fs)
    
#    tt, sen1 = gen.generador_senoidal(fs, f01, int(N/4), a0)
#    sen1[int(fs/f01):] = 0
#    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
#    sen2[int(fs/f02):] = 0
    
    tt, sen1 = gen.generador_senoidal(fs, f01, N, a0)
    sen1[int(fs/f01):] = 0
    spectrum1 = tools.spectrum_analyzer(sen1, fs, N, plot = False)
    tt, sen2 = gen.generador_senoidal(fs, f02, N, a0)
    sen2[:int(3*fs/f02)] = 0
    sen2[int(4*fs/f02):] = 0
    spectrum2 = tools.spectrum_analyzer(sen2, fs, N, plot = False)
#    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
#    sen2[int(fs/f02):] = 0
    plt.figure()
    plt.subplot(2,1,1)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum1[0:int(N//2+1)]))
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum2[0:int(N//2+1)]))
    
#    e = 2.0/N * np.abs(spectrum1[0:int(N//2+1)]) - 2.0/N * np.abs(spectrum2[0:int(N//2+1)])
#    plt.figure()
#    plt.stem(ff[0:int(N//2+1)], e)
    
    
#    signal = sen1 + sen2
#    tt = np.linspace(0, (N-1)/fs, N)
#    
#    plt.figure(figsize = (12, 12))
#    plt.subplot(2,1,1)
#    plt.plot(tt, signal, label = str(f01) + " Hz y " + str(f02) + ' Hz')
#    plt.grid()
#    plt.xlabel('Tiempo [segundos]')
#    plt.ylabel('Amplitud [V]')
#    plt.title('Señal en el tiempo')
#    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
#    axes_hdl.legend(loc='upper right')
#    
#    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
#    
#    plt.subplot(2,1,2)
#    plt.stem(ff[0:int(N//2+1)], 2.0/N * np.abs(spectrum[0:int(N//2+1)]))
#    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,100))
#    plt.grid()
#    plt.ylabel('Magnitud [V]')
#    plt.title('Espectro de la señal')
#    
#    energia_total = tools.energy(spectrum)
#    energia_f0 = pow(2.0/N * np.abs(spectrum[m_f01]),2)/2
#    
#    imax = np.where(np.abs(spectrum[0:int(N//2+1)]) == np.max(np.abs(spectrum[0:int(N//2+1)])))
#    print(imax)
#    print(ff[imax])  
#    
#    print('La energia total es ' + str(energia_total))
#    print('La energia en f0 es ' + str(energia_f0))   

def prueba_fase():
    
    fs = 1000
    N = 1000
    f01 = 9*fs/N
    f02 = 8*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f01 = int(N*(f01)/fs)
    
    tt, sen1 = gen.generador_senoidal(fs, f01, int(N/4), a0)
    sen1[int(fs/f01):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
    sen2[int(fs/f02):] = 0
    
    signal = np.concatenate((sen1, sen2))
    tt = np.linspace(0, (N-1)/fs, N)

    
    plt.figure(figsize = (12, 12))
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,1)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum[0:int(N//2+1)]),np.real(spectrum[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((5,10))
    plt.grid()
    plt.ylabel('Fase [rad]')
    plt.title('Fase de la señal')
    
    tt, sen1 = gen.generador_senoidal(fs, f02, int(N/4), a0)
    sen1[int(fs/f01):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f01, int(3*N/4), a0)
    sen2[int(fs/f02):] = 0
    
    signal = np.concatenate((sen1, sen2))
    tt = np.linspace(0, (N-1)/fs, N)
    
    spectrum = tools.spectrum_analyzer(signal, fs, N, plot = False)
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum[0:int(N//2+1)]),np.real(spectrum[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((5,10))
    plt.grid()
    plt.ylabel('Fase [rad]')
    plt.title('Fase de la señal')

def prueba_fase_cuadradas():
    
    fs = 1000
    N = 1000
    f01 = 9*fs/N
    f02 = 8*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    m_f01 = int(N*(f02)/fs)
    
    cuad1 = np.ones(N)
    cuad1[int(fs/f02):] = 0
    
    cuad2 = np.ones(N)
    cuad2[:int(fs/f01)] = 0
    cuad2[int(2*fs/f01):] = 0

    tt = np.linspace(0, (N-1)/fs, N)

    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.plot(tt, cuad1)
    plt.xlabel('Tiempo [seg]')
    plt.grid()
    plt.ylabel('Amplitud [V]')
    plt.title('Cuadrada 1')
    
    plt.subplot(2,1,2)
    plt.plot(tt, cuad2)
    plt.xlabel('Tiempo [seg]')
    plt.grid()
    plt.ylabel('Amplitud [V]')
    plt.title('Cuadrada 2')
    
    spectrum1 = tools.spectrum_analyzer(cuad1, fs, N, plot = False)
    spectrum2 = tools.spectrum_analyzer(cuad2, fs, N, plot = False)
    
    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum1[0:int(N//2+1)]),np.real(spectrum1[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,10))
    plt.grid()
    plt.ylabel('Fase [rad]')
    plt.title('Fase de la señal')
    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum2[0:int(N//2+1)]),np.real(spectrum2[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
#    plt.xlim((0,10))
    plt.grid()
    plt.ylabel('Fase [rad]')
    plt.title('Fase de la señal')

def prueba():

    fs = 1000
    N = 1000
    f01 = 9*fs/N
    f02 = 8*fs/N
    a0 = np.sqrt(2)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    tt, sen1 = gen.generador_senoidal(fs, f01, int(N/4), a0)
    sen1[int(fs/f01):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f02, int(3*N/4), a0)
    sen2[int(fs/f02):] = 0
    
    signal1 = np.concatenate((sen1, sen2))
    
    tt, sen1 = gen.generador_senoidal(fs, f02, int(N/4), a0)
    sen1[int(fs/f02):] = 0
    tt, sen2 = gen.generador_senoidal(fs, f01, int(3*N/4), a0)
    sen2[int(fs/f01):] = 0
    
    signal2 = np.concatenate((sen1, sen2))
    
    spectrum1 = tools.spectrum_analyzer(signal1, fs, N, plot = False)
    spectrum2 = tools.spectrum_analyzer(signal2, fs, N, plot = False)
    
    tt = np.linspace(0, (N-1)/fs, N)
    
    plt.subplot(2,1,1)
    plt.plot(tt, signal1)
    plt.subplot(2,1,2)
    plt.plot(tt, signal2)
    

    plt.figure(figsize = (12, 12))
    plt.subplot(2,1,1)
    plt.title("Senoidal de " + str(f01) + ' Hz y ' + str(f02) + ' Hz')
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum1[0:int(N//2+1)]),np.real(spectrum1[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,20))
    plt.grid()
    plt.ylabel('Fase [rad]')

    
    plt.subplot(2,1,2)
    plt.stem(ff[0:int(N//2+1)], np.arctan2(np.imag(spectrum2[0:int(N//2+1)]),np.real(spectrum2[0:int(N//2+1)])))
    plt.xlabel('Frecuencia [Hz]')
    plt.xlim((0,20))
    plt.grid()
    plt.ylabel('Fase [rad]')
    plt.title("Senoidal de " + str(f02) + ' Hz y ' + str(f01) + ' Hz')

#signal_1()
#signal_2()
#signal_3()
#signal_4()
#signal_5()
#signal_6()
#signal_7()
#signal_8()
#signal_9()
#signal_prueba1()
#signal_prueba2()
#prueba_fase()
#prueba_fase_cuadradas()
prueba()