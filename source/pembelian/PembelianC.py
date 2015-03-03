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

class Pembelian(object):
	def Pembelian__init(self):
		#inisialisasisiasi INDEX Halaman Pembelian
		self.INDEX_ST_PEMBELIAN_MENU = 0
		self.INDEX_ST_PEMBELIAN_INVOICEPEMBELIAN = 1
		self.INDEX_ST_PEMBELIAN_INVOICEPEMBELIAN_BARU = 2
		self.INDEX_ST_PEMBELIAN_OP_TAMBAHPRODUK = 3
		self.INDEX_ST_PEMBELIAN_PENERIMAAN = 4
		self.INDEX_ST_PEMBELIAN_HUTANG = 5
		self.INDEX_ST_PEMBELIAN_HUTANG_RINCIAN = 6
		self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG = 7
		self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN = 8	
		
		#Tombol Pada Halaman Menu
		self.tb_Pembelian_InvoicePembelian.clicked.connect(self.Pembelian_GoTo_InvoicePembelian)
		self.tb_Pembelian_HutangUsaha.clicked.connect(self.Pembelian_GoTo_HutangUsaha)
		self.tb_Pembelian_PembayaranHutang.clicked.connect(self.Pembelian_GoTo_PembayaranHutang)
		self.tb_Pembelian_ReturPembelian.clicked.connect(self.Pembelian_GoTo_ReturPembelian)
		
		#Tombol pada Invoice Pembelian
		self.tb_Pembelian_InvoicePembelian_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		self.tb_Pembelian_InvoicePembelian_Baru.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Baru)
		self.tb_Pembelian_InvoicePembelian_Rincian.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Rincian)
		self.tbl_Pembelian_InvoicePembelian.cellDoubleClicked.connect(self.Pembelian_GoTo_InvoicePembelian_Rincian)
		
		#Tombol pada Invoice Pembelian Baru
		self.tb_Pembelian_InvoicePembelian_Baru_TambahBaris.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Baru_TambahBaris)
		self.tb_Pembelian_InvoicePembelian_Baru_HapusBaris.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Baru_HapusBaris)
		self.tb_Pembelian_InvoicePembelian_Baru_Rekam.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Baru_Rekam)
		self.tb_Pembelian_InvoicePembelian_Baru_Tutup.clicked.connect(self.Pembelian_GoTo_InvoicePembelian)
		self.tb_Pembelian_InvoicePembelian_Baru_Batal.clicked.connect(self.Pembelian_GoTo_InvoicePembelian_Batal)
		self.tbl_Pembelian_InvoicePembelian_Baru.cellDoubleClicked.connect(self.Pembelian_GoTo_InvoicePembelian_Baru_PilihVendor)
		self.tbl_Pembelian_InvoicePembelian_Baru.cellChanged.connect(self.Pembelian_GoTo_InvoicePembelian_Baru_TotalHarga)
		
		#~ self.tb_Pembelian_InvoicePembelian_Baru_Nama.clicked.connect(functools.partial())
		
		#Tombol pada Hutang Usaha
		self.tb_Pembelian_HutangUsaha_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		self.tb_Pembelian_HutangUsaha_Perincian.clicked.connect(self.Pembelian_GoTo_HutangUsaha_Rincian)
		self.tb_Pembelian_RincianHutang_Tutup.clicked.connect(self.Pembelian_GoTo_HutangUsaha)
		
		#Tombol pada Pembayaran Hutang
		
		#Tombol pada Retur Pembelian
	
	def Pembelian_GoTo_Menu(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_MENU)
		return	
	
	def Popup_NamaAlamat(self, namaTombol):
		data = []
		def isi():
			namaTombol.setText(str(data[0]))
		def batal():
			namaTombol.setText("-")
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi,batal)
			
	def Pembelian_GoTo_InvoicePembelian(self):
		jumlahRow = self.tbl_Pembelian_InvoicePembelian.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Pembelian_InvoicePembelian.removeRow(x)
		self.tbl_Pembelian_InvoicePembelian.setRowCount(0)
		query = "SELECT * FROM `gd_invoice_penjualan` GROUP BY `kodeTransaksi`"
		result = self.DatabaseRunQuery(query)
		for a in range (0,len(result)):
			self.tbl_Pembelian_InvoicePembelian.insertRow(a)
			self.tbl_Pembelian_InvoicePembelian.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][1]))) #noinvoice
			self.tbl_Pembelian_InvoicePembelian.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][4]))) #tanggal
			self.tbl_Pembelian_InvoicePembelian.setItem(a,2,QtGui.QTableWidgetItem("IDR")) #kurs
			self.tbl_Pembelian_InvoicePembelian.setItem(a,3,QtGui.QTableWidgetItem(str(result[a][6]))) #nilai
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_INVOICEPEMBELIAN)
		return
	
	def Pembelian_GoTo_InvoicePembelian_Rincian(self):
		self.tbl_Pembelian_InvoicePembelian_Baru.setColumnWidth(0,200)
		self.tbl_Pembelian_InvoicePembelian_Baru.setColumnWidth(1,200)
		curRow = self.tbl_Pembelian_InvoicePembelian.currentRow()
		noInvoice = str(self.tbl_Pembelian_InvoicePembelian.item(curRow,0).text())
		self.le_Pembelian_InvoicePembelian_Baru_NoPO.setText(noInvoice)
		query = "SELECT * FROM `gd_pembelian_barang` WHERE `noInvoice` LIKE '"+noInvoice+"'"
		result = self.DatabaseRunQuery(query)
		jumlahRow = self.tbl_Pembelian_InvoicePembelian_Baru.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Pembelian_InvoicePembelian_Baru.removeRow(x)
		self.tbl_Pembelian_InvoicePembelian_Baru.setRowCount(0)
		for a in range (0,len(result)):
			self.tbl_Pembelian_InvoicePembelian_Baru.insertRow(a)
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][4]))) #supplier
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][3]))) #barang
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][6]))) #jumlah
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,3,QtGui.QTableWidgetItem(str(result[a][7]))) #satuan
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][5]))) #harga
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,6,QtGui.QTableWidgetItem(str(result[a][8]))) #total harga
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_INVOICEPEMBELIAN_BARU)
		return
	
	def Pembelian_GoTo_InvoicePembelian_Baru(self):
		self.le_Pembelian_InvoicePembelian_Baru_NoPO.setText("")
		self.tbl_Pembelian_InvoicePembelian_Baru.setColumnWidth(0,200)
		self.tbl_Pembelian_InvoicePembelian_Baru.setColumnWidth(1,200)
		jumlahRow = self.tbl_Pembelian_InvoicePembelian_Baru.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Pembelian_InvoicePembelian_Baru.removeRow(x)
		self.tbl_Pembelian_InvoicePembelian_Baru.setRowCount(0)
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_INVOICEPEMBELIAN_BARU)
		return

	def Pembelian_GoTo_InvoicePembelian_Baru_TambahBaris(self):
		jumlahRow = self.tbl_Pembelian_InvoicePembelian_Baru.rowCount()
		a = jumlahRow
		self.tbl_Pembelian_InvoicePembelian_Baru.insertRow(a)
		self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,2,QtGui.QTableWidgetItem("0"))
		self.tbl_Pembelian_InvoicePembelian_Baru.setItem(a,4,QtGui.QTableWidgetItem("0"))
		return
	
	def Pembelian_GoTo_InvoicePembelian_Baru_PilihVendor(self, row, col):
		if (col==0):
			self.Popup_NamaAlamat_Tabel(self.tbl_Pembelian_InvoicePembelian_Baru,row)
		pass
		
	def Pembelian_GoTo_InvoicePembelian_Baru_TotalHarga(self,row,col):
		try:
			jumlah = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(row,2).text())
			harga = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(row,4).text())
			totalHarga = int(jumlah)*int(harga)
			self.tbl_Pembelian_InvoicePembelian_Baru.setItem(row,6,QtGui.QTableWidgetItem(str(totalHarga)))
		except:
			pass
		return
	
	def Pembelian_GoTo_InvoicePembelian_Baru_HapusBaris(self):
		currentRow = self.tbl_Pembelian_InvoicePembelian_Baru.currentRow()
		self.tbl_Pembelian_InvoicePembelian_Baru.removeRow(currentRow)
		pass
	
	def Pembelian_GoTo_InvoicePembelian_Batal(self):
		jumlahRow = self.tbl_Pembelian_InvoicePembelian_Baru.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Pembelian_InvoicePembelian_Baru.removeRow(x)
		self.tbl_Pembelian_InvoicePembelian_Baru.setRowCount(0)
		self.le_Pembelian_InvoicePembelian_Baru_NoPO.setText("")
		self.Pembelian_GoTo_InvoicePembelian()
		pass
		
	def Pembelian_GoTo_InvoicePembelian_Baru_Rekam(self):
		noInvoice = str(self.le_Pembelian_InvoicePembelian_Baru_NoPO.text())
		jumlahRow = self.tbl_Pembelian_InvoicePembelian_Baru.rowCount()
		for a in range(0, jumlahRow):
			namaBarang = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,1).text())
			kodeVendor = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,0).text())
			hargaBarang = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,4).text())
			jumlahBarang = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,2).text())
			satuan = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,3).text())
			totalHarga = str(self.tbl_Pembelian_InvoicePembelian_Baru.item(a,6).text())
			query = "INSERT INTO `"+self.dbDatabase+"`.`gd_pembelian_barang`"+\
				"(`noInvoice`, `namaBarang`, `kodeVendor`, `hargaBarang`, `jumlahBarang`, `satuan`, `totalHarga`) "+\
				"VALUES ('"+noInvoice+"', '"+namaBarang+"', '"+kodeVendor+"', '"+hargaBarang+"', '"+jumlahBarang+"', '"+satuan+"', '"+totalHarga+"');"
			self.DatabaseRunQuery(query)
		self.Pembelian_GoTo_InvoicePembelian()
		return
	
	def Pembelian_GoTo_OrderPembelian_TambahProduk(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_OP_TAMBAHPRODUK)
		self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Satuan.clear()
		self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Nama.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Jumlah.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Harga.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Diskon.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Pajak.clear()
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Kode.clear()
		
		#Autocomplete dianu meneh
		query = "SELECT * FROM gd_data_produk"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Nama.addItem(self.DatabaseRunQuery(query)[a][5])
		query = "SELECT * FROM gd_satuan_pengukuran"
		for a in range(0,len(self.DatabaseRunQuery(query))):
			self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Satuan.addItem(self.DatabaseRunQuery(query)[a][2])
		nama = str(self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+nama+"'"
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Kode.setText(kodeBarang)
		return
	
	def Pembelian_OrderPembelian_TambahProduk(self):
		#nama = str(self.tb_Pembelian_OrderPembelian_Nama.text())
		#query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = str(self.tb_Pembelian_OrderPembelian_Nama.text())
		kodeTransaksi = str(self.le_Pembelian_OrderPembelian_NoPO.text())
		kodeBarang = str(self.le_Pembelian_OrderPembelian_TambahProduk_Input_Kode.text())
		jumlah = str(self.le_Pembelian_OrderPembelian_TambahProduk_Input_Jumlah.text())
		harga = str(self.le_Pembelian_OrderPembelian_TambahProduk_Input_Harga.text())
		diskon = str(self.le_Pembelian_OrderPembelian_TambahProduk_Input_Diskon.text())
		pajak = str(self.le_Pembelian_OrderPembelian_TambahProduk_Input_Pajak.text())
		query = "SELECT * FROM `gd_data_pajak` WHERE `namaPajak` LIKE '"+pajak+"'"
		tanggalMasuk = str(self.dte_Pembelian_OrderPembelian_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		try:
			kodePajak = str(self.DatabaseRunQuery(query)[0][1])
		except:
			kodePajak = ""
		kodeMatauang = str(self.cb_Pembelian_OrderPembelian_Kurs.currentText())
		query = "INSERT INTO `gd_order_pembelian` (`kodeTransaksi`,`kodeMatauang`,`kodePelanggan`,`kodeBarang`"+\
			",`jumlah`,`harga`,`diskon`,`kodePajak`) VALUES"+\
			"('"+kodeTransaksi+"','"+kodeMatauang+"','"+kodePelanggan+"','"+kodeBarang+"','"+jumlah+"','"+harga+"','"+diskon+"','"+kodePajak+"')"
		self.DatabaseRunQuery(query)
		
		query2 = "INSERT INTO `gd_data_penyimpanan` (`kodeBarang`,`tanggalMasuk`,`hargaBeli`,`pemasok`,`stok`,`kurs`) VALUES ('"+kodeBarang+"','"+tanggalMasuk+"','"+harga+"','"+kodePelanggan+"','"+jumlah+"','"+kodeMatauang+"')"
		self.DatabaseRunQuery(query2)
		
		jumlahRow = self.tbl_Pembelian_OrderPembelian.rowCount()
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Pembelian_OrderPembelian.removeRow(a)
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_ORDERPEMBELIAN)
		query = "SELECT * FROM `gd_order_pembelian` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		result = self.DatabaseRunQuery(query)
		if len(result) != 0:
			for a in range(0,len(result)):
				print "tambah row"
				self.tbl_Pembelian_OrderPembelian.insertRow(a)
				self.tbl_Pembelian_OrderPembelian.setItem(a,0,QtGui.QTableWidgetItem(result[a][4])) #kode
				sql = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` = '"+result[a][4]+"'"
				self.tbl_Pembelian_OrderPembelian.setItem(a,1,QtGui.QTableWidgetItem(str(self.DatabaseRunQuery(sql)[0][5]))) #nama produk
				kodeSatuan = str(self.DatabaseRunQuery(sql)[0][3])
				satuan_query =  "SELECT * FROM `gd_satuan_pengukuran` WHERE `kodeSatuan` = '"+kodeSatuan+"'"
				satuan = str(self.DatabaseRunQuery(satuan_query)[0][2])
				self.tbl_Pembelian_OrderPembelian.setItem(a,3,QtGui.QTableWidgetItem(satuan)) #satuan
				self.tbl_Pembelian_OrderPembelian.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][5]))) #jumlah
				self.tbl_Pembelian_OrderPembelian.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][6]))) #harga
				self.tbl_Pembelian_OrderPembelian.setItem(a,5,QtGui.QTableWidgetItem(result[a][7])) #diskon
				total = result[a][6]*result[a][5]
				self.tbl_Pembelian_OrderPembelian.setItem(a,6,QtGui.QTableWidgetItem(str(total))) #total harga
				self.tbl_Pembelian_OrderPembelian.setItem(a,7,QtGui.QTableWidgetItem(result[a][8])) #pajak
		
	def Pembelian_OrderPembelian_TambahProduk_UpdateKode(self):
		namaProduk = str(self.cb_Pembelian_OrderPembelian_TambahProduk_Input_Nama.currentText())
		query = "SELECT * FROM `gd_data_produk` WHERE `namaBarang` LIKE '"+namaProduk+"'"
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Kode.setText
		kodeBarang = self.DatabaseRunQuery(query)[0][1]
		self.le_Pembelian_OrderPembelian_TambahProduk_Input_Kode.setText(kodeBarang)
		pass
	
	def Pembelian_OrderPembelian_Batal(self):
		jumlahRow = self.tbl_Pembelian_OrderPembelian.rowCount()
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Pembelian_OrderPembelian.removeRow(a)
		kodeTransaksi = str(self.le_Pembelian_OrderPembelian_NoPO.text())
		del_query = "DELETE FROM `gd_order_pembelian` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		self.DatabaseRunQuery(del_query)
		
	def Pembelian_OrderPembelian_HapusBaris(self):
		kodeTransaksi = str(self.le_Pembelian_OrderPembelian_NoPO.text())
		currentRow = self.tbl_Pembelian_OrderPembelian.currentRow()
		kodeBarang = str(self.tbl_Pembelian_OrderPembelian.item(currentRow,0).text())
		query = "DELETE FROM `gd_order_pembelian` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"' AND `kodeBarang` LIKE '"+kodeBarang+"';"
		self.DatabaseRunQuery(query)
		self.tbl_Pembelian_OrderPembelian.removeRow(currentRow)
		
	def Pembelian_OrderPembelian_Rekam(self):
		#nama = str(self.tb_Pembelian_OrderPembelian_Nama.text())
		#query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = str(self.tb_Pembelian_OrderPembelian_Nama.text())
		kodeTransaksi = str(self.le_Pembelian_OrderPembelian_NoPO.text())
		jumlahRow = self.tbl_Pembelian_OrderPembelian.rowCount()
		tanggalMasuk = str(self.dte_Pembelian_OrderPembelian_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		kodeMatauang = str(self.cb_Pembelian_OrderPembelian_Kurs.currentText())
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				kodeBarang = str(self.tbl_Pembelian_OrderPembelian.item(a,0).text())
				jumlahDibeli =  str(self.tbl_Pembelian_OrderPembelian.item(a,2).text())
				query = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` LIKE '"+kodeBarang+"'"
				stok = self.DatabaseRunQuery(query)[0][7]
				stok = int(stok + long(jumlahDibeli))
				self.DatabaseInsertReplace(self.dbDatabase,"gd_data_produk",
															"kodeBarang", kodeBarang,
															["stok"],
															[stok])
		query = "SELECT SUM(`harga`*`jumlah`) FROM `gd_order_pembelian` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		totalHarga = str(self.DatabaseRunQuery(query)[0][0])
		print totalSaldoHutang
		print kodePelanggan
		query = "INSERT INTO `"+self.dbDatabase+"`.`gd_hutang`"+\
				"(`kodePelanggan`, `kodeTransaksi`, `hargaTotal`) "+\
				"VALUES ('"+kodePelanggan+"', '"+kodeTransaksi+"', '"+totalHarga+"');"
		self.DatabaseRunQuery(query)
		
		query2 = "INSERT INTO `"+self.dbDatabase+"`.`gd_invoice_pembelian`"+\
				"(`kodeTransaksi`, `kodePelanggan`, `totalHarga`, `tanggal`, `kodeMatauang`) "+\
				"VALUES ('"+kodeTransaksi+"', '"+kodePelanggan+"', '"+totalHarga+"', '"+tanggalMasuk+"', '"+kodeMatauang+"');"
		self.DatabaseRunQuery(query2)
	
	def Pembelian_GoTo_HutangUsaha(self):
		self.tbl_Pembelian_HutangUsaha.setColumnWidth(0,300) #perbesar kolom nama pelanggan
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_HUTANG)
		jumlahRow = self.tbl_Pembelian_HutangUsaha.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow+1):
				self.tbl_Pembelian_HutangUsaha.removeRow(x)
		query = "SELECT * FROM `gd_pembelian_barang` GROUP BY `kodeVendor`"
		data = self.DatabaseRunQuery(query)
		querytotal = "SELECT  SUM(`totalHarga`) FROM `gd_pembelian_barang` GROUP BY `kodeVendor`"
		result = self.DatabaseRunQuery(querytotal)
		for a in range (0,len(result)):
			kodePelanggan = str(data[a][4])
			print data
			print kodePelanggan
			query = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` LIKE '"+kodePelanggan+"'"
			nama = str(self.DatabaseRunQuery(query)[0][2])
			totalHutang = str(int(result[a][0]))
			self.tbl_Pembelian_HutangUsaha.insertRow(a)
			self.tbl_Pembelian_HutangUsaha.setItem(a,0,QtGui.QTableWidgetItem(kodePelanggan)) #kode
			self.tbl_Pembelian_HutangUsaha.setItem(a,1,QtGui.QTableWidgetItem(nama)) #nama
			self.tbl_Pembelian_HutangUsaha.setItem(a,4,QtGui.QTableWidgetItem(totalHutang)) #hutang saldo	
		#query = "SELECT SUM(`jumlahTagihan`) FROM `gd_hutang`"
		#self.lb_Pembelian_HutangUsaha_TotalNilai.setText("Rp "+str(int(self.DatabaseRunQuery(query)[0][0])))
		return
	
	def Pembelian_GoTo_HutangUsaha_Rincian(self):
		currentRow = self.tbl_Pembelian_HutangUsaha.currentRow()
		nama = str(self.tbl_Pembelian_HutangUsaha.item(currentRow,1).text())
		query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = str(self.DatabaseRunQuery(query)[0][1])
		jumlahRow = self.tbl_Pembelian_RincianHutang.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Pembelian_RincianHutang.removeRow(x)
		self.tbl_Pembelian_RincianHutang.setRowCount(0)
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_HUTANG_RINCIAN)
		self.lb_Pembelian_RincianHutang_Title_Nama.setText(nama)
		query = "SELECT * FROM `gd_pembelian_barang` WHERE `kodeVendor` LIKE '"+kodePelanggan+"' GROUP BY `noInvoice`"
		result = self.DatabaseRunQuery(query)
		for a in range (0,len(result)):
			self.tbl_Pembelian_RincianHutang.insertRow(a)
			self.tbl_Pembelian_RincianHutang.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][1])))
		return
	
	def Pembelian_GoTo_PembayaranHutang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG)
		return
	
	def Pembelian_GoTo_ReturPembelian(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN)
		return
	
