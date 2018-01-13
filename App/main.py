'''
Created on 13 ene. 2018

@author: Javi-PC
'''
import Configuracion
import Deteccion.ObtenedorDeImagenes as camara
from cv2 import *


if __name__ == '__main__':
    
    while True:
        foto = camara.obtener()
        imshow("testcam", foto)
        if waitKey(1) & 0xFF == ord('q'):
            sys.exit()
    