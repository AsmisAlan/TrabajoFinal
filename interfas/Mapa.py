# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:50:19 2015

@author: alan
"""

from PyQt4 import QtGui, uic , QtCore
mapax = uic.loadUiType("interfas/mapa.ui")[0]
class Mapa(QtGui.QWidget,mapax):
    
    def __init__(self,direccion, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)
        self.mapa.setUrl(QtCore.QUrl( self.set_direccion(direccion)))       
        
    def set_direccion(self , direccion ):
        url = "http://maps.google.com/maps/api/staticmap?"
        center = "center="+direccion
        zoom = "&zoom = 15"
        size = "&size=791x501"
        markers = "&markers==color:blue%7Clabel:X" + direccion 
        #color = "&color = orange"
        path = "&route=" + direccion
        imgformat = "&format=png"
        maptype="&maptype=roadmap"        
        sensor = "&sensor=false"
        url = url + center + zoom + size + markers+ path + imgformat + maptype + sensor
        return url
