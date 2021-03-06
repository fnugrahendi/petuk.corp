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

class DaftarTransaksiJurnal(object):
	def __init__(self,parent=None):
		pass
	def BukuBesar_DaftarTransaksiJurnal(self):
		"""Draw info Daftar Transaksi Jurnal """
		#set index
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL)
		field = self.BukuBesar_TransaksiJurnal_Field.index
		CTANGGAL = 0
		CNOMOR_REFERENSI = 1
		CKETERANGAN = 2
		CNILAI = 3
		
		#at first we clear the rows
		for r in range(0,self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.rowCount()+1):
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.removeRow(r)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setRowCount(0)
		
		result = self.DatabaseFetchResult(self.dbDatabase, "gd_transaksi_jurnal")
		for row in range(0,len(result)):
			
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.insertRow(row)
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
		self.BukuBesar_DaftarTransaksiJurnal_RowColumnTerpilih = [-1,-1]
		
		def _SetActiveIndex(a,b):
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			data = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+nomorreferensi+"' ;")[0] #id always field 0
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = data[0]
			self.BukuBesar_DaftarTransaksiJurnal_RowColumnTerpilih = [a,b]
			
		def _EditCertainCell(a,b):
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			data = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+nomorreferensi+"' ;")[0]
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = data[0]
			self.BukuBesar_DaftarTransaksiJurnal_Tambah(data)
			return
		def _OpenCertainCell():
			a = self.BukuBesar_DaftarTransaksiJurnal_RowColumnTerpilih[0]
			if (a<0):
				return
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			data = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+nomorreferensi+"' ;")[0]
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = data[0]
			self.BukuBesar_DaftarTransaksiJurnal_Tambah(data)
			
		def _DeleteCertainCell():
			a = self.BukuBesar_DaftarTransaksiJurnal_RowColumnTerpilih[0]
			if (a<0):
				return
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			sql = "DELETE FROM `gd_transaksi_jurnal` WHERE `gd_transaksi_jurnal`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			sql = "DELETE FROM `gd_detail_transaksi_jurnal` WHERE `gd_detail_transaksi_jurnal`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.removeRow(a)
			
		def _ConfirmDeleteCertainCell():
			a = self.BukuBesar_DaftarTransaksiJurnal_RowColumnTerpilih[0]
			if (a<0):
				return
			nomorreferensi = str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.item(a,CNOMOR_REFERENSI).text())
			self.DataMaster_Popup("Anda yakin akan menghapus data "+nomorreferensi+"?",_DeleteCertainCell)
			
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setColumnWidth(2,300)#check this miracle out!
		
		#--------------------Data Rekening tabel
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked)
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked)
		#----sinyal
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellClicked.connect(_SetActiveIndex)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.cellDoubleClicked.connect(_EditCertainCell)
		#----sinyal tombol
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah.clicked.connect(self.BukuBesar_DaftarTransaksiJurnal_Tambah)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Buka.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Buka.clicked.connect(_OpenCertainCell)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Delete.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Delete.clicked.connect(_ConfirmDeleteCertainCell)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tutup.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tutup.clicked.connect(self.BukuBesar_Menu)
		
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Cetak.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Cetak.clicked.connect(functools.partial(self.BukuBesar_DaftarTransaksiJurnal_Cetak,"2015-01-01 00:00:00","2015-02-01 00:00:00"))
		#-----search bar
		self.GarvinDisconnect(self.le_BukuBesar_Search.textEdited)
		self.le_BukuBesar_Search.textEdited.connect(self.BukuBesar_DaftarTransaksiJurnal_RedrawInfo)
		
	def BukuBesar_DaftarTransaksiJurnal_Tambah(self,dataTransaksiJurnal=False):
		""" masuk & kontrol Room tambah Daftar Transaksi jurnal """
		#-----set index
		self.st_BukuBesar.setCurrentIndex(self.INDEX_ST_BUKUBESAR_DAFTARTRANSAKSIJURNAL_TAMBAH)
		#-----set fungsi
		field = self.BukuBesar_DetailTransaksiJurnal_Field.index
		CKODE_AKUN = 0
		CNAMA_AKUN = 1
		CDEPARTEMEN = 2
		CDEBIT = 3
		CKREDIT = 4
		if dataTransaksiJurnal==False:
			self.BukuBesar_DaftarTransaksiJurnal_idEDIT = -1
		
		def hitungulang():
			"kepicu ketika cell diubah"
			#hitung balance
			jmlKredit = 0
			jmlDebit = 0
			if self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()>0:
				for row in range(0,self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()):
					#----check kalau diisi selain angka
					nilaiKredit = 0.0
					nilaiDebit = 0.0
					try:
						nilaiKredit = float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())
					except ValueError:
					#------ambil bilangan disitu dgn regex bila sukses, bila tidak beri nilai 0
						try:
							t = self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text()
							self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).setText(str(re.search('\d+', t).group()))
						except AttributeError:
							self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).setText("0")
						except:pass
						nilaiKredit = float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())
					except:
						pass
					jmlKredit = jmlKredit + nilaiKredit
					try:
						nilaiDebit =  float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())
					except ValueError:
						try:
							t = self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text()
							self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).setText(str(re.search('\d+', t).group()))
						except AttributeError:
							self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).setText("0")
						except:pass
						nilaiDebit =  float(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())
					except:
						pass
					jmlDebit = jmlDebit+nilaiDebit
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtDebit.setText(str(jmlDebit))
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtKredit.setText(str(jmlKredit))
			self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setText(str(jmlDebit - jmlKredit))
			if (jmlDebit!=jmlKredit):
				self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setStyleSheet("QLabel{color:red;}")
			else:
				self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VBalance.setStyleSheet("")
		
		def tambahbaris():
			newrow = self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.insertRow(newrow)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow,CKODE_AKUN)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(newrow, CKODE_AKUN, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow,CNAMA_AKUN)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(newrow, CNAMA_AKUN, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow,CDEPARTEMEN)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(newrow, CDEPARTEMEN, item)
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow, CDEPARTEMEN).setText("0")
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow,CDEBIT)==None):
				item = QtGui.QTableWidgetItem()
				item.setText("0")
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(newrow, CDEBIT, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(newrow,CKREDIT)==None):
				item = QtGui.QTableWidgetItem()
				item.setText("0")
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(newrow, CKREDIT, item)
		
		#at first we clear the rows
		self.clearTable(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List)
		
		#-- transaksi jurnal kode cek hanya untuk baru
		self.GarvinDisconnect(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.textChanged)
		
		idies = []
		if (self.BukuBesar_DaftarTransaksiJurnal_idEDIT > -1):
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("kodeTransaksi")])
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setReadOnly(True)
			self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.setDateTime(QDateTime.fromString(str(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.setText(dataTransaksiJurnal[self.BukuBesar_TransaksiJurnal_Field.index("catatan")])
			
			sql = "SELECT * FROM `gd_detail_transaksi_jurnal` WHERE `kodeTransaksi` LIKE '"+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"' ;"
			result = self.DatabaseRunQuery(sql)
			for r in range(0,len(result)):
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.insertRow(r)
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
				try:
					namaAkun = self.DatabaseRunQuery(sql)[0][self.DataMaster_DataRekening_Field.index("namaAkun")]
				except:
					namaAkun = ""
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CNAMA_AKUN).setText(str(namaAkun))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEPARTEMEN).setText(str(result[r][field("kodeDepartemen")]))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CDEBIT).setText(str(result[r][field("debit")]))
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,CKREDIT).setText(str(result[r][field("kredit")]))
				idies.append(result[r][0])
		else:
			#tambah baru
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setReadOnly(False)
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText("")
			#Generate code Untuk tambah baru
			self.BukuBesar_DaftarTransaksiJurnal_Tambah_GenerateKode()
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.textChanged.connect(self.BukuBesar_DaftarTransaksiJurnal_Tambah_KodeCek)
			tanggal = datetime.now()
			self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.setDateTime(QDateTime.fromString(tanggal.strftime("%Y-%m-%d %H:%M:%S"),"yyyy-MM-dd hh:mm:ss"))
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.setText("")
			tambahbaris()
		
		#-----------hapus baris
		#----Hapus baris hanya terjadi bila sudah di Act_Simpan, sql query diantrikan
		sqltorun = []
		def _SetActiveIndex(a,b):
			self.BukuBesar_DaftarTransaksiJurnal_Tambah_RowColumnTerpilih = [a,b]
		
		def _DeleteCertainCell():
			a = self.BukuBesar_DaftarTransaksiJurnal_Tambah_RowColumnTerpilih[0]
			if (a<0):
				return
			#----- a<len(idies) secure wether the data is already on database or not, if it hasn't then it just do plain delete from table, else it will delete it from database
			if (a<len(idies)):
				sqltorun.append( "DELETE FROM `gd_detail_transaksi_jurnal` WHERE `gd_detail_transaksi_jurnal`.`id` = "+str(idies[a])+" ;")
				idies.pop(a)
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.removeRow(a)
			hitungulang()
			
		def _ConfirmDeleteCertainCell():
			a = self.BukuBesar_DaftarTransaksiJurnal_Tambah_RowColumnTerpilih[0]
			if (a<0):
				return
			self.DataMaster_Popup("Anda yakin akan menghapus data baris "+str(a+1)+"?",_DeleteCertainCell)
			
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellClicked)
		self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellClicked.connect(_SetActiveIndex)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.connect(self.BukuBesar_DaftarTransaksiJurnal_PilihRekening)
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.connect(self.BukuBesar_DaftarTransaksiJurnal_PilihDepartemen)
		
		
		
		hitungulang()
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellChanged.connect(hitungulang)
		
		#----Tombol-tombol di room ini
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Batal.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Batal.clicked.connect(self.BukuBesar_DaftarTransaksiJurnal)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_TambahBaris.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_TambahBaris.clicked.connect(tambahbaris)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Delete.clicked)
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Delete.clicked.connect(_ConfirmDeleteCertainCell)
		self.GarvinDisconnect(self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Simpan.clicked)
		#-----kalau len idies 0, langsung masuk ke for tambahan baru: tanpa masalah
		self.tb_BukuBesar_DaftarTransaksiJurnal_Tambah_Simpan.clicked.connect(functools.partial(self.BukuBesar_DaftarTransaksiJurnal_Tambah_Act_Simpan,idies,sqltorun))
		return
	
	#-------------------------------------------------------------------- TAMBAH ACT SIMPAN
	def BukuBesar_DaftarTransaksiJurnal_Tambah_Act_Simpan(self,idies=None,sqltorun=None):
		if idies==None: #-- avoid call by reference default value, as it will just append more 
			idies = []
		if sqltorun==None:
			sqltorun = []
		CKODE_AKUN = 0
		CNAMA_AKUN = 1
		CDEPARTEMEN = 2
		CDEBIT = 3
		CKREDIT = 4
		#edit (simpen replace)
		#update dan tambah detail transaksi jurnal
		row = 0
		for tablerowid in idies:
			sql = """UPDATE `"""+self.dbDatabase+"""`.`gd_detail_transaksi_jurnal` 
					SET `kodeTransaksi` = '"""+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"""',
						`noAkunJurnal` 	= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKODE_AKUN).text())+"""',
						`kodeDepartemen`= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEPARTEMEN).text())+"""',
						`debit`			= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())+"""',
						`kredit`		= '"""+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())+"""',
						`tanggal`		= '"""+str(self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))+"""'
						
					WHERE `gd_detail_transaksi_jurnal`.`id` ="""+str(tablerowid)+""";
			"""
			self.DatabaseRunQuery(sql)
			row+=1
		if self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()>len(idies):
			#"ada tambahan baru"
			for row in range(len(idies),self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.rowCount()):
				sql = """INSERT INTO `"""+self.dbDatabase+"""`.`gd_detail_transaksi_jurnal` (
						`id` ,
						`kodeTransaksi` ,
						`noAkunJurnal` ,
						`kodeDepartemen` ,
						`debit` ,
						`kredit` ,
						`tanggal`
					)
					VALUES (
						NULL ,"""+\
						"'"+str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())+"',"+\
						"'"+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKODE_AKUN).text())+"',"+\
						"'"+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEPARTEMEN).text())+"',"+\
						"'"+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CDEBIT).text())+"',"+\
						"'"+str(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CKREDIT).text())+"',"+\
						"'"+str(self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))+"' );"
				self.DatabaseRunQuery(sql)
				
		self.DatabaseInsertReplace(self.dbDatabase,
									"gd_transaksi_jurnal",
									"kodeTransaksi",
									str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text()),
									["kodeTransaksi","catatan","nilaiTransaksi","tanggal"],
									[
										str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text()),	
										str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_Keterangan.text()),
										str(self.lb_BukuBesar_DaftarTransaksiJurnal_Tambah_Fsum_VtDebit.text()),
										str(self.dte_BukuBesar_DaftarTransaksiJurnal_Tambah_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
									]
								)
		#---------at last, we execute sqltorun queries
		for sql in sqltorun:
			self.DatabaseRunQuery(sql)
		self.BukuBesar_DaftarTransaksiJurnal()
		return
		
	def BukuBesar_DaftarTransaksiJurnal_PilihDepartemen(self,row,column):
		self.BukuBesar_DaftarTransaksiJurnal_Tambah_RowColumnTerpilih = [row,column]
		
		if column!=2:
			return
		ok = ["-"]
		def ubah():
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,column).setText(str(ok[0]))
		self.DataMaster_DataDepartemen_Popup_Pilih(ok,ubah)
	
	def BukuBesar_DaftarTransaksiJurnal_PilihRekening(self,row,column):
		"pilih rekening untuk data transaksi jurnal pada baris $row"
		CNOMOR_REKENING = 0
		CNAMA_REKENING = 1
		data = ["",""]
		if (column>1):
			"bukan pilih data rekening"
			return
		def UbahCell():
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNOMOR_REKENING)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(row, CNOMOR_REKENING, item)
			if (self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNAMA_REKENING)==None):
				item = QtGui.QTableWidgetItem()
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.setItem(row, CNAMA_REKENING, item)
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNOMOR_REKENING).setText(str(data[0]))
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(row,CNAMA_REKENING).setText(str(data[1]))
			self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
			self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
		self.DataMaster_DataRekening_Popup_Pilih(data,UbahCell)
	
	#~ def BukuBesar_DaftarTransaksiJurnal_Tambah_GenerateKode(self):
		#~ sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_transaksi_jurnal` ORDER BY `gd_transaksi_jurnal`.`id` DESC LIMIT 0 , 1"
		#~ result = self.DatabaseRunQuery(sql)
		#~ kode_default = str(int(result[0][0])+1)
		#~ while (len(kode_default)<8):
			#~ kode_default = "0"+kode_default
		#~ kode_default = "GJ" +kode_default
		#~ self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(kode_default)

	def BukuBesar_DaftarTransaksiJurnal_Tambah_GenerateKode(self):
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_transaksi_jurnal` ORDER BY `gd_transaksi_jurnal`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "GJ" + kode_default
		self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(kode_default)
	
	def BukuBesar_DaftarTransaksiJurnal_Tambah_KodeCek(self,stuf=None):
		kodebaru = ""
		kodeterlarang = str(self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.text())
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_transaksi_jurnal","kodeTransaksi",kodeterlarang	)
		if (len(result)>0):
			self.statusbar.showMessage("Kode "+kodeterlarang+" sudah terpakai, diberikan kode lain",10000)
			while len(result)>0:
				nilai = int(re.findall("\d+",kodeterlarang)[0])
				nilai+=1
				kodebaru = str(nilai)
				while (len(kodebaru)<8):
					kodebaru = "0"+kodebaru
				kodebaru = "GJ"+kodebaru
				kodeterlarang = kodebaru
				result = self.DatabaseFetchResult(self.dbDatabase,"gd_transaksi_jurnal","kodeTransaksi",kodeterlarang	)
			self.le_BukuBesar_DaftarTransaksiJurnal_Tambah_NomorReferensi.setText(kodebaru)
			
		
	def BukuBesar_DaftarTransaksiJurnal_RedrawInfo(self,searchtext):
		searchtext = str(searchtext)
		field = self.BukuBesar_TransaksiJurnal_Field.index
		CTANGGAL = 0
		CNOMOR_REFERENSI = 1
		CKETERANGAN = 2
		CNILAI = 3
		
		def DrawIfExist(hasil):
			for row in range(0,len(result)):
				try:
					idtertampil.index(result[row][0])
					#---sudah ada id tersebut di list
					continue
				except ValueError:
					idtertampil.append(result[row][0])
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.insertRow(row)
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
		#at first we clear the rows
		for r in range(0,self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.rowCount()+1):
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.removeRow(r)
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Fcontent_List.setRowCount(0)
		
		idtertampil = []
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `gd_transaksi_jurnal`.`kodeTransaksi` LIKE '%"+searchtext+"%'")
		DrawIfExist(result)
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `gd_transaksi_jurnal`.`catatan` LIKE '%"+searchtext+"%'")
		DrawIfExist(result)
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `gd_transaksi_jurnal`.`tanggal` LIKE '%"+searchtext+"%'")
		DrawIfExist(result)
		
	def BukuBesar_DaftarTransaksiJurnal_Cetak(self,start="2015-01-01 00:00:00",end="2015-02-20 23:59:59"):
		data = [[],[]]
		result = self.DatabaseRunQuery("SELECT * FROM `gd_transaksi_jurnal` WHERE `tanggal` >= '"+str(start)+"' AND `tanggal` <= '"+str(end)+"'")
		for x in range(0,len(result)):
			data[0].append(result[x])
			detail = self.DatabaseFetchResult(self.dbDatabase,"gd_detail_transaksi_jurnal","kodeTransaksi",result[x][self.BukuBesar_TransaksiJurnal_Field.index("kodeTransaksi")])
			data[1].append(detail)
		
		self.L_BukuBesar_DTJ_Create("General Journal List",data)
		
