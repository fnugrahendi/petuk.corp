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

from DaftarTransaksiJurnal import DaftarTransaksiJurnal

class BukuBesar(DaftarTransaksiJurnal):
	def BukuBesar_init(self):
		
		#---------------------------------------------------------------Buku Besar init 
		#init konstanta index
		self.INDEX_ST_BUKUBESAR_MENU = 0
		self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL = 1
		self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL_TAMBAH = 2
		
		self.BukuBesar_DaftarTransaksiJurnal_idEDIT = -1
		self.tb_BukuBesar_DaftarTransaksiJurnal.clicked.connect(functools.partial(self.BukuBesar_DaftarTransaksiJurnal))
		self.st_BukuBesar.setCurrentIndex(0)
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_transaksi_jurnal';")
		self.BukuBesar_TransaksiJurnal_Field = list(itertools.chain.from_iterable(result))
		
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_detail_transaksi_jurnal';")
		self.BukuBesar_DetailTransaksiJurnal_Field = list(itertools.chain.from_iterable(result))
		
	def BukuBesar_Goto(self,st_index):
		self.st_BukuBesar.setCurrentIndex(st_index)
		return
	def BukuBesar_Menu(self):
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_MENU)
