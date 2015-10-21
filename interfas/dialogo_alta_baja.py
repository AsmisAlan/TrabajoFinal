# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:25 2015

@author: Franco
"""



from PyQt4 import QtGui, uic
import Error_alta_baja


dialogo_alta_baja = uic.loadUiType('alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar)
        
    def guardar(self,Control):
        error = ''
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += 'nombre' 
        apellido = self.linea_apellido.text()
        if (apellido == ''):
            error += ', apellido' 
        try:
            dni = int(self.linea_dni.text())
        except(ValueError):
            error += ', dni' 
        try:
            telefono = int(self.linea_telefono.text())
        except(ValueError):
            error += ', telefono'
        direccion = self.linea_direccion.text()
        if (direccion == ''):
            error += ', direccion'
            
        if (error != ''):
            self.error(error)
        
        
    def error(self,error):
        self.error = Error_alta_baja.Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + error)
        
             

        
  