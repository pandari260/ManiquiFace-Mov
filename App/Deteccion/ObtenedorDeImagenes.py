'''
Created on 13 ene. 2018
Este modulo se encarga de obtener las imagenes de la camara para cualquiera que las necesite
@author: Javi-PC
'''
import cv2
import Configuracion as Configuracion



alto = float(Configuracion.leer("ObtenedorDeImagenes","alto"))
ancho = float(Configuracion.leer("ObtenedorDeImagenes","ancho")) 
#inicializacion de la camara
vc = cv2.VideoCapture(0)
vc.set(cv2.CAP_PROP_FRAME_WIDTH, ancho)
vc.set(cv2.CAP_PROP_FRAME_HEIGHT, alto)

def main():
    print(ancho)
    print(alto)

main()