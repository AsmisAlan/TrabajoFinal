# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:45:25 2015

@author: Franco
"""



from PyQt4 import QtGui, uic
from interfas.Error_alta_baja import Error_alta_baja
from entidades.Persona import Persona
from interfas.ManejoTablas import *



dialogo_alta_baja = uic.loadUiType('interfas/alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self,lista,tabla,mascotas= None,pos= None, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.pos = pos
        self.lista  = lista
        self.tabla = tabla
       
        if(pos != None):
            persona = self.lista.lista[self.pos]
            self.lista_mascotas = mascotas
            self.linea_nombre.setText(persona.get_nombre())
            self.linea_apellido.setText(persona.get_apellido())
            self.dni_viejo = persona.get_DNI()
            self.linea_dni.setText(str(persona.get_DNI()))
            self.linea_telefono.setText(str(persona.get_telefono()))
            self.linea_direccion.setText(persona.get_direc())
            self.text.setText('MODIFICAR '+ lista.get_roll())
        else:
            self.text.setText('NUEVO '+ lista.get_roll() )
        
        self.boton_guardar.clicked.connect(self.guardar)
            
        
    def guardar(self):
        error = ''
        dni  = 0
        telefono = 0
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += 'nombre' 
        apellido = self.linea_apellido.text()
        if (apellido == ''):
            error += ', apellido' 
        try:
            dni = int(self.linea_dni.text())
        except(ValueError):
            error += ', dni' 
        try:
            telefono = int(self.linea_telefono.text())
        except(ValueError):
            error += ', telefono'
        direccion = self.linea_direccion.text()
        if (direccion == ''):
            error += ', direccion'
            
        if (error != ''): #verifica que los campos sean correctos
            self.mostra_error(error)
        else:
            self.guardar_como(Persona(nombre,apellido,dni,telefono,direccion+ 'Concepcion del Uruguay'))            
            
            
    def guardar_como(self,persona):
        if self.pos == None :            
            if(self.lista.control_agregar(persona)):
                add_in_tabla(self.tabla,self.lista)
                self.close()
            else:
                self.mostra_error('El '+self.lista.get_roll()+' con el documento' +str(persona.get_DNI())+ ' ya existe.')
        else:
            if (self.dni_viejo == persona.get_DNI()):
                self.lista.lista[self.pos] = persona
                setChangeTabla(self.tabla , self.lista,self.pos,self.tabla.currentRow())
                self.close()
            else:
                if self.lista.obtener_por_dni(persona.get_DNI()) == None :
                    self.lista.lista[self.pos] = persona
                    if (self.lista.roll == 'CLIENTE'):
                        self.lista_mascotas.modificar_dueño(self.dni_viejo,persona.get_DNI())
                    else:
                        self.lista_mascotas.modificar_paseador(self.dni_viejo,persona.get_DNI())
                    setChangeTabla(self.tabla , self.lista,self.pos,self.tabla.currentRow())
                    self.close()
                else:
                    self.mostra_error('El '+self.lista.get_roll()+' con el documento' +str(persona.get_DNI())+ ' ya existe.')
            
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
  