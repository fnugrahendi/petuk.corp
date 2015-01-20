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
		self.tb_Pembelian_OrderPembelian.clicked.connect(self.)
		
		
	def Pembelian_GoTo_PermintaanBarang(self):
		return
	
	def Pembelian_GoTo_OrderPembelian(self):
		return
	
	def Pembelian_GoTo_PenerimaanBarang(self):
		return
	
	def Pembelian_GoTo_HutangUsaha(self):
		return
	
	def Pembelian_GoTo_PembayaranHutang(self):
		return
	
	def Pembelian_GoTo_ReturPembelian(self):
		return
