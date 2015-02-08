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
except:
	def _fromUtf8(s):
		return s

class DataNamaAlamat(object):
	def __init__(self, parent=None):
		pass
	
	def DataMaster_DataNamaAlamat_RefreshList(self,searchtext):
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_nama_alamat","namaPelanggan","%"+str(searchtext)+"%")
		tinggi = len(result)*80
		self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataCommon_Fbody_Slist.setMaximumSize(QtCore.QSize(350, 600))
		for x in range(0,len(result)):
			obj_Tb_ListPelanggan = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataNamaAlamat_List"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")]))
			if (len(obj_Tb_ListPelanggan)<1):
				print "bikin baru"
				obj_Tb_Pelanggan = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
				obj_Tb_Pelanggan.setObjectName("dtb_DataMaster_DataNamaAlamat_List"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")]))
				local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")])
				obj_Tb_Pelanggan.setText(local_name)
				self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_Pelanggan,QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
				#~ obj_Tb_Pelanggan.clicked.connect(functools.partial(self.DataMaster_DataNamaAlamat_DrawInfo,result[x]))
			else:
				print "pakai yang ada"
				for y in range(0,len(obj_Tb_ListPelanggan)):
					self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0].addWidget(obj_Tb_ListPelanggan[y],QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
					obj_Tb_ListPelanggan[y].show()
					obj_Tb_ListPelanggan[y].setText(str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]))
					#~ obj_Tb_ListPelanggan[y].clicked.disconnect()
					#~ obj_Tb_ListPelanggan[y].clicked.connect(functools.partial(self.DataMaster_DataNamaAlamat_DrawInfo,result[x]))
			
	
	def DataMaster_DataNamaAlamat_DrawInfo(self,data): #nama,perusahaan,tipe,npwp,diskon,jatuhtempo,diskonawal,dendaketerlambatan,alamat,kodepelanggan
		field = self.DataMaster_DataNamaAlamat_Field.index
		f14 = QtGui.QFont()
		f14.setPointSize(14)
		f14.setBold(False)
		f14.setItalic(False)
		f14.setWeight(75)
		
		
		#--------------------------------------------------------------------------------------------------------Nama
		try:
			#~ if (self.DataMaster_CommonRoom_cleared==1):
				#~ skipkeexcept
			self.lb_DataMaster_DataNamaAlamat_Nama.setText(data[field("namaPelanggan")])
			self.lb_DataMaster_DataNamaAlamat_Nama.setFont(f14)
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Nama, 0, 0, 1, 3,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Nama.show()
		except:
			self.lb_DataMaster_DataNamaAlamat_Nama = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Nama.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Nama"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Nama, 0, 0, 1, 3,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Nama.setText(data[field("namaPelanggan")])
			self.lb_DataMaster_DataNamaAlamat_Nama.setFont(f14)
		#--------------------------------------------------------------------------------------------------------Kode
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kode, 0, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_kode.show()
			self.lb_DataMaster_DataNamaAlamat_kode.setText("\n\n" + str(data[field("kodePelanggan")]))
		except:
			self.lb_DataMaster_DataNamaAlamat_kode = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_kode.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_kode"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kode, 0, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_kode.setText("\n\n" + str(data[field("kodePelanggan")]))
			
		#--------------------------------------------------------------------------------------------------------Tipe
		
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_tipe, 0, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_tipe.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ltipe, 0, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ltipe.show()
			self.lb_DataMaster_DataNamaAlamat_tipe.setText(data[field("tipe")])
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setText("Tipe :")
		except:
			self.lb_DataMaster_DataNamaAlamat_tipe = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_tipe.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_tipe"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_tipe, 0, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_tipe.setText(data[field("tipe")])
			
			self.lb_DataMaster_DataNamaAlamat_Ltipe = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ltipe"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ltipe, 0, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ltipe.setText("Tipe :")
			
		#--------------------------------------------------------------------------------------------------------Kontak
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kontak, 1, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_kontak.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lkontak, 1, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lkontak.show()
			self.lb_DataMaster_DataNamaAlamat_kontak.setText(data[field("kontak")])
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setText("Kontak :")
		except:
			self.lb_DataMaster_DataNamaAlamat_kontak = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_kontak.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_kontak"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_kontak, 1, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_kontak.setText(data[field("kontak")])
			
			self.lb_DataMaster_DataNamaAlamat_Lkontak = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lkontak"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lkontak, 1, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lkontak.setText("Kontak :")
		
		#--------------------------------------------------------------------------------------------------------NPWP
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_npwp, 1, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_npwp.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lnpwp, 1, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lnpwp.show()
			self.lb_DataMaster_DataNamaAlamat_npwp.setText(data[field("npwp")])
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setText("NPWP :")
		except:
			self.lb_DataMaster_DataNamaAlamat_npwp = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_npwp.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_npwp"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_npwp, 1, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_npwp.setText(data[field("npwp")])
			
			self.lb_DataMaster_DataNamaAlamat_Lnpwp = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lnpwp"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lnpwp, 1, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lnpwp.setText("NPWP :")
			
		#--------------------------------------------------------------------------------------------------------Alamat
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_alamat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_alamat.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lalamat, 2, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Lalamat.show()
			self.lb_DataMaster_DataNamaAlamat_alamat.setText(data[field("alamat")])
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setText("Alamat :")
		except:
			self.lb_DataMaster_DataNamaAlamat_alamat = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_alamat.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_alamat"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_alamat, 2, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_alamat.setText(data[field("alamat")])
			
			self.lb_DataMaster_DataNamaAlamat_Lalamat = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Lalamat"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Lalamat, 2, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Lalamat.setText("Alamat :")
		
		#--------------------------------------------------------------------------------------------------------Denda
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_denda, 2, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_denda.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldenda, 2, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ldenda.show()
			self.lb_DataMaster_DataNamaAlamat_denda.setText(str(data[field("dendaKeterlambatan")]))
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setText("Denda Keterlambatan :")
		except:
			self.lb_DataMaster_DataNamaAlamat_denda = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_denda.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_denda"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_denda, 2, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_denda.setText(str(data[field("dendaKeterlambatan")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ldenda = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ldenda"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldenda, 2, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ldenda.setText("Denda Keterlambatan :")
			
		#--------------------------------------------------------------------------------------------------------Diskon
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskon, 3, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_diskon.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldiskon, 3, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ldiskon.show()
			
			self.lb_DataMaster_DataNamaAlamat_diskon.setText(str(data[field("diskon")]))
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setText("Diskon :")
		except:
			self.lb_DataMaster_DataNamaAlamat_diskon = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_diskon.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_diskon"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskon, 3, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_diskon.setText(str(data[field("diskon")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ldiskon = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ldiskon"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ldiskon, 3, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ldiskon.setText("Diskon :")
		
		#--------------------------------------------------------------------------------------------------------diskonAwal
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskonAwal, 3, 7, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_diskonAwal.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_LdiskonAwal, 3, 6, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.show()
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setText(str(data[field("diskonAwal")]))
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setText("Diskon Awal :")
		except:
			self.lb_DataMaster_DataNamaAlamat_diskonAwal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_diskonAwal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_diskonAwal, 3, 7, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_diskonAwal.setText(str(data[field("diskonAwal")]))
			
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_LdiskonAwal"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_LdiskonAwal, 3, 6, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_LdiskonAwal.setText("Diskon Awal :")
		
		#--------------------------------------------------------------------------------------------------------jatuhtempo
		try:
			if (self.DataMaster_CommonRoom_cleared==1):
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_jatuhtempo, 4, 1, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_jatuhtempo.show()
				self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo, 4, 0, 1, 1,QtCore.Qt.AlignTop)
				self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.show()
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setText(str(data[field("jatuhtempo")]))
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setText("Jatuh Tempo :")
		except:
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_jatuhtempo"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_jatuhtempo, 4, 1, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_jatuhtempo.setText(str(data[field("jatuhtempo")]))
			
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo = QtGui.QLabel(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setObjectName(_fromUtf8("lb_DataMaster_DataNamaAlamat_Ljatuhtempo"))
			self.fr_DataMaster_DataCommon_Fbody_FR_Ftop.findChildren(QtGui.QGridLayout)[0].addWidget(self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo, 4, 0, 1, 1,QtCore.Qt.AlignTop)
			self.lb_DataMaster_DataNamaAlamat_Ljatuhtempo.setText("Jatuh Tempo :")
		
		
		#--------------------------------------------------------------------------------------------------------Frame Bawah (graphic)
		try:
			#~ if (self.DataMaster_CommonRoom_cleared==1):
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.fr_DataMaster_DataNamaAlamat_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataNamaAlamat_FGraph.show()
			
		except:
			self.fr_DataMaster_DataNamaAlamat_FGraph = QtGui.QFrame(self.fr_DataMaster_DataCommon_Fbody_FR_Ftop)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setFrameShape(QtGui.QFrame.StyledPanel)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setFrameShadow(QtGui.QFrame.Raised)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setObjectName(_fromUtf8("fr_DataMaster_DataNamaAlamat_FGraph"))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setStyleSheet(_fromUtf8("border-style:none;border-width:0px;border-color:rgb(197, 197, 197);"))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMaximumSize(QtCore.QSize(1366,400))
			self.igr_DataMaster_DataCommon_Fbody_FR_Ftop.addWidget(self.fr_DataMaster_DataNamaAlamat_FGraph, 5, 0, 20, 20,QtCore.Qt.AlignBottom)
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMaximumSize(QtCore.QSize(1366,300))
			self.fr_DataMaster_DataNamaAlamat_FGraph.setMinimumSize(QtCore.QSize(400,300))
			
			self.ihl_DataMaster_DataNamaAlamat_FGraph = QtGui.QHBoxLayout(self.fr_DataMaster_DataNamaAlamat_FGraph)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setSpacing(2)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setContentsMargins(1, 1, 1, 1)
			self.ihl_DataMaster_DataNamaAlamat_FGraph.setObjectName(_fromUtf8("ihl_DataMaster_DataNamaAlamat_FGraph"))
			
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
			
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang = QtSvg.QSvgWidget(self.fr_DataMaster_DataNamaAlamat_FGraph)
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang.load("./img/DataMaster_svg.svg")
			self.svg_DataMaster_DataNamaAlamat_TransaksiOrang.setGeometry(QtCore.QRect(10, 10, svgW, svgH))
			#~ self.ihl_DataMaster_DataNamaAlamat_FGraph.addWidget(self.svg_DataMaster_DataNamaAlamat_TransaksiOrang)

		self.DataMaster_CommonRoom_cleared = 0
		
		try:
			self.lb_DataMaster_DataNamaAlamat_Nama.clicked.disconnect()
		except:
			pass
		try:
			datadihapus = str(self.lb_DataMaster_DataNamaAlamat_Nama.text())
		except:
			datadihapus = ""
		self.tb_DataMaster_DataCommon_Delete.clicked.connect(functools.partial(self.DataMaster_Popup,"Anda yakin akan menghapus data "+datadihapus+" ini?",self.DataMaster_DataNamaAlamat_Delete,500,200,None,None))
		
		
	def DataMaster_DataNamaAlamat_Tambah_Act_Simpan(self):
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(False)
		nama = str(self.le_DataMaster_DataNamaAlamat_Tambah_Nama.text())
		tipe = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText())
		npwp = str(self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.text())
		diskon = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.value())
		jatuhtempo = ("0000-00-00 00:00:00" if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()==0) else str(self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.dateTime().toString("yyyy-MM-dd hh:mm:ss")) )
		diskonawal = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.value())
		dendaketerlambatan = str(self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.text())
		alamat = str(self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.text())
		kodepelanggan = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		kontak = str(self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.text())
		noakunpiutang= str(self.tb_DataMaster_DataNamaAlamat_Tambah_NoAkunPiutang.text())
		noakunhutang = str(self.tb_DataMaster_DataNamaAlamat_Tambah_NoAkunHutang.text())
		sql = ""
		if (self.DataMaster_DataNamaAlamat_Edit_idEDIT >=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
			"SET `namaPelanggan` = '"+nama+"',"+\
				"`kodePelanggan` = '"+kodepelanggan+"',"+\
				"`tipe` = '"+tipe+"',"+\
				"`npwp` = '"+npwp+"',"+\
				"`diskon` = '"+diskon+"',"+\
				"`jatuhTempo` = '"+jatuhtempo+"',"+\
				"`diskonAwal` = '"+diskonawal+"',"+\
				"`dendaKeterlambatan` = '"+dendaketerlambatan+"',"+\
				"`alamat` = '"+alamat+"',"+\
				"`kontak` = '"+kontak+"',"+\
				"`noAkunPiutang` = '"+noakunpiutang+"',"+\
				"`noAkunHutang` = '"+noakunhutang+"'"+\
			"WHERE `gd_nama_alamat`.`id`='"+str(self.DataMaster_DataNamaAlamat_Edit_idEDIT)+"'"
			self.DataMaster_DataNamaAlamat_Edit_idEDIT = -1
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
				"(`id`, `kodePelanggan`, `namaPelanggan`, `tipe`, `npwp`, `diskon`, `jatuhTempo`, `diskonAwal`, `dendaKeterlambatan`, `alamat`, `kontak`, `noAkunPiutang`, `noAkunHutang`)"+\
				"VALUES "+\
				"(NULL, '"+kodepelanggan+"', '"+nama+"', '"+tipe+"', '"+npwp+"', '"+diskon+"', '"+jatuhtempo+"', '"+diskonawal+"', '"+dendaketerlambatan+"', '"+alamat+"', '"+kontak+"' , '"+noakunpiutang+"', '"+noakunhutang+"');"
		self.DatabaseRunQuery(sql)
		#----------------------------------------------------------------------------------------------------------back to where it should be
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT)
	
	def DataMaster_DataNamaAlamat_Tambah_GenerateKode(self):
		"""	Generate kode otomatis untuk lineEdit le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan, 
			dipanggil ketika menambah data nama alamat baru, atau ganti tipe pada combo box cb_
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`gd_nama_alamat` ORDER BY `gd_nama_alamat`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "00000000"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<8):
				kode_default = "0"+kode_default
		kode_default = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText()).upper() + "."+kode_default
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(kode_default)
	

	
	def DataMaster_DataNamaAlamat_Edit(self):
		field = self.DataMaster_DataNamaAlamat_Field.index
		try:
			kode = str(self.lb_DataMaster_DataNamaAlamat_kode.text()).replace("\n","")
		except:
			return
		sql = "SELECT * FROM `gd_nama_alamat` WHERE `kodePelanggan` = '"+kode+"' LIMIT 0 , 1"
		barang = self.DatabaseRunQuery(sql)
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(_fromUtf8(barang[0][field("kodePelanggan")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(True)
		self.le_DataMaster_DataNamaAlamat_Tambah_Nama.setText(_fromUtf8(barang[0][field("namaPelanggan")]))
		self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.setCurrentIndex(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.findText(_fromUtf8(barang[0][field("tipe")])))
		self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.setText(_fromUtf8(barang[0][field("kontak")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.setText(_fromUtf8(barang[0][field("npwp")]))
		self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.setValue((barang[0][field("diskon")]))
		self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.setValue((barang[0][field("diskonAwal")]))
		self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.setText(_fromUtf8(str(barang[0][field("dendaKeterlambatan")])))
		self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.setText(_fromUtf8(barang[0][field("alamat")]))
		self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setCheckState((0 if (str(barang[0][field("jatuhtempo")])=="None") else 2))
		self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setDateTime(QDateTime.fromString(str(barang[0][field("jatuhtempo")]),"yyyy-MM-dd hh:mm:ss"))
		self.tb_DataMaster_DataNamaAlamat_Tambah_NoAkunPiutang.setText(str(barang[0][field("noAkunPiutang")]))
		self.tb_DataMaster_DataNamaAlamat_Tambah_NoAkunHutang.setText(str(barang[0][field("noAkunHutang")]))
		self.DataMaster_DataNamaAlamat_Edit_idEDIT = barang[0][field("id")]
		self.DataMaster_Goto(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT_TAMBAH)
	
	def DataMaster_DataNamaAlamat_Delete(self):
		try:
			kode = str(self.lb_DataMaster_DataNamaAlamat_kode.text()).replace("\n","")
		except:
			return
		sql = "DELETE FROM `"+self.dbDatabase+"`.`gd_nama_alamat` WHERE `gd_nama_alamat`.`kodePelanggan` = '"+kode+"'"
		self.DatabaseRunQuery(sql)
		self.DataMaster_Goto_Common(self.INDEX_ST_DATAMASTER_DATANAMAALAMAT)
	
	def DataMaster_DataNamaAlamat_Popup_Tambah(self, fcallback_ok=None,fcallback_cancel=None,fcallback_enter=None,fcallback_exit=None):
		"""
		Tampilkan popup untuk menambah DataNamaAlamat
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
			self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(None)
			self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(self.st_DataMaster_DataNamaAlamat_Tambah)
			self.ivl_DataMaster_DataNamaAlamat_Tambah_Luar.addWidget(self.fr_DataMaster_DataNamaAlamat_Tambah)
			self.fr_DataMaster_DataNamaAlamat_Tambah_Fbot.show()
			fcallback_exit() #-----(C)
			
		self.DataMaster_DataNamaAlamat_Tambah_GenerateKode()
		self.DataMaster_Popup("",functools.partial(self.DataMaster_DataNamaAlamat_Popup_Act_Tambah,fcallback_ok),WinW-10,WinH-200,exit_function,fcallback_cancel) #----B
		
		FrameWindow = self.findChild(QtGui.QFrame,_fromUtf8("DataMaster_Popup_FrameWindow"))
		self.fr_DataMaster_DataNamaAlamat_Tambah.setParent(FrameWindow)
		self.fr_DataMaster_DataNamaAlamat_Tambah.show()
		self.fr_DataMaster_DataNamaAlamat_Tambah.setGeometry(QtCore.QRect(5,5,WinW-20,WinH-250))
		self.fr_DataMaster_DataNamaAlamat_Tambah_Fbot.hide()
	
	def DataMaster_DataNamaAlamat_Popup_Act_Tambah(self,fcallback_exit):
		
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setReadOnly(False)
		nama = str(self.le_DataMaster_DataNamaAlamat_Tambah_Nama.text())
		tipe = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText())
		npwp = str(self.le_DataMaster_DataNamaAlamat_Tambah_NPWP.text())
		diskon = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_Diskon.value())
		jatuhtempo = ("0000-00-00 00:00:00" if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()==0) else str(self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.dateTime().toString("yyyy-MM-dd hh:mm:ss")) )
		diskonawal = str(self.dsb_DataMaster_DataNamaAlamat_Tambah_DiskonAwal.value())
		dendaketerlambatan = str(self.le_DataMaster_DataNamaAlamat_Tambah_DendaKeterlambatan.text())
		alamat = str(self.le_DataMaster_DataNamaAlamat_Tambah_Alamat.text())
		kodepelanggan = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		kontak = str(self.le_DataMaster_DataNamaAlamat_Tambah_Kontak.text())
		sql = ""
		if (self.DataMaster_DataNamaAlamat_Edit_idEDIT >=0):
			sql = "UPDATE `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
			"SET `namaPelanggan` = '"+nama+"',"+\
				"`kodePelanggan` = '"+kodepelanggan+"',"+\
				"`tipe` = '"+tipe+"',"+\
				"`npwp` = '"+npwp+"',"+\
				"`diskon` = '"+diskon+"',"+\
				"`jatuhTempo` = '"+jatuhtempo+"',"+\
				"`diskonAwal` = '"+diskonawal+"',"+\
				"`dendaKeterlambatan` = '"+dendaketerlambatan+"',"+\
				"`alamat` = '"+alamat+"',"+\
				"`kontak` = '"+kontak+"'"+\
			"WHERE `gd_nama_alamat`.`id`='"+str(self.DataMaster_DataNamaAlamat_Edit_idEDIT)+"'"
			self.DataMaster_DataNamaAlamat_Edit_idEDIT = -1
		else:
			sql = "INSERT INTO `"+self.dbDatabase+"`.`gd_nama_alamat` "+\
				"(`id`, `kodePelanggan`, `namaPelanggan`, `tipe`, `npwp`, `diskon`, `jatuhTempo`, `diskonAwal`, `dendaKeterlambatan`, `alamat`, `kontak`)"+\
				"VALUES "+\
				"(NULL, '"+kodepelanggan+"', '"+nama+"', '"+tipe+"', '"+npwp+"', '"+diskon+"', '"+jatuhtempo+"', '"+diskonawal+"', '"+dendaketerlambatan+"', '"+alamat+"', '"+kontak+"');"
		self.DatabaseRunQuery(sql)
		fcallback_exit()
		return
	def DataMaster_DataNamaAlamat_Tambah_JatuhTempoSet(self):
		self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setReadOnly(False) if (self.chk_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.checkState()>0) else self.dte_DataMaster_DataNamaAlamat_Tambah_JatuhTempo.setReadOnly(True)
	
	def DataMaster_DataNamaAlamat_Tambah_Tipe_Change(self):
		t = str(self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.text())
		cb = str(self.cb_DataMaster_DataNamaAlamat_Tambah_Tipe.currentText()).upper()
		aa = t.replace("EMPLOYEE",cb)
		aa = aa.replace("VENDOR",cb)
		aa = aa.replace("CUSTOMER",cb)
		aa = aa.replace("OTHER",cb)
		self.le_DataMaster_DataNamaAlamat_Tambah_KodePelanggan.setText(_fromUtf8(aa))
	
	def DataMaster_DataNamaAlamat_Popup_Pilih(self,dipilih,fcb_ok=False, fcb_cancel=False, hideSurrounding=False):
		"""Buka popup untuk pilih dataNamaAlamat, carane hack dewe yoh neng fcb_ok
		"""
		self.GarvinDisconnect(self.le_DataMaster_DataCommon_Search.textChanged)
		self.le_DataMaster_DataCommon_Search.setText("")
		self.le_DataMaster_DataCommon_Search.textChanged.connect(self.DataMaster_DataNamaAlamat_RefreshList)
		
		WinW = self.centralwidget.geometry().width()
		WinH = self.centralwidget.geometry().height()
		#--- fungsi exit:kembalikan
		def revertDataNamaAlamat():
			self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setParent(self.fr_DataMaster_DataCommon_Fbody)
			self.ihl_DataMaster_DataCommon_Fbody.insertWidget(0,self.fr_DataMaster_DataCommon_Fbody_Slist_Container,1)
			self.fr_DataMaster_DataCommon_Fbody_Slist_Container.show()
		
		#------ Is it weak reference? when will python's garbage collector delete this revertDataNamaAlamat()?
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
			revertDataNamaAlamat()
		
		
		#--- Popup dipanggil dulu, baru dimanipulasi isinya
		#thanks to function_exit
		self.DataMaster_Popup("",fcb_ok,360,WinH-250,revertDataNamaAlamat,fcb_cancel,True)
		
		
		FrameWindow = self.findChild(QtGui.QFrame,"DataMaster_Popup_FrameWindow")
		PopupW = FrameWindow.geometry().width()
		PopupH = FrameWindow.geometry().height()
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setParent(FrameWindow)
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.show()
		self.fr_DataMaster_DataCommon_Fbody_Slist_Container.setGeometry(QtCore.QRect(5,5,PopupW-5,PopupH-50))
		
		#Hapus layout list, buat baru
		self.clearLayout(self.scontent_DataMaster_DataCommon_Fbody_Slist.findChildren(QtGui.QVBoxLayout)[0])
		
		result = self.DatabaseFetchResult(self.dbDatabase,"gd_nama_alamat")
		tinggi = len(result)*80
		#~ self.sc_DataMaster_DataNamaAlamat_Fbody_Slist.setMinimumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataNamaAlamat_Fbody_Slist.setMinimumSize(QtCore.QSize(330, 600))
		#~ self.sc_DataMaster_DataNamaAlamat_Fbody_Slist.setMaximumSize(QtCore.QSize(330, tinggi)) if (tinggi < 600) else self.sc_DataMaster_DataNamaAlamat_Fbody_Slist.setMaximumSize(QtCore.QSize(330, 600))
		for x in range(0,len(result)):
			Tb_ListNamaAlamat = self.findChildren(QtGui.QPushButton,"dtb_DataMaster_DataNamaAlamat_List"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")]))
			if (len(Tb_ListNamaAlamat)<1):
				Tb_NamaAlamat = QtGui.QPushButton(self.scontent_DataMaster_DataCommon_Fbody_Slist)
				Tb_NamaAlamat.setObjectName("dtb_DataMaster_DataNamaAlamat_List"+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")]))
			else:
				Tb_NamaAlamat = Tb_ListNamaAlamat[0]

			local_name = str(result[x][self.DataMaster_DataNamaAlamat_Field.index("namaPelanggan")]) +\
						"\n ("+str(result[x][self.DataMaster_DataNamaAlamat_Field.index("tipe")])+")"
			Tb_NamaAlamat.setText(local_name)
			Tb_NamaAlamat.show()
			#--- disini nambahnya
			self.ivl_DataMaster_DataCommon_Fbody_Slist.addWidget(Tb_NamaAlamat)
			self.GarvinDisconnect(Tb_NamaAlamat.clicked)
			Tb_NamaAlamat.clicked.connect(functools.partial(ubahDipilih,str(result[x][self.DataMaster_DataNamaAlamat_Field.index("kodePelanggan")])))
			Tb_NamaAlamat.clicked.connect(self.DataMaster_Popup_Tutup)
			Tb_NamaAlamat.clicked.connect(fcb_ok)
        
		#~ Tb_ListNamaAlamat = self.findChildren(QtGui.QPushButton,QRegExp("dynamic_tb_DataMaster_DataNamaAlamat_List\w+"))
