# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'installer_ui.ui'
#
# Created: Mon Feb 09 16:09:14 2015
#      by: PyQt4 UI code generator 4.10.1
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
        MainWindow.resize(717, 390)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralWidget)
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.st_InstallDir = QtGui.QWidget()
        self.st_InstallDir.setObjectName(_fromUtf8("st_InstallDir"))
        self.gridLayout_3 = QtGui.QGridLayout(self.st_InstallDir)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.frame_2 = QtGui.QFrame(self.st_InstallDir)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.tb_Install = QtGui.QPushButton(self.frame_2)
        self.tb_Install.setObjectName(_fromUtf8("tb_Install"))
        self.gridLayout_2.addWidget(self.tb_Install, 2, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 2, 0, 1, 1)
        self.tb_Quit = QtGui.QPushButton(self.frame_2)
        self.tb_Quit.setObjectName(_fromUtf8("tb_Quit"))
        self.gridLayout_2.addWidget(self.tb_Quit, 2, 2, 1, 1)
        self.frame = QtGui.QFrame(self.frame_2)
        self.frame.setMinimumSize(QtCore.QSize(300, 0))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.le_InstallDir = QtGui.QLineEdit(self.frame)
        self.le_InstallDir.setObjectName(_fromUtf8("le_InstallDir"))
        self.horizontalLayout.addWidget(self.le_InstallDir)
        self.tb_Browse = QtGui.QPushButton(self.frame)
        self.tb_Browse.setObjectName(_fromUtf8("tb_Browse"))
        self.horizontalLayout.addWidget(self.tb_Browse)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 3)
        self.lb_Judul = QtGui.QLabel(self.frame_2)
        self.lb_Judul.setObjectName(_fromUtf8("lb_Judul"))
        self.gridLayout_2.addWidget(self.lb_Judul, 0, 0, 1, 3)
        self.gridLayout_3.addWidget(self.frame_2, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 1, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 2, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem4, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.st_InstallDir)
        self.st_InstallBin = QtGui.QWidget()
        self.st_InstallBin.setObjectName(_fromUtf8("st_InstallBin"))
        self.gridLayout = QtGui.QGridLayout(self.st_InstallBin)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem5 = QtGui.QSpacerItem(20, 86, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 0, 1, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(172, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 1, 0, 1, 1)
        self.fr_InstallBin = QtGui.QFrame(self.st_InstallBin)
        self.fr_InstallBin.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_InstallBin.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_InstallBin.setObjectName(_fromUtf8("fr_InstallBin"))
        self.gridLayout_4 = QtGui.QGridLayout(self.fr_InstallBin)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.tb_InstallBin_Next = QtGui.QPushButton(self.fr_InstallBin)
        self.tb_InstallBin_Next.setObjectName(_fromUtf8("tb_InstallBin_Next"))
        self.gridLayout_4.addWidget(self.tb_InstallBin_Next, 2, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 2, 0, 1, 1)
        self.fr_InstallBin_Mid = QtGui.QFrame(self.fr_InstallBin)
        self.fr_InstallBin_Mid.setMinimumSize(QtCore.QSize(300, 43))
        self.fr_InstallBin_Mid.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_InstallBin_Mid.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_InstallBin_Mid.setObjectName(_fromUtf8("fr_InstallBin_Mid"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.fr_InstallBin_Mid)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.gridLayout_4.addWidget(self.fr_InstallBin_Mid, 1, 0, 1, 3)
        self.lb_InstallBin_Judul = QtGui.QLabel(self.fr_InstallBin)
        self.lb_InstallBin_Judul.setObjectName(_fromUtf8("lb_InstallBin_Judul"))
        self.gridLayout_4.addWidget(self.lb_InstallBin_Judul, 0, 0, 1, 3)
        self.gridLayout.addWidget(self.fr_InstallBin, 1, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(171, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem8, 1, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 86, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 2, 1, 1, 1)
        self.stackedWidget.addWidget(self.st_InstallBin)
        self.st_Popup = QtGui.QWidget()
        self.st_Popup.setObjectName(_fromUtf8("st_Popup"))
        self.fr_Popup = QtGui.QFrame(self.st_Popup)
        self.fr_Popup.setGeometry(QtCore.QRect(0, 20, 480, 230))
        self.fr_Popup.setMinimumSize(QtCore.QSize(480, 230))
        self.fr_Popup.setMaximumSize(QtCore.QSize(480, 230))
        self.fr_Popup.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Popup.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Popup.setObjectName(_fromUtf8("fr_Popup"))
        self.fr_Popup_S = QtGui.QFrame(self.fr_Popup)
        self.fr_Popup_S.setGeometry(QtCore.QRect(20, 20, 450, 200))
        self.fr_Popup_S.setMinimumSize(QtCore.QSize(450, 200))
        self.fr_Popup_S.setMaximumSize(QtCore.QSize(450, 200))
        self.fr_Popup_S.setStyleSheet(_fromUtf8("background-color: rgb(67, 89, 118);"))
        self.fr_Popup_S.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Popup_S.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Popup_S.setObjectName(_fromUtf8("fr_Popup_S"))
        self.fr_Popup_H = QtGui.QFrame(self.fr_Popup)
        self.fr_Popup_H.setGeometry(QtCore.QRect(10, 10, 450, 200))
        self.fr_Popup_H.setMinimumSize(QtCore.QSize(450, 200))
        self.fr_Popup_H.setMaximumSize(QtCore.QSize(450, 200))
        self.fr_Popup_H.setStyleSheet(_fromUtf8("QFrame{\n"
"    background-color: rgb(242, 243, 245);\n"
"    \n"
"    border-color: rgb(127,123, 135);\n"
"    border-width:2px;\n"
"    border-style: outset;\n"
"}\n"
"QLabel{border-width:0px;}\n"
"\n"
"QPushButton{\n"
"    height:20px;\n"
"    width:80px;\n"
"}"))
        self.fr_Popup_H.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Popup_H.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Popup_H.setObjectName(_fromUtf8("fr_Popup_H"))
        self.ifr_Popup_H = QtGui.QGridLayout(self.fr_Popup_H)
        self.ifr_Popup_H.setObjectName(_fromUtf8("ifr_Popup_H"))
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ifr_Popup_H.addItem(spacerItem10, 1, 4, 1, 1)
        self.tb_Popup_Cancel = QtGui.QPushButton(self.fr_Popup_H)
        self.tb_Popup_Cancel.setObjectName(_fromUtf8("tb_Popup_Cancel"))
        self.ifr_Popup_H.addWidget(self.tb_Popup_Cancel, 1, 3, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.ifr_Popup_H.addItem(spacerItem11, 1, 0, 1, 1)
        self.tb_Popup_Ok = QtGui.QPushButton(self.fr_Popup_H)
        self.tb_Popup_Ok.setObjectName(_fromUtf8("tb_Popup_Ok"))
        self.ifr_Popup_H.addWidget(self.tb_Popup_Ok, 1, 1, 1, 1)
        spacerItem12 = QtGui.QSpacerItem(80, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.ifr_Popup_H.addItem(spacerItem12, 1, 2, 1, 1)
        self.lb_Popup_Text = QtGui.QLabel(self.fr_Popup_H)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lb_Popup_Text.setFont(font)
        self.lb_Popup_Text.setObjectName(_fromUtf8("lb_Popup_Text"))
        self.ifr_Popup_H.addWidget(self.lb_Popup_Text, 0, 0, 1, 5)
        self.stackedWidget.addWidget(self.st_Popup)
        self.horizontalLayout_2.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 717, 21))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tb_Install.setText(_translate("MainWindow", "Install", None))
        self.tb_Quit.setText(_translate("MainWindow", "Quit", None))
        self.tb_Browse.setText(_translate("MainWindow", "Browse", None))
        self.lb_Judul.setText(_translate("MainWindow", "-   Install directory:", None))
        self.tb_InstallBin_Next.setText(_translate("MainWindow", "Next", None))
        self.lb_InstallBin_Judul.setText(_translate("MainWindow", "Menginstall Garvin Accounting", None))
        self.tb_Popup_Cancel.setText(_translate("MainWindow", "CANCEL", None))
        self.tb_Popup_Ok.setText(_translate("MainWindow", "YES", None))
        self.lb_Popup_Text.setText(_translate("MainWindow", "TextLabel", None))

