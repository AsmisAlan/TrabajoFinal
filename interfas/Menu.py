# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:37 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic 
from Menu_gestion import Menu_gestion
from Submenu_alta_baja_mascota import Submenu_alta_baja_mascota
from Submenu_alta_baja_paseo import Submenu_alta_baja_paseo

Menu = uic.loadUiType("Menu.ui")[0]
class Menu(QtGui.QMainWindow,Menu):
    
    def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
         self.boton_cliente.clicked.connect(self.gestionCliente)
         self.boton_mascota.clicked.connect(self.gestionMascota)
         self.boton_paseador.clicked.connect(self.gestionPaseador)
         self.boton_nuevo_paseo.clicked.connect(self.gestionPaseo)
         self.boton_mapa.clicked.connect(self.verRecorrido)
    
    def gestionCliente(self):
        self.menu_cliente = Menu_gestion('CLIENTE')
        self.menu_cliente.setVisible(True)
        
    def gestionMascota(self):
        self.menu_mascota = Menu_gestion('MASCOTA')
        self.menu_mascota.setVisible(True)
    
    def gestionPaseador(self):
        self.menu_paseador = Menu_gestion('PASEADOR')
        self.menu_paseador.setVisible(True)
    
    def gestionPaseo(self):
        self.menu_nuevo_paseo = Submenu_alta_baja_paseo()
        self.menu_nuevo_paseo.setVisible(True)
    
    def verRecorrido(self):
        print('estoy en la vista de mapas de recorridos')
        
        
    def CargarTabla(self,lista):
        print('aca se va a cargar una tabla con los paseos :)')
        
        
app = QtGui.QApplication(sys.argv)
menu = Menu(None)
menu.show()
app.exec_()