# -*- coding: utf-8 -*-


import sys, os
import hashlib
import time

def crearHash(algoritmoAUtilizar,archivo):    
    if(algoritmoAUtilizar=='md5'):
        sha= hashlib.md5()
    elif (algoritmoAUtilizar=='sha1'):   
        sha= hashlib.sha1()
    elif (algoritmoAUtilizar=='sha224'):   
        sha= hashlib.sha224()
    elif (algoritmoAUtilizar=='sha256'):   
        sha= hashlib.sha256()
    elif (algoritmoAUtilizar=='sha384'):   
        sha= hashlib.sha384()    
    elif (algoritmoAUtilizar=='sha512'):   
        sha= hashlib.sha512()       
    with open(archivo,'rb') as afile:
            buffer= afile.read(2048)
            while len(buffer) > 0:
                sha.update(buffer)
                buffer = afile.read(2048)  
            hashFile=sha.hexdigest()
    return hashFile        


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

def escribirHaOr(l):
    print(l)
    alg=l[0]
    l.pop(0)
    f = open (t, "w")
    for x in range(len(l)):       
        q=buscarFichero(l[x])
        print(q)
        v=crearHash(alg,q)
        f.write(l[x]+","+v+"\n")
    f.close()

print ("\n Indique el nombre del directorio donde se encuentra el fichero de configuración junto a su nombre: ")
d = input()
print ("\n Indique el nombre del directorio donde va a querer que se encuentra el fichero con los hashes junto a su nombre:")
t = input()
print ("\n Indique el nombre del directorio donde se encuentra el log junto a su nombre:")
l = input()
print ("\n Indique el nombre del directorio donde alojará el programa principal:")
dirPro=input()
print ("Indique su contraseña:")
password = input()

if(hashlib.sha256((password).encode('utf-8')).hexdigest() == 'b20b0f63ce2ed361e8845d6bf2e59811aaa06ec96bcdb92f9bc0c5a25e83c9a6'):  

    f = open (dirPro+"Programa1.py", "r")
    lineas=f.readlines()
    f.close()
    
    f = open (dirPro+"Programa1.py", "w")
    for linea in lineas: 
        if ((linea.find("d = r"))!=-1):
            f.write("d = r"+ "'"+d+ "'"+' \n')
        elif((linea.find("f = r"))!=-1):
            f.write("f = r"+ "'"+t+ "'"+' \n')
        elif((linea.find("l = r"))!=-1):
            f.write("l = r"+ "'"+l+ "'"+' \n')
        else:
            f.write(linea)
    f.close()        
   
    
    #
    z=[]
    zz=[]
    f = open (d, "r")
    lineashashes=f.readlines()
    for q in lineashashes:
        z.append(q.rsplit("\n"))
    f.close()
    print(z[0][0])
    for r in range(len(z)):
        zz.append(z[r][0])
    print(zz)
    escribirHaOr(zz)
    
    #
    
    
    
    f = open (dirPro+"Grafica.py", "r")
    lineass=f.readlines()
    f.close()
    
    f = open (dirPro+"Grafica.py", "w")
    for linea in lineass:
        if (linea.find("log = r")!=-1):        
            f.write("log = r"+'"'+ l +'"'+' \n')
        else:
            f.write(linea)
    f.close()    

else:
   exit()


   
