# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:55:50 2015

@author: alan
"""


from PyQt4 import QtGui, uic ,QtCore
from interfas.dialogo_alta_baja import Submenu_alta_baja
from interfas.Submenu_alta_baja_mascota import Submenu_alta_baja_mascota

Menu = uic.loadUiType("interfas/Menu_gestion.ui")[0]
class Menu_gestion(QtGui.QWidget,Menu):

    def __init__(self,string, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.texto_menu = string
         self.titulo_submenu.setText('GESTION ' + string )
         if (string != 'MASCOTA'):   
             self.boton_nuevo.clicked.connect(self.nuevo)
             self.tabla_mascota.close()
         else:
             self.boton_nuevo.clicked.connect(self.nueva_mascota)
             self.tabla_persona.close()
             
    
    def nuevo(self):
        self.nuevo = Submenu_alta_baja()
        self.nuevo.setVisible(True)
        self.nuevo.text.setText('NUEVO ' + self.texto_menu )
    

    def nueva_mascota(self):
        self.nueva_mascota = Submenu_alta_baja_mascota()
        self.nueva_mascota.setVisible(True)
    
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')

        
