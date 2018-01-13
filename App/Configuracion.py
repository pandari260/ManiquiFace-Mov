'''
Created on 13 ene. 2018

@author: Javi-PC
'''

import ConfigParser  
import sys

nombreArchivo = "config.cfg"
opcion = ""
cfg = ConfigParser.ConfigParser()  

def update():
    f = open(nombreArchivo, "w")  
    cfg.write(f) 
    f.close()
    
def nuevaSeccion(nombre):
    cfg.add_section(nombre)
    update()

def nuevaOpcion(section, option, value):
    cfg.set(section, option, value)
    update()

def leer(seccion, nombre):
    cfg.read(nombreArchivo)
    return cfg.get(seccion, nombre)

  
    




if __name__ == '__main__':
    print(leer("login", "nombre"))   
