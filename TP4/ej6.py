# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:19:29 2018

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
from scipy.interpolate import CubicSpline

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
    
    qrs_pattern1 = vertical_flaten(mat_struct['qrs_pattern1'])
    hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    hb_1 = hb_1.reshape(len(hb_1))
    hb_2 = vertical_flaten(mat_struct['heartbeat_pattern2'])
    qrs_detections = vertical_flaten(mat_struct['qrs_detections'])
    
    corr_np = np.correlate(ecg_one_lead[5000:12000], hb_1.reshape(len(hb_1)), "same")
    corr = signal.correlate(ecg_one_lead[5000:12000], hb_1, mode='same')
    
    reverse_hb_1 = hb_1[::-1]
    
    latidos = signal.lfilter((reverse_hb_1), 1.0, (ecg_one_lead[5000:12000]))
#    latidos = latidos*latidos
    
#%% Resultados
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(ecg_one_lead[5000:12000])
    plt.title("ECG")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(latidos)
    plt.title("Deteccion")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.suptitle("Matched filter manual")
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(ecg_one_lead[5000:12000])
    plt.title("ECG")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(corr)
    plt.title("Deteccion")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.suptitle("Matched filter usando signal correlation")
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(ecg_one_lead[5000:12000])
    plt.title("ECG")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(corr_np)
    plt.title("Deteccion")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.suptitle("Matched filter usando numpy correlation")
    
    plt.figure()
    plt.plot(qrs_pattern1)
    


testbench()