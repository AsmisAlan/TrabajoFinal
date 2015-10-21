# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 15:30:06 2015

@author: alan
"""

from PyQt4 import QtGui, uic

dialogo_alta_baja_paseo= uic.loadUiType('alta_baja_paseo.ui')[0]

class Submenu_alta_baja_paseo(QtGui.QWidget, dialogo_alta_baja_paseo):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        