#!/usr/bin/env python
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
from GUI import Ui_MainWindow
#----Buku Besar
from bukubesar import BukuBesar
from datamaster import DataMaster

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s


class MainGUI(QtGui.QMainWindow, Ui_MainWindow,BukuBesar,DataMaster):
	def __init__(self, parent= None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.st_Penjualan.setCurrentIndex(0)
		
		def ___metu():
			exit(0)
			return True
		self.tb_Penjualan_Keluar.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan keluar dari aplikasi?",___metu))
        
        
        
		self.dbHost = "127.0.0.1"
		self.dbPort = 44559
		self.dbDatabase = "gd_db_akunting"
		self.dbPass = "nyungsep"
		self.dbUser = "gd_user_akunting"
        #---------------------------------------------------------------Penjualan Init Itut
		#Tombol pada Halaman Menu
		self.tb_Penjualan_PenawaranHarga.clicked.connect(self.Penjualan_GoTo_PenawaranHarga)
		self.tb_Penjualan_OrderPenjualan.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_Pengiriman.clicked.connect(self.Penjualan_GoTo_Pengiriman)
		self.tb_Penjualan_Piutang.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		self.tb_Penjualan_PembayaranPiutang.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		self.tb_Penjualan_Retur.clicked.connect(self.Penjualan_GoTo_ReturPenjualan)
		
		#Tombol pada Halaman PenawaranHarga
		self.tb_PenawaranHarga_tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_PenawaranHarga_baru.clicked.connect(self.Penjualan_GoTo_PenawaranHarga_baru)
		
		self.tb_Penjualan_PenawaranHarga_baru_rekam.clicked.connect(self.Penjualan_PenawaranHarga_Baru_Rekam)
		self.tb_Penjualan_PenawaranHarga_baru_tutup.clicked.connect(self.Penjualan_GoTo_PenawaranHarga)
		
		#Tombol pada Halaman OrderPenjualan
		self.tb_Penjualan_OrderPenjualan_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_OrderPenjualan_Baru.clicked.connect(self.Penjualan_GoTo_OP_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Batal.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Simpan.clicked.connect(self.Penjualan_OrderPenjualan_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_HapusBaris.clicked.connect(functools.partial(self.HapusBaris,self.tbl_Penjualan_OrderPenjualan))
		
		#Tombol pada Halaman Pengiriman
		self.tb_Penjualan_Pengiriman_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_Pengiriman_Baru.clicked.connect(self.Penjualan_GoTo_Pengiriman_Baru)
		self.tb_Penjualan_PengirimanBaru_Tutup.clicked.connect(self.Penjualan_GoTo_Pengiriman)
		
		#Tombol pada Halaman Piutang
		self.tb_Penjualan_Piutang_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_RincianPiutang_Tutup.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		
		#Tombol pada Halaman Pembayaran Piutang
		self.tb_Penjualan_PembayaranPiutang_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_PembayaranPiutang_Baru.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang_Baru)
		self.tb_Penjualan_PembayaranPiutang_Baru_Batal.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		
		self.INDEX_ST_PENJUALAN_MENU = 0
		self.INDEX_ST_PENJUALAN_PH = 1
		self.INDEX_ST_PENJUALAN_PHB = 2
		self.INDEX_ST_PENJUALAN_OP = 3
		self.INDEX_ST_PENJUALAN_OP_TAMBAHPRODUK = 4
		self.INDEX_ST_PENJUALAN_PENGIRIMAN = 5
		self.INDEX_ST_PENJUALAN_PENGIRIMANB = 6
		self.INDEX_ST_PENJUALAN_PU = 7
		self.INDEX_ST_PENJUALAN_RPU = 8
		self.INDEX_ST_PENJUALAN_PP = 9
		self.INDEX_ST_PENJUALAN_PPB = 10
		self.INDEX_ST_PENJUALAN_RP = 11
		
		
		#---------------------------------------------------------------Data Master init
		#init konstanta index
		self.INDEX_ST_DATAMASTER_MENU = 0
		self.INDEX_ST_DATAMASTER_COMMON = 1
		self.INDEX_ST_DATAMASTER_DATANAMAALAMAT = 21 #just make it unique
		self.INDEX_ST_DATAMASTER_DATANAMAALAMAT_TAMBAH = 2
		self.INDEX_ST_DATAMASTER_DATAPRODUK = 31 #just make it unique
		self.INDEX_ST_DATAMASTER_DATAPRODUK_TAMBAH = 3
		self.INDEX_ST_DATAMASTER_DATAPAJAK = 41 #just make it unique
		self.INDEX_ST_DATAMASTER_DATAPAJAK_TAMBAH = 4
		self.INDEX_ST_DATAMASTER_DATAPROYEK = 51
		self.INDEX_ST_DATAMASTER_DATAPROYEK_TAMBAH = 5
		self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN = 61
		self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN_TAMBAH = 6
		self.INDEX_ST_DATAMASTER_DATAREKENING = 7
		self.INDEX_ST_DATAMASTER_DATAREKENING_TAMBAH = 8
		
		#init room2
		#---------------------------------------------------------------Satuan Pengukuran combobox di room Data Produk & room Satuan Pengukuran
		
		sql = "SELECT * FROM `gd_satuan_pengukuran` "
		result = self.DatabaseRunQuery(sql)
		for a in range(0,len(result)):
			self.cb_DataMaster_DataProduk_Tambah_Satuan.addItem(str(result[a][2])+" (kode: "+result[a][1]+")")
			self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.addItem(str(result[a][2])+" (kode: "+result[a][1]+")")
		
		#---------------------------------------------------------------DataNamaAlamat
		self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setReadOnly(True)
		self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.stateChanged.connect(self.DataMaster_DataNamaAlamat_Tambah_JatuhTempoSet)
		self.DataMaster_DataNamaAlamat_Edit_idEDIT = -1 #untuk penanda apakah update atau insert pada tombol simpan
		
		#---------------------------------------------------------------DataProduk
		self.DataMaster_DataProduk_Edit_idEDIT = -1
		#---------------------------------------------------------------DataPajak
		self.DataMaster_DataPajak_Edit_idEDIT = -1
		
		#---------------------------------------------------------------DataProyek
		#List pilihan di Data Proyek
		self.sc_DataMaster_DataProyek_Tambah_Penjab.hide()
		self.lb_DataMaster_DataProyek_Tambah_PilihPenjab.hide()
		#~ self.ile_DataMaster_DataProyek_Tambah_PenanggungJawab.hide()
		self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.setReadOnly(True)
		
		#Tombol biru: Buka popup tambah
		def ____DataMaster_DataProyek_Tambah_Penjab_Ok():
			self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setText(self.le_DataMaster_DataNamaAlamat_Tambah_Nama.text())
			self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.setText(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
			
		self.tb_DataMaster_DataProyek_Tambah_PenanggungJawab.clicked.connect(functools.partial(self.DataMaster_DataNamaAlamat_Popup_Tambah,____DataMaster_DataProyek_Tambah_Penjab_Ok,self.DataMaster_None,self.DataMaster_None,self.DataMaster_None))
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.textEdited.connect(self.DataMaster_DataProyek_Tambah_Showlist_Change)
		#~ QtCore.QObject.connect(self.le_DataMaster_DataProyek_Tambah_PenanggungJawab, QtCore.SIGNAL(_fromUtf8("editingFinished()")), MainWindow.showFullScreen)
		self.DataMaster_DataProyek_Edit_idEDIT = -1
		
		
		#---------------------------------------------------------------DataSatuan
		self.DataMaster_DataSatuanPengukuran_Edit_idEDIT = -1
		
		
		#---------------------------------------------------------------DataRekening
		self.DataMaster_DataRekening_Edit_idEDIT = -1
		
		
		#----------------------------------------------------------------Set index and window size
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_MENU)
		self.showFullScreen()
		
		#---------------------------------------------------------------sinyal pindah room
		self.tb_DataMaster_DataNamaAlamat.clicked.connect				(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATANAMAALAMAT))
		self.tb_DataMaster_DataNamaAlamat_Tambah_Batal.clicked.connect	(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATANAMAALAMAT))
		self.tb_DataMaster_DataNamaAlamat_Tambah_Simpan.clicked.connect	(self.DataMaster_DataNamaAlamat_Tambah_Act_Simpan)
		QtCore.QObject.connect(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(QString)")), self.DataMaster_DataNamaAlamat_Tambah_Tipe_Change)
		
		
		self.tb_DataMaster_DataProduk.clicked.connect					(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPRODUK))
		self.tb_DataMaster_DataProduk_Tambah_Batal.clicked.connect		(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPRODUK))
		self.tb_DataMaster_DataProduk_Tambah_Simpan.clicked.connect		(self.DataMaster_DataProduk_Tambah_Act_Simpan)
		
		self.tb_DataMaster_DataPajak.clicked.connect					(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPAJAK))
		self.tb_DataMaster_DataPajak_Tambah_Batal.clicked.connect		(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPAJAK))
		self.tb_DataMaster_DataPajak_Tambah_Simpan.clicked.connect		(self.DataMaster_DataPajak_Tambah_Act_Simpan)
		
		self.tb_DataMaster_DataProyek.clicked.connect					(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPROYEK))
		self.tb_DataMaster_DataProyek_Tambah_Batal.clicked.connect		(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATAPROYEK))
		self.tb_DataMaster_DataProyek_Tambah_Simpan.clicked.connect		(self.DataMaster_DataProyek_Tambah_Act_Simpan)
		
		self.tb_DataMaster_DataSatuanPengukuran.clicked.connect				(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN))
		self.tb_DataMaster_DataSatuanPengukuran_Tambah_Batal.clicked.connect(functools.partial(self.DataMaster_Goto_Common,self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN))
		self.tb_DataMaster_DataSatuanPengukuran_Tambah_Simpan.clicked.connect(self.DataMaster_DataSatuanPengukuran_Tambah_Act_Simpan)
		
		self.tb_DataMaster_DataRekening.clicked.connect(self.DataMaster_DataRekening)
		
		self.tb_DataMaster_DataCommon_Tutup.clicked.connect(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_MENU)
		
		self.initDatabase()
		cursor = self.db.cursor()
		#Get Field gd_nama_alamat
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_nama_alamat';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataNamaAlamat_Field = list(itertools.chain.from_iterable(result))
		#Get Field gd_data_produk
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_data_produk';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataProduk_Field = list(itertools.chain.from_iterable(result))
		#Get Field gd_data_pajak
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_data_pajak';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataPajak_Field = list(itertools.chain.from_iterable(result))
		#Get Field gd_proyek
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_proyek';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataProyek_Field = list(itertools.chain.from_iterable(result))
		#Get Field gd_satuan_pengukuran
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_satuan_pengukuran';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataSatuanPengukuran_Field = list(itertools.chain.from_iterable(result))
		#Get Field gd_rekening_jurnal
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_rekening_jurnal';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataRekening_Field = list(itertools.chain.from_iterable(result))
		self.db.close()
		
		self.DataMaster_CommonRoom_cleared = 0
		
		
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
		
	#-------------------------------------------------------------------DataMaster
	#-------------------------------------------------------------------DataMaster
	def DataMaster_None(self):
		None
	
	def initDatabase(self):
		try:
			self.db = MySQLdb.connect(self.dbHost,self.dbUser,self.dbPass,self.dbDatabase)
			print ("connected database to generic mysql port")
		except:
			try:
				self.db = MySQLdb.Connect(host=self.dbHost, port=self.dbPort, user=self.dbUser, passwd=self.dbPass, db=self.dbDatabase)
				print ("connected database to default port")
			except:
				print ("This software should be ran with correct procedure. Contact customer service for help.")
				print ("run mysql? only works on makin's platform (y/n)")
				if (raw_input()=="y"):
					os.system("start mysql/mysql5.6.12/bin/mysqld --port="+str(self.dbPort))
					import time
					time.sleep(3)
					print "ok"
					self.db = MySQLdb.Connect(host=self.dbHost, port=self.dbPort, user=self.dbUser, passwd=self.dbPass, db=self.dbDatabase)
					
		return
	
	
	#-------------------------------------------------------------------Penjualan
	#-------------------------------------------------------------------Penjualan
	
	
	def Penjualan_GoTo_Menu(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_MENU)
		
	def Penjualan_GoTo_PenawaranHarga(self):
		rownum = self.tbl_Penjualan_PenawaranHarga.rowCount()
		for b in range (0, rownum):
			self.tbl_Penjualan_PenawaranHarga.removeRow(b)
		self.tbl_Penjualan_PenawaranHarga.setRowCount(0)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PH)
		self.initDatabase()
		cursor = self.db.cursor()
		query = "SELECT * FROM gd_order_penjualan"
		cursor.execute(query)
		result = cursor.fetchall()
		for a in range(0, len(result)):
			self.tbl_Penjualan_PenawaranHarga.insertRow(a)
			self.tbl_Penjualan_PenawaranHarga.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][2])))
			self.tbl_Penjualan_PenawaranHarga.setItem(a,2,QtGui.QTableWidgetItem(result[a][1]))
		self.db.close()
		
	def Penjualan_GoTo_OrderPenjualan(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP)
		self.cb_Penjualan_OrderPenjualan_Nama.clear()
		self.cb_Penjualan_OrderPenjualan_Gudang.clear()
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		print jumlahRow
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Penjualan_OrderPenjualan.removeRow(a)
		kodePenjualan = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		print kodePenjualan
		query = "SELECT * FROM gd_nama_alamat"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_Nama.addItem(self.DatabaseRunQuery(query)[a][2])
		query = "SELECT * FROM gd_data_gudang"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_Gudang.addItem(self.DatabaseRunQuery(query)[a][2])
		query = "SELECT * FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodePenjualan+"'"
		result = self.DatabaseRunQuery(query) 
		if len(result) != 0:
			for a in range(0,len(result)):
				print "tambah row"
				self.tbl_Penjualan_OrderPenjualan.insertRow(a)
				self.tbl_Penjualan_OrderPenjualan.setItem(a,0,QtGui.QTableWidgetItem(result[a][3])) #kode
				sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+result[a][3]+"'"
				self.tbl_Penjualan_OrderPenjualan.setItem(a,1,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][5]))) #nama produk
				self.tbl_Penjualan_OrderPenjualan.setItem(a,3,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][3]))) #jumlah
				self.tbl_Penjualan_OrderPenjualan.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][4]))) #satuan
				self.tbl_Penjualan_OrderPenjualan.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][5]))) #harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,5,QtGui.QTableWidgetItem(result[a][6])) #diskon
				total = result[a][4]*result[a][5]
				self.tbl_Penjualan_OrderPenjualan.setItem(a,6,QtGui.QTableWidgetItem(str(total))) #total harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,7,QtGui.QTableWidgetItem(result[a][7]))
		
	
	def Penjualan_GoTo_OP_TambahProduk(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP_TAMBAHPRODUK)
		print "pindah"
		self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Satuan.clear()
		self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.clear()
		query = "SELECT * FROM gd_data_produk"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.addItem(self.DatabaseRunQuery(query)[a][5])
		query = "SELECT * FROM gd_satuan_pengukuran"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Satuan.addItem(self.DatabaseRunQuery(query)[a][1])
		nama = str(self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+nama+"'"
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.setText(kodeBarang)
			
	def Penjualan_OrderPenjualan_TambahProduk(self):
		nama = str(self.cb_Penjualan_OrderPenjualan_Nama.currentText())
		query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = self.DatabaseRunQuery(query)[0][1]
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		kodeBarang = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.text())
		jumlah = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Jumlah.text())
		harga = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Harga.text())
		diskon = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Diskon.text())
		pajak = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Pajak.text())
		query = "SELECT * FROM `gd_data_pajak` WHERE `namaPajak` LIKE '"+pajak+"'"
		kodePajak = str(self.DatabaseRunQuery(query)[0][1])
		kodeMatauang = str(self.cb_Penjualan_OrderPenjualan_Kurs.currentText())
		query = "INSERT INTO `gd_order_penjualan` (`kodeTransaksi`,`kodeMatauang`,`kodePelanggan`,`kodeBarang`"+\
			",`jumlah`,`harga`,`diskon`,`kodePajak`) VALUES"+\
			"('"+kodeTransaksi+"','"+kodeMatauang+"','"+kodePelanggan+"','"+kodeBarang+"','"+jumlah+"','"+harga+"','"+diskon+"','"+kodePajak+"')"
		self.DatabaseRunQuery(query)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP)
		
	def HapusBaris(self, namaTabel):
		#print self.tbl_Penjualan_OrderPenjualan.currentRow()
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		currentRow = self.tbl_Penjualan_OrderPenjualan.currentRow()
		kodeBarang = str(self.tbl_Penjualan_OrderPenjualan.item(currentRow,0).text())
		query = "DELETE FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"' AND `kodeBarang` LIKE '"+kodeBarang+"';"
		print query
		self.DatabaseRunQuery(query)
		namaTabel.removeRow(currentRow)
		
	def Penjualan_GoTo_Pengiriman(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PENGIRIMAN)
		
	def Penjualan_GoTo_Pengiriman_Baru(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PENGIRIMANB)
	
	def Penjualan_GoTo_PiutangUsaha(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PU)
	
	def Penjualan_GoTo_PembayaranPiutang(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PP)
	
	def Penjualan_GoTo_ReturPenjualan(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_RP)

	def Penjualan_GoTo_PenawaranHarga_baru(self):
		self.cb_Penjualan_PenawaranHarga_Baru_Nama.clear()
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PHB)
		query = "SELECT * FROM gd_nama_alamat"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_PenawaranHarga_Baru_Nama.addItem(self.DatabaseRunQuery(query)[a][2])
		query = "SELECT * FROM gd_data_gudang"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_PenawaranHarga_Baru_Gudang.addItem(self.DatabaseRunQuery(query)[a][2])
		
	def Penjualan_PenawaranHarga_Baru_TabelComplete(self):
		self.initDatabase()
		cursorb = self.db.cursor()
		query = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` LIKE '0001';"
		cursorb.execute(query)
		result = cursorb.fetchall()
		print len(result)
		kode = result[0][1]
		nama = result[0][5]
		deskripsi = result[0][2]
		satuan = result[0][3]
		self.tbl_Penjualan_PenawaranHarga_baru.setItem(0,0,QtGui.QTableWidgetItem(kode))
		self.tbl_Penjualan_PenawaranHarga_baru.setItem(0,1,QtGui.QTableWidgetItem(nama))
		self.tbl_Penjualan_PenawaranHarga_baru.setItem(0,3,QtGui.QTableWidgetItem(satuan))
		self.db.commit()
		self.db.close()
	
	def Penjualan_PenawaranHarga_Baru_Rekam(self):
		nama = str(self.cb_Penjualan_PenawaranHarga_Baru_Nama.currentText())
		kodeTransaksi = str(self.le_Penjualan_PenawaranHarga_baru_SOPenawaran.text())
		#departemen = str(self.le_Penjualan_PenawaranHarga_baru_Departemen.text())
		jumlahRow = self.tbl_Penjualan_PenawaranHarga_baru.rowCount()
		
		#~ kodeBarang = 
		
		self.initDatabase()
		cursor = self.db.cursor()
		#~ kodeBarang = int(self.tbl_Penjualan_PenawaranHarga_baru.item(0,0))
		query = "INSERT INTO `"+self.dbDatabase+"`.`gd_order_penjualan`"+\
			" (`nama`, `kodeTransaksi`, `departemen`) "+\
			"VALUES ('"+nama+"', '"+SOPenawaran+"', '"+departemen+"');"
		cursor.execute(query)
		self.db.commit()
		self.db.close()
		
	def Penjualan_GoTo_PembayaranPiutang_Baru(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PPB)

	def DatabaseRunQuery(self,query):
		self.initDatabase()
		cursor = self.db.cursor()
		try:
			cursor.execute(query)
		except Exception, e:
			print repr(e)
			self.statusbar.showMessage(repr(e),20000)
		result = cursor.fetchall()
		self.db.commit()
		self.db.close()
		return result
	
		
	def clearLayout(self, layout):
		for i in reversed(range(layout.count())):
			item = layout.itemAt(i)
			
			if isinstance(item, QtGui.QWidgetItem):
				#~ print "widget" + str(item)
				item.widget().close()
				#--------------------------------------------------------------------------------------------------or
				#--------------------------------------------------------------------------------------------------item.widget().setParent(None)
			elif isinstance(item, QtGui.QSpacerItem):
				#~ print "spacer " + str(item)
				None
				#just so it's not a layout "else" bellow
				#--------------------------------------------------------------------------------------------------no need to do extra stuff
			else:
				#~ print "layout " + str(item)
				self.clearLayout(item.layout())
			#------------------------------------------------------------------------------------------------------remove the item from layout
			layout.removeItem(item)
	def clearGrid(self,grid):
		for r in reversed(range(grid.rowCount())):
			for c in reversed(range(grid.columnCount())):
				item = grid.itemAtPosition(r,c)
				if isinstance(item, QtGui.QWidgetItem):
					item.widget().close()
				elif isinstance(item, QtGui.QSpacerItem):
					None
				else:
					#~ self.clearGrid(item.grid())
					None
				grid.removeItem(item)
		self.DataMaster_CommonRoom_cleared = 1
	
	def GarvinDisconnect(self,stuff):
		"nyimpel2ke disconnect signal, cara manggil koyo self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)"
		try:
			stuff.disconnect()
			return 1
		except:
			return 0
	
if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	dmw = MainGUI()
	dmw.showFullScreen()
	sys.exit(app.exec_())
