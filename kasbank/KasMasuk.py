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
		self.tb_KasMasuk_Tutup.clicked.connect()
		pass
	
	
	def KasBank_KasMasuk(self):
		""" The room control itself """
		self.KasBank_Goto("KASMASUK")
		
		self.KasBank_KasMasuk_RefreshList()
		
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk.cellClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk.cellDoubleClicked)
		self.KasBankUI.tbl_KasMasuk.cellClicked.connect(self.KasBank_KasMasuk_SetActiveIndex)
		self.KasBankUI.tbl_KasMasuk.cellDoubleClicked.connect(self.KasBank_KasMasuk_Edit)


	def KasBank_KasMasuk_RefreshList(self,searchtext=""):
		""" Refresh list of the table """
		field = self.KasBank_KasMasuk_Field.index
		
		CTANGGAL = 0
		CKODE = 1
		CPENYETOR = 2
		CKETERANGAN = 3
		CNILAI = 4
		
		TABLECOLUMNS = [
						["Tanggal", "Kode Referensi", "Penyetor", "Keterangan", "Nilai"],
						["tanggal", "kodeTransaksi", "kodePenyetor","catatan","nilaiTotal"]
						]
		
		#at first we clear the rows
		for r in range(0,self.KasBankUI.tbl_KasMasuk.rowCount()+1):
			self.KasBankUI.tbl_KasMasuk.removeRow(r)
		self.KasBankUI.tbl_KasMasuk.setRowCount(0)
		
		#--- record if such row has displayed
		idies = []
		#--- auto search for all of displayed column based on fieldlist on TABLECOLUMNS[1]
		for x in range(0,len(TABLECOLUMNS[1])):
			result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_masuk",TABLECOLUMNS[1][x],"%"+str(searchtext)+"%")
			for row in range(0,len(result)):
				if (row in idies):
					continue
				self.KasBankUI.tbl_KasMasuk.insertRow(row)
				idies.append(row)
				for kolom in range(0,len(TABLECOLUMNS[1])):
					if (self.KasBankUI.tbl_KasMasuk.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasMasuk.setItem(row, kolom, item)
					self.KasBankUI.tbl_KasMasuk.item(row,kolom).setText(str(result[row][	field(TABLECOLUMNS[1][kolom])	]))
	
	def KasBank_KasMasuk_SetActiveIndex(self,row,col):
		""" This function reconnect the signal of button Buka """
		self.KasBankUI.tb_KasMasuk_Buka.clicked.connect(functools.partial(self.KasBank_KasMasuk_Edit,row,col))
		#~ print "active "+str(row)+","+str(col)
		
		#-- this function
	def KasBank_KasMasuk_Edit(self,row,col):
		print "jalankan edit untuk "
		print row,col
