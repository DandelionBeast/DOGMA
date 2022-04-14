# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacekGlbpK.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 86, 216, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"*{\n"
"	border: none;\n"
"}\n"
"\n"
"QLabel {\n"
"color: white;\n"
"}")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(153, 153, 255);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Side_menu_Container = QFrame(self.centralwidget)
        self.Side_menu_Container.setObjectName(u"Side_menu_Container")
        self.Side_menu_Container.setMaximumSize(QSize(0, 16777215))
        self.Side_menu_Container.setStyleSheet(u"background-color: rgb(160, 160, 150);")
        self.Side_menu_Container.setFrameShape(QFrame.StyledPanel)
        self.Side_menu_Container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Side_menu_Container)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.Side_menu_Container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(198, 0))
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_7 = QFrame(self.slide_menu)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(6, 6, 6, 6)
        self.label_2 = QLabel(self.frame_7)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.pushButton_9 = QPushButton(self.frame_7)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setAutoFillBackground(False)
        icon = QIcon()
        icon.addFile(u":/icons/Icons/wine-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon)

        self.horizontalLayout_8.addWidget(self.pushButton_9)


        self.verticalLayout_5.addWidget(self.frame_7, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.slide_menu)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_8)
        self.toolBox.setObjectName(u"toolBox")
        palette1 = QPalette()
        brush2 = QBrush(QColor(100, 100, 100, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush2)
        self.toolBox.setPalette(palette1)
        self.toolBox.setStyleSheet(u"QToolBox{\n"
"	background-color: rgb(100, 100, 100);\n"
"	text-align: left;\n"
"}\n"
"QToolbox::tab {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	text-align: left;\n"
"}\n"
"\n"
"\n"
"     ")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 180, 438))
        palette2 = QPalette()
        brush3 = QBrush(QColor(160, 160, 150, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        self.page.setPalette(palette2)
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QPushButton {\n"
"color: white;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_13 = QPushButton(self.frame_10)
        self.pushButton_13.setObjectName(u"pushButton_13")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/logo-microsoft.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon1)
        self.pushButton_13.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.frame_10)
        self.pushButton_12.setObjectName(u"pushButton_12")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/logo-xbox.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_12)

        self.pushButton_11 = QPushButton(self.frame_10)
        self.pushButton_11.setObjectName(u"pushButton_11")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/bus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_11.setIcon(icon3)
        self.pushButton_11.setIconSize(QSize(32, 32))

        self.verticalLayout_8.addWidget(self.pushButton_11)


        self.verticalLayout_7.addWidget(self.frame_10, 0, Qt.AlignTop)

        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/chevron-down-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon4, u"Calculators")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 180, 438))
        self.verticalLayout_9 = QVBoxLayout(self.page_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.page_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_10.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.frame_11)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_10.addWidget(self.pushButton_15)


        self.verticalLayout_9.addWidget(self.frame_11, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page_2, icon4, u"Weapon Tables")

        self.verticalLayout_6.addWidget(self.toolBox)


        self.verticalLayout_5.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.slide_menu)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.pushButton_10 = QPushButton(self.frame_9)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon5)
        self.pushButton_10.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.pushButton_10)


        self.verticalLayout_5.addWidget(self.frame_9, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.Side_menu_Container)

        self.Main_Body = QFrame(self.centralwidget)
        self.Main_Body.setObjectName(u"Main_Body")
        palette3 = QPalette()
        brush4 = QBrush(QColor(153, 153, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.Main_Body.setPalette(palette3)
        self.Main_Body.setStyleSheet(u"app.setStyle(\"fusion\")")
        self.Main_Body.setFrameShape(QFrame.StyledPanel)
        self.Main_Body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.Main_Body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.Main_Body)
        self.header_frame.setObjectName(u"header_frame")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.header_frame.setPalette(palette4)
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.frame_5 = QFrame(self.header_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(50, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_8 = QPushButton(self.frame_5)
        self.pushButton_8.setObjectName(u"pushButton_8")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/reorder-three-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon6)
        self.pushButton_8.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_8)


        self.horizontalLayout_2.addWidget(self.frame_5, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_3 = QFrame(self.header_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(6000, 6000))

        self.horizontalLayout_6.addWidget(self.lineEdit, 0, Qt.AlignLeft)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton_6.setPalette(palette5)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/search-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.pushButton_6, 0, Qt.AlignLeft)


        self.horizontalLayout_2.addWidget(self.frame_3, 0, Qt.AlignLeft|Qt.AlignTop)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton_5.setPalette(palette6)
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/cloud-download-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon8)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton_4.setPalette(palette7)
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/megaphone-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon9)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.frame_2, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.frame.setPalette(palette8)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton_3.setPalette(palette9)
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/arrow-undo-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon10)
        self.pushButton_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton_2.setPalette(palette10)
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/repeat-sharp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon11)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.pushButton.setPalette(palette11)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/backspace-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_contents = QFrame(self.Main_Body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush4)
        self.main_body_contents.setPalette(palette12)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.main_body_contents)

        self.Footer = QFrame(self.Main_Body)
        self.Footer.setObjectName(u"Footer")
        self.Footer.setFrameShape(QFrame.StyledPanel)
        self.Footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Footer)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.Footer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Semibold")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.verticalLayout_3.addWidget(self.label)


        self.horizontalLayout_3.addWidget(self.frame_4, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.Footer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/accessibility-outline.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon13)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.pushButton_7)


        self.horizontalLayout_3.addWidget(self.frame_6, 0, Qt.AlignBottom)

        self.Size_Grip = QFrame(self.Footer)
        self.Size_Grip.setObjectName(u"Size_Grip")
        self.Size_Grip.setMinimumSize(QSize(15, 15))
        self.Size_Grip.setMaximumSize(QSize(15, 15))
        self.Size_Grip.setFrameShape(QFrame.StyledPanel)
        self.Size_Grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.Size_Grip, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.Footer, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.Main_Body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Appname", None))
        self.pushButton_9.setText("")
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"ITEM 1", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"ITEM 2", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"ITEM 3", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Calculators", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"All Weapons", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Strength Weapons", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Weapon Tables", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_8.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_3.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dogma Indexer v1.0.0", None))
        self.pushButton_7.setText("")
    # retranslateUi

