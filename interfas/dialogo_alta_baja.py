# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:25 2015

@author: Franco
"""



from PyQt4 import QtGui, uic



dialogo_alta_baja = uic.loadUiType('alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar)
        
    def guardar(self,Control):
        nombre = self.linea_nombre.getText()
        apellido = self.linea_apellido.getText()
        dni = self.linea_dni.getText()
        telefono = self.linea_telefono.getText()
        direccion = self.linea_direccion.getText()
             
             
error_dialogo_alta_baja = uic.loadUiType('Error_cliente.ui')[0]

class Error_alta_baja(QtGui.QDialog, error_dialogo_alta_baja):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        

  