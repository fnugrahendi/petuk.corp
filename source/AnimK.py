from PyQt4 import QtCore, QtGui

class GarvinButton(QtGui.QPushButton):
	"""custom qpushbutton ta kei ono sinyal dihover & dileave"""
	"""gawe slot? http://www.pythoncentral.io/pysidepyqt-tutorial-creating-your-own-signals-and-slots/"""
	try:
		dihover = QtCore.pyqtSignal()
		dileave = QtCore.pyqtSignal()
	except:#-- get ready for pyside migrate
		dihover = QtCore.Signal()
		dileave = QtCore.Signal()
		
	def __init__(self,text="",parent=None):
		super(GarvinButton,self).__init__(text,parent)
		
	def enterEvent(self, event):
		self.dihover.emit()
		return QtGui.QPushButton.enterEvent(self, event)
		
	def enterEvent(self, event):
		self.dileave.emit()
		return QtGui.QPushButton.leaveEvent(self, event)
	
class GarvinButtonExit(GarvinButton):
	"""njajal Custom qpushbutton animasi hover & leave"""
	def __init__(self,text="",parent=None):
		super(GarvinButtonExit,self).__init__(text,parent)
		self.minValue = 0 #-- for alpha, no prefix
		self.maxValue = 80
		self.minValueR = 3 #-- for border radius
		self.maxValueR = 20
		self.alphav = self.minValue
		self.border = self.maxValueR
		self.setStyleSheet("background-color:rgba(50,50,50,"+str(self.alphav)+");")
		self.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
		self.animTimerIn = QtCore.QTimer(self)
		self.animTimerIn.timeout.connect(self.colorIn)
		self.animTimerOut = QtCore.QTimer(self)
		self.animTimerOut.timeout.connect(self.colorOut)
	
	def colorIn(self):
		"""animasi perbarui warna alpha """
		self.alphav += 1
		self.border += 1
		if (self.alphav>=self.maxValue):
			self.animTimerIn.stop()
		self.animate(self.alphav,((self.border-self.minValue)*(self.maxValueR-self.minValueR)/(self.maxValue-self.minValue)	))
			
	def colorOut(self):
		"""animasi perbarui warna alpha """
		self.alphav -= 1
		self.border -= 1
		if (self.alphav<=self.minValue):
			self.animTimerOut.stop()
		if (self.alphav>=self.minValue):
			#~ self.animate(self.alphav,(self.border/20))
			self.animate(self.alphav,((self.border-self.minValue)*(self.maxValueR-self.minValueR)/(self.maxValue-self.minValue)	))
	
	def enterEvent(self, event):
		"""reimplement enterEvent bro"""
		self.alphav = self.minValue
		self.border = self.minValue #-- samakan, diskala di animate calling
		self.animTimerIn.start(2)
		
		return QtGui.QPushButton.enterEvent(self, event)
		
	def leaveEvent(self, event):
		self.alphav = self.maxValue
		self.border = self.maxValue #-- samakan, diskala di animate calling
		self.animTimerOut.start(2)
		
		return QtGui.QPushButton.leaveEvent(self, event)
	
	def animate(self,alphav,radius=0):
		warna = "rgba(150,10,10,"+str(alphav)+")"
		self.setStyleSheet(	"background-color:"+warna+"; border-style:outset; border-color:"+warna+"; border-width:1px;border-radius:"+str(radius)+"px;")
		
	
class GarvinButtonExitBackup(QtGui.QPushButton):
	def __init__(self,text="",parent=None):
		super(GarvinButtonExit,self).__init__(text,parent)
		# ...
		self.innercolor = QtGui.QColor(255,255,255,0)
		#~ self.setFlat(True)
		#~ self.setStyleSheet("border-color:#000000;border-width:2px;border-radius:40px;background-color:red;")

	def setcolor(self,value): self.innercolor = value
	def getcolor(self): return self.innercolor
	color = QtCore.pyqtProperty(QtGui.QColor,getcolor,setcolor)

	def paintEvent(self, event):
		p = QtGui.QPainter(self)
		p.fillRect(self.rect(),self.color)
		# ...
		p.end()

	def animated(self,value): 
		self.update()
		
	def enterEvent(self, event):
		self.ani = QtCore.QPropertyAnimation(self,"color")
		self.ani.setStartValue(self.color)
		self.ani.setEndValue(QtGui.QColor(0,0,10,255))
		self.ani.setDuration(500)
		self.ani.valueChanged.connect(self.animated)
		self.ani.start()
		return QtGui.QPushButton.enterEvent(self, event)
		
	def leaveEvent(self, event):
		self.ani2 = QtCore.QPropertyAnimation(self,"color")
		self.ani2.setStartValue(self.color)
		self.ani2.setEndValue(QtGui.QColor(255,255,255,0))
		self.ani2.setDuration(500)
		self.ani2.valueChanged.connect(self.animated)
		self.ani2.start()
		return QtGui.QPushButton.leaveEvent(self, event)
		
