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
		cmd = "\""+wget +"\""+ " --no-check-certificate https://github.com/fnugrahendi/petuk.corp/blob/master/currentversion.md -o "+downloadfolder+"currentversion.md.o -O "+downloadfolder+"currentversion.md"
		print cmd
		subprocess.Popen(cmd,shell=True)
		self.UpdaterTimer = QtCore.QTimer(self)
		self.UpdaterTimer.timeout.connect(functools.partial(self.Updater_CekSudah,"currentversion.md",self.Updater_Download))
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
		versiini = [1,
					1,
					1,
					1,
					1,
					1,
					1,
					1]
		versigarvin = versiini
		f = open(downloadfolder+"currentversion.md","r")
		data = f.read()
		f.close()
		
		data = data[data.find("=start")+6:data.find("=end")]
		exec(data)
		todownload = []
		downloadcmd = []
		for x in range(len(versiini)):
			if versigarvin[x]>versiini[x]:
				todownload.append(component[x]+str(versigarvin[x])+".grvz")
				downloadcmd.append(serverprefix+str(versigarvin[x])+"/"+todownload[-1])
		
		pesantext = "Modul berikut perlu di update:\n"
		for moduldownload in todownload:
			pesantext += "\t"+moduldownload+"\n"
		pesantext += "Download update sekarang?"
		self.DataMaster_Popup(pesantext)
		
		print "Updater sejatinya akan mendownload dan mengupdate modul berikut: "
		print downloadcmd
