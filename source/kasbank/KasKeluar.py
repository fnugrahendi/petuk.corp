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

class KasKeluar(object):
	def __init__(self,parent=None):
		self.KasBankUI.tb_KasKeluar_Tutup.clicked.connect(functools.partial(self.KasBank_Goto,"MENU"))
		pass
	
	
	def KasBank_KasKeluar(self):
		""" The room control itself """
		self.KasBank_Goto("KASKELUAR")
		CNOMOR_REFERENSI = 1
		self.KasBank_KasKeluar_RefreshList()
		self.KasBank_KasKeluar_RowColumnTerpilih = [-1,-1]
		
		def deletecertainrow():
			row = self.KasBank_KasKeluar_RowColumnTerpilih[0]
			nomorreferensi = str(self.KasBankUI.tbl_KasKeluar.item(row,CNOMOR_REFERENSI).text())
			sql = "DELETE FROM `gd_kas_keluar` WHERE `gd_kas_keluar`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			sql = "DELETE FROM `gd_detail_kas_keluar` WHERE `gd_detail_kas_keluar`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			self.KasBankUI.tbl_KasKeluar.removeRow(row)
			
		def confirmdeletecertainrow():
			row = self.KasBank_KasKeluar_RowColumnTerpilih[0]
			if row>=0:
				nomorreferensi = str(self.KasBankUI.tbl_KasKeluar.item(row,CNOMOR_REFERENSI).text())
				self.DataMaster_Popup("Anda yakin akan menghapus data "+nomorreferensi+"?",deletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tbl_KasKeluar.cellClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasKeluar.cellDoubleClicked)
		self.KasBankUI.tbl_KasKeluar.cellClicked.connect(self.KasBank_KasKeluar_SetActiveIndex)
		self.KasBankUI.tbl_KasKeluar.cellDoubleClicked.connect(self.KasBank_KasKeluar_Edit)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah.clicked)
		self.KasBankUI.tb_KasKeluar_Tambah.clicked.connect(self.KasBank_KasKeluar_Tambah)
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tutup.clicked)
		self.KasBankUI.tb_KasKeluar_Tutup.clicked.connect(self.KasBank_Menu)
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Delete.clicked)
		self.KasBankUI.tb_KasKeluar_Delete.clicked.connect(confirmdeletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.le_KasKeluar_Search.textChanged)
		self.KasBankUI.le_KasKeluar_Search.textChanged.connect(self.KasBank_KasKeluar_RefreshList)

	def KasBank_KasKeluar_RefreshList(self,searchtext=""):
		""" Refresh list of the table """
		field = self.KasBank_KasKeluar_Field.index
		searchtext=str(searchtext)
		CTANGGAL = 0
		CKODE = 1
		CPENERIMA = 2
		CKETERANGAN = 3
		CNILAI = 4
		
		TABLECOLUMNS = [
						["Tanggal", "Kode Referensi",	"Catatan",	"Nilai",		"Nomor Akun Kas/Bank",	"Penerima"],
						["tanggal", "kodeTransaksi", 	"catatan",	"nilaiTotal",	"noAkunKas",			"kodePelanggan"]
						]
		
		#at first we clear the rows
		self.clearTable(self.KasBankUI.tbl_KasKeluar)
		
		#--- record if such row has displayed
		idies = []
		#--- auto search for all of displayed column based on fieldlist on TABLECOLUMNS[1]
		for x in range(0,len(TABLECOLUMNS[1])):
			result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_keluar",TABLECOLUMNS[1][x],"%"+str(searchtext)+"%")
			for row in range(0,len(result)):
				if (row in idies):
					continue
				self.KasBankUI.tbl_KasKeluar.insertRow(row)
				idies.append(row)
				for kolom in range(0,len(TABLECOLUMNS[1])):
					if (self.KasBankUI.tbl_KasKeluar.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasKeluar.setItem(row, kolom, item)
					self.KasBankUI.tbl_KasKeluar.item(row,kolom).setText(str(result[row][	field(TABLECOLUMNS[1][kolom])	]))
	
	def KasBank_KasKeluar_SetActiveIndex(self,row,col):
		""" This function reconnect the signal of button Buka """
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Buka.clicked)
		self.KasBankUI.tb_KasKeluar_Buka.clicked.connect(functools.partial(self.KasBank_KasKeluar_Edit,row,col))
		self.KasBank_KasKeluar_RowColumnTerpilih = [row,col]
		
	def KasBank_KasKeluar_Edit(self,row,col):
		CKODE = 1
		data = self.DatabaseFetchResult(self.dbDatabase,
										"gd_kas_keluar",
										"kodeTransaksi",
										str(self.KasBankUI.tbl_KasKeluar.item(row,CKODE).text())
										)
		self.KasBank_KasKeluar_Tambah(data[0])
	
	def KasBank_KasKeluar_Tambah_GenerateKode(self):
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_kas_keluar` ORDER BY `gd_kas_keluar`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = "CD" + kode_default
		self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setText(kode_default)
	
	def KasBank_KasKeluar_Tambah_KodeCek(self,stuf=None):
		kodebaru = ""
		kodeterlarang = str(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.text())
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_keluar","kodeTransaksi",kodeterlarang	)
		if (len(result)>0):
			self.statusbar.showMessage("Kode "+kodeterlarang+" sudah terpakai, diberikan kode lain",10000)
			while len(result)>0:
				nilai = int(re.findall("\d+",kodeterlarang)[0])
				nilai+=1
				kodebaru = str(nilai)
				while (len(kodebaru)<8):
					kodebaru = "0"+kodebaru
				kodebaru = "CD"+kodebaru
				kodeterlarang = kodebaru
				result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_keluar","kodeTransaksi",kodeterlarang	)
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setText(kodebaru)
	
	def KasBank_KasKeluar_Tambah(self,dataKasKeluar=False):
		fkm = self.KasBank_KasKeluar_Field.index
		fkmdetail = self.KasBank_DetailKasKeluar_Field.index
		self.KasBank_Goto("KASKeluar_TAMBAH")
		
		#-- we all need to clear table
		self.clearTable(self.KasBankUI.tbl_KasKeluar_Tambah)
		
		#--- disconnect kode cek (khusus tambah baru)
		self.GarvinDisconnect(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.textChanged)
		
		TABLECOLUMNS = [
							["Nomor Akun", "Nama Akun", "Nilai Detail"],
							["noAkunDetail","gd_rekening_jurnal`.`namaAkun","nilaiDetail"]
						]
		idies = []
		if (dataKasKeluar==False):
			#--- new mode
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setReadOnly(False)
			self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.setText("")
			self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.setText("")
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setText("")
			self.KasBankUI.le_KasKeluar_Tambah_Form_Catatan.setText("")
			self.KasBankUI.lb_KasKeluar_Tambah_Form_Nilai.setText("")
			self.KasBank_KasKeluar_Tambah_GenerateKode()
			self.GarvinDisconnect(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.textChanged)
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.textChanged.connect(self.KasBank_KasKeluar_Tambah_KodeCek)
		else:
			# --- edit mode
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setReadOnly(True)
			self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.setText(str(dataKasKeluar[fkm("kodePelanggan")]))
			self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.setText(str(dataKasKeluar[fkm("noAkunKas")]))
			self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.setText(str(dataKasKeluar[fkm("kodeTransaksi")]))
			self.KasBankUI.le_KasKeluar_Tambah_Form_Catatan.setText(str(dataKasKeluar[fkm("catatan")]))
			self.KasBankUI.lb_KasKeluar_Tambah_Form_Nilai.setText(str(dataKasKeluar[fkm("nilaiTotal")]))
			self.KasBankUI.dte_KasKeluar_Tambah_Form_Tanggal.setDateTime(QDateTime.fromString(str(dataKasKeluar[fkm("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
			result = self.DatabaseFetchResult(self.dbDatabase,"gd_detail_kas_keluar","kodeTransaksi",str(dataKasKeluar[fkm("kodeTransaksi")]))
			
			for row in range(0,len(result)):
				self.KasBankUI.tbl_KasKeluar_Tambah.insertRow(row)
				idies.append(result[row][0]) #--- field id dari result ada di nomor kolom [0]
				for kolom in range(0,len(TABLECOLUMNS[1])):
					if (self.KasBankUI.tbl_KasKeluar_Tambah.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasKeluar_Tambah.setItem(row, kolom, item)
				self.KasBankUI.tbl_KasKeluar_Tambah.item(row,0).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][0])]))
				self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][2])]))
				try:
					namaakun = self.DatabaseFetchResult(self.dbDatabase,"gd_rekening_jurnal","noAkun",(result[row][fkmdetail(TABLECOLUMNS[1][0])])	)[0][self.DataMaster_DataRekening_Field.index("namaAkun")]
				except:
					namaakun = ""
				self.KasBankUI.tbl_KasKeluar_Tambah.item(row,1).setText(str(namaakun))
		
		#----Hapus baris hanya terjadi bila sudah di Act_Simpan, sql query diantrikan
		sqltorun = []
		
		def hitungulang():
			total = 0
			for row in range(0,self.KasBankUI.tbl_KasKeluar_Tambah.rowCount()):
			#----check kalau diisi selain angka
				nilai_row = 0.0
				try:
					nilai_row = float(self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).text())
				except ValueError:
				#------ambil bilangan disitu dgn regex bila sukses, bila tidak beri nilai 0
					try:
						t = self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).text()
						self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).setText(str(re.search('\d+', t).group()))
					except AttributeError:
						self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).setText("0")
					except:pass
					nilai_row = float(self.KasBankUI.tbl_KasKeluar_Tambah.item(row,2).text())
				except:pass
				total = total + nilai_row
				self.KasBankUI.lb_KasKeluar_Tambah_Form_Nilai.setText(str(total))
			#----- end def hitung ulang
		
		def setactiveindex(a,b):
			self.KasBank_KasKeluar_Tambah_RowColumnTerpilih = [a,b]
		
		def tambahbaris():
			newrow = self.KasBankUI.tbl_KasKeluar_Tambah.rowCount()
			self.KasBankUI.tbl_KasKeluar_Tambah.insertRow(newrow)
			for x in range(len(TABLECOLUMNS[1])):
				if (self.KasBankUI.tbl_KasKeluar_Tambah.item(newrow,x)==None):
					item = QtGui.QTableWidgetItem()
					self.KasBankUI.tbl_KasKeluar_Tambah.setItem(newrow, x, item)
			
		def deletecertainrow():
			baris = self.KasBank_KasKeluar_Tambah_RowColumnTerpilih[0]
			if baris<0:
				return
			if (baris<len(idies)):
				sqltorun.append( "DELETE FROM `gd_detail_kas_keluar` WHERE `gd_detail_kas_keluar`.`id` = "+str(idies[baris])+" ;")
				idies.pop(baris)
			self.KasBankUI.tbl_KasKeluar_Tambah.removeRow(baris)
			hitungulang()
			
		def confirmdeletecertainrow():
			""" show popup to delete certain row, if user make sure, commit the delete with deletecertainrow"""
			baris = self.KasBank_KasKeluar_Tambah_RowColumnTerpilih[0]
			if (baris<0):
				return
			self.DataMaster_Popup("Anda yakin akan menghapus data baris "+str(baris+1)+"?",deletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.clicked)
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.clicked)
		self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.clicked.connect	(self.KasBank_KasKeluar_Tambah_Pilih_Penerima)
		self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.clicked.connect	(self.KasBank_KasKeluar_Tambah_Pilih_AkunKas)
		
		self.GarvinDisconnect(self.KasBankUI.tbl_KasKeluar_Tambah.cellDoubleClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasKeluar_Tambah.cellClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasKeluar_Tambah.cellChanged)
		self.KasBankUI.tbl_KasKeluar_Tambah.cellDoubleClicked.connect(self.KasBank_KasKeluar_Tambah_EditTable)
		self.KasBankUI.tbl_KasKeluar_Tambah.cellClicked.connect(setactiveindex)
		self.KasBankUI.tbl_KasKeluar_Tambah.cellChanged.connect(hitungulang)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_TambahBaris.clicked)
		self.KasBankUI.tb_KasKeluar_Tambah_TambahBaris.clicked.connect(tambahbaris)
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_HapusBaris.clicked)
		self.KasBankUI.tb_KasKeluar_Tambah_HapusBaris.clicked.connect(confirmdeletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_Simpan.clicked)
		self.GarvinDisconnect(self.KasBankUI.tb_KasKeluar_Tambah_Batal.clicked)
		self.KasBankUI.tb_KasKeluar_Tambah_Simpan.clicked.connect(functools.partial(self.KasBank_KasKeluar_Tambah_Act_Simpan,idies,sqltorun))
		self.KasBankUI.tb_KasKeluar_Tambah_Batal.clicked.connect(self.KasBank_KasKeluar)
	
	def KasBank_KasKeluar_Tambah_Act_Simpan(self,idies,sqltorun):
		if idies==None: #-- avoid call by reference default value, as it will just append more 
			idies = []
		if sqltorun==None:
			sqltorun = []
		CNOAKUN = 0
		CNILAI = 2
		#--- edit (simpen replace)
		#--- update dan tambah detail transaksi jurnal
		tablerow = 0
		for tablerowid in idies:
			self.DatabaseInsertReplace(self.dbDatabase,"gd_detail_kas_keluar","id",tablerowid,
										["kodeTransaksi","noAkunDetail","nilaiDetail"],
										[str(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.text()),
										str(self.KasBankUI.tbl_KasKeluar_Tambah.item(tablerow,CNOAKUN).text()),
										str(self.KasBankUI.tbl_KasKeluar_Tambah.item(tablerow,CNILAI	).text())
										]
									)
			tablerow+=1
		if self.KasBankUI.tbl_KasKeluar_Tambah.rowCount()>len(idies):
			#"ada tambahan baru"
			for tablerow in range(len(idies),self.KasBankUI.tbl_KasKeluar_Tambah.rowCount()):
				self.DatabaseInsertReplace(self.dbDatabase,"gd_detail_kas_keluar",	None,None,
											["kodeTransaksi","noAkunDetail","nilaiDetail"],
											[str(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.text()),
											str(self.KasBankUI.tbl_KasKeluar_Tambah.item(tablerow,CNOAKUN).text()),
											str(self.KasBankUI.tbl_KasKeluar_Tambah.item(tablerow,CNILAI	).text())
											]	)
		self.DatabaseInsertReplace(self.dbDatabase,"gd_kas_keluar","kodeTransaksi",str(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.text()),
											["kodeTransaksi", "noAkunKas", "kodePelanggan", "catatan", "tanggal", "nilaiTotal"],
											[
												str(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.text()),
												str(self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.text()),
												str(self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.text()),
												str(self.KasBankUI.le_KasKeluar_Tambah_Form_Catatan.text()),
												str(self.KasBankUI.dte_KasKeluar_Tambah_Form_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss")),
												str(self.KasBankUI.lb_KasKeluar_Tambah_Form_Nilai.text())
											]	)
		#---------at last, we execute sqltorun queries
		for sql in sqltorun:
			self.DatabaseRunQuery(sql)
		self.KasBank_KasKeluar()
		
	def KasBank_KasKeluar_Tambah_Pilih_AkunKas(self):
		data = ["",""]
		def isi():
			self.KasBankUI.tb_KasKeluar_Tambah_Form_NoAkun.setText(str(data[0]))
		self.DataMaster_DataRekening_Popup_Pilih(data,isi)
		
	def KasBank_KasKeluar_Tambah_Pilih_Penerima(self):
		data = []
		def isi():
			self.KasBankUI.tb_KasKeluar_Tambah_Form_Penerima.setText(str(data[0]))
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi)
		
	def KasBank_KasKeluar_Tambah_EditTable(self,row,column):
		self.KasBank_KasKeluar_Tambah_RowColumnTerpilih = [row,column]
		if (column<2):
			data = ["",""]
			def isi():
				self.KasBankUI.tbl_KasKeluar_Tambah.item(row,0).setText(str(data[0]))
				self.KasBankUI.tbl_KasKeluar_Tambah.item(row,1).setText(str(data[1]))
			self.DataMaster_DataRekening_Popup_Pilih(data,isi)
