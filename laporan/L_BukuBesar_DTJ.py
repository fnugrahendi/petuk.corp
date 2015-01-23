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

from html import HTML

class L_BukuBesar_DTJ(object):
	def __init__(self, parent=None):
		pass
		
		
	def L_BukuBesar_DTJ_init(self):
		pass
	
	def L_BukuBesar_DTJ_Create(nama,data):
		fjurnal = self.BukuBesar_TransaksiJurnal_Field.index
		fdetail = self.BukuBesar_DetailTransaksiJurnal_Field.index
		
