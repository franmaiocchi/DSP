# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:41:02 2018

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
    peak_offset = 369
    # para listar las variables que hay en el archivo
    #io.whosmat('ECG_TP4.mat')
    mat_struct = sio.loadmat('./ECG_TP4.mat')
    
    ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
    N = len(ecg_one_lead)
    ecg_one_lead = ecg_one_lead.reshape(N)
    
    hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    hb_1 = hb_1.reshape(len(hb_1))
    hb_2 = vertical_flaten(mat_struct['heartbeat_pattern2'])
    hb_2 = hb_2.reshape(len(hb_2))
    qrs_detections = vertical_flaten(mat_struct['qrs_detections'])
    qrs_detections = qrs_detections.reshape(len(qrs_detections))
    
    zoom_region = np.arange(5000, 12000, dtype='uint')
    
    det = qrs_detections[6:14]
    
    reverse_hb_1 = hb_1[::-1]
    
    latidos = signal.lfilter((reverse_hb_1), 1.0, (ecg_one_lead[zoom_region]))
    neg = np.where(latidos < 0)
    latidos[neg] = 0
    latidos = latidos/np.max(latidos)
    latidos = latidos*latidos
    picos, _ = signal.find_peaks(latidos, height = 0.2, distance = 250)

    
#%% Resultados
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(zoom_region, ecg_one_lead[zoom_region])
    plt.vlines(zoom_region[picos-peak_offset], ymin = -33000, ymax = 33000, color = 'r', linestyles = 'dashed')
    plt.vlines(det, ymin = -33000, ymax = 33000, color = 'r', linestyles = 'dashed')
    plt.title("ECG")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.subplot(2,1,2)
    plt.plot(zoom_region, latidos)
    plt.plot(zoom_region[picos], latidos[picos], "x")
    plt.title("Deteccion")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.suptitle("Matched filter manual")
        
testbench()