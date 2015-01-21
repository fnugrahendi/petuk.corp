import MySQLdb
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4 import QtSvg
from PyQt4.QtCore import * #nganggo QDateTime, ra apal e package ngarepe opo QtCore.QDateTime rung nyobo
from PyQt4.QtGui import *
import sip #lali nggo ngopo
import sys,os
import functools #partial
import itertools #ubah tuple ke array
import re #regular expression
from datetime import datetime #tanggal, a= datetime.now(); cobo dicheck dir(a); a.year,

class KasMasuk(object):
	def __init__(self,parent=None):
		pass
			
	def KasBank_KasMasuk(self):
		self.st_kasbank.setCurrentIndex(self.INDEX_ST_KASBANK_KASMASUK)
		
		CTANGGAL = 0
		CKODE = 1
		CPENYETOR = 2
		CKETERANGAN = 3
		CNILAI = 4
		
		
		#at first we clear the rows
		for r in range(0,self.st_kasbank.tbl_KasMasuk.rowCount()+1):
			self.st_kasbank.tbl_KasMasuk.removeRow(r)
		self.st_kasbank.tbl_KasMasuk.setRowCount(0)
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_masuk")

