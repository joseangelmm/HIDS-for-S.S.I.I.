# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 13:07:09 2018

@author: josea
"""
import sys, os
import hashlib
import time

def buscarFichero(nombreArchivo):  
    path = ''  
    if sys.platform == "win32": 
        directorio =  'C:\\'
    elif sys.platform == "darwin"  :
        directorio =  '/'     
    elif sys.platform == "win64"  :
        directorio =  'C:\\'      
    elif sys.platform == "linux2"  :
        directorio =  '/'    
    for root, _, files in os.walk(directorio):
        if nombreArchivo in files:
           path = os.path.join(root, nombreArchivo)
           break
    return path
    
def crearHash(algoritmoAUtilizar,archivo):
    if(algoritmoAUtilizar=="md5"):
        sha= hashlib.md5()
    elif (algoritmoAUtilizar=="sha1"):   
        sha= hashlib.sha1()
    elif (algoritmoAUtilizar=="sha224"):   
        sha= hashlib.sha224()
    elif (algoritmoAUtilizar=="sha256"):   
        sha= hashlib.sha256()
    elif (algoritmoAUtilizar=="sha384"):   
        sha= hashlib.sha384()    
    elif (algoritmoAUtilizar=="sha512"):   
        sha= hashlib.sha512()
    
    
    with open(archivo,'rb') as afile:
            buffer= afile.read(1024)
            while len(buffer) > 0:
                sha.update(buffer)
                buffer = afile.read(2048)  
            hashFile=sha.hexdigest()
    return hashFile        
    
    
def leerHashes(directorioHashes):
    hashesOriginales= []
    diccionario = {}
    hashesOriginales = [line.rstrip("\n") for line in open(directorioHashes)]  
    for a in range(len(hashesOriginales)):
        hashesOriginalesI = hashesOriginales[a].split(',')
        diccionario[hashesOriginalesI[0]]=[hashesOriginalesI[1]]
    return diccionario

def leerArchivoConfiguracion(ficheroConfiguracion):
    Datos = []
    Datos = [line.rstrip("\n") for line in open(ficheroConfiguracion)]  
    return Datos
    
def hashesDirectorios(algoritmoAUtilizar,directorio):
    for dirName, subdirList, fileList in os.walk(directorio):
        nombreFichero = []
        hashFichero = []
        listaArchivos = []
        for fname in fileList:    
            listaArchivos.append(fname)
            for file in listaArchivos:
                nombreFichero.append(file)
                hashFichero.append(crearHash(algoritmoAUtilizar,directorio+file))
        nombreFichero.pop(0)
        hashFichero.pop(0)
        return(nombreFichero,hashFichero)           

def comprobacionFinal(hashesOriginales,hashesRealizados,Log):   
    l=0 
    k="debido a los archivos: "
    for n in hashesRealizados.keys():
        v=hashesOriginales.get(n)
        if(v!=hashesRealizados.get(n)):
            l+=1
            k+=n+" "
    f = open (Log, "a")
    ll=float(l)
    t=float(len(hashesOriginales))
    p=100*(l/len(hashesOriginales))
    q=((ll/t)*100)
    f.write(time.strftime("%x")+"-"+time.strftime("%X")+": "+str(q)+" % de error "+k+"\n")
    f.close()       

def main(directorioHashes, ficheroConfiguracion,Log):
    listadoHashes=leerHashes(directorioHashes)
    ficheroConfiguracio=leerArchivoConfiguracion(ficheroConfiguracion)
    algoritmoAUtilizar=ficheroConfiguracio[0]
    ficheroConfiguracio.pop(0)
    nuevoDiccionario = {}
    for a in range(len(ficheroConfiguracio)):
        t=buscarFichero(ficheroConfiguracio[a])
        nuevoDiccionario[ficheroConfiguracio[a]]=[crearHash(algoritmoAUtilizar,t)]
    comprobacionFinal(listadoHashes,nuevoDiccionario,Log)
    
d = r'C:\Users\josea\Desktop\aa.txt' 
f = r'C:\Users\josea\Downloads\ssii\hash\hashesnuevos.txt' 
l = r'C:\Users\josea\Downloads\ssii\log\log.txt' 
main(f,d,l)
