# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 20:46:58 2018

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
    ecg_one_lead = ecg_one_lead.reshape(N)
    
    df = fs/N
    ff = np.linspace(0, int((N-1)*df), int(N))
    
#    Segmentos de interés
    regs_interes = ( 
            np.array([5, 5.2]) *60*fs, # minutos a muestras
            np.array([12, 12.4]) *60*fs, # minutos a muestras
            np.array([15, 15.2]) *60*fs, # minutos a muestras
            )

    
    aux = signal.medfilt(ecg_one_lead, 199)
    b = signal.medfilt(aux, 599)
    x = ecg_one_lead - b
    
    spectrum = fft(b)
    psd = pow((1/N)*np.abs(spectrum), 2)
    
    plt.figure()
    plt.plot(ff[0:int(N//2+1)], psd[0:int(N//2+1)])
    
    for ii in regs_interes:
    
        # intervalo limitado de 0 a cant_muestras
        zoom_region = np.arange(np.max([0, ii[0]]), np.min([N, ii[1]]), dtype='uint')
        
        plt.figure()
        plt.plot(zoom_region, ecg_one_lead[zoom_region], label='ECG', lw=2)
        plt.plot(zoom_region, x[zoom_region], label = 'ECG Filtrado')
#        plt.plot(zoom_region, ECG_f_win[zoom_region], label='Win')
#        plt.plot(zoom_region, ECG_f_butt[zoom_region], label='Butter')
        
        plt.title('ECG filtering example from ' + str(ii[0]) + ' to ' + str(ii[1]) )
        plt.ylabel('Adimensional')
        plt.xlabel('Muestras (#)')
        
        axes_hdl = plt.gca()
        axes_hdl.legend()
        axes_hdl.set_yticks(())
                
        plt.show()

testbench()
    