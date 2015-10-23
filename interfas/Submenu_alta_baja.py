# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:25 2015

@author: Franco
"""



from PyQt4 import QtGui, uic
from interfas.Error_alta_baja import Error_alta_baja
from entidades.Persona import Persona



dialogo_alta_baja = uic.loadUiType('interfas/alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self,persona = None, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.persona_aux  = persona
        self.boton_guardar.clicked.connect(self.guardar(lista))
        
    def guardar(self):
        if(self.persona_aux == None):
            self.linea_nombre.setText(self.persona_aux.get_nombre())
            self.linea_apellido.setText(self.persona_aux.get_apellido())
            self.linea_dni.setText(self.persona_aux.get_DNI())
            self.linea_telefono.setText(self.persona_aux.get_telefono())
            self.linea_direccion.setText(self.persona_aux.get_apellido())
        error = ''
        dni  = 0
        telefono = 0
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
            self.mostra_error(error)
        else:
            return Persona(nombre,apellido,dni,telefono,direccion,'Cliente')        
            self.close()
        
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
             

        
  