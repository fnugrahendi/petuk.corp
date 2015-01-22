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
		self.KasBankUI.tb_KasMasuk_Tutup.clicked.connect(functools.partial(self.KasBank_Goto,"MENU"))
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
		self.clearTable(self.KasBankUI.tbl_KasMasuk)
		
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
		
	def KasBank_KasMasuk_Edit(self,row,col):
		CKODE = 1
		data = self.DatabaseFetchResult(self.dbDatabase,
										"gd_kas_masuk",
										"kodeTransaksi",
										str(self.KasBankUI.tbl_KasMasuk.item(row,CKODE).text())
										)
		self.KasBank_KasMasuk_Tambah(data[0])
	
	def KasBank_KasMasuk_Tambah(self,dataKasMasuk=False):
		fkm = self.KasBank_KasMasuk_Field.index
		fkmdetail = self.KasBank_DetailKasMasuk_Field.index
		self.KasBank_Goto("KASMASUK_TAMBAH")
		
		TABLECOLUMNS = [
							["Nomor Akun", "Nama Akun", "Nilai Detail"],
							["noAkunDetail","gd_rekening_jurnal`.`namaAkun","nilaiDetail"]
						]
		if (dataKasMasuk==False):
			self.KasBank_KasMasuk_IDedit = -1
		else:
			# --- edit mode
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText(str(dataKasMasuk[fkm("kodePenyetor")]))
			self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.setText(str(dataKasMasuk[fkm("noAkunKas")]))
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setText(str(dataKasMasuk[fkm("kodeTransaksi")]))
			self.KasBankUI.le_KasMasuk_Tambah_Form_Catatan.setText(str(dataKasMasuk[fkm("catatan")]))
			self.KasBankUI.lb_KasMasuk_Tambah_Form_Nilai.setText(str(dataKasMasuk[fkm("nilaiTotal")]))
			self.KasBankUI.dte_KasMasuk_Tambah_Form_Tanggal.setDateTime(QDateTime.fromString(str(dataKasMasuk[fkm("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
			result = self.DatabaseFetchResult(self.dbDatabase,"gd_detail_kas_masuk","kodeTransaksi",str(dataKasMasuk[fkm("kodeTransaksi")]))
			self.clearTable(self.KasBankUI.tbl_KasMasuk_Tambah)
			idies = []
			for row in range(0,len(result)):
				self.KasBankUI.tbl_KasMasuk_Tambah.insertRow(row)
				idies.append(row)
				for kolom in range(0,len(TABLECOLUMNS[1])):
					if (self.KasBankUI.tbl_KasMasuk_Tambah.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasMasuk_Tambah.setItem(row, kolom, item)
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,0).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][0])]))
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][2])]))
				namaakun = self.DatabaseFetchResult(self.dbDatabase,"gd_rekening_jurnal","noAkun",(result[row][fkmdetail(TABLECOLUMNS[1][0])])	)[0][self.DataMaster_DataRekening_Field.index("namaAkun")]
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,1).setText(str(namaakun))
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.clicked.connect(self.KasBank_KasMasuk_Tambah_Pilih_Penyetor)
		
	def KasBank_KasMasuk_Tambah_Pilih_AkunKas(self):
		
		pass
		
	def KasBank_KasMasuk_Tambah_Pilih_Penyetor(self):
		data = []
		def isi():
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText(str(data[0]))
		def batal():
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText("-")
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi,batal)
		pass
	
