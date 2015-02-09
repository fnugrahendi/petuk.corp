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
from penjualan import Penjualan
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
except:
	def _fromUtf8(s):
		return s

class MainGUI(QtGui.QMainWindow, Ui_MainWindow,BukuBesar,DataMaster,Penjualan,Pembelian,KasBank,Laporan,Login,Updater):
	def __init__(self, parent= None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.showFullScreen()
		def ___metu():
			exit(0)
			return True
        
		#-- data
		self.Path = str(__file__).replace("Garvin.py","").replace("\\","/")
		self.DataPath = self.Path+"../data/"
		print self.DataPath
		if not os.path.exists(self.DataPath): os.makedirs(self.DataPath)
		
		
		self.SQLtoRun = []
		self.dbHost = "127.0.0.1"
		self.dbPort = 44559
		self.dbDatabase = "gd_db_akunting"
		self.dbPass = "nyungsep"
		self.dbUser = "gd_user_akunting"
		self.Login_init()
		
		
		#--- check if garvin is recent version
		#~ self.GarvinCheckIsUpdated()
	
	def GarvinInit(self):
		#-- init dipindah disini, karena dipanggil setelah berhasil login (set database dsb) di fungsi self.Login_Done
		self.DataMaster_init()
		self.BukuBesar_init()
		self.Penjualan_init()
		self.Pembelian__init()
		self.KasBank_init()
		
		#--- kalau pindah tab, set semua stackedWidget ke index 0 (suppose to be _Menu index)
		self.tabWidget.setCurrentIndex(0)
		self.tabWidget.currentChanged.connect(self.ResetRooms)
		#--- startup program aswell, stackedwidget room should be on Menu Index 
		self.ResetRooms()
		#--- startup program, set semua datetimeedit ke waktu skrg		
		self.GarvinSetDate(self)
		self.Laporan_BuktiInvoice("INV0007")
	
	def Popup_NamaAlamat_Tabel(self,namaTabel,row):
		data = []
		def isi():
			namaTabel.setItem(row,0,QtGui.QTableWidgetItem(str(data[0])))
		def batal():
			namaTabel.setItem(row,0,QtGui.QTableWidgetItem("-"))
		self.DataMaster_DataNamaAlamat_Popup_Pilih(data,isi,batal)	
		
	def Popup_Rekening(self, namaTombol):
		data = ["",""]
		def isi():
			namaTombol.setText(str(data[0]))
		def batal():
			pass
			#~ namaTombol.setText("-")
		self.DataMaster_DataRekening_Popup_Pilih(data,isi,batal)
		print namaTombol.text()
		
	def initDatabase(self):
		try:
			if str(self.db).find("open")!= (-1):
				return True #-- sudah terkoneksi dan open, skip semua termasuk self.cursor creation
			else:
				jumpmetoexeptweakprogrammingbutDRY
		except:
			#-- Belum terkoneksi, koneksikan
			try:
				self.db = MySQLdb.connect(self.dbHost,self.dbUser,self.dbPass,self.dbDatabase)
				print ("connected database to generic mysql port")
			except:
				try:
					print "gagal"
					self.db = MySQLdb.Connect(host=self.dbHost, port=self.dbPort, user=self.dbUser, passwd=self.dbPass, db=self.dbDatabase)
					print ("connected database to Garvin port")
				except:
					print "gagal"
					#~ exit (1)
		#-- sudah terkoneksi, bentuk cursor
		try:
			self.cursor = self.db.cursor()
			return True
		except NameError:return False
		except:return False
		
		#~ try:print "self.db is: "+repr(self.db) +" and its type is: "+str(type(self.db))
		#~ except:pass
		return True
	
	def ResetRooms(self):
		#--- search pakai regexp, karena ternyata tab widget pakai stackedwidget juga!
		for st in self.findChildren(QtGui.QStackedWidget,QRegExp("st_\w+")):
			st.setCurrentIndex(0)
		
	def DatabaseRunQuery(self,query):
		if (not self.initDatabase()):
			return None
		#~ try:
			#~ cursor = self.db.cursor()
		#~ except AttributeError:
			#~ return None
		#~ except:
			#~ return ([])
		try:
			self.cursor.execute(query)
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
		result = self.cursor.fetchall()
		self.db.commit()
		#~ self.db.close() #-- test, to no reconnect!
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
	def DatabaseFetchResult(self,db,table,keyfield=False,keyvalue=False,OrderBy=False):
		""" biasa fetch result wae result in array, 
		misal data = self.DatabaseFetchResult(self.dbDatabase,"gd_nama_alamat","kodePelanggan","%MAKIN%")
		OrderBy berisi list 2 element ["nama field", "tipe"] misal ["kodeTransaksi", "ASC"]
		"""
		if keyfield==False:
			sql = "SELECT * FROM `"+str(db)+"`.`"+str(table)+"` "
			if OrderBy!=False: sql = sql+ " ORDER BY `"+OrderBy[0]+"` "+OrderBy[1]+ " ;"
			else: sql = sql+";"
			return self.DatabaseRunQuery(sql)
		elif (type(keyvalue)==list):
			sql = "SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE "
			for x in xrange(0,len(keyvalue)):
				sql = sql + "`"+str(keyfield[x])+"` LIKE '"+str(keyvalue[x])+"' AND "
			sql = sql[:-4] #-- remove last "AND "
			if OrderBy!=False: sql = sql+ " ORDER BY `"+OrderBy[0]+"` "+OrderBy[1]+ " ;"
			else: sql = sql+";"
			return self.DatabaseRunQuery(sql)
		elif (type(keyvalue)==str):
			sql ="SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE `"+str(keyfield)+"` LIKE '"+str(keyvalue)+"' "
			if OrderBy!=False: sql = sql+ " ORDER BY `"+OrderBy[0]+"` "+OrderBy[1]+ " ;"
			else: sql = sql+";"
			return self.DatabaseRunQuery(sql)
		else:
			sql = "SELECT * FROM `"+str(db)+"`.`"+str(table)+"` WHERE `"+str(keyfield)+"` = "+str(keyvalue)+";"
			if OrderBy!=False: sql = sql+ " ORDER BY `"+OrderBy[0]+"` "+OrderBy[1]+ " ;"
			else: sql = sql+";"
			return self.DatabaseRunQuery(sql)
	
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
	
	def GarvinSetDate(self,parentobject):
		""" set all QDateTimeEdit children of parameter <parentobject> to current timestamp """
		#--- startup program, set semua datetimeedit ke waktu skrg		
		tanggal = datetime.now()
		dtedte = parentobject.findChildren(QtGui.QDateTimeEdit)
		for dte in dtedte:
			dte.setDateTime(QDateTime.fromString(tanggal.strftime("%Y-%m-%d %H:%M:%S"),"yyyy-MM-dd hh:mm:ss"))

	def GarvinLoadConfig(self):
		#-- maksude diantara baris kunci, config tersimpan dalam bentuk hex ascii number
		#-- misal 	101262004472696E6B202020202020202020202024
		#-- 		DATADISINI00000000000000000000000000000000
		#--			101262004472696E6B202020202020202020202024 <-- lanjutannya
		#-- 		DATADISINI00000000000000000000000000000000 <-- lanjut lagi kalau butuh lebih dari sebaris
		self.ConfigKey = [
							["FILE VERSION","LAST LOGIN"],
							[	"1011D2004C4C204B4542414200434F43412D434F2B",
								"101262004472696E6B202020202020202020202024"
							] 
						]
		
		try:
			f = open(self.DataPath+"garvin.dat",'r')
			self.UserData = f.read()
			f.close()
		except:
			self.UserData = ""
	
	def GarvinGetConfig(self,configname):
		self.GarvinLoadConfig()
		configname = configname.upper()
		if (configname in self.ConfigKey[0]):
			key = self.ConfigKey[1][self.ConfigKey[0].index(configname)]
			
			configdata = ""
			datas = re.findall(key+"\n(.*)",self.UserData)
			#-- ambil semua data untuk config ini (bisa lebih dari satu baris)
			if len(datas)<1:
				return ""
			for data in datas:
				teks = re.findall("([0-9a-fA-F]{2})",data)
				#-- ubah masing2 hex ke karakter
				for tek in teks:
					if tek!="00":
						configdata = configdata+chr(int(tek,16))
			return configdata
		else:
			return ""
	
	def GarvinSetConfig(self,configname,configvalue):
		self.GarvinLoadConfig()
		configname = configname.upper()
		if (configname in self.ConfigKey[0]):
			key = self.ConfigKey[1][self.ConfigKey[0].index(configname)]
			posisi = self.UserData.find(key)
			if (posisi>=0):
				#-- edit
				pass
				bagianatas = self.UserData[0:posisi-1] #-- dikurangi satu untuk karakter titikdua ":"
				bagianbawah = self.UserData[posisi:]
				while (bagianbawah.find(key)>=0):
					bagianbawah = bagianbawah[bagianbawah.find("\n")+1:]
				#-- setelah perulangan sekali lagi
				bagianbawah = bagianbawah[bagianbawah.find("\n")+1:]
				encodeddata = ""
				for i in xrange(len(configvalue)):
					encodeddata = encodeddata + (	ord(configvalue[i]).__hex__().replace("0x","")	)
				encodeddata = encodeddata.upper()
				lbaris = encodeddata 
				encodeddata = ":"
				while (len(lbaris)>42): #-- selama baris terakhir masih lebih besar dari 42 karakter (intel ihex) maka dibagi dalam n baris
					encodeddata = encodeddata +key+"\n:" + lbaris[:42] + "\n:"
					lbaris = lbaris[42:]
				while (len(lbaris)<42):
					lbaris=lbaris+"0"
				encodeddata = encodeddata +key+"\n:" + lbaris +"\n" #-- tambah newline juga di akhir
				self.UserData = bagianatas+encodeddata+bagianbawah
				
			else:
				#-- buat baru
				encodeddata = ""
				for i in xrange(len(configvalue)):
					encodeddata = encodeddata + (	ord(configvalue[i]).__hex__().replace("0x","")	)
				encodeddata = encodeddata.upper()
				lbaris = encodeddata 
				encodeddata = ":"
				while (len(lbaris)>42): #-- selama baris terakhir masih lebih besar dari 42 karakter (intel ihex) maka dibagi dalam n baris
					encodeddata = encodeddata +key+"\n:" + lbaris[:42] + "\n:"
					lbaris = lbaris[42:]
				while (len(lbaris)<42):
					lbaris=lbaris+"0"
				encodeddata = encodeddata +key+"\n:" + lbaris +"\n" #-- tambah newline juga di akhir
				self.UserData = encodeddata + self.UserData
				pass
			f = open(self.DataPath+"garvin.dat",'w')
			f.write(self.UserData)
			f.close()
		else:
			return False

	def GarvinGetObject(self,induk,tipe,nama,creation_cb=False):
		""" one of those DRY, 
			Kembalikan object dengan objectname nama bila object belum ada, buat instance baru dengan objectname tersebut 
			contoh dtb_DataMaster_DataRekening_Tambah_Baru = GarvinGetObject(self.fr_DataMaster_DataRekening_Tambah, QtGui.QPushButton, "dtb_DataMaster_DataRekening_Tambah_Baru", self.ivl_DataMaster_DataRekening_Dalam.addWidget)
			creation_cb diisi fungsi callback yang diexecusi dengan parameter instance kembalian
		"""
		objectlama = induk.findChild(tipe,nama)
		if objectlama==None:
			objectbaru = tipe()
			objectbaru.setObjectName(nama)
			if creation_cb != False: creation_cb(objectbaru)
			return objectbaru
		else:
			objectlama.show()
			return objectlama
			
	def GarvinGenerateKode(self,table,LineEdit,prefix,panjang):
		""" melakukan generate kode untuk diisikan pada LineEdit berdasar data2 yang sudah ada di table dengan prefix dan panjang digit bilangan kode 
		"""
		sql = "SELECT `id` FROM `"+self.dbDatabase+"`.`"+table+"` ORDER BY `"+table+"`.`id` DESC LIMIT 0 , 1"
		result = self.DatabaseRunQuery(sql)
		if len(result)<1:
			kode_default = "0"
		else:
			kode_default = str(int(result[0][0])+1)
			while (len(kode_default)<panjang):
				kode_default = "0"+kode_default
		kode_default = prefix + kode_default
		LineEdit.setText(kode_default)
	
	def GarvinGenerateKode_Cek(self,table,fieldmatch,LineEdit,prefix=False,panjang=False):
		"""
			Melakukan checking apakah untuk nama yang telah ditulis pada LineEdit.text belum ada di fieldmatch pada table
		"""
		kodebaru = ""
		kodeterlarang = str(LineEdit.text())
		result = self.DatabaseFetchResult(self.dbDatabase,table,fieldmatch,kodeterlarang	)
		if (len(result)>0):
			if (prefix==False):
				#--- hanya tampilkan pesan
				self.statusbar.showMessage("Kode "+kodeterlarang+" sudah terpakai",10000)
			else:
				#-- bantu generate
				self.statusbar.showMessage("Kode "+kodeterlarang+" sudah terpakai, diberikan kode lain",10000)
				while len(result)>0:
					nilai = int(re.findall("\d+",kodeterlarang)[0])
					nilai+=1
					kodebaru = str(nilai)
					while (len(kodebaru)<panjang):
						kodebaru = "0"+kodebaru
					kodebaru = prefix+kodebaru
					kodeterlarang = kodebaru
					result = self.DatabaseFetchResult(self.dbDatabase,table,fieldmatch,kodeterlarang	)
				LineEdit.setText(kodebaru)
	
	def Terbilang(self,x):   
		angka = {1:'satu ',2:'dua ',3:'tiga ',4:'empat ',5:'lima ',6:'enam ',7:'tujuh ',\
			 8:'delapan ',9:'sembilan '}
		b = 'puluh '
		c = 'ratus '
		d = 'ribu '
		e = 'juta '
		f = 'miliyar '
		g = 'triliun '
		y = str(x)         
		n = len(y)        
		if n <= 3 :        
			if n == 1 :   
				if y == '0' :   
					return ''   
				else :         
					return angka[int(y)]   
			elif n == 2 :
				if y[0] == '1' :                
					if y[1] == '1' :
						return 'sebelas'
					elif y[0] == '0':
						x = y[1]
						return self.Terbilang(x)
					elif y[1] == '0' :
						return 'sepuluh'
					else :
						return angka[int(y[1])] + ' belas'
				elif y[0] == '0' :
					x = y[1]
					return self.Terbilang(x)
				else :
					x = y[1]
					return angka[int(y[0])] + b + self.Terbilang(x)
			else :
				if y[0] == '1' :
					x = y[1:]
					return 'seratus ' + self.Terbilang(x)
				elif y[0] == '0' : 
					x = y[1:]
					return self.Terbilang(x)
				else :
					x = y[1:]
					return angka[int(y[0])] + c + self.Terbilang(x)
		elif 3< n <=6 :
			p = y[-3:]
			q = y[:-3]
			if q == '1' :
				return 'seribu ' + self.Terbilang(p)
			return self.Terbilang(q) + d + self.Terbilang(p)
		elif 6 < n <= 9 :
			r = y[-6:]
			s = y[:-6]
			if r == '000000':
				return self.Terbilang(s) + e
			return self.Terbilang(s) + e + self.Terbilang(r)
		elif 9 < n <= 12 :
			t = y[-9:]
			u = y[:-9]
			return self.Terbilang(u) + f + self.Terbilang(t)
		else:
			v = y[-12:]
			w = y[:-12]
			return self.Terbilang(w) + g + self.Terbilang(v)
	
	def GarvinImage(self,NamaFrame,ResourceImage):
		""" Jadikan ResourceImage sebagai background dari frame NamaFrame
			misal 
			self.GarvinImage(self.LoginUI.fr_Connect_Logo,":/Login/img/LogoMedium.png") (nek rc)
			atau 
			self.GarvinImage(self.LoginUI.fr_Connect_Logo,"../img/LogoMedium.png") (nek link biasa)
		"""
		originalSS = str(NamaFrame.styleSheet())
		originalSS = originalSS + " QFrame{background-image: url("+ResourceImage+");}"
		NamaFrame.setStyleSheet(originalSS)
	
	
if __name__=="__main__":
	#-- dynamic linking, ben nek dicompile dadi binary .exe ora marai kabotan startup/file e gedhe
	Path = str(__file__).replace("Garvin.py","").replace("\\","/")
	DataPath = Path+"../data/"

	loginrcpath = Path+"../image/"+"Image_rc.py"
	resfile = open(loginrcpath)
	resource = resfile.read()
	resfile.close()
	resource = resource[:resource.find("def qInitResources")]
	exec(resource)
	QtCore.qRegisterResourceData(0x01, qt_resource_struct, qt_resource_name, qt_resource_data)

	
	app = QtGui.QApplication(sys.argv)
	dmw = MainGUI()
	#~ dmw.showFullScreen()
	sys.exit(app.exec_())
#bismillah
