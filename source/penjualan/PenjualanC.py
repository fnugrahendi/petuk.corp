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

class Penjualan(object):
	def Penjualan_init(self):
		#---------------------------------------------------------------Penjualan Init Itut
		self.st_Penjualan.setCurrentIndex(0)
		#Tombol pada Halaman Menu
		self.tb_Penjualan_Invoice.clicked.connect(self.Penjualan_GoTo_Invoice)
		self.tb_Penjualan_OrderPenjualan.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_Piutang.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		self.tb_Penjualan_UangMuka.clicked.connect(self.Penjualan_GoTo_UangMuka)
		
		#Tombol pada invoice
		self.tb_Penjualan_DaftarInvoice_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_DaftarInvoice_Baru.clicked.connect(self.Penjualan_GoTo_Invoice_Baru)
		self.tb_Penjualan_DaftarInvoice_Rincian.clicked.connect(self.Penjualan_GoTo_Invoice_Rincian)
		
		#Tombol pada Invoice baru
		self.tb_Penjualan_InvoicePenjualan_Baru_Nama.clicked.connect(functools.partial(self.Popup_NamaAlamat,self.tb_Penjualan_InvoicePenjualan_Baru_Nama))
		self.tb_Penjualan_InvoicePenjualan_Tutup.clicked.connect(self.Penjualan_GoTo_Invoice)
		self.tb_Penjualan_InvoicePenjualan_Input_KodeProduk.clicked.connect(functools.partial(self.Popup_Produk,self.tb_Penjualan_InvoicePenjualan_Input_KodeProduk))
		self.tb_Penjualan_InvoicePenjualan_Input_HargaPokok.clicked.connect(self.Penjualan_GoTo_Invoice_TambahBarang)
		self.tb_Penjualan_InvoicePenjualan_Rekam.clicked.connect(self.Penjualan_Invoice_Rekam)
		self.tb_Penjualan_Invoice_TambahBarang_Tabel_Tambah.clicked.connect(self.Penjualan_Invoice_TambahBarang_TambahBaris)
		self.Penjualan_Invoice_TambahBarang_Batal.clicked.connect(self.Penjualan_GoTo_Invoice_Batal)
		self.tb_Penjualan_Invoice_TambahBarang_Simpan.clicked.connect(self.Penjualan_Invoice_TambahBarang_Simpan)
		
		#selain tombol
		self.tbl_Penjualan_Invoice_TambahBarang.cellDoubleClicked.connect(self.Penjualan_Invoice_TambahBarang_PilihVendor)
		self.le_Penjualan_InvoicePenjualan_Input_HargaJual.textChanged.connect(self.Penjualan_Invoice_TotalHarga)
		self.le_Penjualan_InvoicePenjualan_Input_Jumlah.textChanged.connect(self.Penjualan_Invoice_TotalHarga)
		self.tbl_Penjualan_Invoice_TambahBarang.cellChanged.connect(self.Penjualan_Invoice_TambahBarang_TotalHarga)
		self.tbl_Penjualan_Piutang.cellDoubleClicked.connect(self.Penjualan_GoTo_PiutangUsaha_Rincian)
		self.tbl_Penjualan_RincianPiutang.cellDoubleClicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		
		#Tombol&Sinyal pada Halaman OrderPenjualan
		self.tb_Penjualan_OrderPenjualan_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_OrderPenjualan_Baru.clicked.connect(self.Penjualan_GoTo_OP_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Batal.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_OrderPenjualan_TambahProduk_Simpan.clicked.connect(self.Penjualan_OrderPenjualan_TambahProduk)
		self.tb_Penjualan_OrderPenjualan_HapusBaris.clicked.connect(functools.partial(self.Penjualan_HapusBaris,self.tbl_Penjualan_OrderPenjualan))
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
		self.tb_Penjualan_RincianPiutang_Perincian.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		self.tb_Penjualan_PembayaranPiutang_Baru.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang_Baru)
		self.tb_Penjualan_PembayaranPiutang_Baru_Batal.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		self.tb_Penjualan_PembayaranPiutang_Baru_Akun.clicked.connect(functools.partial(self.Popup_Rekening, self.tb_Penjualan_PembayaranPiutang_Baru_Akun))
		
		#Tombol pada Halaman UangMuka
		self.tb_Penjualan_UangMuka_Kembali.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_Penjualan_UangMuka_BuatBaru.clicked.connect(self.Penjualan_GoTo_UangMuka_Baru)
		self.tb_Penjualan_UangMuka_Baru_Batal.clicked.connect(self.Penjualan_GoTo_UangMuka)
		
		self.INDEX_ST_PENJUALAN_MENU = 0
		self.INDEX_ST_PENJUALAN_DI = 1
		self.INDEX_ST_PENJUALAN_IP = 2
		self.INDEX_ST_PENJUALAN_I_TB = 3
		self.INDEX_ST_PENJUALAN_OP = 4
		self.INDEX_ST_PENJUALAN_PENGIRIMAN = 5
		self.INDEX_ST_PENJUALAN_PENGIRIMANB = 6
		self.INDEX_ST_PENJUALAN_PU = 8
		self.INDEX_ST_PENJUALAN_RPU = 9
		self.INDEX_ST_PENJUALAN_PP = 10
		self.INDEX_ST_PENJUALAN_PPB = 11
		self.INDEX_ST_PENJUALAN_UM = 12
		self.INDEX_ST_PENJUALAN_UMB = 13

	def Popup_Produk(self, namaTombol):
		data = []
		def isi():
			namaTombol.setText(str(data[0]))
			kodeProduk = namaTombol.text()
			query = "SELECT * FROM `gd_data_produk` WHERE `kodeBarang` LIKE '"+kodeProduk+"'"
			#print query
			nama = self.DatabaseRunQuery(str(query))
			#print nama
			self.le_Penjualan_InvoicePenjualan_Input_NamaProduk.setText(nama[0][5])
		def batal():
			namaTombol.setText("-")
		self.DataMaster_DataProduk_Popup_Pilih(data,isi,batal)
		print namaTombol.text()
		
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
		print "go to daftar invoice"
		rownum = self.tbl_Penjualan_DaftarInvoice.rowCount()
		self.tbl_Penjualan_DaftarInvoice.setColumnWidth(2,300)
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
		
	def Penjualan_Generate_NoInvoice(self):
		query = "SELECT * FROM `gd_invoice_penjualan`"
		dataInvoice = self.DatabaseRunQuery(query)
		lastRow = len(dataInvoice)-1
		kode = dataInvoice[lastRow][1]
		kodeNum = int(kode[3:7])
		kodePreset = kodeNum+1
		kodeInvoice = str(kodePreset)
		kodeInvoice = "INV000"+kodeInvoice
		self.le_Penjualan_InvoicePenjualan_SOPenawaran.setText(kodeInvoice)
	
	def Penjualan_GoTo_Invoice_Baru(self):
		self.Penjualan_Generate_NoInvoice()
		self.le_Penjualan_InvoicePenjualan_Input_Jumlah.setReadOnly(False)
		self.le_Penjualan_InvoicePenjualan_Input_HargaJual.setReadOnly(False)
		self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.setReadOnly(False)
		self.le_Penjualan_InvoicePenjualan_Input_NamaProduk.setReadOnly(False)
		self.le_Penjualan_InvoicePenjualan_Input_Jumlah.setText("0")
		self.le_Penjualan_InvoicePenjualan_Input_HargaJual.setText("0")
		self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.setText("0")
		self.tb_Penjualan_InvoicePenjualan_Input_KodeProduk.setText("-")
		self.tb_Penjualan_InvoicePenjualan_Baru_Nama.setText("-")
		self.le_Penjualan_InvoicePenjualan_Input_NamaProduk.setText("")
		self.le_Penjualan_InvoicePenjualan_Keterangan.setText("")
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_IP)
		
	def Penjualan_GoTo_Invoice_Rincian(self):
		currentRow = self.tbl_Penjualan_DaftarInvoice.currentRow()
		self.tb_Penjualan_InvoicePenjualan_Baru_Nama.setText(str(self.tbl_Penjualan_DaftarInvoice.item(currentRow,2).text()))
		self.le_Penjualan_InvoicePenjualan_SOPenawaran.setText(str(self.tbl_Penjualan_DaftarInvoice.item(currentRow,0).text()))
		self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.setText(str(self.tbl_Penjualan_DaftarInvoice.item(currentRow,4).text()))
		query = str("SELECT * FROM")
		#self.le_Penjualan_InvoicePenjualan_Input_Jumlah.setReadOnly(True)
		#self.le_Penjualan_InvoicePenjualan_Input_HargaJual.setReadOnly(True)
		#self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.setReadOnly(True)
		#self.le_Penjualan_InvoicePenjualan_Input_NamaProduk.setReadOnly(True)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_IP)
		
	def Penjualan_GoTo_Invoice_Batal(self):
		del self.SQLtoRun[:]
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_IP)
	
	def Penjualan_Invoice_TotalHarga(self):
		jumlah = str(self.le_Penjualan_InvoicePenjualan_Input_Jumlah.text())
		harga = str(self.le_Penjualan_InvoicePenjualan_Input_HargaJual.text())
		try:
			totalHarga = int(jumlah)*int(harga)
			self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.setText(str(totalHarga))
		except:
			pass
	
	def Penjualan_Invoice_Rekam(self):
		kodeTransaksi = str(self.le_Penjualan_InvoicePenjualan_SOPenawaran.text())
		kodePelanggan = str(self.tb_Penjualan_InvoicePenjualan_Baru_Nama.text())
		tanggal = str(self.dte_Penjualan_InvoicePenjualan_Input_Tanggal.dateTime().toString("yyyy-MM-dd"))
		catatan = str(self.le_Penjualan_InvoicePenjualan_Keterangan.text())
		nilai = str(self.le_Penjualan_InvoicePenjualan_Input_TotalHarga.text())
		hargaPokok = str(self.tb_Penjualan_InvoicePenjualan_Input_HargaPokok.text())
		query = "INSERT INTO `gd_invoice_penjualan` "+\
			"(`kodeTransaksi`,`kodePelanggan`,`tanggal`,`catatan`,`nilai`,`hargaPokok`) "+\
			"VALUES ('"+kodeTransaksi+"','"+kodePelanggan+"','"+tanggal+"','"+catatan+"','"+nilai+"','"+hargaPokok+"')"
		self.DatabaseRunQuery(str(query))
		jumlahBarang = len(self.SQLtoRun)
		for a in range(0,jumlahBarang):
			self.DatabaseRunQuery(self.SQLtoRun[a])
		del self.SQLtoRun[:]
		self.Penjualan_GoTo_Invoice()
		pass
	
	def Penjualan_GoTo_Invoice_TambahBarang(self):
		rownum = self.tbl_Penjualan_Invoice_TambahBarang.rowCount()
		for b in range (0, rownum):
			self.tbl_Penjualan_Invoice_TambahBarang.removeRow(b)
		self.tbl_Penjualan_Invoice_TambahBarang.setRowCount(0)
		self.tbl_Penjualan_Invoice_TambahBarang.setColumnWidth(0,300)
		noInvoice = str(self.le_Penjualan_InvoicePenjualan_SOPenawaran.text())
		query = "SELECT * FROM `gd_pembelian_barang` WHERE `noInvoice` LIKE '"+noInvoice+"'"
		barang = self.DatabaseRunQuery(query)
		if (len(barang) != 0):
			for i in range(0,len(barang)):
				self.tbl_Penjualan_Invoice_TambahBarang.insertRow(i)
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,0,QtGui.QTableWidgetItem(barang[i][4])) #vendor
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,1,QtGui.QTableWidgetItem(barang[i][3])) #barang
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,2,QtGui.QTableWidgetItem(barang[i][7])) #satuan
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,3,QtGui.QTableWidgetItem(barang[i][6])) #jumlah
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,4,QtGui.QTableWidgetItem(barang[i][5])) #harga
				self.tbl_Penjualan_Invoice_TambahBarang.setItem(i,5,QtGui.QTableWidgetItem(barang[i][8])) #totalHarga
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_I_TB)
		
	def Penjualan_Invoice_TambahBarang_TambahBaris(self):
		jumlahRow = self.tbl_Penjualan_Invoice_TambahBarang.rowCount()
		a = jumlahRow
		self.tbl_Penjualan_Invoice_TambahBarang.insertRow(a)
		self.tbl_Penjualan_Invoice_TambahBarang.setItem(a,3,QtGui.QTableWidgetItem("0"))
		self.tbl_Penjualan_Invoice_TambahBarang.setItem(a,4,QtGui.QTableWidgetItem("0"))
		pass
	
	def Penjualan_Invoice_TambahBarang_HapusBaris(self):
		currentRow = self.tbl_Penjualan_Invoice_TambahBarang.currentRow()
		self.tbl_Penjualan_Invoice_TambahBarang.removeRow(currentRow)
		pass
		
	
	def Penjualan_Invoice_TambahBarang_Simpan(self):
		self.SQLtoRun = []
		hargaPokok = 0
		jumlahRow = self.tbl_Penjualan_Invoice_TambahBarang.rowCount()
		for a in range(0, jumlahRow):
			noInvoice = str(self.le_Penjualan_InvoicePenjualan_SOPenawaran.text())
			namaBarang = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,1).text())
			kodeVendor = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,0).text())
			hargaBarang = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,4).text())
			jumlahBarang = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,3).text())
			satuan = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,2).text())
			totalHarga = str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,5).text())
			query = "INSERT INTO `"+self.dbDatabase+"`.`gd_pembelian_barang`"+\
				"(`noInvoice`, `namaBarang`, `kodeVendor`, `hargaBarang`, `jumlahBarang`, `satuan`, `totalHarga`) "+\
				"VALUES ('"+noInvoice+"', '"+namaBarang+"', '"+kodeVendor+"', '"+hargaBarang+"', '"+jumlahBarang+"', '"+satuan+"', '"+totalHarga+"');"
			self.SQLtoRun.append(query)
			#~ self.DatabaseRunQuery(query)
		for a in range (0, jumlahRow):
			hargaPokok = hargaPokok + int(str(self.tbl_Penjualan_Invoice_TambahBarang.item(a,5).text()))
			self.tb_Penjualan_InvoicePenjualan_Input_HargaPokok.setText(str(hargaPokok))
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_IP)
		pass
	
	def Penjualan_Invoice_TambahBarang_TotalHarga(self,row,col):
		try:
			jumlah = str(self.tbl_Penjualan_Invoice_TambahBarang.item(row,3).text())
			harga = str(self.tbl_Penjualan_Invoice_TambahBarang.item(row,4).text())
			totalHarga = int(jumlah)*int(harga)
			self.tbl_Penjualan_Invoice_TambahBarang.setItem(row,5,QtGui.QTableWidgetItem(str(totalHarga)))
		except:
			pass
		return
	
	def Penjualan_Invoice_TambahBarang_PilihVendor(self, row, col):
		if (col==0):
			self.Popup_NamaAlamat_Tabel(self.tbl_Penjualan_Invoice_TambahBarang,row)
		pass
			
	
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
		#~ self.DatabaseInsertAvoidreplace(self.dbDatabase, "gd_invoice_penjualan","kodeTransaksi",kodeTransaksi,
										#~ ["kodeTransaksi", "kodePelanggan", "totalHarga", "tanggal", "kodeMatauang"],
										#~ ["kodeTransaksi", "kodePelanggan", "totalHarga", "tanggal", "kodeMatauang"])
		self.DatabaseRunQuery(query2)

	def Penjualan_OrderPenjualan_Batal(self):
		jumlahRow = self.tbl_Penjualan_OrderPenjualan.rowCount()
		if jumlahRow != 0:
			for a in range (0,jumlahRow):
				self.tbl_Penjualan_OrderPenjualan.removeRow(a)
		kodeTransaksi = str(self.le_Penjualan_OrderPenjualan_NoSO.text())
		del_query = "DELETE FROM `gd_order_penjualan` WHERE `kodeTransaksi` LIKE '"+kodeTransaksi+"'"
		self.DatabaseRunQuery(del_query)

	def Penjualan_HapusBaris(self, namaTabel):
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
		self.tbl_Penjualan_Piutang.setColumnWidth(1,250) #perbesar kolom penerimaan
		self.tbl_Penjualan_Piutang.setColumnWidth(0,300) #perbesar kolom nama pelanggan
		jumlahRow = self.tbl_Penjualan_Piutang.rowCount()
		for x in range (0,jumlahRow):
			self.tbl_Penjualan_Piutang.removeRow(x)
		self.tbl_Penjualan_Piutang.setRowCount(0)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PU)
		query = "SELECT `kodePelanggan` FROM `gd_invoice_penjualan` GROUP BY `kodePelanggan`"
		result = self.DatabaseRunQuery(query)
		for a in range (0,len(result)):
			kodePelanggan = str(result[a][0])
			query = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` LIKE '"+kodePelanggan+"'"
			nama = str(self.DatabaseRunQuery(query)[0][2])
			self.tbl_Penjualan_Piutang.insertRow(a)
			self.tbl_Penjualan_Piutang.setItem(a,0,QtGui.QTableWidgetItem(kodePelanggan)) #kode
			self.tbl_Penjualan_Piutang.setItem(a,1,QtGui.QTableWidgetItem(nama)) #nama
		
	def Penjualan_GoTo_PiutangUsaha_Rincian(self):
		currentRow = self.tbl_Penjualan_Piutang.currentRow()
		nama = str(self.tbl_Penjualan_Piutang.item(currentRow,1).text())
		query = "SELECT * FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = str(self.DatabaseRunQuery(query)[0][1])
		jumlahRow = self.tbl_Penjualan_RincianPiutang.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Penjualan_RincianPiutang.removeRow(x)
		self.tbl_Penjualan_RincianPiutang.setRowCount(0)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_RPU)
		self.lb_Penjualan_RincianPiutang_title_nama.setText(nama)
		query = "SELECT * FROM `gd_invoice_penjualan` WHERE `kodePelanggan` LIKE '"+kodePelanggan+"'"
		result = self.DatabaseRunQuery(query)
		print result
		for a in range (0,len(result)):
			self.tbl_Penjualan_RincianPiutang.insertRow(a)
			self.tbl_Penjualan_RincianPiutang.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][4]))) #tanggal
			self.tbl_Penjualan_RincianPiutang.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][1]))) #no invoice
		return
	
	def Penjualan_GoTo_PembayaranPiutang(self):
		self.tbl_Penjualan_PembayaranPiutang.setColumnWidth(2,300)
		curRow = self.tbl_Penjualan_RincianPiutang.currentRow()
		noInvoice = str(self.tbl_Penjualan_RincianPiutang.item(curRow,1).text())
		query = "SELECT * FROM `gd_piutang` WHERE `noInvoice` LIKE '"+noInvoice+"'"
		result = self.DatabaseRunQuery(query)
		jumlahRow = self.tbl_Penjualan_PembayaranPiutang.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Penjualan_PembayaranPiutang.removeRow(x)
		for a in range (0,len(result)):
			self.tbl_Penjualan_PembayaranPiutang.insertRow(a)
			self.tbl_Penjualan_PembayaranPiutang.setItem(a,0,QtGui.QTableWidgetItem(str(result[a][2]))) #no ref
			self.tbl_Penjualan_PembayaranPiutang.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][3]))) #tanggal
			self.tbl_Penjualan_PembayaranPiutang.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][4]))) #pelanggan
			self.tbl_Penjualan_PembayaranPiutang.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][6]))) #nilai
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PP)
		return
		
	def Penjualan_GoTo_PembayaranPiutang_Baru(self):
		nama = str(self.lb_Penjualan_RincianPiutang_title_nama.text())
		self.le_Penjualan_PembayaranPiutang_Baru_Nama.setText(nama)
		curRow = self.tbl_Penjualan_RincianPiutang.currentRow()
		noInvoice = str(self.tbl_Penjualan_RincianPiutang.item(curRow,1).text())
		self.le_Penjualan_PembayaranPiutang_Baru_NoInvoice.setText(noInvoice)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_PPB)
		return
	
	def Penjualan_PembayaranPiutang_Rekam(self):
		noInvoice = str(self.le_Penjualan_PembayaranPiutang_Baru_NoInvoice.text())
		noRef = str(self.le_Penjualan_PembayaranPiutang_Baru_NoRef.text())
		tgl = str(self.dte_Penjualan_PembayaranPiutang_Baru_Tanggal.dateTime().toString("yyyy-MM-dd hh:mm:ss"))
		nama = str(self.le_Penjualan_PembayaranPiutang_Baru_Nama.text())
		query = "SELECT `kodePelanggan` FROM `gd_nama_alamat` WHERE `namaPelanggan` LIKE '"+nama+"'"
		kodePelanggan = self.DatabaseRunQuery(query)[0]
		catatan = str(self.le_Penjualan_PembayaranPiutang_Baru_Catatan.text())
		jumlahPenerimaan = str(self.le_Penjualan_PembayaranPiutang_Baru_Nominal.text())
		#jumlahPenerimaan = int(jumlahPenerimaan)
		noAkunKas = str(self.tb_Penjualan_PembayaranPiutang_Baru_Akun.text())
		noAkunPiutang = 13000002
		query = "SELECT `jumlahTagihan` FROM `gd_piutang` WHERE `noInvoice` LIKE '"+noInvoice+"'"
		jumlahTagihan = self.DatabaseRunQuery(query)[0]
		query_insert = "INSERT INTO `gd_piutang` (`noInvoice`,`noReferensi`,`tanggal`,`kodePelanggan`,`catatan`,`jumlahPenerimaan`,`jumlahTagihan`,`noAkunKas`,`noAkunPiutang`)"+\
			"VALUES ('"+noInvoice+"','"+noRef+"','"+tgl+"','"+kodePelanggan+"','"+catatan+"','"+jumlahPenerimaan+"','"+jumlahTagihan+"','"+noAkunKas+"','"+noAkunPiutang+"')"
		self.DatabaseRunQuery(query_insert)
		pass
	
	def Penjualan_GoTo_UangMuka(self):
		jumlahRow = self.tbl_Penjualan_UangMuka.rowCount()
		if jumlahRow != 0:
			for x in range (0,jumlahRow):
				self.tbl_Penjualan_UangMuka.removeRow(x)
		query = "SELECT * FROM `gd_uang_muka`"
		result = self.DatabaseRunQuery(query)
		jumData = len(result)
		for a in range(0,jumData):
			self.tbl_Penjualan_UangMuka.insertRow(a)
			self.tbl_Penjualan_UangMuka.setItem(a,0,QtGui.QTableWidgetItem(str(a+1))) #no
			self.tbl_Penjualan_UangMuka.setItem(a,1,QtGui.QTableWidgetItem(str(result[a][1]))) #no ref
			self.tbl_Penjualan_UangMuka.setItem(a,2,QtGui.QTableWidgetItem(str(result[a][5]))) #pelanggan
			self.tbl_Penjualan_UangMuka.setItem(a,3,QtGui.QTableWidgetItem(str(result[a][2]))) #tanggal
			self.tbl_Penjualan_UangMuka.setItem(a,4,QtGui.QTableWidgetItem(str(result[a][3]))) #catatan
			self.tbl_Penjualan_UangMuka.setItem(a,5,QtGui.QTableWidgetItem(str(result[a][4]))) #jumlah
			self.tbl_Penjualan_UangMuka.setItem(a,6,QtGui.QTableWidgetItem(str(result[a][6]))) #kas/bank
		self.tbl_Penjualan_UangMuka.setColumnWidth(0,45)
		self.tbl_Penjualan_UangMuka.setColumnWidth(2,250)
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_UM)
		pass
		
	def Penjualan_GoTo_UangMuka_Baru(self):
		self.st_Penjualan.setCurrentIndex(self.INDEX_ST_PENJUALAN_UMB)
		pass
