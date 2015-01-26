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
		
