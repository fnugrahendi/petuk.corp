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
		self.INDEX_ST_PEMBELIAN_PERMINTAANBARANG = 1
		self.INDEX_ST_PEMBELIAN_ORDERPEMBELIAN = 2
		self.INDEX_ST_PEMBELIAN_PENERIMAAN = 3
		self.INDEX_ST_PEMBELIAN_HUTANG = 4
		self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG = 5
		self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN = 6
		
		#Tombol Pada Halaman Menu
		self.tb_Pembelian_PermintaanBarang.clicked.connect(self.Pembelian_GoTo_PermintaanBarang)
		self.tb_Pembelian_OrderPembelian.clicked.connect(self.Pembelian_GoTo_OrderPembelian)
		self.tb_Pembelian_Penerimaan.clicked.connect(self.Pembelian_GoTo_PenerimaanBarang)
		self.tb_Pembelian_HutangUsaha.clicked.connect(self.Pembelian_GoTo_HutangUsaha)
		self.tb_Pembelian_PembayaranHutang.clicked.connect(self.Pembelian_GoTo_PembayaranHutang)
		self.tb_Pembelian_ReturPembelian.clicked.connect(self.Pembelian_GoTo_ReturPembelian)
		
		#Tombol pada Permintaan Barang
		self.tb_Pembelian_PermintaanBarang_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Order Pembelian
		self.tb_Pembelian_OrderPembelian_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Penerimaan Barang
		
		#Tombol pada Hutang Usaha
		self.tb_Pembelian_HutangUsaha_Tutup.clicked.connect(self.Pembelian_GoTo_Menu)
		
		#Tombol pada Pembayaran Hutang
		
		#Tombol pada Retur Pembelian
	
	def Pembelian_GoTo_Menu(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_MENU)
		return	
		
	def Pembelian_GoTo_PermintaanBarang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PERMINTAANBARANG)
		return
	
	def Pembelian_GoTo_OrderPembelian(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_ORDERPEMBELIAN)
		return
	
	def Pembelian_GoTo_PenerimaanBarang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PENERIMAAN)
		return
	
	def Pembelian_GoTo_HutangUsaha(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_HUTANG)
		return
	
	def Pembelian_GoTo_PembayaranHutang(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_PEMBAYARANHUTANG)
		return
	
	def Pembelian_GoTo_ReturPembelian(self):
		self.st_Pembelian.setCurrentIndex(self.INDEX_ST_PEMBELIAN_RETURPEMBELIAN)
		return
