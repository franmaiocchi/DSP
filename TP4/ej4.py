# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 20:12:09 2018

@author: Francisco
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import pdsmodulos.generador as gen
import numpy as np
import pdsmodulos.tools as tools
from scipy import signal
from scipy.fftpack import fft
import scipy.io as sio

#%% Variables de ECG_TP4.mat

# ecg_lead: Registro de ECG muestreado a fs=1 KHz durante una prueba de esfuerzo
# qrs_pattern1: Complejo de ondas QRS normal
# heartbeat_pattern1: Latido normal
# heartbeat_pattern2: Latido de origen ventricular
# qrs_detections: vector con las localizaciones (en # de muestras) donde ocurren los latidos
#%%

def vertical_flaten(a):
    
    return a.reshape(a.shape[0],1)

def testbench():
    
    fs = 1000
    # para listar las variables que hay en el archivo
    #io.whosmat('ECG_TP4.mat')
    mat_struct = sio.loadmat('./ECG_TP4.mat')
    
    ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
    N = len(ecg_one_lead)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
    hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    
#    plt.figure(1)
#    plt.plot(ecg_one_lead)
#    
#    plt.figure(2)
#    plt.plot(hb_1)
    
    spectrum = fft(ecg_one_lead.reshape(N))
    psd = pow((1/N)*np.abs(spectrum), 2)
    
#    plt.figure(3)
#    plt.plot(ff[0:int(N//2+1)], psd[0:int(N//2+1)])
    
    # Defina la plantilla del filtro
    
    fs0 = 1     # fin de la banda de detenida 0
    fc0 = 1.2     # comienzo de la banda de paso
    fc1 = 20    # fin de la banda de paso
    fs1 = 40    # comienzo de la banda de detenida 1
    
    frecs = np.array([0.0, fs0, fc0, fc1, fs1, fs/2]) / (fs/2)
    
    cant_coef = 4001
    
    # filter design
    ripple = 0.5 # dB
    atenuacion = 40 # dB
    
    gains = np.array([-atenuacion, -atenuacion, -ripple, -ripple, -atenuacion, -atenuacion])
    gains = 10**(gains/20)
    num_win1 =   signal.firwin2(cant_coef, frecs, gains , window='blackmanharris' )
    butter = signal.iirdesign(wp=np.array([fc0, fc1]) / (fs/2), ws=np.array([fs0, fs1]) / (fs/2), gpass=0.5, gstop=40., analog=False, ftype='butter', output='sos')
    
    # Esto sirve para plotear los filtros
    w, fir1 = signal.freqz(num_win1, 1)
    w, h_butter = signal.sosfreqz(butter)

    w = w / np.pi * (fs/2)
    
    plt.figure()
    plt.plot(w, 20 * np.log10(abs(fir1)), label='FIR-Win')
    
    plt.figure()
    plt.plot(w, 20*np.log10(np.abs(h_butter)), label='IIR-Butter' )
    
    ECG_f_win = signal.filtfilt(num_win1, 1, ecg_one_lead.reshape(N))
    ECG_f_butt = signal.sosfiltfilt(butter, ecg_one_lead.reshape(N))
    
    # Segmentos de interés
    regs_interes = ( 
            np.array([5, 5.2]) *60*fs, # minutos a muestras
            np.array([12, 12.4]) *60*fs, # minutos a muestras
            np.array([15, 15.2]) *60*fs, # minutos a muestras
            )
    
    for ii in regs_interes:
    
        # intervalo limitado de 0 a cant_muestras
        zoom_region = np.arange(np.max([0, ii[0]]), np.min([N, ii[1]]), dtype='uint')
        
        plt.figure()
        plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
        plt.plot(zoom_region, ECG_f_win[zoom_region], label='Win')
        plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
        
        plt.title('ECG filtering example from ' + str(ii[0]) + ' to ' + str(ii[1]) )
        plt.ylabel('Adimensional')
        plt.xlabel('Muestras (#)')
        
        axes_hdl = plt.gca()
        axes_hdl.legend()
        axes_hdl.set_yticks(())
                
        plt.show()

testbench()