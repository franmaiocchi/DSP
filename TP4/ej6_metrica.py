# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 20:41:51 2018

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
    # para listar las variables que hay en el archivo
    #io.whosmat('ECG_TP4.mat')
    mat_struct = sio.loadmat('./ECG_TP4.mat')
    
    ecg_one_lead = vertical_flaten(mat_struct['ecg_lead'])
    N = len(ecg_one_lead)
    ecg_one_lead = ecg_one_lead.reshape(N)
    plt.plot(ecg_one_lead)
    
    hb_1 = vertical_flaten(mat_struct['heartbeat_pattern1'])
    hb_1 = hb_1.reshape(len(hb_1))
    hb_2 = vertical_flaten(mat_struct['heartbeat_pattern2'])
    hb_2 = hb_2.reshape(len(hb_2))
    qrs_detections = vertical_flaten(mat_struct['qrs_detections'])
    qrs_detections = qrs_detections.reshape(len(qrs_detections))
    
    aux = []
    
    for i in range(1, len(qrs_detections)):
        aux.append(qrs_detections[i] - qrs_detections[i-1]) 
    
    print("La distancia minima entre picos segun la qrs_detections es: " + str(np.min(aux)))

    
    b = signal.medfilt(signal.medfilt(ecg_one_lead, 199), 599)
    x = ecg_one_lead - b
    
    zoom_region = np.arange(5000, 12000, dtype='uint')
    
    det = qrs_detections[6:14]
    
    reverse_hb_1 = hb_1[::-1]
    
    latidos = signal.lfilter((reverse_hb_1), 1.0, (x))
    neg = np.where(latidos < 0)
    latidos[neg] = 0
    latidos = latidos/np.max(latidos)
    latidos = latidos*latidos
    
    # Voy a analizar los parametros de los picos posta
#    width_template = signal.peak_widths(latidos, (qrs_detections + peak_offset), rel_height=0.5)
##    prominences_template = signal.peak_prominences(latidos, (qrs_detections + peak_offset), wlen = 10)
#    width_min_location = np.where(width_template[0] == np.min(width_template[0]))
#    width_max_location = np.where(width_template[0] == np.max(width_template[0]))
#    print("El width_template minimo es: " + str(np.min(width_template[0])) + " en " + str(qrs_detections[int(width_min_location[0])]))
#    print("El width_template maximo es: " + str(np.max(width_template[0])) + " en " + str(qrs_detections[int(width_max_location[0])]))
#    print("El width_template average es: " + str(np.average(width_template[0])))
##    print("La prominencia minima es: " + str(np.min(prominences_template[0])))
##    print("La prominencia maxima es: " + str(np.max(prominences_template[0])))
##    print("La prominencia average es: " + str(np.average(prominences_template[0])))
##    print("La altura del pico minimo del template es: " + str(np.min(latidos[qrs_detections+peak_offset])))
    
#    picos, _ = signal.find_peaks(latidos, distance = 325, height = 0.08, width = (5, 30), rel_height = 0.5)
#    picos, _ = signal.find_peaks(latidos, height = 0.03515, rel_height=0.5, width=(11, 23.5), distance = 50, prominence = 0.073)
#    picos, _ = signal.find_peaks(latidos, height = 0.03515, rel_height=0.5, width=(10, 24), distance = 50, prominence = 0.0745) #1898
    picos, _ = signal.find_peaks(latidos, rel_height=0.5, width=(10, 25), prominence = 0.0744)
    half_width = signal.peak_widths(latidos, picos, rel_height=0.5)
    prominences = signal.peak_prominences(latidos, picos)
    width_min_location = np.where(half_width[0] == np.min(half_width[0]))
    width_max_location = np.where(half_width[0] == np.max(half_width[0]))
    prominence_min_location = np.where(prominences[0] == np.min(prominences[0]))
    prominence_max_location = np.where(prominences[0] == np.max(prominences[0]))
    print("El half_width minimo es: " + str(np.min(half_width[0])) + " en " + str(picos[int(width_min_location[0])]))
    print("El half_width maximo es: " + str(np.max(half_width[0])) + " en " + str(picos[int(width_max_location[0])]))
    print("El half_width average es: " + str(np.average(half_width[0])))
    print("El prominence minimo es: " + str(np.min(prominences[0])) + " en " + str(picos[int(prominence_min_location[0])]))
    print("El prominence maximo es: " + str(np.max(prominences[0])) + " en " + str(picos[int(prominence_max_location[0])]))
    print("El prominence average es: " + str(np.average(prominences[0])))
    print("La altura del pico minimo es: " + str(np.min(latidos[picos])) + " en " + str(np.where(latidos == np.min(latidos[picos]))))
    
    print("Numero de picos de qrs_detections: " + str(len(qrs_detections)))
    print("Numero de picos de mi detector: " + str(len(picos)))
    
    
    plt.figure()
    plt.subplot(2,1,1)
    plt.plot(ecg_one_lead)
    plt.vlines((picos-peak_offset), ymin = -330000, ymax = 330000, color = 'r', linestyles = 'dashed')
#    plt.vlines(qrs_detections, ymin = -330000, ymax = 330000, color = 'r', linestyles = 'dashed')
    plt.title("ECG")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.xlim(50000,60000)
    plt.ylim(-30000, 30000)
    plt.subplot(2,1,2)
    plt.plot(latidos)
    plt.plot(picos, latidos[picos], "x")
    plt.hlines(*half_width[1:], color="C2")
    plt.title("Deteccion")
    plt.ylabel('Adimensional')
    plt.grid()
    plt.xlim(50000,60000)
    plt.suptitle("Matched filter manual")

    
testbench()