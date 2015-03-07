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
				["bin", 		1, "localhost"],
				["data", 		1, "localhost"],
				["doc", 		1, "localhost"],
				["image", 		1, "localhost"],
				["installer", 	1, "localhost"],
				["mysql", 		1, "localhost"],
				["source", 		1, "localhost"]
			]#-- TODO SOFTCODE & LOAD THIS, UPDATE THE VaLUE ON SOFTWARE UPDATE TOO
		versigarvin = versiini
		f = open(downloadfolder+"currentversion.rb","r")
		data = f.read()
		f.close()
		print data
		data = data[data.find("ruby")+4:]
		exec(data)
		print versigarvin
		self.Updater_Todownload = []
		self.Updater_Downloadcmd = []
		for x in range(len(versiini)):
			if versigarvin[x][1]>versiini[x][1]:
				self.Updater_Todownload.append(versigarvin[x][0]+str(versigarvin[x][1])+".grvz")
				self.Updater_Downloadcmd.append(wget+str(versigarvin[x][2]) +\
							" -o "+downloadfolder+self.Updater_Todownload[-1]+".o "+\
							" -O "+downloadfolder+self.Updater_Todownload[-1]
							)
		
		print self.Updater_Todownload
		print self.Updater_Downloadcmd
		if len(self.Updater_Todownload)>0:
			pesantext = "Modul berikut perlu di update:\n"
			for moduldownload in self.Updater_Todownload:
				pesantext += "\t"+moduldownload+"\n"
			pesantext += "Download update sekarang? (proses berjalan di background)"
			self.DataMaster_Popup(pesantext,self.Updater_Download_Act)
		
		#~ print "Updater sejatinya akan mendownload dan mengupdate modul berikut: "
		#~ print self.Updater_Downloadcmd
		#~ for cmd in self.Updater_Downloadcmd:
			#~ print cmd
			#~ subprocess.Popen(cmd,shell=True)
	
	def Updater_Download_Act(self):
		for cmd in self.Updater_Downloadcmd:
			print cmd
			subprocess.Popen(cmd,shell=True)
		print self.Updater_Todownload
		cmd = "\""+self.BasePath+"downloader/updateinstaller/updateinstaller.exe\" "
		for didownload in self.Updater_Todownload:
			cmd = cmd+ didownload + " "
		print cmd
		subprocess.Popen(cmd, shell=True)
	
	def Updater_Download_Act_CekSudah(self):
		""" cek sudah, timernya self.UpdaterTimer bisa"""
		#-- cek masing2 file
		selesai = True
		for donlotan in self.Updater_Todownload:
			try:
				f = open(self.Updater_Todownload+".o","r")
				data = f.read()
				f.close()
				if not("saved" in data):
					selesai = False
					break
			except:
				selesai = False
				break
		if selesai:
			self.GarvinDisconnect(self.UpdaterTimer.timeout)
			print "Download update selesai"
			#-- extract
			#~ self.DataMaster_Popup("Lakukan update sekarang?"
