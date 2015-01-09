#!/usr/bin/env python
import MySQLdb
from PyQt4.QtCore import QObject, pyqtSignal
from PyQt4 import QtCore
from PyQt4 import QtGui
import sys,os
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
		self.tb_Penjualan_Keluar.clicked.connect(___metu)
        
		#Tombol pada Halaman Menu
		self.tb_Penjualan_PenawaranHarga.clicked.connect(self.Penjualan_GoTo_PenawaranHarga)
		self.tb_Penjualan_OrderPenjualan.clicked.connect(self.Penjualan_GoTo_OrderPenjualan)
		self.tb_Penjualan_Pengiriman.clicked.connect(self.Penjualan_GoTo_Pengiriman)
		self.tb_Penjualan_Piutang.clicked.connect(self.Penjualan_GoTo_PiutangUsaha)
		self.tb_Penjualan_PembayaranPiutang.clicked.connect(self.Penjualan_GoTo_PembayaranPiutang)
		self.tb_Penjualan_Retur.clicked.connect(self.Penjualan_GoTo_ReturPenjualan)
		
		self.tb_PenawaranHarga_tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		self.tb_PenawaranHarga_baru.clicked.connect(self.Penjualan_GoTo_PenawaranHarga_baru)
		#self.tbl_Penjualan_PenawaranHarga_baru.cellChanged.connect(self.Penjualan_PenawaranHarga_Baru_TabelComplete)
		#QtCore.QObject.connect( self.tbl_Penjualan_PenawaranHarga_baru, QtCore.SIGNAL("cellChanged(int,int)"), self.Penjualan_PenawaranHarga_Baru_TabelComplete)
		#self.isiKodeBarang.connect(self.Penjualan_PenawaranHarga_Baru_TabelComplete)
		#self.isiKodeBarang.emit(0,0)
		
		self.tb_Penjualan_PenawaranHarga_baru_rekam.clicked.connect(self.Penjualan_PenawaranHarga_Baru_Rekam)
		self.tb_Penjualan_PenawaranHarga_baru_tutup.clicked.connect(self.Penjualan_GoTo_PenawaranHarga)
		
		self.tb_Penjualan_OrderPenjualan_Tutup.clicked.connect(self.Penjualan_GoTo_Menu)
		
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
		self.INDEX_ST_PENJUALAN_PENGIRIMAN = 4
		self.INDEX_ST_PENJUALAN_PENGIRIMANB = 5
		self.INDEX_ST_PENJUALAN_PU = 6
		self.INDEX_ST_PENJUALAN_RPU = 7
		self.INDEX_ST_PENJUALAN_PP = 8
		self.INDEX_ST_PENJUALAN_PPB = 9
		self.INDEX_ST_PENJUALAN_RP = 10
		
	def initDatabase(self):
		self.dbHost = "127.0.0.1"
		self.dbDatabase = "gd_db_akunting"
		self.dbPass = "nyungsep"
		self.dbUser = "gd_user_akunting"
		try:
			self.db = MySQLdb.connect(self.dbHost,self.dbUser,self.dbPass,self.dbDatabase)
			#print ("Success")
		except:
			print ("This software should be ran with correct procedure. Contact customer service for help.")
		return
		
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
		self.Penjualan_PenawaranHarga_Baru_TabelComplete()
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
		
		kodeBarang = 
		
		self.initDatabase()
		cursor = self.db.cursor()
		kodeBarang = int(self.tbl_Penjualan_PenawaranHarga_baru.item(0,0))
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
	
			
app = QtGui.QApplication(sys.argv)
dmw = MainGUI()
dmw.showFullScreen()
sys.exit(app.exec_())
