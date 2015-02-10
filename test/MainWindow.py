# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Feb 10 14:35:47 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.igr_centralwidget = QtGui.QGridLayout(self.centralwidget)
        self.igr_centralwidget.setObjectName(_fromUtf8("igr_centralwidget"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_centralwidget.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_centralwidget.addItem(spacerItem1, 5, 3, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.igr_centralwidget.addWidget(self.lineEdit_3, 2, 3, 1, 1)
        self.fr_Logo = QtGui.QFrame(self.centralwidget)
        self.fr_Logo.setMinimumSize(QtCore.QSize(170, 170))
        self.fr_Logo.setMaximumSize(QtCore.QSize(170, 170))
        self.fr_Logo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Logo.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Logo.setObjectName(_fromUtf8("fr_Logo"))
        self.igr_centralwidget.addWidget(self.fr_Logo, 5, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_centralwidget.addItem(spacerItem2, 5, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_centralwidget.addItem(spacerItem3, 6, 2, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.igr_centralwidget.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.igr_centralwidget.addWidget(self.lineEdit, 1, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.igr_centralwidget.addWidget(self.lineEdit_4, 2, 2, 1, 1)
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.igr_centralwidget.addWidget(self.lineEdit_5, 3, 2, 1, 1)
        self.lineEdit_6 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.igr_centralwidget.addWidget(self.lineEdit_6, 3, 3, 1, 1)
        self.lineEdit_7 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.igr_centralwidget.addWidget(self.lineEdit_7, 4, 2, 1, 1)
        self.lineEdit_8 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.igr_centralwidget.addWidget(self.lineEdit_8, 4, 3, 1, 1)
        self.fr_Layouttest = QtGui.QFrame(self.centralwidget)
        self.fr_Layouttest.setMinimumSize(QtCore.QSize(200, 0))
        self.fr_Layouttest.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Layouttest.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Layouttest.setObjectName(_fromUtf8("fr_Layouttest"))
        self.ifl_Layouttest = QtGui.QFormLayout(self.fr_Layouttest)
        self.ifl_Layouttest.setObjectName(_fromUtf8("ifl_Layouttest"))
        self.lineEdit_9 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.ifl_Layouttest.setWidget(0, QtGui.QFormLayout.LabelRole, self.lineEdit_9)
        self.lineEdit_10 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.ifl_Layouttest.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEdit_10)
        self.lineEdit_11 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.ifl_Layouttest.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEdit_11)
        self.lineEdit_12 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.ifl_Layouttest.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_12)
        self.lineEdit_13 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.ifl_Layouttest.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_13)
        self.lineEdit_14 = QtGui.QLineEdit(self.fr_Layouttest)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.ifl_Layouttest.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_14)
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.fr_Layouttest)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.ifl_Layouttest.setWidget(3, QtGui.QFormLayout.FieldRole, self.dateTimeEdit)
        self.checkBox = QtGui.QCheckBox(self.fr_Layouttest)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.ifl_Layouttest.setWidget(2, QtGui.QFormLayout.FieldRole, self.checkBox)
        self.igr_centralwidget.addWidget(self.fr_Layouttest, 5, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.checkBox.setText(_translate("MainWindow", "CheckBox", None))

