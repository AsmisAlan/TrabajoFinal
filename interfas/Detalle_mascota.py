# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 12:54:31 2015

@author: Franco
"""

from PyQt4 import QtGui, uic
from interfas.Mapa import Mapa

detalle_mascota = uic.loadUiType('interfas/Detalle_mascota.ui')[0]

class Detalle_mascota(QtGui.QWidget, detalle_mascota):
    
     def __init__(self,mascota,cliente,paseador , parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         
         self.linea_nombre_mascota.setText(mascota.get_nombre())
         self.linea_raza_mascota.setText(mascota.get_raza())
         self.linea_peso_mascota.setText(str(mascota.get_peso()))
         self.linea_nombre_duenio.setText(cliente.get_nombre())
         self.linea_apellido_duenio.setText(cliente.get_apellido())
         self.linea_direccion_duenio.setText(cliente.get_direc())
         self.linea_telefono_duenio.setText(str(cliente.get_telefono()))
         self.linea_dni_duenio.setText(str(cliente.get_DNI()))
         self.linea_nombre_paseador.setText(paseador.get_nombre())
         self.linea_apellido_paseador.setText(paseador.get_apellido())
         self.linea_direccion_paseador.setText(paseador.get_direc())
         self.linea_telefono_paseador.setText(str(paseador.get_telefono()))
         self.linea_dni_paseador.setText(str(paseador.get_DNI()))
         self.boton_mapa_2.clicked.connect(self.mapa2)
         self.boton_mapa.clicked.connect(self.mapa)
         
         
     def mapa(self):
         self.vista_mapa = Mapa(self.linea_direccion_paseador.text())
         self.vista_mapa.setVisible(True)
             
             
     def mapa2(self):
         self.vista_mapa = Mapa(self.linea_direccion_duenio.text())
         self.vista_mapa.setVisible(True)
        
        
        