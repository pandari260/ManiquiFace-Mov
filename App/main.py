'''
Created on 13 ene. 2018

@author: Javi-PC
'''
import Configuracion
import Deteccion.Camara as camara

from cv2 import *
import sys
from Deteccion.Detector import Detector
seEncontro, x,y,w,h = False,0,0,0,0


if __name__ == '__main__':
    path ="cascade.xml"
    detector =Detector(path)
    while True:
        foto = camara.tomarFoto()
        seEncontro, x,y,w,h = detector.detectar(foto)
        print("se encontro: " + str(seEncontro))
        imshow("testcam", foto)
        if waitKey(1) & 0xFF == ord('q'):
            sys.exit()
    