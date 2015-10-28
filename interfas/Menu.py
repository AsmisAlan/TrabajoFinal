# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:37 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic 
from control.Control_mascota import Control_mascota
from control.Control_persona import Control
from control.Control_paseo import Control_paseo
from interfas.Error_alta_baja import Error_alta_baja
from interfas.ManejoTablas import CargarTablaPaseo
from interfas.Submenu_alta_baja_paseo import Submenu_alta_baja_paseo
from interfas.Menu_gestion import Menu_gestion
from interfas.Mapa import Mapa
from interfas.Menu_gestion_mascota import Menu_gestion_mascota
import time




#==============================================================================
#                             MENU PRINCIPAL
#==============================================================================

Menu = uic.loadUiType("interfas/Menu.ui")[0]
class Menu(QtGui.QMainWindow,Menu):
    
    def __init__(self, parent=None):
         QtGui.QMainWindow.__init__(self, parent)
         self.setupUi(self)
         
         self.lista_mascotas = Control_mascota()
         self.lista_clientes = Control('CLIENTE')
         self.lista_paseadores = Control('PASEADOR') 
         self.lista_paseos = Control_paseo()

         self.boton_cliente.clicked.connect(self.gestionCliente)
         self.boton_mascota.clicked.connect(self.gestionMascota)
         self.boton_paseador.clicked.connect(self.gestionPaseador)
         self.boton_nuevo_paseo.clicked.connect(self.gestionPaseo)
         self.llegada.clicked.connect(self.marcarLlegada)
         self.boton_mapa.clicked.connect(self.verRecorrido)
         self.tabla_paseos.clicked.connect(self.activar)
         
    
    def gestionCliente(self):
        self.menu_cliente = Menu_gestion(self.lista_clientes,self.lista_mascotas)
        self.menu_cliente.setVisible(True)
        
    def gestionMascota(self):
        self.menu_mascota = Menu_gestion_mascota(self.lista_clientes,self.lista_paseadores,self.lista_mascotas)
        self.menu_mascota.setVisible(True)
    
    def gestionPaseador(self):
        self.menu_paseador = Menu_gestion(self.lista_paseadores,self.lista_mascotas)
        self.menu_paseador.setVisible(True)
    
    def gestionPaseo(self):
        if(self.lista_paseadores.tamanio() > 0):
            self.menu_nuevo_paseo = Submenu_alta_baja_paseo(self.lista_paseos,self.lista_paseadores,self.tabla_paseos,self.lista_paseadores.cantidad_mascotas(self.lista_mascotas))
            self.menu_nuevo_paseo.setVisible(True)
        else:
            self.mostra_error('No hay Paseadores.')
        
    def marcarLlegada(self):
        self.lista_paseos.obtener(self.tabla_paseos.currentRow()).set_hora_llegada(time.strftime('%H : %M : %S'))
        CargarTablaPaseo(self.tabla_paseos , self.lista_paseos)
        self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
    
    def verRecorrido(self):
        paseador = self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_paseador()  
        direcciones = self.lista_clientes.direcciones(self.lista_mascotas.mascotas(paseador))
        print(direcciones)        
        self.mapa_recorrido = Mapa(direcciones)
        self.mapa_recorrido.setVisible(True)
        
    def activar(self):
        if(self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_hora_llegada().find('-') > -1):
            self.llegada.setEnabled(True)
        else:
            self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText( detalles)
            
        
 

app = QtGui.QApplication(sys.argv)
menu = Menu(None)
menu.show()
app.exec_()