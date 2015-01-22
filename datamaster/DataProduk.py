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

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

class DataProduk(object):
	def __init__(self, parent=None):
		pass
	
	def DataMaster_DataProduk_RefreshList(self,searchtext):
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_data_produk","namaBarang","%"+str(searchtext)+"%")
		tinggi = len(result)*80
		self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
		for x in range(0,len(result)):
			Tb_ListProduk = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataProduk_List"+str(result[x][self.DataMaster_DataProduk_Field.index("kodeBarang")]))
			if (len(Tb_ListProduk)<1):
				Tb_Produk = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
				Tb_Produk.setObjectName(_fromUtf8("dtb_DataMaster_DataProduk_List"+str(result[x][self.DataMaster_DataProduk_Field.index("kodeBarang")])))
				local_name = str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")])
				Tb_Produk.setText(local_name)
				self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_Produk,QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
				Tb_Produk.clicked.connect(functools.partial(self.DataMaster_DataProduk_DrawInfo,result[x]))
			else:
				for y in range(0, len(Tb_ListProduk)):
					self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_ListProduk[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignTop)
					Tb_ListProduk[y].show()
					Tb_ListProduk[y].setText(str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")]))
					Tb_ListProduk[y].clicked.disconnect()
					Tb_ListProduk[y].clicked.connect(functools.partial(self.DataMaster_DataProduk_DrawInfo,result[x]))
	
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
	
	
	def DataMaster_DataProduk_Popup_Pilih(self,dipilih,fcb_ok=False, fcb_cancel=False, hideSurrounding=False):
		"""Buka popup untuk pilih DataProduk, carane hack dewe yoh neng fcb_ok
		"""
		self.GarvinDisconnect(self.le_DataMaster_DataCommon_Search.textChanged)
		self.le_DataMaster_DataCommon_Search.setText("")
		self.le_DataMaster_DataCommon_Search.textChanged.connect(self.DataMaster_DataProduk_RefreshList)
		
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		#--- fungsi exit:kembalikan
		def revertDataProduk():
			self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setParent(self.fr_DataMaster_DataCommon_Fbody)
			self.ihl_DataMaster_DataCommon_Fbody.insertWidget(0,self.fr_DataMaster_DataCommon_Fbody_Slist_Container,1)
			self.fr_DataMaster_DataCommon_Fbody_Slist_Container.show()
		
		#------ Is it weak reference? when will python's garbage collector delete this revertDataProduk()?
		#--- set to none
		if (fcb_ok==False):
			fcb_ok = self.DataMaster_None
		if (fcb_cancel==False):
			fcb_cancel = self.DataMaster_None
		
		#--- bila arraykosong
		if len(dipilih)<1:
			dipilih.append("-")
		
		def ubahDipilih(data):
			""" karena threading, bisa ngubah pakai fungsi: nunggu fungsi dipanggil"""
			dipilih[0] = data
			revertDataProduk()
		
		
		#--- Popup dipanggil dulu, baru dimanipulasi isinya
		#thanks to function_exit
		self.DataMaster_Popup("",fcb_ok,360,WinH-250,revertDataProduk,fcb_cancel,True)
		
		
		FrameWindow = self.findChild(QtGui.QFrame,"DataMaster_Popup_FrameWindow")
		PopupW = FrameWindow.geometry().width()
		PopupH = FrameWindow.geometry().height()
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setParent(FrameWindow)
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.show()
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setGeometry(QtCore.QRect(5,5,PopupW-5,PopupH-50))
		
		#Hapus layout list, buat baru
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_data_produk")
		tinggi = len(result)*80
		#~ self.sc_DataMaster_DataProduk_Fbody_Slist.setMinimumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataProduk_Fbody_Slist.setMinimumSize(QtCore.QSize(330, 600))
		#~ self.sc_DataMaster_DataProduk_Fbody_Slist.setMaximumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataProduk_Fbody_Slist.setMaximumSize(QtCore.QSize(330, 600))
		for x in range(0,len(result)):
			Tb_ListProduk = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataProduk_List"+str(result[x][self.DataMaster_DataProduk_Field.index("kodeBarang")]))
			if (len(Tb_ListProduk)<1):
				Tb_Produk = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
				Tb_Produk.setObjectName("dtb_DataMaster_DataProduk_List"+str(result[x][self.DataMaster_DataProduk_Field.index("kodeBarang")]))
			else:
				Tb_Produk = Tb_ListProduk[0]

			local_name = str(result[x][self.DataMaster_DataProduk_Field.index("namaBarang")])
			Tb_Produk.setText(local_name)
			Tb_Produk.show()
			#--- disini nambahnya
			self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_Produk)
			self.GarvinDisconnect(Tb_Produk.clicked)
			Tb_Produk.clicked.connect(functools.partial(ubahDipilih,str(result[x][self.DataMaster_DataProduk_Field.index("kodeBarang")])))
			Tb_Produk.clicked.connect(self.DataMaster_Popup_Tutup)
			Tb_Produk.clicked.connect(fcb_ok)
        
