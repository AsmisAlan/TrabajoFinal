# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 22:55:50 2015

@author: alan
"""


from PyQt4 import QtGui, uic ,QtCore
from interfas.Submenu_alta_baja import Submenu_alta_baja
from interfas.ManejoTablas import *
from interfas.Mapa import Mapa
from interfas.Detalles_persona import Detalles_persona
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion(QtGui.QWidget,Menu_ge):

    def __init__(self,lista,mascotas, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.tabla_mascota.close()
         self.texto_menu = lista.get_roll() #guardo el roll que poseen los objetos de la lista.
         self.lista = lista #La variable por referencia Self.lista va a apuntar al mismo objeto que la lista.
         self.lista_mascotas = mascotas
         self.titulo_submenu.setText('GESTION ' + self.texto_menu )  
         CargarTabla(self.tabla_persona ,self.lista)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nuevo)
         self.tabla_persona.doubleClicked.connect(self.modificar)
    
    def modificar(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),0) #devuelve el documento de la tabla
        if (pos != None ):
            doc = int (QtGui.QTableWidgetItem.text(pos) ) # combierte el documento qtable gidget en entero
            self.nuevo = Submenu_alta_baja( self.lista,self.tabla_persona,self.lista.obtener_pos_dni(doc) )
            self.nuevo.setVisible(True)

    def nuevo(self):
        #esto pide, la lista , una tabla y la persona si se quiere modificar.
        self.nuevo = Submenu_alta_baja( self.lista,self.tabla_persona ) 
        self.nuevo.setVisible(True)
    
    def detalles(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),0)
        if (pos != None ):
            doc = int (QtGui.QTableWidgetItem.text(pos) )
            self.detallar = Detalles_persona(self.lista.obtener_por_dni(doc),self.lista.get_roll(),self.lista_mascotas)
            self.detallar.setVisible(True)
    
    def direccion(self):
        pos = self.tabla_persona.item(self.tabla_persona.currentRow(),4)
        if (pos != None ):
            direccion = str (QtGui.QTableWidgetItem.text(pos) )
            self.mapa_persona = Mapa(direccion)
            self.mapa_persona.setVisible(True)
            
        
        
