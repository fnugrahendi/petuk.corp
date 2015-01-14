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

class BukuBesar(object):
	
	def BukuBesar_Goto(self,st_index):
		self.st_BukuBesar.setCurrentIndex(st_index)
		return
	
	def BukuBesar_DaftarTransaksiJurnal(self):
		"""Draw info Daftar Transaksi Jurnal """
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL)
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal`")
		field = self.BukuBesar_TransaksiJurnal_Field.index
		CTANGGAL = 0
		CNOMOR_REFERENSI = 1
		CKETERANGAN = 2
		CNILAI = 3
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setRowCount(len(result))
		for row in range(0,len(result)):
			
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CTANGGAL)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setItem(row, CTANGGAL, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CNOMOR_REFERENSI)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setItem(row, CNOMOR_REFERENSI, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CKETERANGAN)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setItem(row, CKETERANGAN, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CNILAI)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setItem(row, CNILAI, item)
			
			item = self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CTANGGAL)
			item.setText(str(result[row][field("tanggal")]))
			item = self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CNOMOR_REFERENSI)
			item.setText(str(result[row][CNOMOR_REFERENSI]))
			item = self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CKETERANGAN)
			item.setText(str(result[row][CKETERANGAN]))
			item = self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(row,CNILAI)
			item.setText(str(result[row][CNILAI]))
		data = None
		def _SetActiveIndex(a,b):
			return
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			data = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+nomorreferensi+"' ;")[0] #id always field 0
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = data[0]
			
		def _EditCertainCell(a,b):
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			data = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+nomorreferensi+"' ;")[0]
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = data[0]
			self.BukuBesar_DaftarTransaksiJurnal_Tambah(data)
			return
		
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setColumnWidth(0,400)#check this miracle out!
		
		#--------------------Data Rekening tabel
		try:
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked.disconnect()
		except:
			pass
		try:
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked.disconnect()
		except:
			pass
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked.connect(_SetActiveIndex)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked.connect(_EditCertainCell)
		
	def BukuBesar_DaftarTransaksiJurnal_Tambah(self,dataTransaksiJurnal=None):
		""" masuk & kontrol Room tambah Daftar Transaksi jurnal """
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL_TAMBAH)
		field = self.BukuBesar_DetailTransaksiJurnal_Field.index
		CKODE_AKUN = 0
		CNAMA_AKUN = 1
		CDEPARTEMEN = 2
		CDEBIT = 3
		CKREDIT = 4
		
		self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("kodeTransaksi")])
		self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.setDateTime(QDateTime.fromString(str(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
		self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("catatan")])
		
		if (self.BukuBesar_DaftarTransaksiJurnal_idEDIT > -1):
			sql = "SELECT * FROM `gd_detail_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"' ;"
			result = self.DatabaseRunQuery(sql)
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setRowCount(len(result))
			for r in range(0,len(result)):
				if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CKODE_AKUN)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(r, CKODE_AKUN, item)
				if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CNAMA_AKUN)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(r, CNAMA_AKUN, item)
				if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEPARTEMEN)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(r, CDEPARTEMEN, item)
				if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEBIT)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(r, CDEBIT, item)
				if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CKREDIT)==None):
					item = QtGui.QTableWidgetItem()
					self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(r, CKREDIT, item)
					
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CKODE_AKUN).setText(str(result[r][field("noAkunJurnal")]))
				sql = "SELECT * FROM `gd_rekening_jurnal` WHERE `noAkun` LIKE '"+str(result[r][field("noAkunJurnal")])+"' ;"
				namaAkun = self.DatabaseRunQuery(sql)[0][self.DataMaster_DataRekening_Field.index("namaAkun")]
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CNAMA_AKUN).setText(str(namaAkun))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEPARTEMEN).setText(str(result[r][field("kodeDepartemen")]))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEBIT).setText(str(result[r][field("debit")]))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CKREDIT).setText(str(result[r][field("kredit")]))
		
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellClicked)
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.connect(self.BukuBesar_DaftarTransaksiJurnal_PilihRekening)
		
		
		#hitung balance
		jmlKredit = 0
		jmlDebit = 0
		#todo: cell changed signal to recount these
		for row in range(0,self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()):
			jmlKredit = jmlKredit+ float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())
			jmlDebit = jmlDebit + float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())
		self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtDebit.setText(str(jmlDebit))
		self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtKredit.setText(str(jmlKredit))
		self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setText(str(jmlDebit - jmlKredit))
		return
	
	def BukuBesar_DaftarTransaksiJurnal_PilihRekening(self,row,column):
		"pilih rekening untuk data transaksi jurnal pada baris $row"
		CNOMOR_REKENING = 0
		CNAMA_REKENING = 1
		if (column>1):
			"bukan pilih data rekening"
			return
		def UbahCell():
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNOMOR_REKENING).setText(self.DataMaster_DataRekening_RekeningTerpilih[0])
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNAMA_REKENING).setText(self.DataMaster_DataRekening_RekeningTerpilih[1])
			self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
			self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
			
			
		self.DataMaster_DataRekening_Popup_Pilih(UbahCell)
	
	

