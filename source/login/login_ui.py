# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login/login_ui.ui'
#
# Created: Tue Feb 10 13:50:23 2015
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

class Ui_fr_Main(object):
    def setupUi(self, fr_Main):
        fr_Main.setObjectName(_fromUtf8("fr_Main"))
        fr_Main.resize(747, 616)
        fr_Main.setStyleSheet(_fromUtf8("background:white;"))
        fr_Main.setFrameShape(QtGui.QFrame.StyledPanel)
        fr_Main.setFrameShadow(QtGui.QFrame.Raised)
        self.igr_Main = QtGui.QGridLayout(fr_Main)
        self.igr_Main.setObjectName(_fromUtf8("igr_Main"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Main.addItem(spacerItem, 0, 0, 1, 1)
        self.st_Main = QtGui.QStackedWidget(fr_Main)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.st_Main.sizePolicy().hasHeightForWidth())
        self.st_Main.setSizePolicy(sizePolicy)
        self.st_Main.setMinimumSize(QtCore.QSize(640, 450))
        self.st_Main.setMaximumSize(QtCore.QSize(1366, 450))
        self.st_Main.setStyleSheet(_fromUtf8(""))
        self.st_Main.setObjectName(_fromUtf8("st_Main"))
        self.st_Connect = QtGui.QWidget()
        self.st_Connect.setObjectName(_fromUtf8("st_Connect"))
        self.gridLayout_2 = QtGui.QGridLayout(self.st_Connect)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.fr_Connect_Container = QtGui.QFrame(self.st_Connect)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Connect_Container.sizePolicy().hasHeightForWidth())
        self.fr_Connect_Container.setSizePolicy(sizePolicy)
        self.fr_Connect_Container.setMinimumSize(QtCore.QSize(380, 450))
        self.fr_Connect_Container.setMaximumSize(QtCore.QSize(360, 450))
        self.fr_Connect_Container.setStyleSheet(_fromUtf8("QFrame{border:0px;}"))
        self.fr_Connect_Container.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Connect_Container.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Connect_Container.setObjectName(_fromUtf8("fr_Connect_Container"))
        self.igr_fr_Connect_Container = QtGui.QGridLayout(self.fr_Connect_Container)
        self.igr_fr_Connect_Container.setSpacing(1)
        self.igr_fr_Connect_Container.setContentsMargins(10, 0, 10, 0)
        self.igr_fr_Connect_Container.setObjectName(_fromUtf8("igr_fr_Connect_Container"))
        self.fr_Connect_Top = QtGui.QFrame(self.fr_Connect_Container)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fr_Connect_Top.sizePolicy().hasHeightForWidth())
        self.fr_Connect_Top.setSizePolicy(sizePolicy)
        self.fr_Connect_Top.setMinimumSize(QtCore.QSize(0, 200))
        self.fr_Connect_Top.setMaximumSize(QtCore.QSize(16777215, 180))
        self.fr_Connect_Top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Connect_Top.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Connect_Top.setObjectName(_fromUtf8("fr_Connect_Top"))
        self.igr_fr_Connect_Top = QtGui.QGridLayout(self.fr_Connect_Top)
        self.igr_fr_Connect_Top.setMargin(0)
        self.igr_fr_Connect_Top.setSpacing(0)
        self.igr_fr_Connect_Top.setObjectName(_fromUtf8("igr_fr_Connect_Top"))
        self.fr_Connect_Logo = QtGui.QFrame(self.fr_Connect_Top)
        self.fr_Connect_Logo.setMinimumSize(QtCore.QSize(162, 169))
        self.fr_Connect_Logo.setMaximumSize(QtCore.QSize(162, 169))
        self.fr_Connect_Logo.setStyleSheet(_fromUtf8("QFrame{border:0px;}"))
        self.fr_Connect_Logo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Connect_Logo.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Connect_Logo.setObjectName(_fromUtf8("fr_Connect_Logo"))
        self.igr_fr_Connect_Top.addWidget(self.fr_Connect_Logo, 0, 0, 1, 1)
        self.igr_fr_Connect_Container.addWidget(self.fr_Connect_Top, 0, 0, 1, 1)
        self.fr_Connect = QtGui.QFrame(self.fr_Connect_Container)
        self.fr_Connect.setMinimumSize(QtCore.QSize(360, 215))
        self.fr_Connect.setMaximumSize(QtCore.QSize(360, 215))
        self.fr_Connect.setStyleSheet(_fromUtf8("QFrame{background-color:rgb(189,215,204);\n"
"border-style:outset;\n"
"border-width:1px;\n"
"    border-color: rgb(231, 231, 231);\n"
"}\n"
"QLabel{border-width:0px;}"))
        self.fr_Connect.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Connect.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Connect.setObjectName(_fromUtf8("fr_Connect"))
        self.igr_Connect = QtGui.QGridLayout(self.fr_Connect)
        self.igr_Connect.setMargin(30)
        self.igr_Connect.setObjectName(_fromUtf8("igr_Connect"))
        self.tb_Connect_Ok = QtGui.QPushButton(self.fr_Connect)
        self.tb_Connect_Ok.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Connect_Ok.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border-style:outset;\n"
"    border-color:rgb(59,38,38);\n"
"    border-width:1px;\n"
"    border-radius:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(79, 48, 48, 255), stop:0.495 rgba(79, 48, 48, 255), stop:0.505 rgba(69, 42, 42, 255), stop:1 rgba(69, 42, 42, 255));\n"
"    color:#ffffff;\n"
"    height:38px;\n"
"    font-weight:bold;\n"
"    font-size:11pt;\n"
"    font-family:Arial Black;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(89, 58, 58, 255), stop:0.495 rgba(89, 58, 58, 255), stop:0.505 rgba(79, 52, 52, 255), stop:1 rgba(79, 52, 52, 255));\n"
"}"))
        self.tb_Connect_Ok.setObjectName(_fromUtf8("tb_Connect_Ok"))
        self.igr_Connect.addWidget(self.tb_Connect_Ok, 3, 0, 1, 2)
        self.le_Connect_Alamat = QtGui.QLineEdit(self.fr_Connect)
        self.le_Connect_Alamat.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    background-color:rgb(242,242,242);\n"
"\n"
"    border-style:outset;\n"
"    border-color:rgb(255,255,255);\n"
"    border-width:1px;\n"
"    border-radius:0px;\n"
"    color:rgb(76,76,76);\n"
"    height:38px;\n"
"    font-weight:light;\n"
"    font-size:11pt;\n"
"    font-family:Arial;\n"
"}"))
        self.le_Connect_Alamat.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Connect_Alamat.setObjectName(_fromUtf8("le_Connect_Alamat"))
        self.igr_Connect.addWidget(self.le_Connect_Alamat, 2, 0, 1, 2)
        self.lb_Connect_Judul = QtGui.QLabel(self.fr_Connect)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial Black"))
        font.setPointSize(15)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.lb_Connect_Judul.setFont(font)
        self.lb_Connect_Judul.setStyleSheet(_fromUtf8("QLabel{\n"
"color:white;\n"
"font-family:Arial Black;\n"
"font-size:15pt;\n"
"}"))
        self.lb_Connect_Judul.setObjectName(_fromUtf8("lb_Connect_Judul"))
        self.igr_Connect.addWidget(self.lb_Connect_Judul, 0, 0, 1, 1)
        self.chk_Connect_Lokal = QtGui.QCheckBox(self.fr_Connect)
        self.chk_Connect_Lokal.setStyleSheet(_fromUtf8("QCheckBox{\n"
"background-color:transparent;\n"
"color:rgb(99,99,99);\n"
"font-size:10pt;\n"
"}\n"
""))
        self.chk_Connect_Lokal.setObjectName(_fromUtf8("chk_Connect_Lokal"))
        self.igr_Connect.addWidget(self.chk_Connect_Lokal, 1, 0, 1, 1)
        self.igr_fr_Connect_Container.addWidget(self.fr_Connect, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.fr_Connect_Container, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 0, 1, 1)
        self.st_Main.addWidget(self.st_Connect)
        self.st_Login = QtGui.QWidget()
        self.st_Login.setObjectName(_fromUtf8("st_Login"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.st_Login)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.fr_Login = QtGui.QFrame(self.st_Login)
        self.fr_Login.setMinimumSize(QtCore.QSize(240, 400))
        self.fr_Login.setMaximumSize(QtCore.QSize(240, 400))
        self.fr_Login.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    height:40px;\n"
"    border-radius:0px;\n"
"    background:rgb(242,242,242);\n"
"}\n"
"QFrame{border:0px;}"))
        self.fr_Login.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Login.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Login.setObjectName(_fromUtf8("fr_Login"))
        self.gridLayout_3 = QtGui.QGridLayout(self.fr_Login)
        self.gridLayout_3.setVerticalSpacing(1)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.le_Login_User = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_User.setText(_fromUtf8(""))
        self.le_Login_User.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Login_User.setObjectName(_fromUtf8("le_Login_User"))
        self.gridLayout_3.addWidget(self.le_Login_User, 1, 0, 1, 1)
        self.le_Login_Password_Confirm = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_Password_Confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Login_Password_Confirm.setObjectName(_fromUtf8("le_Login_Password_Confirm"))
        self.gridLayout_3.addWidget(self.le_Login_Password_Confirm, 3, 0, 1, 1)
        self.frame = QtGui.QFrame(self.fr_Login)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.fr_Login_Logo = QtGui.QFrame(self.frame)
        self.fr_Login_Logo.setGeometry(QtCore.QRect(30, 30, 162, 169))
        self.fr_Login_Logo.setMinimumSize(QtCore.QSize(162, 169))
        self.fr_Login_Logo.setMaximumSize(QtCore.QSize(162, 169))
        self.fr_Login_Logo.setStyleSheet(_fromUtf8("QFrame{border:0px;}"))
        self.fr_Login_Logo.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Login_Logo.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Login_Logo.setObjectName(_fromUtf8("fr_Login_Logo"))
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.le_Login_Password = QtGui.QLineEdit(self.fr_Login)
        self.le_Login_Password.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.le_Login_Password.setAlignment(QtCore.Qt.AlignCenter)
        self.le_Login_Password.setObjectName(_fromUtf8("le_Login_Password"))
        self.gridLayout_3.addWidget(self.le_Login_Password, 2, 0, 1, 1)
        self.tb_Login_Ok = QtGui.QPushButton(self.fr_Login)
        self.tb_Login_Ok.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border-style:outset;\n"
"    border-color:rgb(0,41,96);\n"
"    border-width:1px;\n"
"    border-radius:0px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(12, 63, 125, 255), stop:0.495 rgba(12, 63, 125, 255),  stop:0.505 rgba(14, 55, 107, 255), stop:1 rgba(14, 55, 107, 255));\n"
"    color:#ffffff;\n"
"    height:38px;\n"
"    font-weight:bold;\n"
"    font-size:11pt;\n"
"    font-family:Arial Black;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(22, 73, 135, 255), stop:0.495 rgba(22, 73, 135, 255), stop:0.505 rgba(24, 65, 117, 255), stop:1 rgba(24, 65, 117, 255));\n"
"}"))
        self.tb_Login_Ok.setObjectName(_fromUtf8("tb_Login_Ok"))
        self.gridLayout_3.addWidget(self.tb_Login_Ok, 4, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.fr_Login)
        self.st_Main.addWidget(self.st_Login)
        self.st_Database = QtGui.QWidget()
        self.st_Database.setObjectName(_fromUtf8("st_Database"))
        self.gridLayout = QtGui.QGridLayout(self.st_Database)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.fr_Database = QtGui.QFrame(self.st_Database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_Database.sizePolicy().hasHeightForWidth())
        self.fr_Database.setSizePolicy(sizePolicy)
        self.fr_Database.setMinimumSize(QtCore.QSize(500, 350))
        self.fr_Database.setMaximumSize(QtCore.QSize(800, 350))
        self.fr_Database.setStyleSheet(_fromUtf8("QLabel{\n"
"    border:0px;\n"
"}\n"
"QFrame{\n"
"    border:0px;\n"
"}"))
        self.fr_Database.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Database.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Database.setObjectName(_fromUtf8("fr_Database"))
        self.igr_Database = QtGui.QGridLayout(self.fr_Database)
        self.igr_Database.setObjectName(_fromUtf8("igr_Database"))
        spacerItem3 = QtGui.QSpacerItem(180, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Database.addItem(spacerItem3, 2, 2, 1, 1)
        self.sc_Database_List = QtGui.QScrollArea(self.fr_Database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sc_Database_List.sizePolicy().hasHeightForWidth())
        self.sc_Database_List.setSizePolicy(sizePolicy)
        self.sc_Database_List.setMinimumSize(QtCore.QSize(200, 250))
        self.sc_Database_List.setMaximumSize(QtCore.QSize(200, 250))
        self.sc_Database_List.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:1px;\n"
"border-color: rgb(215, 219, 223);\n"
"height:40px;\n"
"min-width:178px;\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.511111, y1:1, x2:0.49, y2:0.420455, stop:0 rgba(209, 209, 209, 255), stop:1 rgba(237, 237, 237, 255));\n"
"color:black;\n"
"}\n"
"QFrame{\n"
"    border-width:1px;\n"
"    border-style:solid;\n"
"    border-color: rgb(240, 240, 240);\n"
"}"))
        self.sc_Database_List.setWidgetResizable(True)
        self.sc_Database_List.setObjectName(_fromUtf8("sc_Database_List"))
        self.scontent_Database_List = QtGui.QWidget()
        self.scontent_Database_List.setGeometry(QtCore.QRect(0, 0, 198, 248))
        self.scontent_Database_List.setObjectName(_fromUtf8("scontent_Database_List"))
        self.ivl_Database_ListContent = QtGui.QVBoxLayout(self.scontent_Database_List)
        self.ivl_Database_ListContent.setObjectName(_fromUtf8("ivl_Database_ListContent"))
        self.sc_Database_List.setWidget(self.scontent_Database_List)
        self.igr_Database.addWidget(self.sc_Database_List, 2, 1, 1, 1)
        self.tb_Database_Create = QtGui.QPushButton(self.fr_Database)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_Database_Create.sizePolicy().hasHeightForWidth())
        self.tb_Database_Create.setSizePolicy(sizePolicy)
        self.tb_Database_Create.setMinimumSize(QtCore.QSize(200, 0))
        self.tb_Database_Create.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Database_Create.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:1px;\n"
"border-color: rgb(215, 219, 223);\n"
"height:40px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.511111, y1:1, x2:0.49, y2:0.420455, stop:0 rgba(16, 159, 255, 255), stop:1 rgba(98, 187, 255, 255));\n"
"color:white;\n"
"}"))
        self.tb_Database_Create.setObjectName(_fromUtf8("tb_Database_Create"))
        self.igr_Database.addWidget(self.tb_Database_Create, 3, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(180, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Database.addItem(spacerItem4, 2, 0, 1, 1)
        self.fr_Database_Top = QtGui.QFrame(self.fr_Database)
        self.fr_Database_Top.setMinimumSize(QtCore.QSize(0, 30))
        self.fr_Database_Top.setStyleSheet(_fromUtf8("QFrame{\n"
"    border:0px;\n"
"    border-bottom-width:1px;\n"
"    border-bottom-style:solid;\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 0), stop:0.5 rgba(240, 119, 70, 100), stop:0.98 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
"}"))
        self.fr_Database_Top.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Database_Top.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Database_Top.setObjectName(_fromUtf8("fr_Database_Top"))
        self.igr_Database_Top = QtGui.QGridLayout(self.fr_Database_Top)
        self.igr_Database_Top.setContentsMargins(0, -1, 0, -1)
        self.igr_Database_Top.setObjectName(_fromUtf8("igr_Database_Top"))
        spacerItem5 = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Database_Top.addItem(spacerItem5, 1, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.igr_Database_Top.addItem(spacerItem6, 1, 2, 1, 1)
        self.lb_Database_Judul = QtGui.QLabel(self.fr_Database_Top)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_Database_Judul.sizePolicy().hasHeightForWidth())
        self.lb_Database_Judul.setSizePolicy(sizePolicy)
        self.lb_Database_Judul.setMinimumSize(QtCore.QSize(200, 20))
        self.lb_Database_Judul.setMaximumSize(QtCore.QSize(200, 20))
        self.lb_Database_Judul.setStyleSheet(_fromUtf8("border:0px;"))
        self.lb_Database_Judul.setObjectName(_fromUtf8("lb_Database_Judul"))
        self.igr_Database_Top.addWidget(self.lb_Database_Judul, 1, 1, 1, 1)
        self.igr_Database.addWidget(self.fr_Database_Top, 1, 0, 1, 3)
        self.gridLayout.addWidget(self.fr_Database, 0, 0, 1, 1)
        self.st_Main.addWidget(self.st_Database)
        self.st_Database_Create = QtGui.QWidget()
        self.st_Database_Create.setObjectName(_fromUtf8("st_Database_Create"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.st_Database_Create)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fr_Database_Create = QtGui.QFrame(self.st_Database_Create)
        self.fr_Database_Create.setMinimumSize(QtCore.QSize(259, 300))
        self.fr_Database_Create.setMaximumSize(QtCore.QSize(250, 300))
        self.fr_Database_Create.setFrameShape(QtGui.QFrame.StyledPanel)
        self.fr_Database_Create.setFrameShadow(QtGui.QFrame.Raised)
        self.fr_Database_Create.setObjectName(_fromUtf8("fr_Database_Create"))
        self.igr_Database_Create = QtGui.QGridLayout(self.fr_Database_Create)
        self.igr_Database_Create.setObjectName(_fromUtf8("igr_Database_Create"))
        self.lb_Database_Create_Judul = QtGui.QLabel(self.fr_Database_Create)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_Database_Create_Judul.sizePolicy().hasHeightForWidth())
        self.lb_Database_Create_Judul.setSizePolicy(sizePolicy)
        self.lb_Database_Create_Judul.setObjectName(_fromUtf8("lb_Database_Create_Judul"))
        self.igr_Database_Create.addWidget(self.lb_Database_Create_Judul, 1, 1, 1, 1)
        self.le_Database_Create_Nama = QtGui.QLineEdit(self.fr_Database_Create)
        self.le_Database_Create_Nama.setStyleSheet(_fromUtf8("QLineEdit{\n"
"    border-style:inset;\n"
"    border-width:1px;\n"
"    border-color:rgba(205,205,205,200);\n"
"    height:20px;\n"
"    padding:5px;\n"
"    border-radius:3px;\n"
"}"))
        self.le_Database_Create_Nama.setObjectName(_fromUtf8("le_Database_Create_Nama"))
        self.igr_Database_Create.addWidget(self.le_Database_Create_Nama, 2, 0, 1, 3)
        self.tb_Database_Create_Buat = QtGui.QPushButton(self.fr_Database_Create)
        self.tb_Database_Create_Buat.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.tb_Database_Create_Buat.setStyleSheet(_fromUtf8("QPushButton{\n"
"border-style:solid;\n"
"border-width:1px;\n"
"border-radius:1px;\n"
"border-color: rgb(215, 219, 223);\n"
"height:40px;\n"
"margin-left:10px;\n"
"margin-right:10px;\n"
"\n"
"}\n"
"QPushButton::hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0.511111, y1:1, x2:0.49, y2:0.420455, stop:0 rgba(16, 159, 255, 255), stop:1 rgba(98, 187, 255, 255));\n"
"color:white;\n"
"}"))
        self.tb_Database_Create_Buat.setObjectName(_fromUtf8("tb_Database_Create_Buat"))
        self.igr_Database_Create.addWidget(self.tb_Database_Create_Buat, 4, 1, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Database_Create.addItem(spacerItem7, 0, 1, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Database_Create.addItem(spacerItem8, 5, 1, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.igr_Database_Create.addItem(spacerItem9, 3, 1, 1, 1)
        self.horizontalLayout.addWidget(self.fr_Database_Create)
        self.st_Main.addWidget(self.st_Database_Create)
        self.igr_Main.addWidget(self.st_Main, 1, 0, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.igr_Main.addItem(spacerItem10, 3, 0, 1, 1)

        self.retranslateUi(fr_Main)
        self.st_Main.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(fr_Main)

    def retranslateUi(self, fr_Main):
        fr_Main.setWindowTitle(_translate("fr_Main", "Frame", None))
        self.tb_Connect_Ok.setText(_translate("fr_Main", "OK", None))
        self.le_Connect_Alamat.setText(_translate("fr_Main", "localhost", None))
        self.le_Connect_Alamat.setPlaceholderText(_translate("fr_Main", "Alamat IP Server", None))
        self.lb_Connect_Judul.setText(_translate("fr_Main", "HUBUNGKAN KE SERVER", None))
        self.chk_Connect_Lokal.setText(_translate("fr_Main", "Lokal komputer ini", None))
        self.le_Login_User.setPlaceholderText(_translate("fr_Main", "username", None))
        self.le_Login_Password_Confirm.setPlaceholderText(_translate("fr_Main", "confirm password", None))
        self.le_Login_Password.setPlaceholderText(_translate("fr_Main", "password", None))
        self.tb_Login_Ok.setText(_translate("fr_Main", "OK", None))
        self.tb_Database_Create.setText(_translate("fr_Main", "Buat Database Baru", None))
        self.lb_Database_Judul.setText(_translate("fr_Main", "Pilih Database Perusahaan :", None))
        self.lb_Database_Create_Judul.setText(_translate("fr_Main", "Berikan nama data :", None))
        self.le_Database_Create_Nama.setPlaceholderText(_translate("fr_Main", "Nama Database", None))
        self.tb_Database_Create_Buat.setText(_translate("fr_Main", "Buat", None))

