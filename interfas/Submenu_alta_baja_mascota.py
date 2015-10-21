# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 04:35:48 2015

@author: alan
"""
import random
from PyQt4 import QtGui, uic, QtCore
import Error_alta_baja


dialogo_alta_baja_mascota= uic.loadUiType('alta_baja_mascota.ui')[0]

class Submenu_alta_baja_mascota(QtGui.QWidget, dialogo_alta_baja_mascota):
    
    def __init__ (self,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.barra_peso.valueChanged.connect(self.manejo_peso)
        self.chico.show()
        self.mediano.close()
        self.grande.close()
        self.boton_guardar.clicked.connect(self.guardar)
        
        
        
    def manejo_peso(self):
        if (self.Peso.intValue() < 20):
            self.chico.show()
            self.mediano.close()
            self.grande.close()
        elif(self.Peso.intValue() < 50):
            self.chico.close()
            self.mediano.show()
            self.grande.close()
        else:
            self.chico.close()
            self.mediano.close()
            self.grande.show()
            
            
    def guardar(self):
        error = ''
        #ID = len(lista_mascota)
        
        #Paseador = random.choice(lista_paseador).get_dni()
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += ' nombre'
        raza = self.linea_raza.text()
        if (raza == ''):
            error += ' raza'
        peso = self.Peso.intValue()
        
        if(error !=''):
            self.error(error)
        
    def error(self,error):
        self.error = Error_alta_baja.Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + error)
    
        
            