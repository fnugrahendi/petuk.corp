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
		CNOMOR_REFERENSI = 1
		self.KasBank_KasMasuk_RefreshList()
		self.KasBank_KasMasuk_RowColumnTerpilih = [-1,-1]
		
		def deletecertainrow():
			row = self.KasBank_KasMasuk_RowColumnTerpilih[0]
			nomorreferensi = str(self.KasBankUI.tbl_KasMasuk.item(row,CNOMOR_REFERENSI).text())
			sql = "DELETE FROM `gd_kas_masuk` WHERE `gd_kas_masuk`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			sql = "DELETE FROM `gd_detail_kas_masuk` WHERE `gd_detail_kas_masuk`.`kodeTransaksi` LIKE '"+nomorreferensi+"' ;"
			self.DatabaseRunQuery(sql)
			self.KasBankUI.tbl_KasMasuk.removeRow(row)
			
		def confirmdeletecertainrow():
			row = self.KasBank_KasMasuk_RowColumnTerpilih[0]
			if row>=0:
				nomorreferensi = str(self.KasBankUI.tbl_KasMasuk.item(row,CNOMOR_REFERENSI).text())
				self.DataMaster_Popup("Anda yakin akan menghapus data "+nomorreferensi+"?",deletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk.cellClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk.cellDoubleClicked)
		self.KasBankUI.tbl_KasMasuk.cellClicked.connect(self.KasBank_KasMasuk_SetActiveIndex)
		self.KasBankUI.tbl_KasMasuk.cellDoubleClicked.connect(self.KasBank_KasMasuk_Edit)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah.clicked.connect(self.KasBank_KasMasuk_Tambah)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tutup.clicked)
		self.KasBankUI.tb_KasMasuk_Tutup.clicked.connect(self.KasBank_Menu)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Delete.clicked)
		self.KasBankUI.tb_KasMasuk_Delete.clicked.connect(confirmdeletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.le_KasMasuk_Search.textChanged)
		self.KasBankUI.le_KasMasuk_Search.textChanged.connect(self.KasBank_KasMasuk_RefreshList)

	def KasBank_KasMasuk_RefreshList(self,searchtext=""):
		""" Refresh list of the table """
		field = self.KasBank_KasMasuk_Field.index
		searchtext=str(searchtext)
		CTANGGAL = 0
		CKODE = 1
		CPENYETOR = 2
		CKETERANGAN = 3
		CNILAI = 4
		
		TABLECOLUMNS = [
						["Tanggal", "Kode Referensi",	"Catatan",	"Nilai",		"Nomor Akun Kas/Bank",	"Penyetor"],
						["tanggal", "kodeTransaksi", 	"catatan",	"nilaiTotal",	"noAkunKas",			"kodePelanggan"]
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
				
				#--- Right most tablecolumn shows that the details data has undone rekening
				undone = False
				kode = str(result[row][	field("kodeTransaksi")	])
				details = self.DatabaseFetchResult(self.dbDatabase,"gd_detail_kas_masuk","kodeTransaksi",kode)
				for detail in details:
					if str(detail[self.KasBank_DetailKasMasuk_Field.index("noAkunDetail")])=="00000000":
						undone = True
						break
				if (undone):
					kolom = len(TABLECOLUMNS[1])
					if (self.KasBankUI.tbl_KasMasuk.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasMasuk.setItem(row, kolom, item)
					self.KasBankUI.tbl_KasMasuk.item(row,kolom).setText("<<<")
	
	def KasBank_KasMasuk_SetActiveIndex(self,row,col):
		""" This function reconnect the signal of button Buka """
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Buka.clicked)
		self.KasBankUI.tb_KasMasuk_Buka.clicked.connect(functools.partial(self.KasBank_KasMasuk_Edit,row,col))
		self.KasBank_KasMasuk_RowColumnTerpilih = [row,col]
		
	def KasBank_KasMasuk_Edit(self,row,col):
		CKODE = 1
		data = self.DatabaseFetchResult(self.dbDatabase,
										"gd_kas_masuk",
										"kodeTransaksi",
										str(self.KasBankUI.tbl_KasMasuk.item(row,CKODE).text())
										)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Cetak.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_Cetak.clicked.connect(functools.partial(self.KasBank_KasMasuk_Tambah_Cetak,str(self.KasBankUI.tbl_KasMasuk.item(row,CKODE).text())))
		self.KasBank_KasMasuk_Tambah(data[0])
	
	def KasBank_KasMasuk_Tambah_GenerateKode(self):
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_kas_masuk` ORDER BY `gd_kas_masuk`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<5):
				kode_default = "0"+kode_default
		kode_default = "KM" + kode_default
		self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setText(kode_default)
	
	def KasBank_KasMasuk_Tambah_KodeCek(self,stuf=None):
		kodebaru = ""
		kodeterlarang = str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text())
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_masuk","kodeTransaksi",kodeterlarang	)
		if (len(result)>0):
			self.statusbar.showMessage("Kode "+kodeterlarang+" sudah terpakai, diberikan kode lain",10000)
			while len(result)>0:
				nilai = int(re.findall("\d+",kodeterlarang)[0])
				nilai+=1
				kodebaru = str(nilai)
				while (len(kodebaru)<5):
					kodebaru = "0"+kodebaru
				kodebaru = "KM"+kodebaru
				kodeterlarang = kodebaru
				result = self.DatabaseFetchResult(self.dbDatabase,"gd_kas_masuk","kodeTransaksi",kodeterlarang	)
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setText(kodebaru)
			
	def KasBank_KasMasuk_Tambah(self,dataKasMasuk=False):
		fkm = self.KasBank_KasMasuk_Field.index
		fkmdetail = self.KasBank_DetailKasMasuk_Field.index
		self.KasBank_Goto("KASMASUK_TAMBAH")
		
		#-- we all need to clear table
		self.clearTable(self.KasBankUI.tbl_KasMasuk_Tambah)
		
		#--- disconnect kode cek (khusus tambah baru)
		self.GarvinDisconnect(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.textChanged)
		
		TABLECOLUMNS = [
							["Nomor Akun", "Nama Akun", "Nilai Detail", "Keterangan"],
							["noAkunDetail","gd_rekening_jurnal`.`namaAkun","nilaiDetail","catatan"]
						]
		idies = []
		if (dataKasMasuk==False):
			#--- new mode
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setReadOnly(False)
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText("")
			self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.setText("")
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setText("")
			self.KasBankUI.le_KasMasuk_Tambah_Form_Catatan.setText("")
			self.KasBankUI.lb_KasMasuk_Tambah_Form_Nilai.setText("")
			self.KasBank_KasMasuk_Tambah_GenerateKode()
			self.GarvinDisconnect(self.KasBankUI.le_KasKeluar_Tambah_Form_Nomor.textChanged)
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.textChanged.connect(self.KasBank_KasMasuk_Tambah_KodeCek)
		else:
			# --- edit mode
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setReadOnly(True)
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText(str(dataKasMasuk[fkm("kodePelanggan")]))
			self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.setText(str(dataKasMasuk[fkm("noAkunKas")]))
			self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.setText(str(dataKasMasuk[fkm("kodeTransaksi")]))
			self.KasBankUI.le_KasMasuk_Tambah_Form_Catatan.setText(str(dataKasMasuk[fkm("catatan")]))
			self.KasBankUI.lb_KasMasuk_Tambah_Form_Nilai.setText(str(dataKasMasuk[fkm("nilaiTotal")]))
			self.KasBankUI.dte_KasMasuk_Tambah_Form_Tanggal.setDateTime(QDateTime.fromString(str(dataKasMasuk[fkm("tanggal")]),"yyyy-MM-dd hh:mm:ss"))
			result = self.DatabaseFetchResult(self.dbDatabase,"gd_detail_kas_masuk","kodeTransaksi",str(dataKasMasuk[fkm("kodeTransaksi")]))
			
			for row in range(0,len(result)):
				self.KasBankUI.tbl_KasMasuk_Tambah.insertRow(row)
				idies.append(result[row][0]) #--- field id dari result ada di nomor kolom [0]
				for kolom in range(0,len(TABLECOLUMNS[1])):
					if (self.KasBankUI.tbl_KasMasuk_Tambah.item(row,kolom)==None):
						item = QtGui.QTableWidgetItem()
						self.KasBankUI.tbl_KasMasuk_Tambah.setItem(row, kolom, item)
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,0).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][0])]))
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][2])]))
				try:
					namaakun = self.DatabaseFetchResult(self.dbDatabase,"gd_rekening_jurnal","noAkun",(result[row][fkmdetail(TABLECOLUMNS[1][0])])	)[0][self.DataMaster_DataRekening_Field.index("namaAkun")]
				except:
					namaakun = ""
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,1).setText(str(namaakun))
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,3).setText(str(result[row][fkmdetail(TABLECOLUMNS[1][3])]))
				
		#----Hapus baris hanya terjadi bila sudah di Act_Simpan, sql query diantrikan
		sqltorun = []
		
		def hitungulang():
			total = 0
			for row in range(0,self.KasBankUI.tbl_KasMasuk_Tambah.rowCount()):
			#----check kalau diisi selain angka
				nilai_row = 0.0
				try:
					nilai_row = float(self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).text())
				except ValueError:
				#------ambil bilangan disitu dgn regex bila sukses, bila tidak beri nilai 0
					try:
						t = self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).text()
						self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).setText(str(re.search('\d+', t).group()))
					except AttributeError:
						self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).setText("0")
					except:pass
					nilai_row = float(self.KasBankUI.tbl_KasMasuk_Tambah.item(row,2).text())
				except:pass
				total = total + nilai_row
				self.KasBankUI.lb_KasMasuk_Tambah_Form_Nilai.setText(str(total))
			#----- end def hitung ulang
		
		def setactiveindex(a,b):
			self.KasBank_KasMasuk_Tambah_RowColumnTerpilih = [a,b]
		
		def tambahbaris():
			newrow = self.KasBankUI.tbl_KasMasuk_Tambah.rowCount()
			self.KasBankUI.tbl_KasMasuk_Tambah.insertRow(newrow)
			for x in range(len(TABLECOLUMNS[1])):
				if (self.KasBankUI.tbl_KasMasuk_Tambah.item(newrow,x)==None):
					item = QtGui.QTableWidgetItem()
					self.KasBankUI.tbl_KasMasuk_Tambah.setItem(newrow, x, item)
			
		def deletecertainrow():
			baris = self.KasBank_KasMasuk_Tambah_RowColumnTerpilih[0]
			if baris<0:
				return
			if (baris<len(idies)):
				sqltorun.append( "DELETE FROM `gd_detail_kas_masuk` WHERE `gd_detail_kas_masuk`.`id` = "+str(idies[baris])+" ;")
				idies.pop(baris)
			self.KasBankUI.tbl_KasMasuk_Tambah.removeRow(baris)
			hitungulang()
			
		def confirmdeletecertainrow():
			""" show popup to delete certain row, if user make sure, commit the delete with deletecertainrow"""
			baris = self.KasBank_KasMasuk_Tambah_RowColumnTerpilih[0]
			if (baris<0):
				return
			self.DataMaster_Popup("Anda yakin akan menghapus data baris "+str(baris+1)+"?",deletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.clicked)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.clicked.connect	(self.KasBank_KasMasuk_Tambah_Pilih_Penyetor)
		self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.clicked.connect	(self.KasBank_KasMasuk_Tambah_Pilih_AkunKas)
		
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellDoubleClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellClicked)
		self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellChanged)
		self.KasBankUI.tbl_KasMasuk_Tambah.cellDoubleClicked.connect(self.KasBank_KasMasuk_Tambah_EditTable)
		self.KasBankUI.tbl_KasMasuk_Tambah.cellClicked.connect(setactiveindex)
		self.KasBankUI.tbl_KasMasuk_Tambah.cellChanged.connect(hitungulang)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_TambahBaris.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_TambahBaris.clicked.connect(tambahbaris)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_HapusBaris.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_HapusBaris.clicked.connect(confirmdeletecertainrow)
		
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Simpan.clicked)
		self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Batal.clicked)
		self.KasBankUI.tb_KasMasuk_Tambah_Simpan.clicked.connect(functools.partial(self.KasBank_KasMasuk_Tambah_Act_Simpan,idies,sqltorun))
		self.KasBankUI.tb_KasMasuk_Tambah_Batal.clicked.connect(self.KasBank_KasMasuk)
		
		#--- cek sudah di cetak belum
		pass
		datacetak = self.DatabaseFetchResult(self.dbDatabase,"gd_buku_besar","kodeTransaksi",str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text()))
		if len(datacetak)>0:
			#-- Ternyata sudah dicetak. disconnect lagi
			self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellDoubleClicked)
			self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellClicked)
			self.GarvinDisconnect(self.KasBankUI.tbl_KasMasuk_Tambah.cellChanged)
			self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_TambahBaris.clicked)
			self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_HapusBaris.clicked)
			self.GarvinDisconnect(self.KasBankUI.tb_KasMasuk_Tambah_Simpan.clicked)
			self.statusbar.showMessage("Data ini sudah dicetak. Perubahan dikunci.",120000)
			#--- and give it no edit trigger
			self.KasBankUI.tbl_KasMasuk_Tambah.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
		else:
			#-- make sure to have it an edit trigger
			self.KasBankUI.tbl_KasMasuk_Tambah.setEditTriggers(QtGui.QAbstractItemView.AnyKeyPressed|QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed)
			self.statusbar.showMessage("",1)
	
	def KasBank_KasMasuk_Tambah_Act_Simpan(self,idies,sqltorun):
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
			self.DatabaseInsertReplace(self.dbDatabase,"gd_detail_kas_masuk","id",tablerowid,
										["kodeTransaksi","noAkunDetail","nilaiDetail"],
										[str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text()),
										str(self.KasBankUI.tbl_KasMasuk_Tambah.item(tablerow,CNOAKUN).text()),
										str(self.KasBankUI.tbl_KasMasuk_Tambah.item(tablerow,CNILAI	).text())
										]
									)
			tablerow+=1
		if self.KasBankUI.tbl_KasMasuk_Tambah.rowCount()>len(idies):
			#"ada tambahan baru"
			for tablerow in range(len(idies),self.KasBankUI.tbl_KasMasuk_Tambah.rowCount()):
				self.DatabaseInsertReplace(self.dbDatabase,"gd_detail_kas_masuk",	None,None,
											["kodeTransaksi","noAkunDetail","nilaiDetail"],
											[str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text()),
											str(self.KasBankUI.tbl_KasMasuk_Tambah.item(tablerow,CNOAKUN).text()),
											str(self.KasBankUI.tbl_KasMasuk_Tambah.item(tablerow,CNILAI	).text())
											]	)
		self.DatabaseInsertReplace(self.dbDatabase,"gd_kas_masuk","kodeTransaksi",str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text()),
											["kodeTransaksi", "noAkunKas", "kodePelanggan", "catatan", "tanggal", "nilaiTotal"],
											[
												str(self.KasBankUI.le_KasMasuk_Tambah_Form_Nomor.text()),
												str(self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.text()),
												str(self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.text()),
												str(self.KasBankUI.le_KasMasuk_Tambah_Form_Catatan.text()),
												str(self.KasBankUI.dte_KasMasuk_Tambah_Form_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss")),
												str(self.KasBankUI.lb_KasMasuk_Tambah_Form_Nilai.text())
											]	)
		#---------at last, we execute sqltorun queries
		for sql in sqltorun:
			self.DatabaseRunQuery(sql)
		self.KasBank_KasMasuk()
		
	def KasBank_KasMasuk_Tambah_Pilih_AkunKas(self):
		data = ["",""]
		def isi():
			self.KasBankUI.tb_KasMasuk_Tambah_Form_NoAkun.setText(str(data[0]))
		self.DataMaster_DataRekening_Popup_Pilih(data,isi)
		
	def KasBank_KasMasuk_Tambah_Pilih_Penyetor(self):
		data = []
		def isi():
			self.KasBankUI.tb_KasMasuk_Tambah_Form_Penyetor.setText(str(data[0]))
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi)
		
	def KasBank_KasMasuk_Tambah_EditTable(self,row,column):
		self.KasBank_KasMasuk_Tambah_RowColumnTerpilih = [row,column]
		if (column<2):
			data = ["",""]
			def isi():
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,0).setText(str(data[0]))
				self.KasBankUI.tbl_KasMasuk_Tambah.item(row,1).setText(str(data[1]))
			self.DataMaster_DataRekening_Popup_Pilih(data,isi)

	def KasBank_KasMasuk_Tambah_Cetak(self,kode):
		""" Menyimpan data ke gd_buku_besar 
		tipe: masuk, rekening Debit, sumber kredit"""
		#--- step 0: initialize, untuk class kembaran edit hanya di step ini
		table = "gd_kas_masuk"
		tabledetail = table.replace("gd_","gd_detail_")
			#-- field index
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='"+table+"';")
		dataf = list(itertools.chain.from_iterable(result)).index
		result = self.DatabaseRunQuery("SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='"+tabledetail+"';")
		detailf = list(itertools.chain.from_iterable(result)).index
		
		#--- step 1: cek sudah di cetak belum
		pass
		datacetak = self.DatabaseFetchResult(self.dbDatabase,"gd_buku_besar","kodeTransaksi",kode)
		if len(datacetak)>0:
			self.DataMaster_Popup("Data ini sudah dicetak pada tanggal "+str(datacetak[0][2]))
			return
		#--- step 2: ambil data
		datas = self.DatabaseFetchResult(self.dbDatabase,table,"kodeTransaksi",kode)
		details=self.DatabaseFetchResult(self.dbDatabase,tabledetail,"kodeTransaksi",kode)
		
		if (len(datas)==0):
			return
		else:
			data = datas[0]
			datas = None #garbagecollector get me
			
		#--- step 3: simpan ke buku besar untuk data (noAkunKasBank)
		KB = table.replace("gd_","").replace("_masuk","").replace("_keluar","")
		KB = KB[0].upper()+KB[1:]
		noakunkasbank = "noAkun"+KB #-- noAkunKas di field Kas, noAkunBank di field Bank
		
		
		if "masuk" in table:datakreditdebit = "debit" #-- bila kas/bank masuk, debit ke noAkunKasBank
		else:datakreditdebit = "kredit" #-- sebaliknya
		self.DatabaseInsertReplace(self.dbDatabase,"gd_buku_besar",None,None,
									["kodeTransaksi","tanggal","noAkun",datakreditdebit],
									[
										data[dataf("kodeTransaksi")],
										data[dataf("tanggal")],
										data[dataf(noakunkasbank)],
										data[dataf("nilaiTotal")]
									]
								)
		#--- step 4: simpan ke buku besar untuk setiap detail
		if "masuk" in table: detailkreditdebit = "kredit"#-- bila kas/bank masuk, kredit ke noAkunDetail
		else:detailkreditdebit = "debit" #-- otherwise
		for detail in details:
			self.DatabaseInsertReplace(self.dbDatabase,"gd_buku_besar",None,None,
										["kodeTransaksi","tanggal","noAkun",detailkreditdebit],
										[
											data[dataf("kodeTransaksi")],
											data[dataf("tanggal")],
											detail[detailf("noAkunDetail")],
											detail[detailf("nilaiDetail")]
										]
									)
		#-- done
