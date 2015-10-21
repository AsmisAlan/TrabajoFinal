# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:55:50 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic ,QtCore


Menu = uic.loadUiType("Menu_paseador.ui")[0]
class Menu_paseador(QtGui.QMainWindow,Menu):
    
    def __init__(self, parent=None):
         QtGui.QDialog.__init__(self, parent)
         self.setupUi(self)
         self.boton_nuevo.clicked.connect(self.nuevoPaseador)
         self.boton_detalles.clicked.connect(self.detallesPaseador)
         self.boton_mapa.clicked.connect(self.direccionPaseador)
    
    def nuevoPaseador(self):
        print('nuevo')
        
    def detallesPaseador(self):
        print('detalles')
    
    def direccionPaseador(self):
        print('mapa')
