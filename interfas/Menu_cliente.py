# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:25 2015

@author: Franco
"""

import sys

from PyQt4 import QtCore, QtGui, uic

from entidades import Cliente
from control import Control


menu_cliente = uic.loadUiType('Menu_cliente.ui')[0]

class Menu_Cliente(QtGui.QWidget,menu_cliente):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_alta_cliente.clicked.connect(self.iniciar_alta)
    
    
    def iniciar_alta(self):
        self.boton_alta_cliente = Submenu_alta(None)
        self.boton_alta_cliente.show()




submenu_alta = uic.loadUiType('Submenu_alta.ui')[0]

class Submenu_alta(QtGui.QWidget, submenu_alta,Control):
    
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
        
        nuevo_cliente = Cliente(nombre, apellido, dni, telefono,direccion)
        
        if not(Control.control_cliente(nuevo_cliente)):
             self.close()
        else:
            error = Error_cliente()
            error.show()
             
             
error_alta = uic.loadUiType('Error_cliente.ui')[0]

class Error_cliente(QtGui.QDialog, error_alta):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        




app = QtGui.QApplication(sys.argv)
MyWindow = Menu_Cliente(None)
MyWindow.show()
app.exec_()        