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
		self.showFullScreen()
		
		self.PageL = ["INSTALL FOLDER","INSTALL BIN","QUIT"]
		
		self.InstallDir()
		
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
		dialog.setFileMode(QtGui.QFileDialog.Directory);
		namafolder = dialog.getExistingDirectory(self, ("Pilih folder instalasi"),"",QtGui.QFileDialog.ShowDirsOnly| QtGui.QFileDialog.DontResolveSymlinks);
		self.le_InstallDir.setText(namafolder)
	
	def InstallBin_Act(self):
		self.aatime.stop()
		archiveBin = "../archive/bin.grvz"
		
		installpath = str(self.le_InstallDir.text())
		if not os.path.exists(installpath): os.makedirs(installpath)
		os.system("..\\7z.exe -y x "+archiveBin+" -o"+installpath+" -pnyungsep")
		self.tb_InstallBin_Next.show()
		
	
	def InstallBin(self):
		self.Goto("Install Bin")
		self.tb_InstallBin_Next.hide()
		self.aatime = QtCore.QTimer(self)
		self.aatime.timeout.connect(self.InstallBin_Act)
		self.aatime.start(100)
		
		
	
	def Quit(self):
		exit (0)
	
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
