import wget
import re

class Updater(object):
	def __init__(self, parent=None):
		pass
	def GarvinCheckVersion(self):
		sukses = True
		try:
			import urllib
		except:
			print "install urllib yoh, kiye dinggo updater"
			return False

		f = urllib.urlopen("https://github.com/fnugrahendi/petuk.corp/blob/master/currentversion.md")
		data = f.read()
		f.close()
		versi = re.findall("current garvin version is (\d+\.\d+) today is",data)
		if (len(versi)<1):
			return False
		else:
			versi = versi[0]
		return versi
	def GarvinCheckClientVersion(self):
		f= open("data/garvin.dat","r")
		data = f.read()
		f.close()
		versi = re.findall(":1011A200534D414C4C2050495A5A4100484153201A\n:1011B20053454C4543544544004249472050495AFF\n:1011C2005A4100424947204B4542414200534D415A\n:1011D2004C4C204B4542414200434F43412D434F2B\n:1011E2004C4100504550534900466F6F64202(\d+E\d+)F\d+[.\n]+",data)
		if (len(versi)<1):
			print "Garvin korup, instal ulang!"
		else:
			versi=versi[0].replace("E",".")
			return versi
	def GarvinCheckIsUpdated(self):
		if (self.GarvinCheckVersion()==self.GarvinCheckClientVersion()):
			print "current Garvin used version is the latest"
		else:
			print "Garvin should be updated"
