# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 23:00:37 2015

@author: alan
"""

import sys
from PyQt4 import QtGui, uic 
from entidades.Persona import Persona
from entidades.Mascota import Mascota
from entidades.Paseo import Paseo
from control.Control_mascota import Control_mascota
from control.Control_persona import Control
from control.Control_paseo import Control_paseo
from interfas.Error_alta_baja import Error_alta_baja
import time





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
    
def CargarTabla(tabla,lista):
        fila = 0
        for aux in lista.lista:
            tabla.insertRow(fila)
            nombre = QtGui.QTableWidgetItem( aux.get_nombre() )
            apellido =QtGui.QTableWidgetItem( aux.get_apellido() )
            dni = QtGui.QTableWidgetItem( str(aux.get_DNI()) )
            tel = QtGui.QTableWidgetItem( str(aux.get_telefono() ))
            direc = QtGui.QTableWidgetItem( aux.get_direc() )
            tabla.setItem(fila ,0 , dni)
            tabla.setItem(fila ,1 , nombre )
            tabla.setItem(fila ,2, apellido)
            tabla.setItem(fila ,3 ,tel )
            tabla.setItem(fila ,4,direc )
            fila+=1
            
def CargarTablaMascota(tabla_mascota,lista):
        fila = 0
        for aux in lista.lista:
            tabla_mascota.insertRow(fila)
            nombre = QtGui.QTableWidgetItem(aux.get_nombre() )
            peso =QtGui.QTableWidgetItem( str(aux.get_peso()) )
            raza = QtGui.QTableWidgetItem( aux.get_raza() )
            dueño = QtGui.QTableWidgetItem(str( aux.get_dueño() ))
            paseador = QtGui.QTableWidgetItem( str(aux.get_paseador()) )
            tabla_mascota.setItem(fila ,0 , nombre)
            tabla_mascota.setItem(fila ,1 ,raza)
            tabla_mascota.setItem(fila ,2, peso)
            tabla_mascota.setItem(fila ,3 ,dueño )
            tabla_mascota.setItem(fila ,4,paseador)
            fila+=1
    
    
def add_in_tabla_paseo(tabla,lista):
    aux = lista.tamanio() -1
    tabla.insertRow(aux)
    paseador = QtGui.QTableWidgetItem(lista.obtener(aux).get_paseador().get_apellido_nombre() )
    horaS =QtGui.QTableWidgetItem( lista.obtener(aux).get_hora_salida() )
    ID = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_id() ) )
    tiempo = QtGui.QTableWidgetItem( str(lista.obtener(aux).get_tiempo_tentativo() ) + ' hs')
    horal = QtGui.QTableWidgetItem( lista.obtener(aux).get_hora_llegada()) 
    tabla.setItem(aux ,0 ,ID)
    tabla.setItem(aux ,1 ,paseador )
    tabla.setItem(aux ,2, horaS)
    tabla.setItem(aux ,3 ,tiempo  )
    tabla.setItem(aux ,4,horal )
    
def CargarTablaPaseo(tabla,lista):
        fila = 0
        for aux in lista.lista:
            #tabla.insertRow(fila)
            paseador = QtGui.QTableWidgetItem( aux.get_paseador().get_apellido_nombre() )
            horaS =QtGui.QTableWidgetItem( aux.get_hora_salida() )
            ID = QtGui.QTableWidgetItem( str(aux.get_id()) )
            tiempo = QtGui.QTableWidgetItem( str(aux.get_tiempo_tentativo())+ ' hs')
            horal = QtGui.QTableWidgetItem( aux.get_hora_llegada() )
            tabla.setItem(fila ,0 ,ID)
            tabla.setItem(fila ,1 , paseador )
            tabla.setItem(fila ,2, horaS)
            tabla.setItem(fila ,3 ,tiempo )
            tabla.setItem(fila ,4,horal )
            fila+=1
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
        self.menu_cliente = Menu_gestion(self.lista_clientes)
        self.menu_cliente.setVisible(True)
        
    def gestionMascota(self):
        self.menu_mascota = Menu_gestion_mascota(self.lista_clientes,self.lista_paseadores,self.lista_mascotas)
        self.menu_mascota.setVisible(True)
    
    def gestionPaseador(self):
        self.menu_paseador = Menu_gestion(self.lista_paseadores)
        self.menu_paseador.setVisible(True)
    
    def gestionPaseo(self):
        if(self.lista_paseadores.tamanio() > 0):
            self.menu_nuevo_paseo = Submenu_alta_baja_paseo(self.lista_paseos,self.lista_paseadores,self.tabla_paseos)
            self.menu_nuevo_paseo.setVisible(True)
        else:
            self.mostra_error('No hay Paseadores.')
        
    def marcarLlegada(self):
        self.lista_paseos.obtener(self.tabla_paseos.currentRow()).set_hora_llegada(time.strftime('%H : %M : %S'))
        CargarTablaPaseo(self.tabla_paseos , self.lista_paseos)
        self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
    
    def verRecorrido(self):
        print('estoy en la vista de mapas de recorridos')
        
    def activar(self):
        print(self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_hora_llegada().find('-'))
        if(self.lista_paseos.obtener(self.tabla_paseos.currentRow()).get_hora_llegada().find('-') > -1):
            self.llegada.setEnabled(True)
        else:
            self.llegada.setEnabled(False)
        self.boton_mapa.setEnabled(True)
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText( detalles)
            
        
        

        
        
        
#==============================================================================
#              MENU DE GESTION (paseadores , clientes)
#==============================================================================
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion(QtGui.QWidget,Menu_ge):

    def __init__(self,lista, parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nuevo)
         self.tabla_mascota.close()
         
         self.texto_menu = lista.get_roll() #guardo el roll que poseen los objetos de la lista.
         self.lista = lista #La variable por referencia Self.lista va a apuntar al mismo objeto que la lista.
         self.titulo_submenu.setText('GESTION ' + self.texto_menu )  
         CargarTabla(self.tabla_persona ,self.lista)

    def nuevo(self):
        #esto pide, la lista , una tabla y la persona si se quiere modificar.
        self.nuevo = Submenu_alta_baja( self.lista,self.tabla_persona ) 
        self.nuevo.setVisible(True)
    
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')
        
#==============================================================================
#                        MENU DE GESTION (mascotas )
#==============================================================================
        
        
Menu_ge = uic.loadUiType("interfas/Menu_gestion.ui")[0]

class Menu_gestion_mascota(QtGui.QWidget,Menu_ge):

    def __init__(self,lista_clientes,lista_paseadores,lista_mascotas , parent=None ):
         QtGui.QWidget.__init__(self, parent)
         self.setupUi(self)
         
         self.boton_detalles.clicked.connect(self.detalles)
         self.boton_mapa.clicked.connect(self.direccion)
         self.boton_nuevo.clicked.connect(self.nueva_mascota)
         self.tabla_persona.close()
          
         #La variable por referencia Self.lista_clientes va a apuntar al mismo objeto que la lista_clientes.
         self.lista_clientes = lista_clientes 
         #La variable por referencia Self.lista_paseadores va a apuntar al mismo objeto que la lista_paseadores.
         self.lista_paseadores = lista_paseadores
         #La variable por referencia Self.lista_mascotas va a apuntar al mismo objeto que la lista_mascotas.
         self.lista_mascotas = lista_mascotas
         self.titulo_submenu.setText('GESTION MASCOTAS' )
         CargarTablaMascota(self.tabla_mascota ,self.lista_mascotas)
             
    

    def nueva_mascota(self):
        #debe haber por lo menos un paseador y un cliente para asignar la mascota.
        if(self.lista_clientes.tamanio() > 0) and (self.lista_paseadores.tamanio() >0):
            self.nueva_mascota = Submenu_alta_baja_mascota(self.lista_mascotas,self.lista_clientes,self.lista_paseadores.obtener_Random(),self.tabla_mascota)
            self.nueva_mascota.setVisible(True)
        else:
            self.error = Error_alta_baja()
            self.error.setVisible(True)
            self.error.mensaje_error.setText('Debes tener al menos 1 cliente/paseador.')
            self.error.titulo.setText('Error')

    
    def detalles(self):
        print('detalles')
    
    def direccion(self):
        print('mapa')
        
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (CLIENTE / PASEADOR)
#==============================================================================
        

dialogo_alta_baja = uic.loadUiType('interfas/alta_baja.ui')[0]

class Submenu_alta_baja(QtGui.QWidget, dialogo_alta_baja):
    
    def __init__ (self,lista,tabla,persona = None, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar)
        
        self.lista  = lista
        self.tabla = tabla
        if(persona != None):
            self.linea_nombre.setText(persona.get_nombre())
            self.linea_apellido.setText(persona.get_apellido())
            self.linea_dni.setText(persona.get_DNI())
            self.linea_telefono.setText(persona.get_telefono())
            self.linea_direccion.setText(persona.get_direccion())
            self.text.setText('MODIFICAR '+ lista.get_roll())
        else:
            self.text.setText('NUEVO '+ lista.get_roll() )
            
        
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
            if(self.lista.control_agregar(Persona(nombre,apellido,dni,telefono,direccion))):
                add_in_tabla(self.tabla,self.lista)
                self.close()
            else:
                self.mostra_error('El '+self.lista.get_roll()+' con el documento' +str(dni)+ ' ya existe.')

        
        
    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
#==============================================================================
#                          NUEVO - MODIFICAR (MASCOTA)
#==============================================================================
        
        
dialogo_alta_baja_mascota= uic.loadUiType('interfas/alta_baja_mascota.ui')[0]

class Submenu_alta_baja_mascota(QtGui.QWidget, dialogo_alta_baja_mascota):
    
    def __init__ (self,lista_mascotas,lista_clientes,paseador,tabla,mascota = None,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.barra_peso.valueChanged.connect(self.manejo_peso)
        self.boton_guardar.clicked.connect(self.guardar)
        
        self.lista_mascotas = lista_mascotas
        self.lista_clientes = lista_clientes
        self.chico.show()
        self.mediano.close()
        self.grande.close() 
        self.box_cliente.addItems(self.lista_clientes.ListaNombres())
        self.tabla = tabla
        if(mascota != None):
            self.linea_raza.setText(mascota.get_raza())
            self.barra_peso.setValue(mascota.get_peso())
            self.id = mascota.get_ID()
            self.linea_id.setText(str (self.id))
            self.manejo_peso()
            self.linea_nombre().setText(mascota.get_nombre())
            self.box_paseador.addItem(str(mascota.get_paseador() ))
            self.paseador_asignado=mascota.get_paseador() 
        else:
            self.id = lista_mascotas.tamanio()
            self.linea_id.setText(str (self.id))
            self.paseador_asignado = paseador.get_DNI()
            self.box_paseador.addItem(paseador.get_apellido_nombre())
            
        
        
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
        paseador = self.paseador_asignado
        dueño = self.lista_clientes.obtener(self.box_cliente.currentIndex()).get_DNI()
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
            self.lista_mascotas.agregar( Mascota(nombre , raza , peso ,ID,dueño ,paseador))
            add_in_tabla_mascota(self.tabla , self.lista_mascotas )
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
    
    def __init__ (self,lista_paseos ,lista_paseadores , tabla ,parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.boton_guardar.clicked.connect(self.guardar)
        self.tabla = tabla
        self.lista_paseos = lista_paseos
        self.lista_paseadores = lista_paseadores
        self.paseo.setText(str(lista_paseos.tamanio() ))
        self.box_paseador.addItems(lista_paseadores.ListaNombres())
        
        
    def guardar(self):
        error = ''
        ID = self.lista_paseos.tamanio()
        paseador = self.lista_paseadores.obtener(self.box_paseador.currentIndex())
        try:
            tiempo_estimado = int(self.tiempo_estimado.text())
        except(ValueError):
            error = 'EL TIEMPO ESTIMADO SOLO PUEDE SER UN VALOR NUMERICO.'
        tiempo_salida = time.strftime('%H : %M : %S')
        tiempo_llegada = '----------'
        if(error == ''):
            self.lista_paseos.agregar(Paseo(tiempo_salida,tiempo_llegada, tiempo_estimado,ID,paseador))
            add_in_tabla_paseo(self.tabla,self.lista_paseos)
            self.close()
        else:
            self.mostra_error(error)

    def mostra_error(self,detalles):
        self.error = Error_alta_baja()
        self.error.setVisible(True)
        self.error.mensaje_error.setText('Error en el campo: ' + detalles)
        
        
        
#==============================================================================
#                            BLOQUE DE EJECUCION
#==============================================================================
        
app = QtGui.QApplication(sys.argv)
menu = Menu(None)
menu.show()
app.exec_()