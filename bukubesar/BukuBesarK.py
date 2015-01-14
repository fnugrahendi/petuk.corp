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

class BukuBesar(object):
	
	def BukuBesar_Goto(self,st_index):
		self.st_BukuBesar.setCurrentIndex(st_index)
		return
	
	def BukuBesar_DaftarTransaksiJurnal(self):
		"""Draw info Daftar Transaksi Jurnal """
		#set index
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL)
		field = self.BukuBesar_TransaksiJurnal_Field.index
		CTANGGAL = 0
		CNOMOR_REFERENSI = 1
		CKETERANGAN = 2
		CNILAI = 3
		
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal`")
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
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked)
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked)
		#----sinyal
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked.connect(_SetActiveIndex)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked.connect(_EditCertainCell)
		#----sinyal tombol
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah.clicked.connect(self.BukuBesar_DaftarTransaksiJurnal_Tambah)
		
	def BukuBesar_DaftarTransaksiJurnal_Tambah(self,dataTransaksiJurnal=None):
		""" masuk & kontrol Room tambah Daftar Transaksi jurnal """
		#set index
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL_TAMBAH)
		#set fungsi
		field = self.BukuBesar_DetailTransaksiJurnal_Field.index
		CKODE_AKUN = 0
		CNAMA_AKUN = 1
		CDEPARTEMEN = 2
		CDEBIT = 3
		CKREDIT = 4
		
		
		
		idies = []
		if (self.BukuBesar_DaftarTransaksiJurnal_idEDIT > -1):
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("kodeTransaksi")])
			self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.setDateTime(QDateTime.fromString(str(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("catatan")])
			
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
				idies.append(result[r][0])
		else:
			#tambah baru: set text top ke defaultaja
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText("")
			#Generate code setelahnya
			self.BukuBesar_DaftarTransaksiJurnal_Tambah_GenerateKode()
			tanggal = datetime.now()
			self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.setDateTime(QDateTime.fromString(tanggal.strftime("%Y-%m-%d %H:%M:%S"),"yyyy-MM-dd hh:mm:ss"))
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.setText("")
			
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellClicked)
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.connect(self.BukuBesar_DaftarTransaksiJurnal_PilihRekening)
		
		
		#todo: cell changed signal to recount these
		def hitungulang():
			#hitung balance
			jmlKredit = 0
			jmlDebit = 0
			if self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()>0:
				for row in range(0,self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()):
					jmlKredit = jmlKredit+ float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())
					jmlDebit = jmlDebit + float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtDebit.setText(str(jmlDebit))
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtKredit.setText(str(jmlKredit))
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setText(str(jmlDebit - jmlKredit))
			if (jmlDebit!=jmlKredit):
				self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setStyleSheet("QLabel{color:red;}")
			else:
				self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setStyleSheet("")
		#~ if (self.BukuBesar_DaftarTransaksiJurnal_idEDIT > -1):
		hitungulang()
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellChanged.connect(hitungulang)
		
		#----Tombol-tombol di room ini
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Batal.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Batal.clicked.connect(self.BukuBesar_DaftarTransaksiJurnal)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Simpan.clicked)
		if len(idies)==0:
			idies = False
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Simpan.clicked.connect(functools.partial(self.BukuBesar_DaftarTransaksiJurnal_Tambah_Act_Simpan,idies))
		return
	
	def BukuBesar_DaftarTransaksiJurnal_Tambah_Act_Simpan(self,idies=False):
		CKODE_AKUN = 0
		CNAMA_AKUN = 1
		CDEPARTEMEN = 2
		CDEBIT = 3
		CKREDIT = 4
		if idies==False:
			#Tambah baru
			pass
		else:
			#edit (simpen replace)
			row = 0
			for tablerow in idies:
				sql = """UPDATE `"""+self.dbDatabase+"""`.`gd_detail_transaksi_jurnal` 
						SET `kodeTransaksi` = '"""+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"""',
							`noAkunJurnal` 	= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKODE_AKUN).text())+"""',
							`kodeDepartemen`= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEPARTEMEN).text())+"""',
							`debit`			= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())+"""',
							`kredit`		= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())+"""',
							`tanggal`		= '"""+str(self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))+"""'
							
						WHERE `gd_detail_transaksi_jurnal`.`id` ="""+str(tablerow)+""";
				"""
				self.DatabaseRunQuery(sql)
				row+=1
		sql = """UPDATE `"""+self.dbDatabase+"""`.`gd_transaksi_jurnal` 
				SET `nilaiTransaksi` = '"""+str(self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtDebit.text())+"""'
				WHERE `gd_transaksi_jurnal`.`kodeTransaksi` = '"""+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"""';
		"""
		self.DatabaseRunQuery(sql)
		self.BukuBesar_DaftarTransaksiJurnal()
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
	
	def BukuBesar_DaftarTransaksiJurnal_Tambah_GenerateKode(self):
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_transaksi_jurnal` ORDER BY `gd_transaksi_jurnal`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<8):
			kode_default = "0"+kode_default
		kode_default = "GJ" + "."+kode_default
		self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(kode_default)

