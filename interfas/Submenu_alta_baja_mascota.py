# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 04:35:48 2015

@author: alan
"""

from PyQt4 import QtGui, uic

dialogo_alta_baja_mascota= uic.loadUiType('alta_baja_mascota.ui')[0]

class Submenu_alta_baja_mascota(QtGui.QWidget, dialogo_alta_baja_mascota):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.barra_peso.valueChanged.connect(self.manejo_peso)
        self.chico.show()
        self.mediano.close()
        self.grande.close()
        
        
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