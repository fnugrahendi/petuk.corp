import os,sys
from PyQt4 import QtCore
from PyQt4 import QtGui
import functools
import itertools
import re
from subprocess import Popen 

from installer_ui import Ui_MainWindow

class MainGUI(QtGui.QMainWindow,Ui_MainWindow):
	def __init__(self,parent=None):
		super(MainGUI,self).__init__(parent)
		self.setupUi(self)
		self.show()
		#-- path
		self.Path = str(__file__).replace("installer.py","").replace("\\","/")
		print self.Path
		self.BasePath = self.Path+"../"
		try:open(self.BasePath+"archive/eula.txt","r").close()
		except Exception,e:
			print str(e)
			self.BasePath = self.Path
			print ("base path is now",self.BasePath)
		
		#-- icon
		icon = QtGui.QIcon()
		icon.addPixmap(QtGui.QPixmap(self.BasePath+"archive/Garvin.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		self.setWindowIcon(icon)
		
		#-- deteksi 64 bit ataukah 32 bit
		self.arc = 32
		if ("PROGRAMFILES(X86)" in os.environ):#-- bila 64bit
			self.arc = 64
			
		self.PageL = ["INSTALL FOLDER","INSTALL BIN","QUIT"]
		dataf = open(self.BasePath+"archive/eula.txt","r")
		data = dataf.read()
		dataf.close()
		self.te_Lisensi.setText(data)
		self.te_Lisensi.hide()
		self.tb_Lisensi.clicked.connect(self.TampilLisensi)
		
		
		self.InstallDir()
		
	def TampilLisensi(self):
		self.te_Lisensi.show()
		
	def Goto(self,name):
		self.stackedWidget.setCurrentIndex(self.PageL.index(name.upper()))
	
	def InstallDir(self):
		self.Goto("Install Folder")
		self.GarvinDisconnect(self.tb_Browse.clicked)
		self.GarvinDisconnect(self.tb_Install.clicked)
		self.GarvinDisconnect(self.tb_Quit.clicked)
		self.tb_Browse.clicked.connect(self.Browse)
		self.tb_Install.clicked.connect(self.InstallBin)
		self.tb_Quit.clicked.connect(self.Quit)
		
	
	def Browse(self):
		dialog = QtGui.QFileDialog(self)
		dialog.setFileMode(QtGui.QFileDialog.Directory)
		namafolder = str(dialog.getExistingDirectory(self, ("Pilih folder instalasi"),"",QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks))
		
		if not ("garvin" in namafolder.lower()):
			if namafolder[-1]=="\\":
				namafolder=namafolder[:-1]
			namafolder=namafolder+"\Garvin"
		self.le_InstallDir.setText(namafolder)
	
	def InstallBin_Act(self):
		self.aatime.stop()
		archiveBin = self.BasePath+"archive/bin.grvz"
		
		installpath = str(self.le_InstallDir.text())
		if not os.path.exists(installpath): os.makedirs(installpath)
		os.system(self.BasePath+"7z.exe -y x "+archiveBin+" -o"+installpath+" -pnyungsep")
		#~ self.tb_InstallBin_Next.show()
		self.InstallMysql()
		os.makedirs(installpath+"\data")
	
	def InstallBin(self):
		self.Goto("Install Bin")
		self.lb_InstallBin_Judul.setText("Menginstall Garvin Accounting...")
		self.tb_InstallBin_Next.hide()
		self.aatime = QtCore.QTimer(self)
		self.aatime.timeout.connect(self.InstallBin_Act)
		self.aatime.start(100)
	
	def InstallMysql_Act(self):
		self.aatime.stop()
		archiveBin = self.BasePath+"archive/mysql32.grvz"
		if self.arc==64:
			archiveBin = self.BasePath+"archive/mysql64.grvz"
			
		
		installpath = str(self.le_InstallDir.text())
		if not os.path.exists(installpath): os.makedirs(installpath)
		os.system(self.BasePath+"7z.exe -y x "+archiveBin+" -o"+installpath+" -pnyungsep")
		self.InstallConfig()
		
	def InstallMysql(self):
		self.Goto("Install Bin")
		if self.arc==32:self.lb_InstallBin_Judul.setText("Menginstall MySQL database server (32 bit)...")
		else:self.lb_InstallBin_Judul.setText("Menginstall MySQL database server (64 bit)...")
		self.tb_InstallBin_Next.hide()
		self.aatime = QtCore.QTimer(self)
		self.aatime.timeout.connect(self.InstallMysql_Act)
		self.aatime.start(100)
	
	def InstallConfig_Act(self):
		self.aatime.stop()
		print "jalankan", str(self.le_InstallDir.text())+"\\mysql\\bin\\mysqld --port=44559"
		Popen(str(self.le_InstallDir.text())+"\\mysql\\bin\\mysqld --port=44559")
		
		self.aatime = QtCore.QTimer(self)
		self.aatime.timeout.connect(self.InstallConfig_MysqlUser)
		self.aatime.start(10000)
		
		
	def InstallConfig_MysqlUser(self):
		self.aatime.stop()
		querytambahuser = 	"""	CREATE USER 'gd_user_akunting'@'localhost' IDENTIFIED BY 'nyungsep';
								GRANT ALL PRIVILEGES ON *.* TO 'gd_user_akunting'@'localhost' IDENTIFIED BY 'nyungsep' WITH GRANT OPTION MAX_QUERIES_PER_HOUR 0 MAX_CONNECTIONS_PER_HOUR 0 MAX_UPDATES_PER_HOUR 0 MAX_USER_CONNECTIONS 0;
							"""
		f = open("querytambahuser.md","w")
		f.write(querytambahuser)
		f.close()
		print "jalankan",(str(self.le_InstallDir.text())+"\\mysql\\bin\\mysql --port=44559 -u root test < querytambahuser.md")
		os.system(str(self.le_InstallDir.text())+"\\mysql\\bin\\mysql --port=44559 -u root test < querytambahuser.md")
		self.Selesai()
	
		
	def InstallConfig(self):
		self.Goto("Install Bin")
		self.lb_InstallBin_Judul.setText("Melakukan configurasi program...")
		self.tb_InstallBin_Next.hide()
		self.aatime = QtCore.QTimer(self)
		self.aatime.timeout.connect(self.InstallConfig_Act)
		self.aatime.start(100)
	
	def Selesai(self):
		#--- todo tambah source file info
		
		
		self.lb_InstallBin_Judul.setText("Instalasi sukses")
		self.tb_InstallBin_Next.show()
		self.tb_InstallBin_Next.setText("Finish")
		self.tb_InstallBin_Next.clicked.connect(self.Quit)
		
	def Quit(self):
		sys.exit (0)
	
	def GarvinDisconnect(self,stuff):
		"nyimpel2ke disconnect signal, cara manggil koyo self.GarvinDisconnect(self.tbl_BukuBesar_DaftarTransaksiJurnal_Tambah_List.cellDoubleClicked)"
		try:
			stuff.disconnect()
			return True
		except:
			return False
			
if __name__=="__main__":
	app = QtGui.QApplication(sys.argv)
	w = MainGUI()
	sys.exit(app.exec_())
