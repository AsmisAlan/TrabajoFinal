# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:55:50 2015

@author: alan
"""


from PyQt4 import QtGui, uic ,QtCore
from dialogo_alta_baja import Submenu_alta_baja


Menu = uic.loadUiType("Menu_gestion.ui")[0]
class Menu_gestion(QtGui.QWidget,Menu):
    
    def __init__(self,string, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         self.boton_nuevo.clicked.connect(self.nuevo)
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.nuevo = Submenu_alta_baja()
         self.texto_menu = string
         self.titulo_submenu.setText('GESTION ' + string )
    
    def nuevo(self):
        self.nuevo.setVisible(True)
        self.nuevo.text.setText('NUEVO ' + self.texto_menu )
        
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')

        
