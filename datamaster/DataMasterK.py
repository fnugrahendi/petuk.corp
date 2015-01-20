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

from DataDepartemen import DataDepartemen
from DataNamaAlamat import DataNamaAlamat
from DataProyek import DataProyek

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class DataMaster(DataDepartemen,DataNamaAlamat,DataProyek):
	def DataMaster_init(self, parent=None):
		
		super(DataMaster,self).__init__(parent)
		
		self.DataMaster_Focus = QtGui.QFocusEvent(QEvent.FocusIn)
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
		self.INDEX_ST_DATAMASTER_DATADEPARTEMEN = 9
		self.INDEX_ST_DATAMASTER_DATADEPARTEMEN_TAMBAH = 10
		
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
		#~ self.ile_DataMaster_DataProyek_Tambah_PenanggungJawab.hide()
		
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
		self.tb_DataMaster_DataRekening_Tutup.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_MENU))
		
		self.tb_DataMaster_DataDepartemen.clicked.connect				(self.DataMaster_DataDepartemen)
		
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
		#Get Field gd_rekening_jurnal
		sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_data_departemen';"
		cursor.execute(sql)
		result = cursor.fetchall()
		self.DataMaster_DataDepartemen_Field = list(itertools.chain.from_iterable(result))
		self.db.close()
		
		self.DataMaster_CommonRoom_cleared = 0
		
	#-------------------------------------------------------------------DataMaster
	#-------------------------------------------------------------------DataMaster
	def DataMaster_None(self):
		pass
	
	def DataMaster_Goto(self,goto_roomID):
		self.st_DataMaster.setCurrentIndex(goto_roomID)
	
	def DataMaster_Menu(self):
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_MENU)
		
	def DataMaster_Goto_Common(self,as_roomID,keep=False):
		self.st_DataMaster.setCurrentIndex(self.INDEX_ST_DATAMASTER_COMMON)
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		self.clearGrid(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0])
		
		self.GarvinDisconnect(self.le_DataCommon_Search.textChanged.connect)
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
			self.le_DataCommon_Search.setText("")
			self.le_DataCommon_Search.textChanged.connect(self.DataMaster_DataNamaAlamat_RefreshList)
			
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
				obj_Tb_ListPelanggan = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataNamaAlamat_ListNamaAlamat"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]))
				if (len(obj_Tb_ListPelanggan)<1):
					obj_Tb_Pelanggan = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					obj_Tb_Pelanggan.setObjectName(_fromUtf8("dtb_DataMaster_DataNamaAlamat_ListNamaAlamat"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])))
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
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(self.DataMaster_DataProyek_Tambah)
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
		
		elif (as_roomID==self.INDEX_ST_DATAMASTER_DATADEPARTEMEN):
			def DataDepartemen():
				""""Bookmark baris, delete this later"""
				None
			self.lb_DataMaster_DataCommon_Judul.setText("Data Departemen ")
			self.tb_DataMaster_DataCommon_Tambah.clicked.connect(functools.partial(self.DataMaster_Goto,self.INDEX_ST_DATAMASTER_DATADEPARTEMEN_TAMBAH))
			self.tb_DataMaster_DataCommon_Edit.clicked.connect(self.DataMaster_DataDepartemen_Edit)
			self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
			#~ self.le_DataMaster_DataDepartemen_Tambah_KodeDepartemen.setReadOnly(False)
			#~ if (not keep):
				#~ """Kosongkan isi line edit"""
				#~ lels = self.fr_DataMaster_DataDepartemen_Tambah_Fcontent.findChildren(QtGui.QLineEdit)
				#~ for x in range(0,len(lels)):
					#~ lels[x].setText("")
			
			#~ self.DataMaster_DataDepartemen_Tambah_GenerateKode()
			
			sql = "SELECT * FROM `gd_data_departemen` "
			result = self.DatabaseRunQuery(sql)
			tinggi = len(result)*65
			self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
			for x in range(0,len(result)):
				Tb_ListDepartemen = self.findChildren(QtGui.QPushButton,"dynamic_tb_DataMaster_DataDepartemen_List"+str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")]))
				if (len(Tb_ListDepartemen)<1):
					Tb_Departemen = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
					Tb_Departemen.setObjectName(_fromUtf8("dynamic_tb_DataMaster_DataDepartemen_ListDepartemen"+str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")])))
					local_name = str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")])
					Tb_Departemen.setText(local_name)
					self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_Departemen,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_Departemen.clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
				else:
					for y in range(0, len(Tb_ListDepartemen)):
						self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_ListDepartemen[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
						Tb_ListDepartemen[y].show()
						Tb_ListDepartemen[y].setText(str(result[x][self.DataMaster_DataDepartemen_Field.index("namaDepartemen")]))
						Tb_ListDepartemen[y].clicked.disconnect()
						Tb_ListDepartemen[y].clicked.connect(functools.partial(self.DataMaster_DataDepartemen_DrawInfo,result[x]))
		
		
	
	def DataMaster_DataRekening_RefreshInfo(self):
		#---got to clear table first
		for r in range(0,self.tbl_DataMaster_DataRekening_Fcontent_LRekening.rowCount()+1):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.removeRow(r)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(0)
		
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		for row in range(0,len(result)):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.insertRow(row)
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
	def DataMaster_DataRekening(self):
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAREKENING)
		
		#---got to clear table first
		for r in range(0,self.tbl_DataMaster_DataRekening_Fcontent_LRekening.rowCount()+1):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.removeRow(r)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.setRowCount(0)
		
		sql = "SELECT * FROM `gd_rekening_jurnal` ORDER BY `gd_rekening_jurnal`.`noAkun` ASC;"
		result = self.DatabaseRunQuery(sql)
		for row in range(0,len(result)):
			self.tbl_DataMaster_DataRekening_Fcontent_LRekening.insertRow(row)
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
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked.connect(_SetActiveIndex)
		#---Sinyal tombol tambah
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah.clicked)
		self.tb_DataMaster_DataRekening_Tambah.clicked.connect(self.DataMaster_DataRekening_Tambah)
		#---Sinyal tombol hapus
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Delete.clicked)
		self.tb_DataMaster_DataRekening_Delete.clicked.connect(self.DataMaster_DataRekening_Delete)
		#---tombol edit
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Edit.clicked)
		#--- confirmasi edit
		self.tb_DataMaster_DataRekening_Edit.clicked.connect(functools.partial(self.DataMaster_Popup,"Edit nomor rekening jurnal ini? Hanya lanjutkan bila anda faham apa yang anda lakukan!",self.DataMaster_DataRekening_Edit))
	
	def DataMaster_DataRekening_Tambah(self):
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATAREKENING_TAMBAH)
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah_Batal.clicked)
		self.tb_DataMaster_DataRekening_Tambah_Batal.clicked.connect(self.DataMaster_DataRekening)
		self.GarvinDisconnect(self.tb_DataMaster_DataRekening_Tambah_Simpan.clicked)
		self.tb_DataMaster_DataRekening_Tambah_Simpan.clicked.connect(self.DataMaster_DataRekening_Tambah_Act_Simpan)
		pass
		
	def DataMaster_DataRekening_Tambah_Act_Simpan(self):
		nomor = str(self.le_DataMaster_DataRekening_NomorAkun.text())
		nama = str(self.le_DataMaster_DataRekening_NamaAkun.text())
		namaalias = str(self.le_DataMaster_DataRekening_NamaAliasAkun.text())
		jadi = False
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			jadi = self.DatabaseInsertAvoidreplace(self.dbDatabase,"gd_rekening_jurnal","noAkun",nomor,
											["noAkun","namaAkun","namaAliasAkun"],
											[nomor,nama,namaalias],
											"Penyimpanan tidak dapat dilakukan karena telah terdapat nomor akun yang sama!",
											self.DataMaster_DataRekening_Tambah)
		else:
			jadi = self.DatabaseInsertReplace(self.dbDatabase,"gd_rekening_jurnal","id",self.DataMaster_DataRekening_Edit_idEDIT,
											["noAkun","namaAkun","namaAliasAkun"],
											[nomor,nama,namaalias])
		if (jadi):
			#---sukses Kembali ke room DataRekening
			self.DataMaster_DataRekening()
			self.DataMaster_DataRekening_Edit_idEDIT = -1
		#----bila tidak sukses, bertahan di room tambah
		pass
	
	def DataMaster_DataRekening_Edit(self):
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			return
		data = self.DatabaseRunQuery("SELECT * FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
		if len(data)<0:
			return
		
		self.le_DataMaster_DataRekening_NomorAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("noAkun")]))
		self.le_DataMaster_DataRekening_NamaAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("namaAkun")]))
		self.le_DataMaster_DataRekening_NamaAliasAkun.setText(str(data[0][self.DataMaster_DataRekening_Field.index("namaAliasAkun")]))
		self.DataMaster_DataRekening_Tambah()
	
	def DataMaster_DataRekening_Delete(self):
		if (self.DataMaster_DataRekening_Edit_idEDIT<0):
			return
		def _CommitDelete():
			self.DatabaseRunQuery("DELETE FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
			self.DataMaster_DataRekening_RefreshInfo()
		data = self.DatabaseRunQuery("SELECT * FROM `gd_rekening_jurnal` WHERE `id` = "+str(self.DataMaster_DataRekening_Edit_idEDIT)+" ;")
		if len(data)<0:
			return
		self.DataMaster_Popup("Anda yakin akan menghapus rekening "+str(data[0][self.DataMaster_DataRekening_Field.index("noAkun")])+"?\n\n"+\
								"Lanjutkan hapus hanya bila anda mengerti apa yang anda lakukan!",
								_CommitDelete)
		
	def DataMaster_DataRekening_Popup_Pilih(self,fcb_ok=False,fcb_cancel=False):
		"Tunjukkan Popup untuk memilih data rekening, hasil disimpen ke variabel public self.DataMaster_DataRekening_RekeningTerpilih"
		if fcb_ok==False:
			fcb_ok = self.DataMaster_None
		if fcb_cancel==False:
			fcb_cancel = self.DataMaster_None
		
		CNOMOR_REKENING = 0
		CNAMA_REKENING = 1
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
		
		
		def kembalikan():
			#----Kembalikan, dan disconnect sinyal dilakukan di BukuBesar_DaftarTransaksiJurnal_PilihRekening.ubahcell instead
			self.fr_DataMaster_DataRekening.setParent(self.st_DataMaster_DataRekening)
			self.ivl_DataMaster_DataRekening_Luar.addWidget(self.fr_DataMaster_DataRekening)
			self.fr_DataMaster_DataRekening_Fb.show()
			
		#---------------------------------------------------------------Panggil Popup disini
		self.DataMaster_Popup("",fcb_ok,650,WinH-200,kembalikan,fcb_cancel,True)
		
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		
		self.fr_DataMaster_DataRekening.setParent(FrameWindow)
		self.fr_DataMaster_DataRekening.show()
		self.fr_DataMaster_DataRekening.setGeometry(QtCore.QRect(5,5,640,WinH-250))
		self.fr_DataMaster_DataRekening_Fb.hide()
		self.DataMaster_DataRekening_RekeningTerpilih = ["",""]
		
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked)
		self.GarvinDisconnect(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked)
		
		def setDatarekeningTerpilih(row,column):
			self.DataMaster_DataRekening_RekeningTerpilih[0] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNOMOR_REKENING).text())
			self.DataMaster_DataRekening_RekeningTerpilih[1] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNAMA_REKENING).text())
			#----Kembalikan, jangan disconnect sinyal krna ini sinyal itu sendiri, dilakukan di BukuBesar_DaftarTransaksiJurnal_PilihRekening.ubahcell instead
			self.fr_DataMaster_DataRekening.setParent(self.st_DataMaster_DataRekening)
			self.ivl_DataMaster_DataRekening_Luar.addWidget(self.fr_DataMaster_DataRekening)
			self.fr_DataMaster_DataRekening_Fb.show()
			self.DataMaster_Popup_Tutup()
			
		def setDatarekeningTerpilihNC(row,column):
			self.DataMaster_DataRekening_RekeningTerpilih[0] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNOMOR_REKENING).text())
			self.DataMaster_DataRekening_RekeningTerpilih[1] = str(self.tbl_DataMaster_DataRekening_Fcontent_LRekening.item(row,CNAMA_REKENING).text())
		
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked.connect(setDatarekeningTerpilih)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellDoubleClicked.connect(fcb_ok)
		self.tbl_DataMaster_DataRekening_Fcontent_LRekening.cellClicked.connect(setDatarekeningTerpilihNC)
		
	
	
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
	def DataMaster_DataProduk_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataProduk_Tambah_KodeBarang, 
		"""
		self.initDatabase()
		cursor = self.db.cursor()
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_data_produk` ORDER BY `gd_data_produk`.`id` DESC LIMIT 0 , 1"
		cursor.execute(sql)
		result = cursor.fetchall()
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "PRD" + "."+kode_default
		self.le_DataMaster_DataProduk_Tambah_KodeBarang.setText(kode_default)
		self.db.close()
	
	def DataMaster_DataProduk_Delete(self):
		try:
			kode = str(self.lb_DataMaster_DataProduk_Kode.text()).replace("\n","")
		except:
			return
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_data_produk` WHERE `gd_data_produk`.`kodeBarang` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPRODUK)
	
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
	
	def DataMaster_DataProduk_Edit(self):
		field = self.DataMaster_DataProduk_Field.index
		try:
			kode = str(self.lb_DataMaster_DataProduk_Kode.text()).replace("\n","")
		except:
			return
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
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "PJK" + "."+kode_default
		self.le_DataMaster_DataPajak_Tambah_KodePajak.setText(kode_default)
		
	def DataMaster_DataPajak_Delete(self):
		try:
			kode = str(self.lb_DataMaster_DataPajak_Kode.text()).replace("\n","")
		except:
			return
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_data_pajak` WHERE `gd_data_pajak`.`kodePajak` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATAPAJAK)
	
	def DataMaster_DataPajak_Edit(self):
		field = self.DataMaster_DataPajak_Field.index
		try:
			kode = str(self.lb_DataMaster_DataPajak_Kode.text()).replace("\n","")
		except:
			return
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
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "UNIT" + "."+kode_default
		self.le_DataMaster_DataSatuanPengukuran_Tambah_KodeSatuan.setText(kode_default)
		
	def DataMaster_DataSatuanPengukuran_Delete(self):
		try:
			kode = str(self.lb_DataMaster_DataSatuanPengukuran_Kode.text()).replace("\n","")
		except:
			return
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_satuan_pengukuran` WHERE `gd_satuan_pengukuran`.`kodeSatuan` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATASATUANPENGUKURAN)
	
	def DataMaster_DataSatuanPengukuran_Edit(self):
		field = self.DataMaster_DataSatuanPengukuran_Field.index
		try:
			kode = str(self.lb_DataMaster_DataSatuanPengukuran_Kode.text()).replace("\n","")
		except:
			return
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
		
	def DataMaster_Popup(self,text,function_callback,FW=500,FH=200,function_exit=False,function_close=False,hide_surrounding=False):
		
		if (FW == False):
			FW = 500
		if (FH == False):
			FH = 500
		if function_exit==False:
			function_exit = self.DataMaster_None
		if function_close==False:
			function_close = self.DataMaster_None
		if (function_close==None):
			function_close = self.DataMaster_None
		if (function_exit==None):
			function_exit = self.DataMaster_None
			
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
			
		FrameWindowH = self.findChildren(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindowH"))
		if (len(FrameWindowH)<1):
			FrameWindowH = QtGui.QFrame(self.centralwidget)
		else:
			FrameWindowH = FrameWindowH[0]
		if (hide_surrounding):
			FrameWindowH.setGeometry(QtCore.QRect(0, 0, WinW+20, WinH+20))
		else:
			FrameWindowH.setGeometry(QtCore.QRect(0, 0, 0, 0))
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
		FrameWindow.setStyleSheet(_fromUtf8("QFrame{background:#ffffff;border-radius:0px;border-style: solid;border-width: 2px;border-color:#868686;}QFrame>QFrame{border-style:none;border-width:0px;}"))
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
		
		ConfirmOk = self.findChildren(QtGui.QPushButton,_fromUtf8("DataMaster_Popup_ConfirmOk"))
		if (len(ConfirmOk)<1):
			ConfirmOk = QtGui.QPushButton(FrameWindow)
			ConfirmOk.setObjectName(_fromUtf8("DataMaster_Popup_ConfirmOk"))
			ConfirmOk.setText(_fromUtf8("Ok"))
			ConfirmOk.setStyleSheet(_fromUtf8("QPushButton{background:#555555;color:white;}"))
		else:
			ConfirmOk = ConfirmOk[0]
		
		ConfirmOk.setGeometry(QtCore.QRect(FW/2-42-85, FH-45, 85, 30))
		self.GarvinDisconnect(ConfirmOk.clicked)
		
		def tutup(f):
			f.close()
		ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindow))
		ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindowS))
		ConfirmOk.clicked.connect(functools.partial(tutup,FrameWindowH))
		ConfirmOk.clicked.connect(function_callback)
		ConfirmOk.clicked.connect(function_exit)
		ConfirmOk.show()
		
		ConfirmClose = self.findChildren(QtGui.QPushButton,_fromUtf8("DataMaster_Popup_ConfirmClose"))
		if (len(ConfirmClose)<1):
			ConfirmClose = QtGui.QPushButton(FrameWindow)
			ConfirmClose.setObjectName(_fromUtf8("DataMaster_Popup_ConfirmClose"))
			ConfirmClose.setText(_fromUtf8("Cancel"))
			ConfirmClose.setStyleSheet(_fromUtf8("QPushButton{background:#555555;color:white;}"))
		else:
			ConfirmClose = ConfirmClose[0]
		
		ConfirmClose.setGeometry(QtCore.QRect(FW/2-42+85, FH-45, 85, 30))
		self.GarvinDisconnect(ConfirmClose.clicked)
		
		ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindow))
		ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindowS))
		ConfirmClose.clicked.connect(functools.partial(tutup,FrameWindowH))
		ConfirmClose.clicked.connect(function_close)
		ConfirmClose.clicked.connect(function_exit)
		ConfirmClose.show()
		#execute exit function if any
		#~ if (function_exit!=None
		#~ function_exit() if (function_exit!=None) else None
		#~ aa = raw_input()
	
	def DataMaster_Popup_Tutup(self):
		FrameWindow = self.findChild(QtGui.QFrame,("DataMaster_Popup_FrameWindow"))
		FrameWindowS = self.findChild(QtGui.QFrame,("DataMaster_Popup_FrameWindowS"))
		FrameWindowH = self.findChild(QtGui.QFrame,("DataMaster_Popup_FrameWindowH"))
		FrameWindow.close()
		FrameWindowS.close()
		FrameWindowH.close()
	
	
#---- wong males
if __name__=="__main__":
	import os
	os.system("python ../Garvin.py")
