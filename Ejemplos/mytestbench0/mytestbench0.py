# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

# Importacion de modulos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def my_testbench( sig_type ):
    
    # Datos generales de la simulación
    fs = 1000.0 # frecuencia de muestreo (Hz)
    N = 1000    # cantidad de muestras
    
    ts = 1/fs   # tiempo de muestreo
    df = fs/N   # resolución espectral
    
    # grilla de sampleo temporal
    tt = np.linspace(0, (N-1)*ts, N)
    
    # grilla de sampleo frecuencial
    ff = np.linspace(0, (N-1)*df, N)

    # Concatenación de matrices:
    # Creamos una matriz vacia con np.array. Luego, con reshape hacemos que sea una matriz vacia de N filas y 0 columnas
    # De esta forma trabajamos con vectores columna
    # En este momento, la matriz no tiene nada, se le da ese formato para poder operar luego
    # Guardaremos las señales creadas al ir poblando la siguiente matriz vacía
    
    x = np.array([], dtype=np.float).reshape(N,0)
    
    # Idem a esto
    # x = np.array([], dtype=np.float) Matriz vacia de 1x1
    # aux = x.reshape(N,0) matriz vacia de Nx0
        
    # estructuras de control de flujo
    if sig_type['tipo'] == 'senoidal':
         
        # calculo cada senoidal de acuerdo a sus parámetros
        for this_amp, this_freq, this_phase in zip(sig_type['amplitud'], sig_type['frecuencia'], sig_type['fase']):
            # prestar atención que las tuplas dentro de los diccionarios también pueden direccionarse mediante "ii"
            aux = this_amp * np.sin( 2*np.pi*this_freq*tt + this_phase )
            # Aca aux es un vector de 1xN
            # Con reshape lo hacemos de Nx1 para poder concatenarlo a la matriz x
            # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS
            x = np.hstack([x, aux.reshape(N,1)])
    
    elif sig_type['tipo'] == 'ruido':
        
        # calculo cada señal de ruido incorrelado (blanco), Gausiano de acuerdo a sus parámetros
        # de varianza
        for this_var in sig_type['varianza']:
            aux = np.sqrt(this_var) * np.random.randn(N,1)
            # para concatenar horizontalmente es necesario cuidar que tengan iguales FILAS
            x = np.hstack([x, aux] )
        
        # Podemos agregar algún dato extra a la descripción de forma programática
        # {0:.3f} significa 0: primer argunmento de format
        # .3f formato flotante, con 3 decimales
        # $ ... $ indicamos que incluiremos sintaxis LaTex: $\hat{{\sigma}}^2$
        sig_props['descripcion'] = [ sig_props['descripcion'][ii] + ' - $\hat{{\sigma}}^2$ :{0:.3f}'.format( np.var(x[:,ii]))  for ii in range(0,len(sig_props['descripcion'])) ]
    
    else:
        
        print("Tipo de señal no implementado.")        
        return
    
    plt.figure(1)
    line_hdls = plt.plot(tt, x)
    plt.title('Señal: ' + sig_type['tipo'] )
    plt.xlabel('tiempo [segundos]')
    plt.ylabel('Amplitud [V]')
    #    plt.grid(which='both', axis='both')
    
    # presentar una leyenda para cada tipo de señal
    axes_hdl = plt.gca()
    
    # este tipo de sintaxis es *MUY* de Python
    axes_hdl.legend(line_hdls, sig_type['descripcion'], loc='upper right'  )
    
    plt.show()

    
        
# Uso de diferentes tipos de datos en Python            

## tipo de variable diccionario. Puedo crearlo iniciándolo mediante CONSTANTES

sig_props = { 'tipo': 'senoidal', 
              'frecuencia': (1, 2, 3), # Uso de tuplas para las frecuencias 
              'amplitud':   (1, 1, 1),
              'fase':       (0, 0, 0)
             } 
# Como también puedo agregar un campo descripción de manera programática
# este tipo de sintaxis es *MUY* de Python
sig_props['descripcion'] = [ str(a_freq) + ' Hz' for a_freq in sig_props['frecuencia'] ]

## Usar CTRL+1 para comentar o descomentar el bloque de abajo.
#sig_props = { 'tipo': 'ruido', 
#              'varianza': (1, 1, 1) # Uso de tuplas para las frecuencias 
#             } 
#sig_props['descripcion'] = [ '$\sigma^2$ = ' + str(a_var) for a_var in sig_props['varianza'] ]
#    
# Invocamos a nuestro testbench exclusivamente: 
my_testbench( sig_props )
    