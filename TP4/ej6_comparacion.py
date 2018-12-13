# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 21:57:13 2018

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
    peak_offset = 369
    mat_struct = sio.loadmat('./ECG_TP4.mat')
    
    ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
    N = len(ecg_one_lead)
    ecg_one_lead = ecg_one_lead.reshape(N)
    hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    hb_1 = hb_1.reshape(len(hb_1))
    qrs_detections = vertical_flaten(mat_struct['qrs_detections'])
    qrs_detections = qrs_detections.reshape(len(qrs_detections))
    
    verdadero_p = 0
    falso_p = 0
    falso_n = 0
    
    b = signal.medfilt(signal.medfilt(ecg_one_lead, 199), 599)
    x = ecg_one_lead - b
    
    reverse_hb_1 = hb_1[::-1]
    
    latidos = signal.lfilter((reverse_hb_1), 1.0, (x))
    neg = np.where(latidos < 0)
    latidos[neg] = 0
    latidos = latidos/np.max(latidos)
    latidos = latidos*latidos

    picos, _ = signal.find_peaks(latidos, rel_height=0.5, width=(10, 25), prominence = 0.0744)
    
    print("Cantidad de latidos del test: " + str(len(qrs_detections)))
    print("Cantidad de latidos del estimador: " + str(len(picos)))
    
    shift_picos = picos - peak_offset
    
#    for lat in qrs_detections:
#        
#        index = np.where(np.logical_and(shift_picos >= (lat - 3), shift_picos <= (lat + 3)))
#        if len(index) == 1:
#            verdadero_p = verdadero_p + 1
#            np.delete(shift_picos, index)
#        else:
#            falso_n = falso_n + 1
#    
#    falso_p = len(picos)
    
    hit = False
    
    for lat in qrs_detections:
        for i in range(len(shift_picos)):
            if ((shift_picos[i] >= (lat-3)) and (shift_picos[i] <= (lat+3))):
                shift_picos = np.delete(shift_picos, i)
                verdadero_p = verdadero_p + 1
                hit = True
                break
        if hit == False:
            falso_n = falso_n + 1
        hit = False
    
    falso_p = len(shift_picos)
    falso_n = falso_n - falso_p
            
    
    print("Verdaderos positivos: " + str(verdadero_p))
    print("Falsos negativos: " + str(falso_n))
    print("Falsos positivos: " + str(falso_p))

    
            
        
        
    
    
testbench()