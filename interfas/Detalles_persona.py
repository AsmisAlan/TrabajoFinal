# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 14:05:43 2015

@author: alan
"""


from PyQt4 import QtGui, uic 
from interfas.Mapa import Mapa
info = uic.loadUiType("interfas/detalles_persona.ui")[0]
class Detalles_persona(QtGui.QDialog,info):
    
    def __init__(self,persona,roll, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)
        self.boton_mapa.clicked.connect(self.mapa)
        self.titulo.setText(roll)
        self.completar_campos(persona)
        
    def completar_campos(self,persona):
        self.nombre.setText( persona.get_nombre() )
        self.apellido.setText (persona.get_apellido() ) 
        self.dni.setText (str (persona.get_DNI()) )
        self.direccion.setText (persona.get_direc() )
        self.telefono.setText(str(persona.get_telefono()))
        
    def mapa(self):
        self.vista_mapa = Mapa(self.direccion.text())
        self.vista_mapa.setVisible(True)
        