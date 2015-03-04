import sys
import subprocess
import re
import urllib
import functools
from PyQt4 import QtCore

class Updater(object):
	def __init__(self, parent=None):
		pass
		
	def GarvinCheckIsUpdated(self):
		wget = "wget"
		if ("win" in sys.platform):#-- bila windows ada nih
			wget = self.BasePath+"downloader/wget_win/wget.exe"
			
		downloadfolder = self.DataPath
		#-- download info versi sekarang 
		cmd = "\""+wget +"\""+ " --no-check-certificate https://raw.githubusercontent.com/fnugrahendi/petuk.corp/master/currentversion.rb -o "+downloadfolder+"currentversion.rb.o -O "+downloadfolder+"currentversion.rb"
		print cmd
		subprocess.Popen(cmd,shell=True)
		self.UpdaterTimer = QtCore.QTimer(self)
		self.UpdaterTimer.timeout.connect(functools.partial(self.Updater_CekSudah,"currentversion.rb",self.Updater_Download))
		self.UpdaterTimer.start(3000)
		
	def Updater_CekSudah(self,namafile,callbackfunction):
		downloadfolder = self.DataPath
		f = open(downloadfolder+namafile+".o","r")
		if "saved" in f.read():
			self.UpdaterTimer.stop()
			print "download "+namafile+" selesai"
			callbackfunction()
		f.close()
		
	def Updater_Download(self):
		wget = "wget"
		if ("win" in sys.platform):#-- bila windows ada nih
			wget = self.BasePath+"downloader/wget_win/wget.exe"
		wget = "\""+ wget+ "\" -c  --no-check-certificate "
		downloadfolder = self.DataPath
		serverprefix = "https://github.com/fnugrahendi/petuk.corp/releases/download/"
		component = ["garvin",
					"bin",
					"data",
					"doc",
					"image",
					"installer",
					"mysql",
					"source"]
		versiini = [
				["garvin",		1, "localhost"],
				["bin", 		2, "localhost"],
				["data", 		1, "localhost"],
				["doc", 		1, "localhost"],
				["image", 		1, "localhost"],
				["installer", 	1, "localhost"],
				["mysql", 		1, "localhost"],
				["source", 		1, "localhost"]
			]
		versigarvin = versiini
		f = open(downloadfolder+"currentversion.rb","r")
		data = f.read()
		f.close()
		
		data = data[data.find("ruby")+6:]
		exec(data)
		todownload = []
		downloadcmd = []
		for x in range(len(versiini)):
			if versigarvin[x][1]>versiini[x][1]:
				todownload.append(versigarvin[x][0]+str(versigarvin[x][1])+".grvz")
				downloadcmd.append(wget+serverprefix+str(versigarvin[x][2]))
		
		pesantext = "Modul berikut perlu di update:\n"
		for moduldownload in todownload:
			pesantext += "\t"+moduldownload+"\n"
		pesantext += "Download update sekarang?"
		self.DataMaster_Popup(pesantext)
		
		#~ print "Updater sejatinya akan mendownload dan mengupdate modul berikut: "
		#~ print downloadcmd
		for cmd in downloadcmd:
			print cmd
			#~ subprocess.Popen(cmd,shell=True)
