import MySQLdb
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSvg
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sip 
import sys,os
import functools
import itertools
import re
from datetime import datetime

from L_BukuBesar_DTJ import L_BukuBesar_DTJ
from html import HTML

class Laporan(L_BukuBesar_DTJ):
	def __init__(self):
		pass #-- doesn't triggered
		
	def Laporan_Init(self):
		super(L_BukuBesar_DTJ,self).__init__(parent)
		
		return
	
	
