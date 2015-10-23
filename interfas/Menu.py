# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:37 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic 
from entidades.Persona import Persona
from entidades.Mascota import Mascota
from control.Control_mascota import Control_mascota
from control.Control_persona import Control
from interfas.Error_alta_baja import Error_alta_baja


lista_mascotas = Control_mascota()
lista_clientes = Control('CLIENTE')
lista_paseadores = Control('PASEADOR') 


def add_in_tabla(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    apellido =QtGui.QTableWidgetItem( lista.obtener(aux).get_apellido() )
    dni = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_DNI()) )
    tel = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_telefono() ))
    direc = QtGui.QTableWidgetItem( lista.obtener(aux).get_direc() )
    tabla.setItem(aux ,0 , dni)
    tabla.setItem(aux ,1 , nombre )
    tabla.setItem(aux ,2, apellido)
    tabla.setItem(aux ,3 ,tel )
    tabla.setItem(aux ,4,direc )

def add_in_tabla_mascota(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    nombre = QtGui.QTableWidgetItem(lista.obtener(aux).get_nombre() )
    peso =QtGui.QTableWidgetItem( str(lista.obtener(aux).get_peso()) )
    raza = QtGui.QTableWidgetItem( lista.obtener(aux).get_raza() )
    dueño = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_dueño() ))
    paseador = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_paseador()) )
    tabla.setItem(aux ,0 , nombre)
    tabla.setItem(aux ,1 ,raza)
    tabla.setItem(aux ,2, peso)
    tabla.setItem(aux ,3 ,dueño )
    tabla.setItem(aux ,4,paseador)
    
#==============================================================================
#                             MENU PRINCIPAL
#==============================================================================

Menu = uic.loadUiType("interfas/Menu.ui")[0]
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
        
        
        
#==============================================================================
#              MENU DE GESTION (mascotas , paseadores , clientes)
#==============================================================================
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion(QtGui.QWidget,Menu_ge):

    def __init__(self,string, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.texto_menu = string
         self.titulo_submenu.setText('GESTION ' + self.texto_menu )
         if (self.texto_menu != 'MASCOTA'):   
             self.boton_nuevo.clicked.connect(self.nuevo)
             self.tabla_mascota.close()
             if(self.texto_menu == 'CLIENTE'):
                self.CargarTabla(lista_clientes)
             else:
                self.CargarTabla(lista_paseadores)
         else:
             self.boton_nuevo.clicked.connect(self.nueva_mascota)
             self.CargarTablaMascota(lista_mascotas)
             self.tabla_persona.close()
             
    
    def nuevo(self):
        self.nuevo = Submenu_alta_baja(self.texto_menu,self.tabla_persona)
        self.nuevo.setVisible(True)
    

    def nueva_mascota(self):
        if(lista_clientes.tamanio() > 0) and (lista_paseadores.tamanio() >0):
            self.nueva_mascota = Submenu_alta_baja_mascota(self.tabla_mascota)
            self.nueva_mascota.setVisible(True)
        else:
            self.error = Error_alta_baja()
            self.error.setVisible(True)
            self.error.mensaje_error.setText('Debes tener al menos 1 cliente/paseador.')
            self.error.titulo.setText('Error')
            
    def CargarTabla(self,lista):
        fila = 0
        for aux in lista.lista:
            self.tabla_persona.insertRow(fila)
            nombre = QtGui.QTableWidgetItem( aux.get_nombre() )
            apellido =QtGui.QTableWidgetItem( aux.get_apellido() )
            dni = QtGui.QTableWidgetItem( str(aux.get_DNI()) )
            tel = QtGui.QTableWidgetItem( str(aux.get_telefono() ))
            direc = QtGui.QTableWidgetItem( aux.get_direc() )
            self.tabla_persona.setItem(fila ,0 , dni)
            self.tabla_persona.setItem(fila ,1 , nombre )
            self.tabla_persona.setItem(fila ,2, apellido)
            self.tabla_persona.setItem(fila ,3 ,tel )
            self.tabla_persona.setItem(fila ,4,direc )
            fila+=1
            
    def CargarTablaMascota(self,lista):
        fila = 0
        for aux in lista.lista:
            self.tabla_mascota.insertRow(fila)
            nombre = QtGui.QTableWidgetItem(aux.get_nombre() )
            peso =QtGui.QTableWidgetItem( str(aux.get_peso()) )
            raza = QtGui.QTableWidgetItem( aux.get_raza() )
            dueño = QtGui.QTableWidgetItem(str( aux.get_dueño() ))
            paseador = QtGui.QTableWidgetItem( str(aux.get_paseador()) )
            self.tabla_mascota.setItem(fila ,0 , nombre)
            self.tabla_mascota.setItem(fila ,1 ,raza)
            self.tabla_mascota.setItem(fila ,2, peso)
            self.tabla_mascota.setItem(fila ,3 ,dueño )
            self.tabla_mascota.setItem(fila ,4,paseador)
            fila+=1

    
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')
        
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (CLIENTE / PASEADOR)
#==============================================================================
        

dialogo_alta_baja = uic.loadUiType('interfas/alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self,string,tabla, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.persona_aux  = string
        self.text.setText('NUEVO '+ string)
        self.boton_guardar.clicked.connect(self.guardar)
        self.tabla = tabla
        if(self.persona_aux == None):
            self.linea_nombre.setText(self.persona_aux.get_nombre())
            self.linea_apellido.setText(self.persona_aux.get_apellido())
            self.linea_dni.setText(self.persona_aux.get_DNI())
            self.linea_telefono.setText(self.persona_aux.get_telefono())
            self.linea_direccion.setText(self.persona_aux.get_direccion())
        
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
            
        if (error != ''):
            self.mostra_error(error)
        else:
            if (self.persona_aux == 'CLIENTE'):
                if(lista_clientes.control_agregar(Persona(nombre,apellido,dni,telefono,direccion))):
                    add_in_tabla(self.tabla,lista_clientes)
                    self.close()
                else:
                    self.mostra_error('El Cliente con el documento' +str(dni)+ 'ya existe.')
            else:
                if(lista_paseadores.control_agregar(Persona(nombre,apellido,dni,telefono,direccion))):   
                    add_in_tabla(self.tabla,lista_paseadores)
                    self.close()
                else:
                    self.mostra_error('El Paseador con el documento' +str(dni)+ 'ya existe.')
        
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (MASCOTA)
#==============================================================================
        
        
dialogo_alta_baja_mascota= uic.loadUiType('interfas/alta_baja_mascota.ui')[0]

class Submenu_alta_baja_mascota(QtGui.QWidget, dialogo_alta_baja_mascota):
    
    def __init__ (self,tabla,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.tabla = tabla
        self.barra_peso.valueChanged.connect(self.manejo_peso)
        self.chico.show()
        self.mediano.close()
        self.grande.close()
        self.id = lista_mascotas.tamanio()
        self.paseador_auto_asignado = lista_paseadores.obtener_Random()
        self.box_paseador.addItem(self.paseador_auto_asignado.get_nombre() +' '+ self.paseador_auto_asignado.get_apellido())
        self.linea_id.setText(str (self.id))
        self.boton_guardar.clicked.connect(self.guardar)
        self.box_cliente.addItems(lista_clientes.ListaNombres())
        
        
    def manejo_peso(self):
        if (self.Peso.intValue() < 20):
            self.chico.show()
            self.mediano.close()
            self.grande.close()
        elif(self.Peso.intValue() < 50):
            self.chico.close()
            self.mediano.show()
            self.grande.close()
        else:
            self.chico.close()
            self.mediano.close()
            self.grande.show()
            
            
    def guardar(self):
        error = ''
        ID = self.id
        paseador = self.paseador_auto_asignado.get_DNI()
        dueño = lista_clientes.obtener(self.box_cliente.currentIndex()).get_DNI()
        print(dueño , '  ' , paseador)
        nombre = self.linea_nombre.text()
        if (nombre == ''):
            error += ' nombre'
        raza = self.linea_raza.text()
        if (raza == ''):
            error += ' raza'
        peso = self.Peso.intValue()
        if(error !=''):
            self.mostra_error(error)
        else:
            lista_mascotas.agregar( Mascota(nombre , raza , peso ,ID,dueño ,paseador))
            add_in_tabla_mascota(self.tabla , lista_mascotas )
            self.close()
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (PASEO)
#==============================================================================
        
dialogo_alta_baja_paseo= uic.loadUiType('interfas/alta_baja_paseo.ui')[0]

class Submenu_alta_baja_paseo(QtGui.QWidget, dialogo_alta_baja_paseo):
    
    def __init__ (self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        
#==============================================================================
#                            BLOQUE DE EJECUCION
#==============================================================================
        
app = QtGui.QApplication(sys.argv)
menu = Menu(None)
menu.show()
app.exec_()