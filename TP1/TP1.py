# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 19:58:09 2018
TP1
Procesamiento Digital de Señales
Francisco Maiocchi
UTN FRBA 2018
"""
#%%  Importacion de librerias
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#%%  Funciones requeridas
def generador_senoidal (fs, f0, N, a0=1, p0=0):
    """   
    brief:  Generador de señales senoidal, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    f0:     frecuencia de la senoidal [Hz]
    a0:     amplitud pico de la señal [V]
    p0:     fase de la señal sinusoidal [rad]
    
    como resultado la señal devuelve:
    
    signal: senoidal evaluada en cada instante 
    tt:     base de tiempo de la señal
    """    
    
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    signal = a0*np.sin(2*np.pi*f0*tt + p0)
    
    return tt, signal

def generador_ruido (fs, N, mean, variance):
    """ 
    
    brief:  Generador de ruido, con argumentos
    
    fs:     frecuencia de muestreo de la señal [Hz]
    N:      cantidad de muestras de la señal a generar
    u:      media
    v:      varianza
    
    como resultado la señal devuelve:
    
    signal: ruido con valor medio u y varianza v 
    tt:     base de tiempo de la señal
    """
    # vector de tiempos
    tt = np.linspace(0, (N-1)/fs, N)
    signal = np.random.normal(mean, np.sqrt(variance), N)  #normal recibe el desvio, no la varianza
    
    return tt, signal     

def generador_cuadrada (a0, N, d):
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal

def generador_triangular (amin, amax, N, d, fs):
    
    tt = np.linspace(0, (N-1)/fs, N)
    Nsim = int(np.round(N*d))
    
    a = amin + (amax - amin)*tt[0:Nsim]/tt[Nsim]
    b = (amin-amax)*tt[Nsim:N]/(tt[N-1] - tt[Nsim]) + amax - (amin-amax)*tt[Nsim]/(tt[N-1] - tt[Nsim])
    
    signal = np.concatenate((a,b))
    return tt, signal
             
    
    
    signal = np.concatenate((a0*np.ones(int(np.round(N*d))),-a0*np.ones(int(np.round(N*(1-d))))))
    return signal
#%%  Testbench de senoidales    
def testbench_senoidal ():
    
    N  = 1000 # muestras
    fs = 1000 # Hz

    ##################
    # a.1) Senoidal #
    #################
    
    a0 = 1 # Volts
    p0 = 0 # radianes
    f0 = 10  # Hz

    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
    grafico = plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
    ##################
    # a.2) Senoidal #
    #################
    
    a0 = 1 # Volts
    p0 = 0 # radianes
    f0 = fs/2   # Hz
    
    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
    plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
    ##################
    # a.3) Senoidal #
    #################
    
    a0 = 1       # Volts
    p0 = np.pi/2 # radianes
    f0 = fs/2    # Hz

    tiempo, señal = generador_senoidal(fs, f0, N, a0, p0)
    plt.plot(tiempo, señal, label = str(f0) + " Hz" )
    
    # Label del ploteo   
    plt.title('Señal: senoidal')
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.xlim((-0.05,1.05))
    plt.ylim((-1.1,1.1))
    # Escribo la leyenda
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')

#%%  Testbench de ruido

def testbench_ruido():
    
    N  = 1000 # muestras
    fs = 1000 # Hz
    
    mean = 0
    variance = 1
    
    tiempo, señal = generador_ruido(fs, N, mean, variance)
    grafico = plt.plot(tiempo, señal, label = '$\sigma^2$ = ' + str(variance) + ' - $\hat{{\sigma}}^2$ :{0:.3f}'.format(np.var(señal)))
    
    
    # Label del ploteo   
    plt.title('Señal: ruido gaussiano')
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    # Escribo la leyenda
    axes_hdl = plt.gca()    # Tomo el objeto axes (Lugar donde se grafica)
    axes_hdl.legend(loc='upper right')

#%%  Testbench cuadrada

def testbench_cuadrada():
    
    N = 1000
    d = 0.22
    plt.plot(generador_cuadrada(1,N,d))
    
#%%  Testbench de triangular

def testbench_triangular():
    
    N  = 1000 # muestras
    fs = 1000 # Hz
    
    amin = -3
    amax = 1
    d = 0.2
    
    tiempo, señal = generador_triangular(amin, amax, N, d, fs)
    plt.plot(tiempo, señal)
    
    # Label del ploteo   
    plt.title('Señal: triangular')
    plt.xlabel('Tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    plt.xlim((-0.05,1.05))
    plt.ylim((1.05*amin,1.05*amax))

    
#%%  Seleccione el testbench que se quiere probar
#testbench_senoidal()
#testbench_ruido()
#testbench_cuadrada()
testbench_triangular()
