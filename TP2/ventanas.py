# -*- coding: utf-8 -*-
"""
Created on Wed Sep 26 16:17:28 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal

def barlett(N):
    
    k = np.linspace(0, (N-1), N)
    w = (2/(N-1))*((N-1)/2 - np.abs(k-(N-1)/2))
    return w
        
def hann(N):
    
    k = np.linspace(0, (N-1), N)
    w = 0.5*(1 - np.cos((2*np.pi*k)/(N-1)))
    return w
    
def blackman(N):
    
    k = np.linspace(0, (N-1), N)
    w = 0.42 - 0.5*np.cos((2*np.pi*k)/(N - 1)) + 0.08*np.cos((4*np.pi*k)/(N - 1))
    return w
    
def flat_top(N):
    # Ojo que saque la ecucacion de wikipedia
    k = np.linspace(0, (N-1), N)
    w = 1 - 1.93*np.cos((2*np.pi*k)/(N - 1)) + 1.29*np.cos((4*np.pi*k)/(N - 1)) - 0.388*np.cos((6*np.pi*k)/(N - 1)) + 0.032*np.cos((8*np.pi*k)/(N - 1))
    w = w/np.max(w)
    return w

def testbench():
    
    fs = 1000
    N = 1000
    
    tt = np.linspace(0, (N-1)/fs, N)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    # Se agregan padding*N ceros para visualizar mejor el espectro de la ventana
    padding = 4
    
    df_padding = fs/(padding*N)
    ff_padding = np.linspace(0, ((padding*N-1)*df_padding), int(padding*N))
    
    ventanas = []
    ventanas_label = []
    
    # Generacion de señales
    ventanas.append(barlett(N))
    ventanas_label.append('Barlett')
    ventanas.append(hann(N))
    ventanas_label.append('Hann')
    ventanas.append(blackman(N))
    ventanas_label.append('Blackman')
    ventanas.append(flat_top(N))
    ventanas_label.append('Flat Top')
    
    for ven, label in zip(ventanas, ventanas_label):
        
        sig = np.concatenate((ven, np.zeros((padding-1)*N)))
        spectrum = tools.spectrum_analyzer(sig, fs, padding*N, plot = False)
        
        fc = np.where((np.abs(spectrum[0:int(N//2+1)])/np.max(np.abs(spectrum[0:int(N//2+1)]))) < (np.sqrt(2)/2))
#        fc = np.where(20*np.log10(np.abs(spectrum[0:int(N//2+1)])/np.max(spectrum[0:int(N//2+1)]) + np.finfo(float).eps) < -3)
        print("La frecuencia de corte de " + label + " es " + str(ff_padding[fc[0][0]]) + " Hz")
        
        cero = np.where((np.abs(spectrum[0:int(N//2+1)])/np.max(np.abs(spectrum[0:int(N//2+1)]))) < 0.001)
        print(str(ff_padding[cero[0][0]]))
        maximo = 20*np.log10(np.max(np.abs(spectrum[cero[0][0]:int(N//2+1)]))/np.max(np.abs(spectrum[0:int(N//2+1)])) + np.finfo(float).eps)
        print(maximo)
        
        plt.figure()
        plt.grid()
        plt.suptitle('Ventana de ' + label)
        
        plt.subplot(2,1,1)
        plt.plot(tt, ven)
        plt.title('Ventana en el tiempo')
        plt.xlabel('Magnitud [V]')
        plt.ylabel('Tiempo [Seg]')
        
        plt.subplot(2,1,2)
        plt.stem(ff_padding[0:int((padding*N)//2+1)], 2.0/(N) * np.abs(spectrum[0:int((padding*N)//2+1)])/(2.0/(N) * np.max(np.abs(spectrum))))
        plt.title('Espectro de la ventana')
        plt.xlim(-1,20)
        plt.xlabel('Magnitud [V]')
        plt.ylabel('Frecuencia [Hz]')

testbench()
    
