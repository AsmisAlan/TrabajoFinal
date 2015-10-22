# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 18:02:42 2015

@author: Franco
"""

from PyQt4 import QtGui, uic, QtCore

error_dialogo_alta_baja = uic.loadUiType('interfas/Error_cliente.ui')[0]

class Error_alta_baja(QtGui.QDialog, error_dialogo_alta_baja):
    
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)