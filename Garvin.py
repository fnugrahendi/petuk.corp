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

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s


class MainGUI(QtGui.QMainWindow, Ui_MainWindow):
	def __init__(self, parent= None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.st_Penjualan.setCurrentIndex(0)
		
		def ___metu():
			exit(0)
			return True
		self.tb_Penjualan_Keluar.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan keluar dari aplikasi?",___metu))
        
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
		
		self.tb_Penjualan_Pengiriman_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_Pengiriman_Baru.clicked.connect(self.Penjualan_GoTo_Pengiriman_Baru)
		self.tb_Penjualan_PengirimanBaru_Tutup.clicked.connect(self.Penjualan_GoTo_Pengiriman)
		
		self.tb_Penjualan_Piutang_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_RincianPiutang_Tutup.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		
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
		def BukuBesarInit():
			"""bookmark baris"""
			pass
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
	def DataMaster_Goto(self,goto_roomID):
		self.st_DataMaster.setCurrentIndex(goto_roomID)
	
	def DataMaster_Goto_Common(self,as_roomID,keep=False):
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_COMMON)
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		self.clearGrid(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0])
		
		#---------------------------------------------------------------Disconnect sinyal bila sudah di hubungkan
		try:
			self.tb_DataMaster_DataCommon_Tambah.clicked.disconnect()
		except:
			pass
		try:
			self.tb_DataMaster_DataCommon_Edit.clicked.disconnect()
		except:
			pass
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		#------------------------------------------------------------------------------------------------------Data Nama Alamat
		#--- Delete? ada di draw info
		if (as_roomID==self.INDEX_ST_DATAMASTER_DATANAMAALAMAT):
			def DataNamaAlamat():
				"""Bookmark baris, delete this later"""
				None
			self.lb_DataMaster_DataCommon_Judul.setText("Data Nama dan Alamat")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATANAMAALAMAT_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataNamaAlamat_Edit)
			self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(False)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			if (not keep):
				"""Kosongkan isi line edit"""
				lels = self.fr_DataMaster_DataNamaAlamat_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				for x in range(0,len(lels)):
					lels[x].setText("")
			
			self.DataMaster_DataNamaAlamat_Tambah_GenerateKode()
			
			#-----------------------------------------------------------Simple QCompleter implementations, buat demo 
			wordList = QStringList
			wordList = ["EMPLOYEE", "VENDOR", "CUSTOMER", "OTHER"]
			c = QCompleter(wordList,self)
			c.setCaseSensitivity(Qt.CaseInsensitive)
			self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setCompleter(c)
			
			
			sql = "SELECT * FROM `gd_nama_alamat` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				obj_Tb_ListPelanggan = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataNamaAlamat_ListPelanggan"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]))
				if (len(obj_Tb_ListPelanggan)<1):
					obj_Tb_Pelanggan = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					obj_Tb_Pelanggan.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataNamaAlamat_ListPelanggan"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])))
					local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
					obj_Tb_Pelanggan.setText(local_name)
					self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_Pelanggan,QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
					obj_Tb_Pelanggan.clicked.connect(functools.partial(self.DataMaster_DataNamaAlamat_DrawInfo,result[x]))
				else:
					for y in range(0,len(obj_Tb_ListPelanggan)):
						self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_ListPelanggan[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
						obj_Tb_ListPelanggan[y].show()
						obj_Tb_ListPelanggan[y].setText(str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]))
						obj_Tb_ListPelanggan[y].clicked.disconnect()
						obj_Tb_ListPelanggan[y].clicked.connect(functools.partial(self.DataMaster_DataNamaAlamat_DrawInfo,result[x]))
			
		#--------------------------------------------------------------------------------------------------------------------------Data Produk
		elif (as_roomID==self.INDEX_ST_DATAMASTER_DATAPRODUK):
			def DataProduk():
				"""Bookmark baris, delete this later"""
				None
			self.lb_DataMaster_DataCommon_Judul.setText("Data Produk")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATAPRODUK_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataProduk_Edit)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			self.le_DataMaster_DataProduk_Tambah_KodeBarang.setReadOnly(False)
			if (not keep):
				"""Kosongkan isi line edit"""
				lels = self.fr_DataMaster_DataProduk_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				for x in range(0,len(lels)):
					lels[x].setText("")
			
			self.DataMaster_DataProduk_Tambah_GenerateKode()
			
			sql = "SELECT * FROM `gd_data_produk` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				obj_Tb_ListProduk = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataProduk_List"+str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")]))
				if (len(obj_Tb_ListProduk)<1):
					obj_Tb_Produk = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					obj_Tb_Produk.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataProduk_ListProduk"+str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")])))
					local_name = str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")])
					obj_Tb_Produk.setText(local_name)
					self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_Produk,QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
					obj_Tb_Produk.clicked.connect(functools.partial(self.DataMaster_DataProduk_DrawInfo,result[x]))
				else:
					for y in range(0, len(obj_Tb_ListProduk)):
						self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(obj_Tb_ListProduk[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
						obj_Tb_ListProduk[y].show()
						obj_Tb_ListProduk[y].setText(str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")]))
						obj_Tb_ListProduk[y].clicked.disconnect()
						obj_Tb_ListProduk[y].clicked.connect(functools.partial(self.DataMaster_DataProduk_DrawInfo,result[x]))
			
		#--------------------------------------------------------------------------------------------------------------------------Data Pajak
		elif (as_roomID==self.INDEX_ST_DATAMASTER_DATAPAJAK):
			def DataPajak():
				"""Bookmark baris, delete this later"""
				None
			self.lb_DataMaster_DataCommon_Judul.setText("Data Pajak")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATAPAJAK_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataPajak_Edit)
			self.le_DataMaster_DataPajak_Tambah_KodePajak.setReadOnly(False)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			
			if (not keep):
				"""Kosongkan isi lineedit"""
				lels = self.fr_DataMaster_DataPajak_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				for x in range(0,len(lels)):
					lels[x].setText("")
			
			self.DataMaster_DataPajak_Tambah_GenerateKode()
			
			sql = "SELECT * FROM `gd_data_pajak` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				obj_Tb_ListPajak = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataPajak_List"+str(result[x][self.DataMaster_DataPajak_Field.index("namaPajak")]))
				if (len(obj_Tb_ListPajak)<1):
					obj_Tb_Pajak = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					obj_Tb_Pajak.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataPajak_ListPajak"+str(result[x][self.DataMaster_DataPajak_Field.index("namaPajak")])))
					local_name = str(result[x][self.DataMaster_DataPajak_Field.index("namaPajak")])
					obj_Tb_Pajak.setText(local_name)
					self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_Pajak,QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
					obj_Tb_Pajak.clicked.connect(functools.partial(self.DataMaster_DataPajak_DrawInfo,result[x]))
				else:
					for y in range(0, len(obj_Tb_ListPajak)):
						self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(obj_Tb_ListPajak[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
						obj_Tb_ListPajak[y].show()
						obj_Tb_ListPajak[y].setText(str(result[x][self.DataMaster_DataPajak_Field.index("namaPajak")]))
						obj_Tb_ListPajak[y].clicked.disconnect()
						obj_Tb_ListPajak[y].clicked.connect(functools.partial(self.DataMaster_DataPajak_DrawInfo,result[x]))
				
				#~ self.pushButton = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
				#~ self.pushButton.setObjectName(_fromUtf8("pushButton"))
				#~ self.pushButton.setText(_fromUtf8(result[x][self.DataMaster_DataPajak_Field.index("namaPajak")]))
				#~ self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(self.pushButton)
			
		elif (as_roomID==self.INDEX_ST_DATAMASTER_DATAPROYEK):
			def DataProyek():
				"""Bookmark baris, delete this later"""
				None
			self.lb_DataMaster_DataCommon_Judul.setText("Data Proyek")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATAPROYEK_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataProyek_Edit)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			self.le_DataMaster_DataProyek_Tambah_KodeProyek.setReadOnly(False)
			if (not keep):
				"""Kosongkan isi line edit"""
				lels = self.fr_DataMaster_DataProyek_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				for x in range(0,len(lels)):
					lels[x].setText("")
			
			self.DataMaster_DataProyek_Tambah_GenerateKode()
			
			sql = "SELECT * FROM `gd_proyek` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				Tb_ListProyek = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataProyek_List"+str(result[x][self.DataMaster_DataProyek_Field.index("namaProyek")]))
				if (len(Tb_ListProyek)<1):
					Tb_Proyek = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					Tb_Proyek.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataProyek_ListProyek"+str(result[x][self.DataMaster_DataProyek_Field.index("namaProyek")])))
					local_name = str(result[x][self.DataMaster_DataProyek_Field.index("namaProyek")])
					Tb_Proyek.setText(local_name)
					self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_Proyek,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_Proyek.clicked.connect(functools.partial(self.DataMaster_DataProyek_DrawInfo,result[x]))
				else:
					for y in range(0, len(Tb_ListProyek)):
						self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_ListProyek[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
						Tb_ListProyek[y].show()
						Tb_ListProyek[y].setText(str(result[x][self.DataMaster_DataProyek_Field.index("namaProyek")]))
						Tb_ListProyek[y].clicked.disconnect()
						Tb_ListProyek[y].clicked.connect(functools.partial(self.DataMaster_DataProyek_DrawInfo,result[x]))
		
		elif (as_roomID==self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN):
			def DataSatuanPengukuran():
				""""Bookmark baris, delete this later"""
				None
				
			self.lb_DataMaster_DataCommon_Judul.setText("Data Satuan Pengukuran")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataSatuanPengukuran_Edit)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setReadOnly(False)
			if (not keep):
				"""Kosongkan isi line edit"""
				lels = self.fr_DataMaster_DataSatuanPengukuran_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				for x in range(0,len(lels)):
					lels[x].setText("")
			
			self.DataMaster_DataSatuanPengukuran_Tambah_GenerateKode()
			
			sql = "SELECT * FROM `gd_satuan_pengukuran` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				Tb_ListSatuan = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataSatuan_List"+str(result[x][self.DataMaster_DataSatuanPengukuran_Field.index("namaSatuan")]))
				if (len(Tb_ListSatuan)<1):
					Tb_Satuan = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					Tb_Satuan.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataSatuan_ListSatuan"+str(result[x][self.DataMaster_DataSatuanPengukuran_Field.index("namaSatuan")])))
					local_name = str(result[x][self.DataMaster_DataSatuanPengukuran_Field.index("namaSatuan")])
					Tb_Satuan.setText(local_name)
					self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_Satuan,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_Satuan.clicked.connect(functools.partial(self.DataMaster_DataSatuanPengukuran_DrawInfo,result[x]))
				else:
					for y in range(0, len(Tb_ListSatuan)):
						self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_ListSatuan[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
						Tb_ListSatuan[y].show()
						Tb_ListSatuan[y].setText(str(result[x][self.DataMaster_DataSatuan_Field.index("namaSatuan")]))
						Tb_ListSatuan[y].clicked.disconnect()
						Tb_ListSatuan[y].clicked.connect(functools.partial(self.DataMaster_DataSatuanPengukuran_DrawInfo,result[x]))
		
	def DataMaster_DataRekening(self):
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(len(result))
		for row in range(0,len(result)):
			
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)==None):
				item = QtGui.QTableWidgetItem()
				#~ item.setColumnWidth(300)
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 0, item)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)==None):
				itema = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 1, itema)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)==None):
				itemb = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 2, itemb)
			
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)
			item.setText(result[row][1])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)
			item.setText(result[row][2])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)
			item.setText(result[row][3])
	
		def _SetActiveIndex(a,b):
			kode = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(a,0).text())
			sql = "SELECT * FROM `gd_rekening_jurnal` WHERE `noAkun` LIKE '"+kode+"' ;"
			res = self.DatabaseRunQuery(sql)
			self.DataMaster_DataRekening_Edit_idEDIT = res[0][0]
			return
		
		QtCore.QObject.disconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening,QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")),_SetActiveIndex)
		#~ QtCore.QObject.disconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening,QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")),aaaaa)
		#~ QtCore.QObject.connect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening, QtCore.SIGNAL(_fromUtf8("cellClicked(int,int)")), _SetActiveIndex)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked.connect(_SetActiveIndex)
		#~ QtCore.QObject.connect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening, QtCore.SIGNAL(_fromUtf8("itemClicked(QTableWidgetItem*)")), aaaaa)
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAREKENING)
	
	def DataMaster_DataRekening_Popup_Pilih(self,fcb_ok=False,fcb_cancel=False):
		if fcb_ok==False:
			fcb_ok = self.DataMaster_None
		if fcb_cancel==False:
			fcb_cancel = self.DataMaster_None
		
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(len(result))
		for row in range(0,len(result)):
			
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)==None):
				item = QtGui.QTableWidgetItem()
				#~ item.setColumnWidth(300)
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 0, item)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)==None):
				itema = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 1, itema)
			if (self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)==None):
				itemb = QtGui.QTableWidgetItem()
				self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setItem(row, 2, itemb)
			
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,0)
			item.setText(result[row][1])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,1)
			item.setText(result[row][2])
			item = self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,2)
			item.setText(result[row][3])
	
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		
		self.DataMaster_Popup("",fcb_ok,650,WinH-200,None,fcb_cancel,True)
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		
		self.fr_DataMaster_DataRekening.setParent(FrameWindow)
		self.fr_DataMaster_DataRekening.show()
		self.fr_DataMaster_DataRekening.setGeometry(QtCore.QRect(5,5,640,WinH-250))
		self.fr_DataMaster_DataRekening_Fb.hide()
		
		
	
	def DataMaster_DataNamaAlamat_DrawInfo(self,data): #nama,perusahaan,tipe,npwp,diskon,jatuhtempo,diskonawal,dendaketerlambatan,alamat,kodepelanggan
		field = self.DataMaster_DataNamaAlamat_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			#~ if (self.DataMaster_CommonRoom_cleared==1):
				#~ skipkeexcept
			self.lb_DataMaster_DataNamaAlamat_Nama.setText(data[field("namaPelanggan")])
			self.lb_DataMaster_DataNamaAlamat_Nama.setFont(f14)
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Nama, 0, 0, 1, 3,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Nama.show()
		except:
			self.lb_DataMaster_DataNamaAlamat_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Nama, 0, 0, 1, 3,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Nama.setText(data[field("namaPelanggan")])
			self.lb_DataMaster_DataNamaAlamat_Nama.setFont(f14)
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kode, 0, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_kode.show()
			self.lb_DataMaster_DataNamaAlamat_kode.setText("\n\n" + str(data[field("kodePelanggan")]))
		except:
			self.lb_DataMaster_DataNamaAlamat_kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_kode.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kode, 0, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_kode.setText("\n\n" + str(data[field("kodePelanggan")]))
			
		#--------------------------------------------------------------------------------------------------------Tipe
		
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_tipe, 0, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_tipe.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ltipe, 0, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ltipe.show()
			self.lb_DataMaster_DataNamaAlamat_tipe.setText(data[field("tipe")])
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setText("Tipe :")
		except:
			self.lb_DataMaster_DataNamaAlamat_tipe = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_tipe.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_tipe"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_tipe, 0, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_tipe.setText(data[field("tipe")])
			
			self.lb_DataMaster_DataNamaAlamat_Ltipe = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ltipe"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ltipe, 0, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setText("Tipe :")
			
		#--------------------------------------------------------------------------------------------------------Kontak
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kontak, 1, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_kontak.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lkontak, 1, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lkontak.show()
			self.lb_DataMaster_DataNamaAlamat_kontak.setText(data[field("kontak")])
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setText("Kontak :")
		except:
			self.lb_DataMaster_DataNamaAlamat_kontak = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_kontak.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_kontak"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kontak, 1, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_kontak.setText(data[field("kontak")])
			
			self.lb_DataMaster_DataNamaAlamat_Lkontak = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lkontak"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lkontak, 1, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setText("Kontak :")
		
		#--------------------------------------------------------------------------------------------------------NPWP
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_npwp, 1, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_npwp.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lnpwp, 1, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lnpwp.show()
			self.lb_DataMaster_DataNamaAlamat_npwp.setText(data[field("npwp")])
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setText("NPWP :")
		except:
			self.lb_DataMaster_DataNamaAlamat_npwp = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_npwp.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_npwp"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_npwp, 1, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_npwp.setText(data[field("npwp")])
			
			self.lb_DataMaster_DataNamaAlamat_Lnpwp = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lnpwp"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lnpwp, 1, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setText("NPWP :")
			
		#--------------------------------------------------------------------------------------------------------Alamat
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_alamat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_alamat.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lalamat, 2, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lalamat.show()
			self.lb_DataMaster_DataNamaAlamat_alamat.setText(data[field("alamat")])
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setText("Alamat :")
		except:
			self.lb_DataMaster_DataNamaAlamat_alamat = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_alamat.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_alamat"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_alamat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_alamat.setText(data[field("alamat")])
			
			self.lb_DataMaster_DataNamaAlamat_Lalamat = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lalamat"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lalamat, 2, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setText("Alamat :")
		
		#--------------------------------------------------------------------------------------------------------Denda
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_denda, 2, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_denda.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldenda, 2, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ldenda.show()
			self.lb_DataMaster_DataNamaAlamat_denda.setText(str(data[field("dendaKeterlambatan")]))
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setText("Denda Keterlambatan :")
		except:
			self.lb_DataMaster_DataNamaAlamat_denda = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_denda.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_denda"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_denda, 2, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_denda.setText(str(data[field("dendaKeterlambatan")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ldenda = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ldenda"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldenda, 2, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setText("Denda Keterlambatan :")
			
		#--------------------------------------------------------------------------------------------------------Diskon
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskon, 3, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_diskon.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldiskon, 3, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ldiskon.show()
			
			self.lb_DataMaster_DataNamaAlamat_diskon.setText(str(data[field("diskon")]))
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setText("Diskon :")
		except:
			self.lb_DataMaster_DataNamaAlamat_diskon = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_diskon.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_diskon"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskon, 3, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_diskon.setText(str(data[field("diskon")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ldiskon = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ldiskon"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldiskon, 3, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setText("Diskon :")
		
		#--------------------------------------------------------------------------------------------------------diskonAwal
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskonAwal, 3, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_diskonAwal.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_LdiskonAwal, 3, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.show()
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setText(str(data[field("diskonAwal")]))
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setText("Diskon Awal :")
		except:
			self.lb_DataMaster_DataNamaAlamat_diskonAwal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_diskonAwal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskonAwal, 3, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setText(str(data[field("diskonAwal")]))
			
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_LdiskonAwal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_LdiskonAwal, 3, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setText("Diskon Awal :")
		
		#--------------------------------------------------------------------------------------------------------jatuhtempo
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_jatuhtempo, 4, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_jatuhtempo.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo, 4, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.show()
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setText(str(data[field("jatuhtempo")]))
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setText("Jatuh Tempo :")
		except:
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_jatuhtempo"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_jatuhtempo, 4, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setText(str(data[field("jatuhtempo")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ljatuhtempo"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo, 4, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setText("Jatuh Tempo :")
		
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			#~ if (self.DataMaster_CommonRoom_cleared==1):
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.fr_DataMaster_DataNamaAlamat_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataNamaAlamat_FGraph.show()
			
		except:
			self.fr_DataMaster_DataNamaAlamat_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataNamaAlamat_FGraph"))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMaximumSize(QtCore.QSize(1366,400))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.fr_DataMaster_DataNamaAlamat_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataNamaAlamat_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataNamaAlamat_FGraph)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataNamaAlamat_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					"<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					"<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataNamaAlamat_FGraph)
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			#~ self.ihl_DataMaster_DataNamaAlamat_FGraph.addWidget(self.svg_DataMaster_DataNamaAlamat_TransaksiOrang)

		self.DataMaster_CommonRoom_cleared = 0
		
		try:
			self.lb_DataMaster_DataNamaAlamat_Nama.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataNamaAlamat_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataNamaAlamat_Delete,500,200,None,None))
		
		
	def DataMaster_DataNamaAlamat_Tambah_Act_Simpan(self):
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(False)
		nama = str(self.le_DataMaster_DataNamaAlamat_Tambah_Nama.text())
		tipe = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText())
		npwp = str(self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.text())
		diskon = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.value())
		jatuhtempo = ("0000-00-00 00:00:00" if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()==0) else str(self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.dateTime().toString("yyyy-MM-dd hh:mm:ss")) )
		diskonawal = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.value())
		dendaketerlambatan = str(self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.text())
		alamat = str(self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.text())
		kodepelanggan = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		kontak = str(self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.text())
		sql = ""
		if (self.DataMaster_DataNamaAlamat_Edit_idEDIT >=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
			"SET `namaPelanggan` = '"+nama+"',"+\
				"`kodePelanggan` = '"+kodepelanggan+"',"+\
				"`tipe` = '"+tipe+"',"+\
				"`npwp` = '"+npwp+"',"+\
				"`diskon` = '"+diskon+"',"+\
				"`jatuhTempo` = '"+jatuhtempo+"',"+\
				"`diskonAwal` = '"+diskonawal+"',"+\
				"`dendaKeterlambatan` = '"+dendaketerlambatan+"',"+\
				"`alamat` = '"+alamat+"',"+\
				"`kontak` = '"+kontak+"'"+\
			"WHERE `gd_nama_alamat`.`id`='"+str(self.DataMaster_DataNamaAlamat_Edit_idEDIT)+"'"
			self.DataMaster_DataNamaAlamat_Edit_idEDIT = -1
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
				"(`id`, `kodePelanggan`, `namaPelanggan`, `tipe`, `npwp`, `diskon`, `jatuhTempo`, `diskonAwal`, `dendaKeterlambatan`, `alamat`, `kontak`)"+\
				"VALUES "+\
				"(NULL, '"+kodepelanggan+"', '"+nama+"', '"+tipe+"', '"+npwp+"', '"+diskon+"', '"+jatuhtempo+"', '"+diskonawal+"', '"+dendaketerlambatan+"', '"+alamat+"', '"+kontak+"');"
		self.DatabaseRunQuery(sql)
		#----------------------------------------------------------------------------------------------------------back to where it should be
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT)
	
	def DataMaster_DataNamaAlamat_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan, 
			dipanggil ketika menambah data nama alamat baru, atau ganti tipe pada combo box cb_
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_nama_alamat` ORDER BY `gd_nama_alamat`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		#beri nilai default untuk kodeID nama alamat untuk memudahkan
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<6):
			kode_default = "0"+kode_default
		kode_default = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText()).upper() + "."+kode_default
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(kode_default)
	
	def DataMaster_DataProduk_Tambah_Act_Simpan(self):
		kode = str(self.le_DataMaster_DataProduk_Tambah_KodeBarang.text())
		nama = str(self.le_DataMaster_DataProduk_Tambah_NamaBarang.text())
		deskripsi = str(self.le_DataMaster_DataProduk_Tambah_Deskripsi.text())
		hpp = str(self.le_DataMaster_DataProduk_Tambah_HPP.text())
		sifat = str(self.cb_DataMaster_DataProduk_Tambah_Sifat.currentText())
		stok = str(self.le_DataMaster_DataProduk_Tambah_Stok.text())
		satuan = str(self.cb_DataMaster_DataProduk_Tambah_Satuan.currentText())
		satuan = str(satuan[satuan.find("(kode: ")+len("(kode: "):-1])
		sql =""
		if (self.DataMaster_DataProduk_Edit_idEDIT>=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_data_produk` "+\
				"SET `kodeBarang` = '"+kode+"',"+\
					"`deskripsi` = '"+deskripsi+"',"+\
					"`kodeSatuan` = '"+satuan+"',"+\
					"`hpp` = '"+hpp+"',"+\
					"`namaBarang` = '"+nama+"',"+\
					"`sifat` = '"+sifat+"',"+\
					"`stok` = '"+stok+"' "+\
				"WHERE `gd_data_produk`.`id`='"+str(self.DataMaster_DataProduk_Edit_idEDIT)+"'"
			self.DataMaster_DataProduk_Edit_idEDIT = -1
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_data_produk`"+\
					" (`id`, `kodeBarang`, `deskripsi`, `kodeSatuan`, `hpp`, `namaBarang`, `sifat`, `stok`) "+\
					"VALUES (NULL, '"+kode+"', '"+deskripsi+"', '"+satuan+"', '"+hpp+"', '"+deskripsi+"', '"+sifat+"', '"+stok+"');"
		self.DatabaseRunQuery(sql)
		self.le_DataMaster_DataProduk_Tambah_KodeBarang.setReadOnly(False)
		#----------------------------------------------------------------------------------------------------------back to where it should be
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPRODUK)
	
	def DataMaster_DataProduk_Popup_Tambah(self, fcallback_ok=None,fcallback_cancel=None,fcallback_enter=None,fcallback_exit=None):
		"""
		Tampilkan popup untuk menambah DataProduk
		fcallback_enter dieksekusi sebelum membangun popup, (A)
		fcallback_ok dieksekusi jika ok di klik pada popup (B)
		fcallback_cancel diekseskusi jika cancel/close diklik pada popup (B)
		fcallback_exit dieksekusi saat fungsi selesai (C)
		"""
		if fcallback_enter==None or fcallback_enter==False:
			fcallback_enter = self.DataMaster_None
		if fcallback_cancel==None or fcallback_cancel==False:
			fcallback_cancel = self.DataMaster_None
		if fcallback_ok==None or fcallback_ok==False:
			fcallback_ok = self.DataMaster_None
		if fcallback_exit==None or fcallback_exit==False:
			fcallback_exit = self.DataMaster_None
			
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		fcallback_enter() #-----A
		def exit_function():
			self.fr_DataMaster_DataProduk_Tambah.setParent(None)
			self.fr_DataMaster_DataProduk_Tambah.setParent(self.st_DataMaster_DataProduk_Tambah)
			self.ivl_DataMaster_DataProduk_Tambah_Luar.addWidget(self.fr_DataMaster_DataProduk_Tambah)
			self.fr_DataMaster_DataProduk_Tambah_Fbot.show()
			fcallback_exit()#---(C)
			
		self.DataMaster_DataProduk_Tambah_GenerateKode()
		self.DataMaster_Popup("",functools.partial(self.DataMaster_DataProduk_Popup_Act_Tambah,fcallback_ok),WinW-10,WinH-200,exit_function,fcallback_cancel) #----B
		
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		self.fr_DataMaster_DataProduk_Tambah.setParent(FrameWindow)
		self.fr_DataMaster_DataProduk_Tambah.show()
		self.fr_DataMaster_DataProduk_Tambah.setGeometry(QtCore.QRect(5,5,WinW-20,WinH-250))
		self.fr_DataMaster_DataProduk_Tambah_Fbot.hide()
		
	def DataMaster_DataProduk_Popup_Act_Tambah(self):
		None
	
	
	def DataMaster_DataProduk_DrawInfo(self,data):
		#~ def field(fieldname):
			#~ return self.DataMaster_DataProduk_Field.index(fieldname)
		
		field = self.DataMaster_DataProduk_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		f12 = QtGui.QFont()
		f12.setPointSize(9)
		f12.setBold(False)
		f12.setItalic(False)
		f12.setWeight(50)
		f12i = QtGui.QFont()
		f12i.setPointSize(9)
		f12i.setBold(False)
		f12i.setItalic(True)
		f12i.setWeight(50)
		common_width = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()/3
		#~ self.clearGrid(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0])
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			self.lb_DataMaster_DataProduk_Nama.setText(data[field("namaBarang")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Nama, 0, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProduk_Nama.show()
		except:
			self.lb_DataMaster_DataProduk_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProduk_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataProduk_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Nama, 0, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProduk_Nama.setText(data[field("namaBarang")])
			self.lb_DataMaster_DataProduk_Nama.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProduk_Nama.setMaximumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProduk_Nama.setFont(f14)
		#-------------------------------------------------------------------------------------------------------Kode
		try:
			self.lb_DataMaster_DataProduk_Kode.setText(""+str(data[field("kodeBarang")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Kode, 1, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProduk_Kode.show()
		except:
			self.lb_DataMaster_DataProduk_Kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProduk_Kode.setObjectName(_fromUtf8("lb_DataMaster_DataProduk_Kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Kode, 1, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProduk_Kode.setText(""+str(data[field("kodeBarang")]))
			self.lb_DataMaster_DataProduk_Kode.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProduk_Kode.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProduk_Kode.setFont(f12)
		#------------------------------------------------------------------------------------------------------Deskripsi
		try:
			self.lw_DataMaster_DataProduk_Deskripsi.item(0).setText(data[field("deskripsi")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lw_DataMaster_DataProduk_Deskripsi, 3, 0, 1, 2,QtCore.Qt.AlignTop)
				self.lw_DataMaster_DataProduk_Deskripsi.show()
		except:
			self.lw_DataMaster_DataProduk_Deskripsi = QtGui.QListWidget(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lw_DataMaster_DataProduk_Deskripsi.setObjectName(_fromUtf8("lw_DataMaster_DataProduk_Deskripsi"))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lw_DataMaster_DataProduk_Deskripsi, 3, 0, 1, 2,QtCore.Qt.AlignTop)
			item = QtGui.QListWidgetItem()
			item.setText(data[field("deskripsi")])
			#~ item.setFont(f12i)
			self.lw_DataMaster_DataProduk_Deskripsi.addItem(item)
			self.lw_DataMaster_DataProduk_Deskripsi.setMinimumSize(QtCore.QSize(common_width*2, 50))
			self.lw_DataMaster_DataProduk_Deskripsi.setMaximumSize(QtCore.QSize(common_width*2, 50))
			
		
		#------------------------------------------------------------------------------------------------------HPP
		try:
			self.lb_DataMaster_DataProduk_HPP.setText("HPP : "+str(data[field("hpp")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_HPP, 0, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProduk_HPP.show()
		except:
			self.lb_DataMaster_DataProduk_HPP = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProduk_HPP.setObjectName(_fromUtf8("lb_DataMaster_DataProduk_HPP"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_HPP, 0, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProduk_HPP.setText("HPP : "+str(data[field("hpp")]))
			self.lb_DataMaster_DataProduk_HPP.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProduk_HPP.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProduk_HPP.setFont(f12)
		
		#------------------------------------------------------------------------------------------------------Sifat
		try:
			self.lb_DataMaster_DataProduk_Sifat.setText("Sifat : "+str(data[field("sifat")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Sifat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProduk_Sifat.show()
		except:
			self.lb_DataMaster_DataProduk_Sifat = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProduk_Sifat.setObjectName(_fromUtf8("lb_DataMaster_DataProduk_Sifat"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Sifat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProduk_Sifat.setText("Sifat : "+str(data[field("sifat")]))
			self.lb_DataMaster_DataProduk_Sifat.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProduk_Sifat.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProduk_Sifat.setFont(f12)
			
		#------------------------------------------------------------------------------------------------------Stok
		sql = "SELECT * FROM `gd_satuan_pengukuran` WHERE `gd_satuan_pengukuran`.`kodeSatuan` = '"+str(data[field("kodeSatuan")])+"' "
		satuanL = self.DatabaseRunQuery(sql)
		if (len(satuanL)<1):
			satuan = ""
		else:
			satuan = satuanL[0][self.DataMaster_DataSatuanPengukuran_Field.index("namaSatuan")]
		try:
			self.lb_DataMaster_DataProduk_Stok.setText("Stok : "+str(data[field("stok")])+ " "+str(satuan))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Stok, 1, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProduk_Stok.show()
		except:
			self.lb_DataMaster_DataProduk_Stok = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProduk_Stok.setObjectName(_fromUtf8("lb_DataMaster_DataProduk_Stok"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProduk_Stok, 1, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProduk_Stok.setText("Stok : "+str(data[field("stok")])+ " "+str(satuan))
			self.lb_DataMaster_DataProduk_Stok.setMinimumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProduk_Stok.setFont(f12)
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProduk_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProduk_FGraph.show()
				#~ print "no rebuild"
				
		except:
			self.fr_DataMaster_DataProduk_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataProduk_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataProduk_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataProduk_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataProduk_FGraph"))
			self.fr_DataMaster_DataProduk_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProduk_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProduk_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataProduk_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataProduk_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataProduk_FGraph)
			self.ihl_DataMaster_DataProduk_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataProduk_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataProduk_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataProduk_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					"<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					"<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataProduk_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataProduk_FGraph)
			self.svg_DataMaster_DataProduk_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataProduk_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			
		self.DataMaster_CommonRoom_cleared = 0
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataProduk_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataProduk_Delete,500,200,None,None))
		
	
	def DataMaster_DataProduk_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataProduk_Tambah_KodeBarang, 
		"""
		self.initDatabase()
		cursor = self.db.cursor()
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_data_produk` ORDER BY `gd_data_produk`.`id` DESC LIMIT 0 , 1"
		cursor.execute(sql)
		result = cursor.fetchall()
		#beri nilai default untuk kodeID nama alamat untuk memudahkan
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<6):
			kode_default = "0"+kode_default
		kode_default = "PRD" + "."+kode_default
		self.le_DataMaster_DataProduk_Tambah_KodeBarang.setText(kode_default)
		self.db.close()
	
	def DataMaster_DataProduk_Delete(self):
		kode = str(self.lb_DataMaster_DataProduk_Kode.text()).replace("\n","")
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_data_produk` WHERE `gd_data_produk`.`kodeBarang` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPRODUK)
	
	
	def DataMaster_DataProduk_Edit(self):
		field = self.DataMaster_DataProduk_Field.index
		kode = str(self.lb_DataMaster_DataProduk_Kode.text()).replace("\n","")
		sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+kode+"' LIMIT 0 , 1"
		barang = self.DatabaseRunQuery(sql)
		
		self.le_DataMaster_DataProduk_Tambah_KodeBarang.setText(_fromUtf8(str(barang[0][field("kodeBarang")])))
		self.le_DataMaster_DataProduk_Tambah_KodeBarang.setReadOnly(True) #---set kode ke Read Only dulu, set to false on _Act_Simpan
		self.le_DataMaster_DataProduk_Tambah_NamaBarang.setText(_fromUtf8(str(barang[0][field("namaBarang")])))
		self.le_DataMaster_DataProduk_Tambah_Deskripsi.setText(	_fromUtf8(str(barang[0][field("deskripsi")])))
		self.le_DataMaster_DataProduk_Tambah_HPP.setText(		_fromUtf8(str(barang[0][field("hpp")])))
		self.cb_DataMaster_DataProduk_Tambah_Sifat.setCurrentIndex(self.cb_DataMaster_DataProduk_Tambah_Sifat.findText( _fromUtf8(str(barang[0][field("sifat")]))))
		self.le_DataMaster_DataProduk_Tambah_Stok.setText(		_fromUtf8(str(barang[0][field("stok")])))
		res = self.DatabaseRunQuery("SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+str(barang[0][field("kodeSatuan")])+"' ;")
		ns = self.DataMaster_DataSatuanPengukuran_Field.index("namaSatuan")
		ks = self.DataMaster_DataSatuanPengukuran_Field.index("kodeSatuan")
		try:
			satuan = str(res[0][ns]) + " (kode: " + str(res[0][ks]) + ")"
		except:
			satuan = ""
		self.cb_DataMaster_DataProduk_Tambah_Satuan.setCurrentIndex(self.cb_DataMaster_DataProduk_Tambah_Satuan.findText(_fromUtf8(satuan)))
		self.DataMaster_DataProduk_Edit_idEDIT = barang[0][field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAPRODUK_TAMBAH)
		
		
	
	def DataMaster_DataPajak_Tambah_Act_Simpan(self):
		kode = str(self.le_DataMaster_DataPajak_Tambah_KodePajak.text())
		nama = str(self.le_DataMaster_DataPajak_Tambah_NamaPajak.text())
		ket = str(self.le_DataMaster_DataPajak_Tambah_Keterangan.text())
		persen = str(self.dsb_DataMaster_DataPajak_Tambah_PersenPajak.value())
		
		if (self.DataMaster_DataPajak_Edit_idEDIT>=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_data_pajak` "+\
			"SET `kodePajak` = '"+kode+"',"+\
				"`namaPajak` = '"+nama+"',"+\
				"`persenPajak` = '"+persen+"',"+\
				"`keterangan` = '"+ket+"'"+\
			"WHERE `gd_data_pajak`.`id`='"+str(self.DataMaster_DataPajak_Edit_idEDIT)+"'"
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_data_pajak`"+\
				" (`id`, `kodePajak`, `namaPajak`, `persenPajak`, `keterangan`) "+\
				"VALUES (NULL, '"+kode+"', '"+nama+"', '"+persen+"', '"+ket+"');"
		self.DatabaseRunQuery(sql)
		#----------------------------------------------------------------------------------------------------------back to where it should be
		self.le_DataMaster_DataPajak_Tambah_KodePajak.setReadOnly(False)
		self.DataMaster_DataPajak_Edit_idEDIT = -1
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPAJAK)
	
	def DataMaster_DataPajak_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataPajak_Tambah_KodePajak, 
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_data_pajak` ORDER BY `gd_data_pajak`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<6):
			kode_default = "0"+kode_default
		kode_default = "PJK" + "."+kode_default
		self.le_DataMaster_DataPajak_Tambah_KodePajak.setText(kode_default)
		
	def DataMaster_DataPajak_Delete(self):
		kode = str(self.lb_DataMaster_DataPajak_Kode.text()).replace("\n","")
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_data_pajak` WHERE `gd_data_pajak`.`kodePajak` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPAJAK)
	
	def DataMaster_DataPajak_Edit(self):
		field = self.DataMaster_DataPajak_Field.index
		kode = str(self.lb_DataMaster_DataPajak_Kode.text()).replace("\n","")
		sql = "SELECT * FROM `gd_data_pajak` WHERE `kodePajak` = '"+kode+"' LIMIT 0 , 1"
		pajak = self.DatabaseRunQuery(sql)[0]
		self.le_DataMaster_DataPajak_Tambah_KodePajak.setText(kode)
		self.le_DataMaster_DataPajak_Tambah_KodePajak.setReadOnly(True)
		
		self.le_DataMaster_DataPajak_Tambah_NamaPajak.setText(pajak[field("namaPajak")])
		self.le_DataMaster_DataPajak_Tambah_Keterangan.setText(pajak[field("keterangan")])
		self.dsb_DataMaster_DataPajak_Tambah_PersenPajak.setValue(pajak[field("persenPajak")])
		self.DataMaster_DataPajak_Edit_idEDIT = pajak[field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAPAJAK_TAMBAH)
		
	
	def DataMaster_DataPajak_DrawInfo(self,data):
		field = self.DataMaster_DataPajak_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		
		f12b = QtGui.QFont()
		f12b.setPointSize(9)
		f12b.setBold(True)
		f12b.setItalic(False)
		f12b.setWeight(75)
		
		f12i = QtGui.QFont()
		f12i.setPointSize(9)
		f12i.setBold(False)
		f12i.setItalic(True)
		f12i.setWeight(50)
		common_width = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()/3
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			self.lb_DataMaster_DataPajak_Nama.setText(data[field("namaPajak")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataPajak_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataPajak_Nama.show()
		except:
			self.lb_DataMaster_DataPajak_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataPajak_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataPajak_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataPajak_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataPajak_Nama.setText(data[field("namaPajak")])
			self.lb_DataMaster_DataPajak_Nama.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataPajak_Nama.setMaximumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataPajak_Nama.setFont(f14)
		
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			self.lb_DataMaster_DataPajak_Kode.setText(data[field("kodePajak")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataPajak_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataPajak_Kode.show()
		except:
			self.lb_DataMaster_DataPajak_Kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataPajak_Kode.setObjectName(_fromUtf8("lb_DataMaster_DataPajak_Kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataPajak_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataPajak_Kode.setText(data[field("kodePajak")])
			self.lb_DataMaster_DataPajak_Kode.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataPajak_Kode.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataPajak_Kode.setFont(f12b)
			
		#--------------------------------------------------------------------------------------------------------Persen
		try:
			self.lb_DataMaster_DataPajak_Persen.setText(str(data[field("persenPajak")])+" %")
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataPajak_Persen, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataPajak_Persen.show()
		except:
			self.lb_DataMaster_DataPajak_Persen = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataPajak_Persen.setObjectName(_fromUtf8("lb_DataMaster_DataPajak_Persen"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataPajak_Persen, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataPajak_Persen.setText(str(data[field("persenPajak")])+" %")
			self.lb_DataMaster_DataPajak_Persen.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataPajak_Persen.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataPajak_Persen.setFont(f12b)
		
		#------------------------------------------------------------------------------------------------------Keterangan
		try:
			self.lw_DataMaster_DataProduk_Keterangan.item(0).setText(data[field("keterangan")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lw_DataMaster_DataProduk_Keterangan, 2, 0, 1, 2,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lw_DataMaster_DataProduk_Keterangan.show()
		except:
			self.lw_DataMaster_DataProduk_Keterangan = QtGui.QListWidget(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lw_DataMaster_DataProduk_Keterangan.setObjectName(_fromUtf8("lw_DataMaster_DataProduk_Keterangan"))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lw_DataMaster_DataProduk_Keterangan, 2, 0, 1, 2,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			item = QtGui.QListWidgetItem()
			item.setText(data[field("keterangan")])
			#~ item.setFont(f12i)
			self.lw_DataMaster_DataProduk_Keterangan.addItem(item)
			self.lw_DataMaster_DataProduk_Keterangan.setMinimumSize(QtCore.QSize(common_width*2, 50))
			self.lw_DataMaster_DataProduk_Keterangan.setMaximumSize(QtCore.QSize(common_width*2, 50))
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataPajak_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataPajak_FGraph.show()
		except:
			self.fr_DataMaster_DataPajak_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataPajak_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataPajak_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataPajak_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataPajak_FGraph"))
			self.fr_DataMaster_DataPajak_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataPajak_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataPajak_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataPajak_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataPajak_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataPajak_FGraph)
			self.ihl_DataMaster_DataPajak_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataPajak_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataPajak_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataPajak_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					"<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					"<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataPajak_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataPajak_FGraph)
			self.svg_DataMaster_DataPajak_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataPajak_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			
		self.DataMaster_CommonRoom_cleared = 0
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataPajak_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataPajak_Delete,500,200,None,None))
		
	
	def DataMaster_DataProyek_Tambah_Act_Simpan(self):
		kode = str(self.le_DataMaster_DataProyek_Tambah_KodeProyek.text())
		nama = str(self.le_DataMaster_DataProyek_Tambah_NamaProyek.text())
		penjab = str(self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.text())
		progress = str(self.dsb_DataMaster_DataProyek_Tambah_Progress.value())
		tmulai = str(self.dte_DataMaster_DataProyek_Tambah_TanggalMulai.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		tslsai = str(self.dte_DataMaster_DataProyek_Tambah_TanggalSelesai.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		anggaran =str(self.le_DataMaster_DataProyek_Tambah_AnggaranTotal.text())
		realisasi=str(self.le_DataMaster_DataProyek_Tambah_RealisasiTotal.text())
		pakaifase= str("1" if (self.chk_DataMaster_DataProyek_Tambah_PakaiFase.checkState()>0) else "0")
		
		if (self.DataMaster_DataProyek_Edit_idEDIT>=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_proyek` "+\
			"SET `kodeProyek` = '"+kode+"',"+\
				"`namaProyek` = '"+nama+"',"+\
				"`kodePenjab` = '"+penjab+"',"+\
				"`progress` = '"+progress+"',"+\
				"`tanggalMulai` = '"+tmulai+"',"+\
				"`tanggalSelesai` = '"+tslsai+"',"+\
				"`anggaranTotal` = '"+anggaran+"',"+\
				"`realisasiTotal` = '"+realisasi+"',"+\
				"`isFase` = '"+pakaifase+"'"+\
			"WHERE `gd_proyek`.`id`='"+str(self.DataMaster_DataProyek_Edit_idEDIT)+"'"
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_proyek`"+\
				" (`id`, `kodeProyek`, `namaProyek`, `kodePenjab`, `progress`, `tanggalMulai`, `tanggalSelesai`, `anggaranTotal`, `realisasiTotal`, `isFase`) "+\
				"VALUES (NULL, '"+kode+"', '"+nama+"', '"+penjab+"', "+progress+", '"+tmulai+"', '"+tslsai+"', '"+anggaran+"', '"+realisasi+"', "+pakaifase+");"
		self.DatabaseRunQuery(sql)
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setReadOnly(False)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPROYEK)
	
	def DataMaster_DataProyek_DrawInfo(self,data):
		field = self.DataMaster_DataProyek_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		
		f12b = QtGui.QFont()
		f12b.setPointSize(9)
		f12b.setBold(False)
		f12b.setItalic(False)
		f12b.setWeight(50)
		
		f12i = QtGui.QFont()
		f12i.setPointSize(9)
		f12i.setBold(False)
		f12i.setItalic(True)
		f12i.setWeight(50)
		common_width = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()/3
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			self.lb_DataMaster_DataProyek_Nama.setText(data[field("namaProyek")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Nama.show()
		except:
			self.lb_DataMaster_DataProyek_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_Nama.setText(data[field("namaProyek")])
			self.lb_DataMaster_DataProyek_Nama.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Nama.setMaximumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Nama.setFont(f14)
		
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			self.lb_DataMaster_DataProyek_Kode.setText(data[field("kodeProyek")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Kode.show()
		except:
			self.lb_DataMaster_DataProyek_Kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Kode.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_Kode.setText(data[field("kodeProyek")])
			self.lb_DataMaster_DataProyek_Kode.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Kode.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12b)
		
		#--------------------------------------------------------------------------------------------------------Penjab
		try:
			sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+str(data[field("kodePenjab")])+"'"
			try:
				penjab = str(self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
			except:
				penjab = "Mohon perbarui data"
			self.lb_DataMaster_DataProyek_Penjab.setText("Penanggung Jawab: "+penjab)
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_Penjab, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_Penjab.show()
		except:
			self.lb_DataMaster_DataProyek_Penjab = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_Penjab.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Penjab"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Penjab, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			
			sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+str(data[field("kodePenjab")])+"'"
			try:
				penjab = str(self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
			except:
				penjab = "Mohon perbarui data"
			
			self.lb_DataMaster_DataProyek_Penjab.setText("Penanggung Jawab: "+penjab)
			self.lb_DataMaster_DataProyek_Penjab.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_Penjab.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12)
		
		#--------------------------------------------------------------------------------------------------------TMulai
		try:
			self.lb_DataMaster_DataProyek_TMulai.setText("Tanggal Mulai: "+str(data[field("tanggalMulai")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_TMulai, 2, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_TMulai.show()
		except:
			self.lb_DataMaster_DataProyek_TMulai = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_TMulai.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_TMulai"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_TMulai, 2, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_TMulai.setText("Tanggal Mulai: "+str(data[field("tanggalMulai")]))
			self.lb_DataMaster_DataProyek_TMulai.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_TMulai.setMaximumSize(QtCore.QSize(common_width, 22))
		
		
		#--------------------------------------------------------------------------------------------------------TSelesai
		try:
			self.lb_DataMaster_DataProyek_TSelesai.setText("Tanggal Selesai: "+str(data[field("tanggalSelesai")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_TSelesai, 3, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_TSelesai.show()
		except:
			self.lb_DataMaster_DataProyek_TSelesai = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_TSelesai.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_TSelesai"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_TSelesai, 3, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_TSelesai.setText("Tanggal Selesai: "+str(data[field("tanggalSelesai")]))
			self.lb_DataMaster_DataProyek_TSelesai.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_TSelesai.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------AnggaranTotal
		try:
			self.lb_DataMaster_DataProyek_AnggaranTotal.setText("Anggaran Total: "+str(data[field("anggaranTotal")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_AnggaranTotal, 2, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_AnggaranTotal.show()
		except:
			self.lb_DataMaster_DataProyek_AnggaranTotal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_AnggaranTotal.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_AnggaranTotal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_AnggaranTotal, 2, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_AnggaranTotal.setText("Anggaran Total: "+str(data[field("anggaranTotal")]))
			self.lb_DataMaster_DataProyek_AnggaranTotal.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_AnggaranTotal.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------RealisasiTotal
		try:
			self.lb_DataMaster_DataProyek_RealisasiTotal.setText("Realisasi Total: "+str(data[field("realisasiTotal")]))
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataProyek_RealisasiTotal, 3, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataProyek_RealisasiTotal.show()
		except:
			self.lb_DataMaster_DataProyek_RealisasiTotal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataProyek_RealisasiTotal.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_RealisasiTotal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_RealisasiTotal, 3, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataProyek_RealisasiTotal.setText("Realisasi Total: "+str(data[field("realisasiTotal")]))
			self.lb_DataMaster_DataProyek_RealisasiTotal.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataProyek_RealisasiTotal.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------Progress
		try:
			self.pb_DataMaster_DataProyek_Progress.setProperty("value", data[field("progress")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.pb_DataMaster_DataProyek_Progress, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.pb_DataMaster_DataProyek_Progress.show()
		except:
			self.pb_DataMaster_DataProyek_Progress = QtGui.QProgressBar(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.pb_DataMaster_DataProyek_Progress.setProperty("value", data[field("progress")])
			self.pb_DataMaster_DataProyek_Progress.setObjectName(_fromUtf8("pb_DataMaster_DataProyek_Progress"))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.pb_DataMaster_DataProyek_Progress, 0, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.pb_DataMaster_DataProyek_Progress.setMinimumSize(QtCore.QSize(100, 22))
			self.pb_DataMaster_DataProyek_Progress.setMaximumSize(QtCore.QSize(100, 22))
			
			#~ self.lb_DataMaster_DataProyek_Progress = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			#~ self.lb_DataMaster_DataProyek_Progress.setObjectName(_fromUtf8("lb_DataMaster_DataProyek_Progress"))
			#~ self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataProyek_Progress, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			#~ self.lb_DataMaster_DataProyek_Progress.setText(data[field("kodeProgress")])
			#~ self.lb_DataMaster_DataProyek_Progress.setMinimumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Progress.setMaximumSize(QtCore.QSize(common_width, 22))
			#~ self.lb_DataMaster_DataProyek_Kode.setFont(f12)
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProyek_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProyek_FGraph.show()
				#~ print "no rebuild"
				
		except:
			self.fr_DataMaster_DataProyek_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataProyek_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataProyek_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataProyek_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataProyek_FGraph"))
			self.fr_DataMaster_DataProyek_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataProyek_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataProyek_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataProyek_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataProyek_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataProyek_FGraph)
			self.ihl_DataMaster_DataProyek_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataProyek_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataProyek_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataProyek_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					"<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					"<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataProyek_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataProyek_FGraph)
			self.svg_DataMaster_DataProyek_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataProyek_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			
		self.DataMaster_CommonRoom_cleared = 0
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataProyek_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataProyek_Delete,500,200,None,None))
	
	
	def DataMaster_DataProyek_Edit(self):
		field = self.DataMaster_DataProyek_Field.index
		kode = str(self.lb_DataMaster_DataProyek_Kode.text()).replace("\n","")
		sql = "SELECT * FROM `gd_proyek` WHERE `kodeProyek` = '"+kode+"' LIMIT 0 , 1"
		proyek = self.DatabaseRunQuery(sql)[0]
		
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setText(_fromUtf8(kode))
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setReadOnly(True)
		self.le_DataMaster_DataProyek_Tambah_NamaProyek.setText(proyek[field("namaProyek")])
		self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.setText(proyek[field("kodePenjab")])
		sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+proyek[field("kodePenjab")]+"'"
		try:
			penjab = self.DatabaseRunQuery(sql)[0][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]
		except:
			penjab = "Mohon perbarui data"
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setText(penjab)
		self.dsb_DataMaster_DataProyek_Tambah_Progress.setValue(float(proyek[field("progress")]))
		self.dte_DataMaster_DataProyek_Tambah_TanggalMulai.setDateTime(QDateTime.fromString(str(proyek[field("tanggalMulai")]),"yyyy-MM-dd hh:mm:ss"))
		self.dte_DataMaster_DataProyek_Tambah_TanggalSelesai.setDateTime(QDateTime.fromString(str(proyek[field("tanggalSelesai")]),"yyyy-MM-dd hh:mm:ss"))
		self.le_DataMaster_DataProyek_Tambah_AnggaranTotal.setText(str(proyek[field("anggaranTotal")]))
		self.le_DataMaster_DataProyek_Tambah_RealisasiTotal.setText(str(proyek[field("realisasiTotal")]))
		self.chk_DataMaster_DataProyek_Tambah_PakaiFase.setCheckState(	int(proyek[field("isFase")])*2	)
		self.DataMaster_DataProyek_Edit_idEDIT = proyek[field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAPROYEK_TAMBAH)
		
		
	def DataMaster_DataProyek_Delete(self):
		kode = str(self.lb_DataMaster_DataProyek_Kode.text()).replace("\n","")
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_proyek` WHERE `gd_proyek`.`kodeProyek` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPROYEK)
	
	
	def DataMaster_DataProyek_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataProyek_Tambah_KodeProyek, 
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_proyek` ORDER BY `gd_proyek`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<6):
			kode_default = "0"+kode_default
		kode_default = "PROYEK" + "."+kode_default
		self.le_DataMaster_DataProyek_Tambah_KodeProyek.setText(kode_default)
		
	def DataMaster_DataSatuanPengukuran_Tambah_Act_Simpan(self):
		kode = str(self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.text())
		nama = str(self.le_DataMaster_DataSatuanPengukuran_Tambah_NamaSatuan.text())
		ket = str(self.le_DataMaster_DataSatuanPengukuran_Tambah_Keterangan.text())
		induk=str(self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.currentText())
		induk = ("NULL" if induk=="Tanpa Induk" else (induk[induk.find("(kode: ")+len("(kode: "):-1] ))
		#~ print induk
		faktor=str(self.dsb_DataMaster_DataSatuanPengukuran_Tambah_FaktorPengali.value())
		
		sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_satuan_pengukuran`"+\
			" (`id`, `kodeSatuan`, `namaSatuan`, `keterangan`, `faktorPengali`, `kodeSatuanParent`) "+\
			"VALUES (NULL, '"+kode+"', '"+nama+"', '"+ket+"', "+faktor+", '"+induk+"');"
		self.DatabaseRunQuery(sql)
		
		self.cb_DataMaster_DataProduk_Tambah_Satuan.clear()
		self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.clear()
		self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.addItem("Tanpa Induk")
		sql = "SELECT * FROM `gd_satuan_pengukuran` "
		result = self.DatabaseRunQuery(sql)
		for a in range(0,len(result)):
			#-----------------------------------------------------------Untuk data produk
			self.cb_DataMaster_DataProduk_Tambah_Satuan.addItem(str(result[a][2])+" (kode: "+result[a][1]+")") 
			self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.addItem(str(result[a][2])+" (kode: "+result[a][1]+")") 
		
		self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setReadOnly(False) #---set kode ke Read Only dulu, set to false on _Act_Simpan
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN)
	
	def DataMaster_DataSatuanPengukuran_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuanPengukuran, 
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_satuan_pengukuran` ORDER BY `gd_satuan_pengukuran`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		kode_default = str(int(result[0][0])+1)
		while (len(kode_default)<6):
			kode_default = "0"+kode_default
		kode_default = "UNIT" + "."+kode_default
		self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setText(kode_default)
		
	def DataMaster_DataSatuanPengukuran_Delete(self):
		kode = str(self.lb_DataMaster_DataSatuanPengukuran_Kode.text()).replace("\n","")
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_satuan_pengukuran` WHERE `gd_satuan_pengukuran`.`kodeSatuan` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN)
	
	def DataMaster_DataSatuanPengukuran_Edit(self):
		field = self.DataMaster_DataSatuanPengukuran_Field.index
		kode = str(self.lb_DataMaster_DataSatuanPengukuran_Kode.text()).replace("\n","")
		sql = "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+kode+"' LIMIT 0 , 1"
		satuan = self.DatabaseRunQuery(sql)[0]
		self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setText(str(kode))
		self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setReadOnly(True) #---set kode ke Read Only dulu, set to false on _Act_Simpan
		self.le_DataMaster_DataSatuanPengukuran_Tambah_NamaSatuan.setText(str(satuan[field("namaSatuan")]))
		self.le_DataMaster_DataSatuanPengukuran_Tambah_Keterangan.setText(str(satuan[field("keterangan")]))
		
		sql = "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+str(satuan[field("kodeSatuanParent")])+"' LIMIT 0 , 1"
		bapak = self.DatabaseRunQuery(sql)
		if len(bapak)>0:
			bapak = bapak[0]
			bapak = str(bapak[field("namaSatuan")])+" (kode: "+str(satuan[field("kodeSatuanParent")])+")"
		else:
			bapak = "Tanpa Induk"
		self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.setCurrentIndex(self.cb_DataMaster_DataSatuanPengukuran_Tambah_SatuanInduk.findText(_fromUtf8(bapak)))
		self.dsb_DataMaster_DataSatuanPengukuran_Tambah_FaktorPengali.setValue(float(		satuan[	field("faktorPengali")	]	))
		
		self.DataMaster_DataSatuanPengukuran_Edit_idEDIT = satuan[field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN_TAMBAH)
		
	
	def DataMaster_DataSatuanPengukuran_DrawInfo(self,data):
		field = self.DataMaster_DataSatuanPengukuran_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		common_width = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()/3
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setText(data[field("namaSatuan")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataSatuanPengukuran_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataSatuanPengukuran_Nama.show()
		except:
			self.lb_DataMaster_DataSatuanPengukuran_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataSatuanPengukuran_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataSatuanPengukuran_Nama, 0, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setText(data[field("namaSatuan")])
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setMaximumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataSatuanPengukuran_Nama.setFont(f14)
		
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			self.lb_DataMaster_DataSatuanPengukuran_Kode.setText(data[field("kodeSatuan")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataSatuanPengukuran_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataSatuanPengukuran_Kode.show()
		except:
			self.lb_DataMaster_DataSatuanPengukuran_Kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataSatuanPengukuran_Kode.setObjectName(_fromUtf8("lb_DataMaster_DataSatuanPengukuran_Kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataSatuanPengukuran_Kode, 1, 0, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataSatuanPengukuran_Kode.setText(data[field("kodeSatuan")])
			self.lb_DataMaster_DataSatuanPengukuran_Kode.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataSatuanPengukuran_Kode.setMaximumSize(QtCore.QSize(common_width, 22))
		#--------------------------------------------------------------------------------------------------------Keterangan
		try:
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan.setText(data[field("keterangan")])
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataSatuanPengukuran_Keterangan, 2, 0, 2, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataSatuanPengukuran_Keterangan.show()
		except:
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan.setObjectName(_fromUtf8("lb_DataMaster_DataSatuanPengukuran_Keterangan"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataSatuanPengukuran_Keterangan, 2, 0, 2, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan.setText(data[field("keterangan")])
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataSatuanPengukuran_Keterangan.setMaximumSize(QtCore.QSize(common_width, 22))
			
		#--------------------------------------------------------------------------------------------------------Induk
		sql = "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+str(data[field("kodeSatuanParent")])+"' LIMIT 0 , 1"
		bapak = self.DatabaseRunQuery(sql)
		if len(bapak)>0:
			bapak = bapak[0]
			bapak =  "Induk dan Pengali: ("+str(data[field("faktorPengali")])+") x " + str(bapak[field("namaSatuan")])
		else:
			bapak = "Tanpa Induk"
		try:
			self.lb_DataMaster_DataSatuanPengukuran_Induk.setText(bapak)
			if (self.DataMaster_CommonRoom_cleared==1):
				self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.lb_DataMaster_DataSatuanPengukuran_Induk, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataSatuanPengukuran_Induk.show()
		except:
			self.lb_DataMaster_DataSatuanPengukuran_Induk = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataSatuanPengukuran_Induk.setObjectName(_fromUtf8("lb_DataMaster_DataSatuanPengukuran_Induk"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataSatuanPengukuran_Induk, 1, 1, 1, 1,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
			
			self.lb_DataMaster_DataSatuanPengukuran_Induk.setText(bapak)
			self.lb_DataMaster_DataSatuanPengukuran_Induk.setMinimumSize(QtCore.QSize(common_width, 22))
			self.lb_DataMaster_DataSatuanPengukuran_Induk.setMaximumSize(QtCore.QSize(common_width, 22))
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.fr_DataMaster_DataSatuanPengukuran_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.show()
		except:
			self.fr_DataMaster_DataSatuanPengukuran_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataSatuanPengukuran_FGraph"))
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.fr_DataMaster_DataSatuanPengukuran_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataSatuanPengukuran_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataSatuanPengukuran_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataSatuanPengukuran_FGraph)
			self.ihl_DataMaster_DataSatuanPengukuran_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataSatuanPengukuran_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataSatuanPengukuran_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataSatuanPengukuran_FGraph"))
			
			svgW = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().width()-100
			svgH = self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.frameGeometry().height()/2
			#~ svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					#~ "<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#444444; fill: #ffffff'/>"+\
					#~ "<rect x='"+str(10+0*svgW/6)+"' y='"+str(-10+svgH-100)+"' height='100' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
					#~ "<rect x='"+str(10+1*svgW/6)+"' y='"+str(-10+svgH-200)+"' height='200' width='80' style='stroke:#ff0000; fill: #CBCBFD'/>"+\
				#~ "</svg>"
			svg = "<svg  xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink'>"+\
					"<rect x='0' y='0' height='"+str(svgH)+"' width='"+str(svgW)+"' style='stroke:#F7F7F7; fill: #ffffff'/>"+\
				"</svg>"
			f = open("./img/DataMaster_svg.svg","w")
			f.write(svg)
			f.close()
			
			self.svg_DataMaster_DataSatuanPengukuran_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataSatuanPengukuran_FGraph)
			self.svg_DataMaster_DataSatuanPengukuran_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataSatuanPengukuran_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			
		self.DataMaster_CommonRoom_cleared = 0
		try:
			self.tb_DataMaster_DataCommon_Delete.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataSatuanPengukuran_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataSatuanPengukuran_Delete,500,200,None,None))
		
	
	
	#show list DataProyek
	def DataMaster_DataProyek_Tambah_Showlist(self):
		self.sc_DataMaster_DataProyek_Tambah_Penjab.show()
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setPlaceholderText("Type to search")
		
	def DataMaster_DataProyek_Tambah_Showlist_Change(self):
		self.lb_DataMaster_DataProyek_Tambah_PilihPenjab.show()
		self.sc_DataMaster_DataProyek_Tambah_Penjab.show()
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setPlaceholderText("Type to search")
		#~ self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setCompleter(
		
		if self.sc_DataMaster_DataProyek_Tambah_Penjab.isVisible():
			self.clearLayout(self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0])
			self.initDatabase()
			cursor = self.db.cursor()
			if str(self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.text()) != "":
				self.clearLayout(self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0])
				sql = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '%"+str(self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.text())+"%' "
			else:
				sql = "SELECT * FROM `gd_nama_alamat` "
			cursor.execute(sql)
			result = cursor.fetchall()
			for x in range(0,len(result)):
				Button = self.findChildren(QtGui.QPushButton,"tb_DataMaster_DataProyek_Penjab_Find"+str(x))
				if len(Button)<1:
					Button = QtGui.QPushButton(self.scontent_DataMaster_DataProyek_Tambah_Penjab)
					local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
					Button.setObjectName(_fromUtf8("tb_DataMaster_DataProyek_Penjab_Find"+str(x)))
					Button.setText(local_name)
					self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0].addWidget(Button,(QtCore.Qt.AlignTop | QtCore.Qt.AlignTop))
					Button.clicked.connect(functools.partial(self.DataMaster_DataProyek_Tambah_Showlist_Selected,result[x]))
				else:
					Button = Button[0]
					local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
					Button.setText(local_name)
					self.scontent_DataMaster_DataProyek_Tambah_Penjab.findChildren(QtGui.QVBoxLayout)[0].addWidget(Button,(QtCore.Qt.AlignTop | QtCore.Qt.AlignTop))
					Button.clicked.disconnect()
					Button.clicked.connect(functools.partial(self.DataMaster_DataProyek_Tambah_Showlist_Selected,result[x]))
					Button.show()
			self.db.close()
		#~ self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.
	
	def DataMaster_DataProyek_Tambah_Showlist_Selected(self,data):
		self.le_DataMaster_DataProyek_Tambah_PenanggungJawab.setText(data[self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
		self.le_DataMaster_DataProyek_Tambah_KodePenanggungJawab.setText(data[self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")])
	
		
	
	def DataMaster_DataNamaAlamat_Tambah_JatuhTempoSet(self):
		self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setReadOnly(False) if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()>0) else self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setReadOnly(True)
	
	def DataMaster_DataNamaAlamat_Tambah_Tipe_Change(self):
		t = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		cb = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText()).upper()
		aa = t.replace("EMPLOYEE",cb)
		aa = aa.replace("VENDOR",cb)
		aa = aa.replace("CUSTOMER",cb)
		aa = aa.replace("OTHER",cb)
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(_fromUtf8(aa))
	
	def DataMaster_DataNamaAlamat_Popup_Tambah(self, fcallback_ok=None,fcallback_cancel=None,fcallback_enter=None,fcallback_exit=None):
		"""
		Tampilkan popup untuk menambah DataNamaAlamat
		fcallback_enter dieksekusi sebelum membangun popup, (A)
		fcallback_ok dieksekusi jika ok di klik pada popup (B)
		fcallback_cancel diekseskusi jika cancel/close diklik pada popup (B)
		fcallback_exit dieksekusi saat fungsi selesai (C)
		"""
		if fcallback_enter==None or fcallback_enter==False:
			fcallback_enter = self.DataMaster_None
		if fcallback_cancel==None or fcallback_cancel==False:
			fcallback_cancel = self.DataMaster_None
		if fcallback_ok==None or fcallback_ok==False:
			fcallback_ok = self.DataMaster_None
		if fcallback_exit==None or fcallback_exit==False:
			fcallback_exit = self.DataMaster_None
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		fcallback_enter() #-----A
		def exit_function():
			self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(None)
			self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(self.st_DataMaster_DataNamaAlamat_Tambah)
			self.ivl_DataMaster_DataNamaAlamat_Tambah_Luar.addWidget(self.fr_DataMaster_DataNamaAlamat_Tambah)
			self.fr_DataMaster_DataNamaAlamat_Tambah_Fbot.show()
			fcallback_exit() #-----(C)
			
		self.DataMaster_DataNamaAlamat_Tambah_GenerateKode()
		self.DataMaster_Popup("",functools.partial(self.DataMaster_DataNamaAlamat_Popup_Act_Tambah,fcallback_ok),WinW-10,WinH-200,exit_function,fcallback_cancel) #----B
		
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(FrameWindow)
		self.fr_DataMaster_DataNamaAlamat_Tambah.show()
		self.fr_DataMaster_DataNamaAlamat_Tambah.setGeometry(QtCore.QRect(5,5,WinW-20,WinH-250))
		self.fr_DataMaster_DataNamaAlamat_Tambah_Fbot.hide()
		
	def DataMaster_DataNamaAlamat_Popup_Act_Tambah(self,fcallback_exit):
		
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(False)
		nama = str(self.le_DataMaster_DataNamaAlamat_Tambah_Nama.text())
		tipe = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText())
		npwp = str(self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.text())
		diskon = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.value())
		jatuhtempo = ("0000-00-00 00:00:00" if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()==0) else str(self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.dateTime().toString("yyyy-MM-dd hh:mm:ss")) )
		diskonawal = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.value())
		dendaketerlambatan = str(self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.text())
		alamat = str(self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.text())
		kodepelanggan = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		kontak = str(self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.text())
		sql = ""
		if (self.DataMaster_DataNamaAlamat_Edit_idEDIT >=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
			"SET `namaPelanggan` = '"+nama+"',"+\
				"`kodePelanggan` = '"+kodepelanggan+"',"+\
				"`tipe` = '"+tipe+"',"+\
				"`npwp` = '"+npwp+"',"+\
				"`diskon` = '"+diskon+"',"+\
				"`jatuhTempo` = '"+jatuhtempo+"',"+\
				"`diskonAwal` = '"+diskonawal+"',"+\
				"`dendaKeterlambatan` = '"+dendaketerlambatan+"',"+\
				"`alamat` = '"+alamat+"',"+\
				"`kontak` = '"+kontak+"'"+\
			"WHERE `gd_nama_alamat`.`id`='"+str(self.DataMaster_DataNamaAlamat_Edit_idEDIT)+"'"
			self.DataMaster_DataNamaAlamat_Edit_idEDIT = -1
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
				"(`id`, `kodePelanggan`, `namaPelanggan`, `tipe`, `npwp`, `diskon`, `jatuhTempo`, `diskonAwal`, `dendaKeterlambatan`, `alamat`, `kontak`)"+\
				"VALUES "+\
				"(NULL, '"+kodepelanggan+"', '"+nama+"', '"+tipe+"', '"+npwp+"', '"+diskon+"', '"+jatuhtempo+"', '"+diskonawal+"', '"+dendaketerlambatan+"', '"+alamat+"', '"+kontak+"');"
		self.DatabaseRunQuery(sql)
		fcallback_exit()
		return
	
	def DataMaster_DataNamaAlamat_Edit(self):
		field = self.DataMaster_DataNamaAlamat_Field.index
		kode = str(self.lb_DataMaster_DataNamaAlamat_kode.text()).replace("\n","")
		sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+kode+"' LIMIT 0 , 1"
		barang = self.DatabaseRunQuery(sql)
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(_fromUtf8(barang[0][field("kodePelanggan")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(True)
		self.le_DataMaster_DataNamaAlamat_Tambah_Nama.setText(_fromUtf8(barang[0][field("namaPelanggan")]))
		self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.setCurrentIndex(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.findText(_fromUtf8(barang[0][field("tipe")])))
		self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.setText(_fromUtf8(barang[0][field("kontak")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.setText(_fromUtf8(barang[0][field("npwp")]))
		self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.setValue((barang[0][field("diskon")]))
		self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.setValue((barang[0][field("diskonAwal")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.setText(_fromUtf8(str(barang[0][field("dendaKeterlambatan")])))
		self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.setText(_fromUtf8(barang[0][field("alamat")]))
		self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setCheckState((0 if (str(barang[0][field("jatuhtempo")])=="None") else 2))
		self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setDateTime(QDateTime.fromString(str(barang[0][field("jatuhtempo")]),"yyyy-MM-dd hh:mm:ss"))
		self.DataMaster_DataNamaAlamat_Edit_idEDIT = barang[0][field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT_TAMBAH)
		
	def DataMaster_Popup(self,text,function_callback,FW=500,FH=200,function_exit=None,function_close=None,hide_surrounding=False):
		#~ print FW
		#~ print FH
		#~ print function_exit
		#~ print function_close
		if (FW == False):
			FW = 500
		if (FH == False):
			FH = 500
		if function_exit==False:
			function_exit = self.DataMaster_None
		if function_close==False:
			function_close = self.DataMaster_None
			
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		if (function_close==None):
			function_close = self.DataMaster_None
		if (function_exit==None):
			function_exit = self.DataMaster_None
		#~ ConfirmClose.clicked.connect(function_exit) if (function_exit!=None) else None
		#~ FW = 500
		#~ FH = 200
		if (hide_surrounding):
			FrameWindowH = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindowH"))
			if (len(FrameWindowH)<1):
				FrameWindowH = QtGui.QFrame(self.centralwidget)
			else:
				FrameWindowH = FrameWindowH[0]
			FrameWindowH.setGeometry(QtCore.QRect(0, 0, WinW+20, WinH+20))
			FrameWindowH.setObjectName(_fromUtf8("DataMaster_Popup_FrameWindowH"))
			FrameWindowH.setStyleSheet(_fromUtf8("QFrame{background:#E3EFE8;border-radius:0px;border-style: solid;border-width: 2px;border-color:#828282;}"))
			FrameWindowH.show()
		
		FrameWindowS = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindowS"))
		if (len(FrameWindowS)<1):
			FrameWindowS = QtGui.QFrame(self.centralwidget)
		else:
			FrameWindowS = FrameWindowS[0]
		FrameWindowS.setGeometry(QtCore.QRect((WinW/2)-FW/2+10, WinH/2- FH/2+10, FW, FH))
		FrameWindowS.setObjectName(_fromUtf8("DataMaster_Popup_FrameWindowS"))
		FrameWindowS.setStyleSheet(_fromUtf8("QFrame{background:#828282;border-radius:0px;border-style: solid;border-width: 2px;border-color:#828282;}"))
		FrameWindowS.show()
		
		FrameWindow = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		if (len(FrameWindow)<1):
			FrameWindow = QtGui.QFrame(self.centralwidget)
		else:
			FrameWindow = FrameWindow[0]
		FrameWindow.setGeometry(QtCore.QRect((WinW/2)-FW/2, WinH/2- FH/2, FW, FH))
		FrameWindow.setObjectName(_fromUtf8("DataMaster_Popup_FrameWindow"))
		FrameWindow.setStyleSheet(_fromUtf8("QFrame{background:#ffffff;border-radius:0px;border-style: solid;border-width: 2px;border-color:#868686;}"))
		FrameWindow.show()
		
		Label = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_Label"))
		if (len(Label)<1):
			Label = QtGui.QLabel(FrameWindow)
		else:
			Label = Label[0]
		Label.setGeometry(QtCore.QRect(10, 10, FW-20, FH-20))
		Label.setObjectName(_fromUtf8("DataMaster_Popup_Label"))
		Label.setText(_fromUtf8(text))
		Label.setStyleSheet(_fromUtf8("QFrame{background:#ffffff;border-radius:0px;border-style: solid;border-width: 0px;border-color:#ffffff;}"))
		Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter)
		Label.show()
		
		ConfirmOk = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_ConfirmOk"))
		if (len(ConfirmOk)<1):
			ConfirmOk = QtGui.QPushButton(FrameWindow)
			ConfirmOk.setGeometry(QtCore.QRect(FW/2-42-85, FH-45, 85, 30))
			ConfirmOk.setObjectName(_fromUtf8("DataMaster_Popup_ConfirmOk"))
			ConfirmOk.setText(_fromUtf8("Ok"))
			ConfirmOk.setStyleSheet(_fromUtf8("QPushButton{background:#555555;color:white;}"))
		else:
			ConfirmOk = ConfirmOk[0]
		try:
			ConfirmOk.clicked.disconnect()
		except:
			pass
		#~ def tutup(f):
			#~ f.close()
		tutup = lambda fr: fr.close()
		ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindow))
		ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindowS))
		if (hide_surrounding):
			ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindowH))
		ConfirmOk.clicked.connect(function_callback)
		ConfirmOk.clicked.connect(function_exit)
		ConfirmOk.show()
		
		ConfirmClose = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_ConfirmClose"))
		if (len(ConfirmClose)<1):
			ConfirmClose = QtGui.QPushButton(FrameWindow)
			ConfirmClose.setGeometry(QtCore.QRect(FW/2-42+85, FH-45, 85, 30))
			ConfirmClose.setObjectName(_fromUtf8("DataMaster_Popup_ConfirmClose"))
			ConfirmClose.setText(_fromUtf8("Cancel"))
			ConfirmClose.setStyleSheet(_fromUtf8("QPushButton{background:#555555;color:white;}"))
		else:
			ConfirmClose = ConfirmClose[0]
		ConfirmClose.show()
		ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindow))
		ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindowS))
		if (hide_surrounding):
			ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindowH))
		ConfirmClose.clicked.connect(function_close)
		ConfirmClose.clicked.connect(function_exit)
		#execute exit function if any
		#~ if (function_exit!=None
		#~ function_exit() if (function_exit!=None) else None
		#~ aa = raw_input()
	
	def DataMaster_DataNamaAlamat_Delete(self):
		kode = str(self.lb_DataMaster_DataNamaAlamat_kode.text()).replace("\n","")
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_nama_alamat` WHERE `gd_nama_alamat`.`kodePelanggan` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT)
	
	
	def initDatabase(self):
		self.dbHost = "127.0.0.1"
		self.dbPort = 44559
		self.dbDatabase = "gd_db_akunting"
		self.dbPass = "nyungsep"
		self.dbUser = "gd_user_akunting"
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



	#------------------------------------------------------------------- Buku Besar
	#------------------------------------------------------------------- Buku Besar
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
				self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.item(r,4).setText(str(result[r][field("kredit")]))
		
		try:
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellClicked.disconnect()
		except:
			pass
		try:
			self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.disconnect()
		except:
			pass
		self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked.connect(self.BukuBesar_DaftarTransaksiJurnal_PilihRekening)
		
		
		return
	
	def BukuBesar_DaftarTransaksiJurnal_PilihRekening(self,row,column):
		
		self.DataMaster_DataRekening_Popup_Pilih()
		
	
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
	
if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	dmw = MainGUI()
	dmw.showFullScreen()
	sys.exit(app.exec_())
