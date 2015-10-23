# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 14:50:19 2015

@author: alan
"""

url = u""

data = urllib.request.urlopen(url).read()

image = QtGui.Qimage()
image.loadFromData(data)

label.setPixmap(qtgui.Qpixmap(image))