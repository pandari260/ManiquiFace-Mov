'''
Created on 12 ene. 2018

@author: Javi-PC
'''

import serial

class ComunicadorSerial(object):
    '''
    Esta clase se ocupa de enviar datos a la placa arduino.
    para ello el metovo enviar recive un entero lo combierte a char y lo envia a la placa por el metodo write
    '''
    def __init__(self, params):
        self.arduino = serial.Serial('COM6', 9600)
    def enviar(self, dato):
        toChar =unichr(60)
        self.arduino.write(bytes(toChar))

        