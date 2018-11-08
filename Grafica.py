# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 23:39:24 2018

@author: josea
"""

import matplotlib.pyplot as plt

def metodoGrafica(log):
    lista= []
    fechas= []
    error= []
    listaNueva=[]
    with open(log,'r') as afile:
        for i in afile.readlines():
            palabras = i[:-1].split(" ")
            for n in palabras:
                lista.append(n)
                
    listaNueva = [line.rstrip("\n") for line in open(log)]    
    for i in listaNueva:
        x=i.split(" ")        
        fa=x[0].split("-")
        faa=fa[0].split("/")
        fab=fa[1].split(":")
        fechas.append(faa[0]+"\n"+faa[1]+"\n"+faa[2]+"\n"+"-"+"\n"+fab[0]+"\n"+fab[1]+"\n"+fab[2])
        error.append(float(x[1]))
    plt.figure(figsize=(10,7))
    plt.plot(fechas,error)
    return plt.show()

log = r"C:\Users\josea\Downloads\ssii\log\log.txt" 
metodoGrafica(log) 
