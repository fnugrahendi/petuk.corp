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
from datetime import datetime #tanggal, a= datetime.now(); cobo dicheck dir(a); a.year, etc.
#----Data tab
from bukubesar import BukuBesar
from datamaster import DataMaster
from pembelian import Pembelian
from kasbank import KasBank
from laporan import Laporan
from login import Login
from updater import Updater

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s


class MainGUI(QtGui.QMainWindow, Ui_MainWindow,BukuBesar,DataMaster,Pembelian,KasBank,Laporan,Login,Updater):
	def __init__(self, parent= None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.st_Penjualan.setCurrentIndex(0)
		self.showFullScreen()
		def ___metu():
			exit(0)
			return True
		#self.tb_Penjualan_Keluar.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan keluar dari aplikasi?",___metu))
        
        
        
		self.dbHost = "127.0.0.1"
		self.dbPort = 44559
		self.dbDatabase = "gd_db_akunting"
		self.dbPass = "nyungsep"
		self.dbUser = "gd_user_akunting"
        #---------------------------------------------------------------Penjualan Init Itut
		#Tombol pada Halaman Menu
		self.tb_Penjualan_Invoice.clicked.connect(self.Penjualan_GoTo_Invoice)
		self.tb_Penjualan_OrderPenjualan.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_Piutang.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		self.tb_Penjualan_PembayaranPiutang.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		
		#Tombol pada invoice
		self.tb_Penjualan_DaftarInvoice_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		
		#Tombol&Sinyal pada Halaman OrderPenjualan
		self.tb_Penjualan_OrderPenjualan_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_OrderPenjualan_Baru.clicked.connect(self.Penjualan_GoTo_OP_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Batal.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Simpan.clicked.connect(self.Penjualan_OrderPenjualan_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_HapusBaris.clicked.connect(functools.partial(self.HapusBaris,self.tbl_Penjualan_OrderPenjualan))
		self.tb_Penjualan_OrderPenjualan_Batal.clicked.connect(self.Penjualan_OrderPenjualan_Batal)
		self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.currentIndexChanged.connect(self.Penjualan_OrderPenjualan_TambahProduk_UpdateKode)
		self.tb_Penjualan_OrderPenjualan_Rekam.clicked.connect(self.Penjualan_OrderPenjualan_Rekam)
		self.tb_Penjualan_OrderPenjualan_Nama.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.tb_Penjualan_OrderPenjualan_Nama))
		
		#Tombol pada Halaman Pengiriman
		self.tb_Penjualan_Pengiriman_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_Pengiriman_Baru.clicked.connect(self.Penjualan_GoTo_Pengiriman_Baru)
		self.tb_Penjualan_PengirimanBaru_Tutup.clicked.connect(self.Penjualan_GoTo_Pengiriman)
		
		#Tombol pada Halaman Piutang
		self.tb_Penjualan_Piutang_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_RincianPiutang_Tutup.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		self.tb_Penjualan_Piutang_Perincian.clicked.connect(self.Penjualan_GoTo_PiutangUsaha_Rincian)
		
		#Tombol pada Halaman Pembayaran Piutang
		self.tb_Penjualan_PembayaranPiutang_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_PembayaranPiutang_Baru.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang_Baru)
		self.tb_Penjualan_PembayaranPiutang_Baru_Batal.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		
		self.INDEX_ST_PENJUALAN_MENU = 0
		self.INDEX_ST_PENJUALAN_DI = 1
		self.INDEX_ST_PENJUALAN_IP = 2
		self.INDEX_ST_PENJUALAN_I_TB = 3
		self.INDEX_ST_PENJUALAN_OP = 4
		self.INDEX_ST_PENJUALAN_PENGIRIMAN = 5
		self.INDEX_ST_PENJUALAN_PENGIRIMANB = 6
		self.INDEX_ST_PENJUALAN_PU = 7
		self.INDEX_ST_PENJUALAN_RPU = 8
		self.INDEX_ST_PENJUALAN_PP = 9
		self.INDEX_ST_PENJUALAN_PPB = 10
		
		self.DataMaster_init()
		self.BukuBesar_init()
		self.Pembelian__init()
		self.KasBank_init()
		self.Login_init()
		
		#--- kalau pindah tab, set semua stackedWidget ke index 0 (suppose to be _Menu index)
		self.tabWidget.currentChanged.connect(self.ResetRooms)
		#--- startup program aswell, stackedwidget room should be on Menu Index 
		self.ResetRooms()
		#--- startup program, set semua datetimeedit ke waktu skrg		
		tanggal = datetime.now()
		dtedte = self.findChildren(QtGui.QDateTimeEdit)
		for dte in dtedte:
			dte.setDateTime(QDateTime.fromString(tanggal.strftime("%Y-%m-%d %H:%M:%S"),"yyyy-MM-dd hh:mm:ss"))
		#~ self.GarvinCheckIsUpdated()
		
		
	def initDatabase(self):
		try:
			self.db = MySQLdb.connect(self.dbHost,self.dbUser,self.dbPass,self.dbDatabase)
			print ("connected database to generic mysql port")
		except:
			try:
				self.db = MySQLdb.Connect(host=self.dbHost, port=self.dbPort, user=self.dbUser, passwd=self.dbPass, db=self.dbDatabase)
				print ("connected database to Garvin port")
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
	
	
	
	def ResetRooms(self):
		#--- search pakai regexp, karena ternyata tab widget pakai stackedwidget juga!
		for st in self.findChildren(QtGui.QStackedWidget,QRegExp("st_\w+")):
			st.setCurrentIndex(0)
	#-------------------------------------------------------------------Penjualan
	#-------------------------------------------------------------------Penjualan
	
	def Penjualan_OrderPenjualan_TambahProduk_UpdateKode(self,index):
		namaProduk = str(self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+namaProduk+"'"
		#self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.setText
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.setText(kodeBarang)
		
	def Penjualan_GoTo_Menu(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_MENU)
		
	def Penjualan_GoTo_Invoice(self):
		rownum = self.tbl_Penjualan_DaftarInvoice.rowCount()
		for b in range (0, rownum):
			self.tbl_Penjualan_DaftarInvoice.removeRow(b)
		self.tbl_Penjualan_DaftarInvoice.setRowCount(0)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_DI)
		query = "SELECT * FROM gd_invoice_penjualan"
		result = self.DatabaseRunQuery(query)
		for a in range(0, len(result)):
			self.tbl_Penjualan_DaftarInvoice.insertRow(a)
			self.tbl_Penjualan_DaftarInvoice.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][1]))) #No Invoice
			self.tbl_Penjualan_DaftarInvoice.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][4]))) #Tanggal
			self.tbl_Penjualan_DaftarInvoice.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][3]))) #Pelanggan
			self.tbl_Penjualan_DaftarInvoice.setItem(a,4,QtGui.QTableWidgetItem(str(int(result[a][6])))) #Nilai
		
	def Penjualan_GoTo_OrderPenjualan(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP)
		self.tb_Penjualan_OrderPenjualan_Nama.setText("")
		self.cb_Penjualan_OrderPenjualan_Gudang.clear()
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		#print jumlahRow
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Penjualan_OrderPenjualan.removeRow(a)
		kodePenjualan = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		#print kodePenjualan
		"""
		query = "SELECT * FROM gd_nama_alamat WHERE `tipe` LIKE 'customer'"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_Nama.addItem(self.DatabaseRunQuery(query)[a][2])"""
		query = "SELECT * FROM gd_data_gudang"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_Gudang.addItem(self.DatabaseRunQuery(query)[a][2])


		query = "SELECT * FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodePenjualan+"'"
		result = self.DatabaseRunQuery(query) 
		print result
		if len(result) != 0:
			for a in range(0,len(result)):
				print "tambah row"
				self.tbl_Penjualan_OrderPenjualan.insertRow(a)
				self.tbl_Penjualan_OrderPenjualan.setItem(a,0,QtGui.QTableWidgetItem(result[a][4])) #kode
				sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+result[a][4]+"'"
				self.tbl_Penjualan_OrderPenjualan.setItem(a,1,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][5]))) #nama produk
				kodeSatuan = str(self.DatabaseRunQuery(sql)[0][3])
				satuan_query =  "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+kodeSatuan+"'"
				satuan = str(self.DatabaseRunQuery(satuan_query)[0][2])
				self.tbl_Penjualan_OrderPenjualan.setItem(a,3,QtGui.QTableWidgetItem(satuan)) #satuan
				self.tbl_Penjualan_OrderPenjualan.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][5]))) #jumlah
				self.tbl_Penjualan_OrderPenjualan.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][6]))) #harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,5,QtGui.QTableWidgetItem(result[a][7])) #diskon
				total = result[a][6]*result[a][5]
				self.tbl_Penjualan_OrderPenjualan.setItem(a,6,QtGui.QTableWidgetItem(str(total))) #total harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,7,QtGui.QTableWidgetItem(result[a][8])) #pajak
		
	
	def Penjualan_GoTo_OP_TambahProduk(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP_TAMBAHPRODUK)
		self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Satuan.clear()
		self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.clear()
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Jumlah.clear()
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Harga.clear()
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Diskon.clear()
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Pajak.clear()
		query = "SELECT * FROM gd_data_produk"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.addItem(self.DatabaseRunQuery(query)[a][5])
		query = "SELECT * FROM gd_satuan_pengukuran"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Satuan.addItem(self.DatabaseRunQuery(query)[a][2])
		nama = str(self.cb_Penjualan_OrderPenjualan_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+nama+"'"
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.setText(kodeBarang)
			
	def Penjualan_OrderPenjualan_TambahProduk(self):
		kodePelanggan = str(self.tb_Penjualan_OrderPenjualan_Nama.text())
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		kodeBarang = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Kode.text())
		jumlah = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Jumlah.text())
		harga = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Harga.text())
		diskon = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Diskon.text())
		pajak = str(self.le_Penjualan_OrderPenjualan_TambahProduk_Input_Pajak.text())
		query = "SELECT * FROM `gd_data_pajak` WHERE `namaPajak` LIKE '"+pajak+"'"
		try:
			kodePajak = str(self.DatabaseRunQuery(query)[0][1])
		except:
			kodePajak = ""
		kodeMatauang = str(self.cb_Penjualan_OrderPenjualan_Kurs.currentText())
		query = "INSERT INTO `gd_order_penjualan` (`kodeTransaksi`,`kodeMatauang`,`kodePelanggan`,`kodeBarang`"+\
			",`jumlah`,`harga`,`diskon`,`kodePajak`) VALUES"+\
			"('"+kodeTransaksi+"','"+kodeMatauang+"','"+kodePelanggan+"','"+kodeBarang+"','"+jumlah+"','"+harga+"','"+diskon+"','"+kodePajak+"')"
		self.DatabaseRunQuery(query)
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Penjualan_OrderPenjualan.removeRow(a)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_OP)
		query = "SELECT * FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(query) 
		print result
		if len(result) != 0:
			for a in range(0,len(result)):
				print "tambah row"
				self.tbl_Penjualan_OrderPenjualan.insertRow(a)
				self.tbl_Penjualan_OrderPenjualan.setItem(a,0,QtGui.QTableWidgetItem(result[a][4])) #kode
				sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+result[a][4]+"'"
				self.tbl_Penjualan_OrderPenjualan.setItem(a,1,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][5]))) #nama produk
				kodeSatuan = str(self.DatabaseRunQuery(sql)[0][3])
				satuan_query =  "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+kodeSatuan+"'"
				satuan = str(self.DatabaseRunQuery(satuan_query)[0][2])
				self.tbl_Penjualan_OrderPenjualan.setItem(a,3,QtGui.QTableWidgetItem(satuan)) #satuan
				self.tbl_Penjualan_OrderPenjualan.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][5]))) #jumlah
				self.tbl_Penjualan_OrderPenjualan.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][6]))) #harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,5,QtGui.QTableWidgetItem(result[a][7])) #diskon
				total = result[a][6]*result[a][5]
				self.tbl_Penjualan_OrderPenjualan.setItem(a,6,QtGui.QTableWidgetItem(str(total))) #total harga
				self.tbl_Penjualan_OrderPenjualan.setItem(a,7,QtGui.QTableWidgetItem(result[a][8])) #pajak
	
	def Penjualan_OrderPenjualan_Rekam(self):
		kodePelanggan = str(self.tb_Penjualan_OrderPenjualan_Nama.text())
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		kodeMatauang = str(self.cb_Penjualan_OrderPenjualan_Kurs.currentText())
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		tanggal = self.dte_Pembelian_OrderPembelian_Tanggal.dateTime()
		tanggal = tanggal.toString("yyyy-MM-dd hh:mm:ss")
		#print tanggal
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				kodeBarang = str(self.tbl_Penjualan_OrderPenjualan.item(a,0).text())
				jumlahDijual =  str(self.tbl_Penjualan_OrderPenjualan.item(a,2).text())
				query = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` LIKE '"+kodeBarang+"'"
				stok = self.DatabaseRunQuery(query)[0][7]
				stok = int(stok - long(jumlahDijual))
				self.DatabaseInsertReplace(self.dbDatabase,"gd_data_produk",
															"kodeBarang", kodeBarang,
															["stok"],
															[stok])
		query = "SELECT SUM(`harga`*`jumlah`) FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		totalHarga = str(self.DatabaseRunQuery(query)[0][0])
		print totalSaldoPiutang
		query = "INSERT INTO `"+self.dbDatabase+"`.`gd_piutang`"+\
				"(`kodePelanggan`, `kodeTransaksi`, `hargaTotal`) "+\
				"VALUES ('"+kodePelanggan+"', '"+kodeTransaksi+"', '"+totalHarga+"');"
		self.DatabaseRunQuery(query)
		
		query2 = "INSERT INTO `"+self.dbDatabase+"`.`gd_invoice_penjualan`"+\
				"(`kodeTransaksi`, `kodePelanggan`, `totalHarga`, `tanggal`, `kodeMatauang`) "+\
				"VALUES ('"+kodeTransaksi+"', '"+kodePelanggan+"', '"+totalHarga+"', '"+tanggal+"', '"+kodeMatauang+"');"
		self.DatabaseRunQuery(query2)

	def Penjualan_OrderPenjualan_Batal(self):
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Penjualan_OrderPenjualan.removeRow(a)
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		del_query = "DELETE FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		self.DatabaseRunQuery(del_query)

	def HapusBaris(self, namaTabel):
		#print self.tbl_Penjualan_OrderPenjualan.currentRow()
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		currentRow = self.tbl_Penjualan_OrderPenjualan.currentRow()
		kodeBarang = str(self.tbl_Penjualan_OrderPenjualan.item(currentRow,0).text())
		query = "DELETE FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"' AND `kodeBarang` LIKE '"+kodeBarang+"';"
		self.DatabaseRunQuery(query)
		namaTabel.removeRow(currentRow)
		
	def Penjualan_GoTo_Pengiriman(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PENGIRIMAN)
		
	def Penjualan_GoTo_Pengiriman_Baru(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PENGIRIMANB)
	
	def Penjualan_GoTo_PiutangUsaha(self):
		jumlahRow = self.tbl_Penjualan_Piutang.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow+1):
				self.tbl_Penjualan_Piutang.removeRow(x)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PU)
		query = "SELECT `kodePelanggan`, SUM(`totalSaldo`) FROM `gd_piutang` GROUP BY `kodePelanggan`"
		result = self.DatabaseRunQuery(query)
		for a in range (0,len(result)):
			kodePelanggan = str(result[a][0])
			query = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` LIKE '"+kodePelanggan+"'"
			nama = str(self.DatabaseRunQuery(query)[0][2])
			saldoPiutang = str(int(result[a][1]))
			self.tbl_Penjualan_Piutang.insertRow(a)
			self.tbl_Penjualan_Piutang.setItem(a,0,QtGui.QTableWidgetItem(nama)) #nama
			self.tbl_Penjualan_Piutang.setItem(a,4,QtGui.QTableWidgetItem(saldoPiutang)) #nama
		query = "SELECT SUM(totalSaldo) FROM `gd_piutang`"
		self.lb_Penjualan_Piutang_TotalNilai.setText("Rp "+str(int(self.DatabaseRunQuery(query)[0][0])))
		
	def Penjualan_GoTo_PiutangUsaha_Rincian(self):
		currentRow = self.tbl_Penjualan_Piutang.currentRow()
		nama = str(self.tbl_Penjualan_Piutang.item(currentRow,0).text())
		query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = str(self.DatabaseRunQuery(query)[0][1])
		jumlahRow = self.tbl_Penjualan_RincianPiutang.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Penjualan_RincianPiutang.removeRow(x)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_RPU)
		self.lb_Penjualan_RincianPiutang_title_nama.setText(nama)
		query = "SELECT * FROM `gd_piutang` WHERE `kodePelanggan` LIKE '"+kodePelanggan+"'"
		result = self.DatabaseRunQuery(query)
		print result
		for a in range (0,len(result)):
			self.tbl_Penjualan_RincianPiutang.insertRow(a)
			self.tbl_Penjualan_RincianPiutang.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][5])))
			self.tbl_Penjualan_RincianPiutang.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][2])))
		return
	
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
		
		self.initDatabase()
		cursor = self.db.cursor()
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
			#------                      Untuk Select *, return list dgn elemen2 kosong untuk menghindari error
			if (query.find("SELECT")!=-1):
				self.db.close()
				tables = (re.findall("`(\w+)`",query))
				for table in tables:
					#--------------------pastikan bukan database, tapi nama table
					if (table!=self.dbDatabase):
						sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='"+str(table)+"';"
						hasil = self.DatabaseRunQuery(sql) #-- scary recursive
						result = []
						for x in range(0,len(hasil)):
							result.append("-")
						#~ self.db.close()
						return result
			print repr(e)
			self.statusbar.showMessage(repr(e),120000)
			#~ sql = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='"+self.dbDatabase+"' AND `TABLE_NAME`='gd_satuan_pengukuran';"
			return
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
			return True
		except:
			return False
	def DatabaseInsertReplace(self,db,table,keyfield,keyvalue,fields,values):
		"""masukkan (list) values pada (list) fields ke table dengan keyfield dan value tertentu, bila sudah ada update, bila belum insert
		note that keyfield must be rewritten on fields too, due too incase keyfields keyvalue is just in-purpose-False escaper that is not used
		if keyfield == None, then it's plain insert
		15 Jan 2015 06:37
		"""
		ada_data = False
		if keyfield==None:
			ada_data = False
		elif (type(keyvalue) == str):
			sql = "SELECT * FROM `"+table+"` WHERE `"+str(keyfield)+"` LIKE '"+str(keyvalue)+"' ;"
			data = self.DatabaseRunQuery(sql)
			if len(data)>0:
				ada_data = True
		else:
			sql = "SELECT * FROM `"+table+"` WHERE `"+str(keyfield)+"` = "+str(keyvalue)+" ;"
			data = self.DatabaseRunQuery(sql)
			if len(data)>0:
				ada_data = True
		if len(fields)!=len(values):
			#salah
			return False
		if (ada_data):
			sql = "UPDATE `"+db+"`.`"+table+"` SET "
			for x in range(0,len(fields)):
				#-- kalau null, atau current timestamp (sql contant/reserved word) tidak pakai petik
				if (str(values[x])=="NULL" or str(values[x])=="CURRENT_TIMESTAMP"):sql = sql + " `"+str(fields[x])+"` = "+str(values[x])+", "
				else:sql = sql + " `"+str(fields[x])+"` = '"+str(values[x])+"', "
				#~ sql = sql + " `"+str(fields[x])+"` = '"+str(values[x])+"', "
			#remove last koma , (-2karakter: dengan spasi setelahnya)
			sql = sql[:-2]
			if (type(keyvalue) == str):
				sql = sql+" WHERE `"+table+"`.`"+str(keyfield)+"` LIKE '"+str(keyvalue)+"';"
			else:
				sql = sql+" WHERE `"+table+"`.`"+str(keyfield)+"` = "+str(keyvalue)+";"
		else:
			sql = "INSERT INTO `"+db+"`.`"+table+"` ("
			for x in range(0,len(fields)):
				sql = sql + " `"+str(fields[x])+"`, "
			sql = sql[:-2]
			sql = sql + ") VALUES ("
			for x in range(0,len(values)):
				#-- kalau null, atau current timestamp (sql contant/reserved word) tidak pakai petik
				if (str(values[x])=="NULL" or str(values[x])=="CURRENT_TIMESTAMP"):sql = sql + " "+str(values[x])+", "
				else:sql = sql + " '"+str(values[x])+"', "
				#~ sql = sql + " '"+str(values[x])+"', "
			sql = sql[:-2]
			sql = sql + ");"
		self.DatabaseRunQuery(sql)
		return True
	def DatabaseInsertAvoidreplace(self,db,table,keyfield,keyvalue,fields,values,showPopupText=False,showPopupFunctionCallback=False):
		"""Masukkan (list) values pada (list) fields ke table dengan keyfield dan value tertentu,
		bila sudah ada batal insert & muncul popup peringatan (diaktivasi), bila belum insert aja"""
		
		if (type(keyvalue) == str):
			sql = "SELECT * FROM `"+table+"` WHERE `"+str(keyfield)+"` LIKE '"+str(keyvalue)+"' ;"
		else:
			sql = "SELECT * FROM `"+table+"` WHERE `"+str(keyfield)+"` = "+str(keyvalue)+" ;"
		data = self.DatabaseRunQuery(sql)
		ada_data = False
		if len(data)>0:
			ada_data = True
		if len(fields)!=len(values):
			#salah
			return False			
		if (ada_data):
			if (showPopupText!=False):
				if showPopupFunctionCallback==False:
					showPopupFunctionCallback = self.DataMaster_None
				self.DataMaster_Popup(str(showPopupText),showPopupFunctionCallback)
			else:
				self.statusbar.showMessage("Penambahan data tidak dilakukan karena terdapat data duplikat untuk "+str(keyvalue),30000)
			return False
		else:
			sql = "INSERT INTO `"+db+"`.`"+table+"` ("
			for x in range(0,len(fields)):
				sql = sql + " `"+str(fields[x])+"`, "
			sql = sql[:-2]
			sql = sql + ") VALUES ("
			for x in range(0,len(values)):
				#-- kalau null, atau current timestamp (sql contant/reserved word) tidak pakai petik
				if (str(values[x])=="NULL" or str(values[x])=="CURRENT_TIMESTAMP"):sql = sql + " "+str(values[x])+", "
				else:sql = sql + " '"+str(values[x])+"', "
			sql = sql[:-2] #-- remove last ", "
			sql = sql + ");"
		self.DatabaseRunQuery(sql)
		return True
	def DatabaseFetchResult(self,db,table,keyfield=False,keyvalue=False):
		""" biasa fetch result wae result in array, 
		misal data = self.DatabaseFetchResult(self.dbDatabase,"gd_nama_alamat","kodePelanggan","%MAKIN%")"""
		if keyfield==False:
			return self.DatabaseRunQuery("SELECT * FROM `"+str(db)+"`.`"+str(table)+"`; ")
		elif (type(keyvalue)==list):
			sql = "SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE "
			for x in xrange(0,len(keyvalue)):
				sql = sql + "`"+str(keyfield[x])+"` LIKE '"+str(keyvalue[x])+"' AND "
			sql = sql[:-4] #-- remove last "AND "
			return self.DatabaseRunQuery(sql)
		elif (type(keyvalue)==str):
			return self.DatabaseRunQuery("SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE `"+str(keyfield)+"` LIKE '"+str(keyvalue)+"';")
		else:
			return self.DatabaseRunQuery("SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE `"+str(keyfield)+"` = "+str(keyvalue)+";")
	
	def clearTable(self,tableobject):
		#at first we clear the rows
		for r in range(0,tableobject.rowCount()+1):
			tableobject.removeRow(r)
		tableobject.setRowCount(0)
	
	def GarvinValidate(self,lineedit,regexp=None):
		"""validate line edit input based on regexp if yielded, or just around alphanumeric
			default : alphanumeric
			"angka" : digit
			"huruf" : huruf
		"""
		if (regexp==None): #-- default
			regexp = QRegExp("[-a-zA-Z0-9\s\.]*")
			lineedit.setValidator(QRegExpValidator(regexp))
		elif (regexp.lower()=="angka"):
			regexp = QRegExp("[0-9\.]*")
			lineedit.setValidator(QRegExpValidator(regexp))
		elif (regexp.lower()=="huruf"):
			regexp = QRegExp("[-a-zA-Z\s\.]*")
			lineedit.setValidator(QRegExpValidator(regexp))
		elif (regexp.lower()=="search"):
			regexp = QRegExp("[-a-zA-Z0-9\s:.]*")
			lineedit.setValidator(QRegExpValidator(regexp))
		else:
			regexp = QRegExp(regexp)
			lineedit.setValidator(QRegExpValidator(regexp))
if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	dmw = MainGUI()
	#~ dmw.showFullScreen()
	sys.exit(app.exec_())
