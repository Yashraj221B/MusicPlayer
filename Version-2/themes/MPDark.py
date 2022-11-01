# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music-player-beta-darkqnimVm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 570)
        MainWindow.setMinimumSize(QSize(530, 570))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: rgb(39, 44, 54);\n"
"	border-radius:10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: n"
                        "one;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertic"
                        "al {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }					")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuFrame = QFrame(self.centralwidget)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMaximumSize(QSize(58, 16777215))
        self.leftMenuFrame.setStyleSheet(u"background-color: rgb(25, 29, 35);")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.vboxLayout = QVBoxLayout(self.leftMenuFrame)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setMinimumSize(QSize(0, 43))
        self.topMenu.setStyleSheet(u"")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.toggle = QPushButton(self.topMenu)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(0, 54))
        font = QFont()
        font.setPointSize(15)
        self.toggle.setFont(font)
        self.toggle.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(D:/YASH FILES/programming/GUI/images/icons/icon_menu.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:rgb(25, 29, 35);\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(62, 70, 86);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(49, 118, 208);\n"
"}")

        self.verticalLayout_8.addWidget(self.toggle)

        self.player_frame = QFrame(self.topMenu)
        self.player_frame.setObjectName(u"player_frame")
        self.player_frame.setStyleSheet(u"background-color: rgb(39, 44, 53);\n"
"border:none;\n"
"border-left:3px solid rgb(0, 85, 255);")
        self.player_frame.setFrameShape(QFrame.StyledPanel)
        self.player_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.player_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player = QPushButton(self.player_frame)
        self.player.setObjectName(u"player")
        self.player.setMinimumSize(QSize(0, 54))
        self.player.setFont(font)
        self.player.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(D:/YASH FILES/programming/GUI/images/icons/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(62, 70, 86);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(49, 118, 208);\n"
"}")

        self.verticalLayout_2.addWidget(self.player)


        self.verticalLayout_8.addWidget(self.player_frame)

        self.weather_frame = QFrame(self.topMenu)
        self.weather_frame.setObjectName(u"weather_frame")
        self.weather_frame.setStyleSheet(u"background-color: rgb(25, 29, 35);")
        self.weather_frame.setFrameShape(QFrame.StyledPanel)
        self.weather_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.weather_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weather = QPushButton(self.weather_frame)
        self.weather.setObjectName(u"weather")
        self.weather.setMinimumSize(QSize(0, 54))
        self.weather.setFont(font)
        self.weather.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(D:/YASH FILES/programming/GUI/images/icons/weather.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 55px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(62, 70, 86);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(49, 118, 208);\n"
"}")

        self.verticalLayout.addWidget(self.weather)


        self.verticalLayout_8.addWidget(self.weather_frame)


        self.vboxLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.setting_frame = QFrame(self.bottomMenu)
        self.setting_frame.setObjectName(u"setting_frame")
        self.setting_frame.setStyleSheet(u"")
        self.setting_frame.setFrameShape(QFrame.StyledPanel)
        self.setting_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.setting_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.setting_frame)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 54))
        self.settings.setFont(font)
        self.settings.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(D:/YASH FILES/programming/GUI/images/icons/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(62, 70, 86);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(49, 118, 208);\n"
"}")

        self.horizontalLayout_3.addWidget(self.settings)


        self.verticalLayout_9.addWidget(self.setting_frame)


        self.vboxLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.gridLayout.addWidget(self.leftMenuFrame, 1, 0, 1, 2)

        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMinimumSize(QSize(0, 40))
        self.titlebar.setStyleSheet(u"background-color: rgb(25, 29, 35);")
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 9, 6, -1)
        self.title = QLabel(self.titlebar)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 20))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.titlebar)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(20, 20))
        self.minimize.setMaximumSize(QSize(20, 20))
        self.minimize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(67, 255, 64);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(53, 203, 51);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(120, 255, 71);\n"
"}")

        self.horizontalLayout_2.addWidget(self.minimize)

        self.resize = QPushButton(self.titlebar)
        self.resize.setObjectName(u"resize")
        self.resize.setMinimumSize(QSize(20, 20))
        self.resize.setMaximumSize(QSize(20, 20))
        self.resize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(251, 226, 36);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(195, 176, 28);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(241, 251, 56);\n"
"}")

        self.horizontalLayout_2.addWidget(self.resize)

        self.close = QPushButton(self.titlebar)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(20, 20))
        self.close.setMaximumSize(QSize(20, 20))
        self.close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(186, 28, 28);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(222, 33, 33);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(163, 24, 24);\n"
"}")

        self.horizontalLayout_2.addWidget(self.close)


        self.gridLayout.addWidget(self.titlebar, 0, 0, 1, 3)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        font2 = QFont()
        font2.setPointSize(40)
        self.stackedWidget.setFont(font2)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(38, 43, 53);")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_2 = QGridLayout(self.home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pause = QPushButton(self.home)
        self.pause.setObjectName(u"pause")
        self.pause.setFont(font)
        self.pause.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.pause, 4, 1, 1, 1)

        self.min = QPushButton(self.home)
        self.min.setObjectName(u"min")
        self.min.setFont(font)
        self.min.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.min, 5, 0, 1, 1)

        self.max = QPushButton(self.home)
        self.max.setObjectName(u"max")
        self.max.setFont(font)
        self.max.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.max, 5, 1, 1, 1)

        self.listWidget = QListWidget(self.home)
        self.listWidget.setObjectName(u"listWidget")
        font3 = QFont()
        font3.setFamily(u"Palatino Linotype")
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        self.listWidget.setFont(font3)
        self.listWidget.setStyleSheet(u"QListWidget {	\n"
"	background-color: rgb(39, 44, 54);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	border:3px solid rgb(61, 69, 85);\n"
"	font: 10pt \"Palatino Linotype\";\n"
"	color:rgb(225,225,225);\n"
"}\n"
"QListWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QListWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"	color:rgb(0,0,0);\n"
"	border-radius:10px;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"")

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)

        self.grip = QFrame(self.home)
        self.grip.setObjectName(u"grip")
        self.grip.setEnabled(True)
        self.grip.setMaximumSize(QSize(16777215, 30))
        self.grip.setStyleSheet(u"")
        self.grip.setFrameShape(QFrame.StyledPanel)
        self.grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.grip)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.grip)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.size_grip = QFrame(self.grip)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(0, 20))
        self.size_grip.setMaximumSize(QSize(20, 16777215))
        self.size_grip.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(98, 98, 98);\n"
"	border-radius:10px;\n"
"}")
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.size_grip)


        self.gridLayout_2.addWidget(self.grip, 6, 0, 1, 2)

        self.status = QLabel(self.home)
        self.status.setObjectName(u"status")
        font5 = QFont()
        font5.setFamily(u"Palatino Linotype")
        font5.setPointSize(15)
        self.status.setFont(font5)
        self.status.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.status.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.status, 2, 0, 1, 2)

        self.play = QPushButton(self.home)
        self.play.setObjectName(u"play")
        self.play.setFont(font)
        self.play.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"	border-radius:12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.play, 4, 0, 1, 1)

        self.volume = QSlider(self.home)
        self.volume.setObjectName(u"volume")
        self.volume.setAutoFillBackground(False)
        self.volume.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 85, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0.446, y1:0.397, x2:0.446, y2:0.650, stop:0.00493097 rgba(255, 255, 255, 0), stop:0.0192113 rgba(0, 85, 255, 255), stop:0.971689 rgba(0, 85, 255, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	height:21px;\n"
"	width:14px;\n"
"	background-color:rgb(0, 85, 255);\n"
"	border-radius:10px;\n"
"	border:4px solid rgb(198,193,44);\n"
"}\n"
"QSlider::handle:hover{\n"
"	background-color: rgb(255, 248, 57)\n"
"}\n"
"QSlider::handle:pressed{\n"
"	background-color: rgb(154, 150, 34);\n"
"}")
        self.volume.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.volume, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.home)
        self.weather_page = QWidget()
        self.weather_page.setObjectName(u"weather_page")
        self.weather_page.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.weather_page)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.frame = QFrame(self.weather_page)
        self.frame.setObjectName(u"frame")
        font6 = QFont()
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setWeight(50)
        self.frame.setFont(font6)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 9, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 8, 0, 1, 1)

        self.grip_2 = QFrame(self.frame)
        self.grip_2.setObjectName(u"grip_2")
        self.grip_2.setEnabled(True)
        self.grip_2.setMaximumSize(QSize(16777215, 30))
        self.grip_2.setStyleSheet(u"")
        self.grip_2.setFrameShape(QFrame.StyledPanel)
        self.grip_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.grip_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_6 = QLabel(self.grip_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 20))
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label_6)

        self.size_grip_2 = QFrame(self.grip_2)
        self.size_grip_2.setObjectName(u"size_grip_2")
        self.size_grip_2.setMinimumSize(QSize(0, 20))
        self.size_grip_2.setMaximumSize(QSize(20, 16777215))
        self.size_grip_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(98, 98, 98);\n"
"	border-radius:10px;\n"
"}")
        self.size_grip_2.setFrameShape(QFrame.StyledPanel)
        self.size_grip_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.size_grip_2)


        self.gridLayout_7.addWidget(self.grip_2, 10, 0, 1, 3)

        self.visiblity = QLabel(self.frame)
        self.visiblity.setObjectName(u"visiblity")
        font7 = QFont()
        font7.setFamily(u"Nirmala UI Semilight")
        font7.setPointSize(14)
        self.visiblity.setFont(font7)
        self.visiblity.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.visiblity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.visiblity, 3, 0, 1, 1)

        self.wind = QLabel(self.frame)
        self.wind.setObjectName(u"wind")
        self.wind.setFont(font7)
        self.wind.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.wind.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.wind, 9, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 7, 1, 1, 1)

        self.baro = QLabel(self.frame)
        self.baro.setObjectName(u"baro")
        self.baro.setFont(font7)
        self.baro.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.baro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.baro, 7, 0, 1, 1)

        self.pred = QLabel(self.frame)
        self.pred.setObjectName(u"pred")
        self.pred.setFont(font7)
        self.pred.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.pred.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.pred, 1, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.time = QLabel(self.frame_6)
        self.time.setObjectName(u"time")
        self.time.setFont(font7)
        self.time.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.time.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.time, 3, 0, 1, 1)

        self.atmos = QLabel(self.frame_6)
        self.atmos.setObjectName(u"atmos")
        self.atmos.setFont(font7)
        self.atmos.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.atmos.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.atmos, 2, 0, 1, 1)

        self.frame_7 = QFrame(self.frame_6)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.temp = QLabel(self.frame_7)
        self.temp.setObjectName(u"temp")
        self.temp.setMaximumSize(QSize(128, 16777207))
        font8 = QFont()
        font8.setFamily(u"Nirmala UI Semilight")
        font8.setPointSize(33)
        self.temp.setFont(font8)
        self.temp.setAutoFillBackground(False)
        self.temp.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.temp)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1)

        self.city = QLabel(self.frame_6)
        self.city.setObjectName(u"city")
        font9 = QFont()
        font9.setFamily(u"Nirmala UI Semilight")
        font9.setPointSize(16)
        font9.setUnderline(False)
        font9.setStrikeOut(False)
        font9.setKerning(True)
        self.city.setFont(font9)
        self.city.setAutoFillBackground(False)
        self.city.setStyleSheet(u"background-color: rgba(73, 102, 235,0);\n"
"color: rgb(255, 255, 255);")
        self.city.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.city, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_6, 0, 0, 1, 3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.dew = QLabel(self.frame)
        self.dew.setObjectName(u"dew")
        self.dew.setFont(font7)
        self.dew.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: rgb(255, 255, 255);")
        self.dew.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.dew, 5, 0, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.uv_progress = QFrame(self.frame_3)
        self.uv_progress.setObjectName(u"uv_progress")
        self.uv_progress.setMinimumSize(QSize(100, 100))
        self.uv_progress.setMaximumSize(QSize(100, 100))
        self.uv_progress.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.754 rgba(226, 226, 226,50), stop:0.755 rgba(119, 255, 221, 255));\n"
"border-radius:50px;")
        self.uv_progress.setFrameShape(QFrame.StyledPanel)
        self.uv_progress.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.uv_progress)
        self.gridLayout_11.setSpacing(0)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_10 = QFrame(self.uv_progress)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setEnabled(True)
        self.frame_10.setMinimumSize(QSize(0, 0))
        self.frame_10.setMaximumSize(QSize(86, 86))
        self.frame_10.setStyleSheet(u"background-color: rgb(38, 43, 53);\n"
"border-radius:43px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.uvnum = QLabel(self.frame_10)
        self.uvnum.setObjectName(u"uvnum")
        self.uvnum.setGeometry(QRect(2, 4, 81, 41))
        font10 = QFont()
        font10.setFamily(u"Nirmala UI Semilight")
        font10.setPointSize(26)
        self.uvnum.setFont(font10)
        self.uvnum.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.uvnum.setTextFormat(Qt.AutoText)
        self.uvnum.setAlignment(Qt.AlignCenter)
        self.uvnum.setMargin(-10)
        self.uvtxt = QLabel(self.frame_10)
        self.uvtxt.setObjectName(u"uvtxt")
        self.uvtxt.setGeometry(QRect(1, 46, 81, 21))
        font11 = QFont()
        font11.setFamily(u"Segoe UI Symbol")
        font11.setPointSize(12)
        self.uvtxt.setFont(font11)
        self.uvtxt.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);")
        self.uvtxt.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.frame_10, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.uv_progress, 3, 0, 1, 1)

        self.humid_3 = QLabel(self.frame_3)
        self.humid_3.setObjectName(u"humid_3")
        font12 = QFont()
        font12.setPointSize(15)
        font12.setStyleStrategy(QFont.PreferDefault)
        self.humid_3.setFont(font12)
        self.humid_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.humid_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.humid_3, 0, 0, 1, 1)

        self.humid_progress = QFrame(self.frame_3)
        self.humid_progress.setObjectName(u"humid_progress")
        self.humid_progress.setMinimumSize(QSize(100, 100))
        self.humid_progress.setMaximumSize(QSize(100, 100))
        self.humid_progress.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.752 rgba(226, 226, 226,50), stop:0.755 rgba(119, 255, 221, 255));\n"
"border-radius:50px;")
        self.humid_progress.setFrameShape(QFrame.StyledPanel)
        self.humid_progress.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.humid_progress)
        self.gridLayout_8.setSpacing(0)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.humid_progress)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setMinimumSize(QSize(0, 0))
        self.frame_8.setMaximumSize(QSize(86, 86))
        self.frame_8.setStyleSheet(u"background-color: rgb(38, 43, 53);\n"
"border-radius:43px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.humidity = QLabel(self.frame_8)
        self.humidity.setObjectName(u"humidity")
        self.humidity.setGeometry(QRect(3, 21, 81, 41))
        self.humidity.setFont(font10)
        self.humidity.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")
        self.humidity.setAlignment(Qt.AlignCenter)
        self.humidity.setMargin(-10)

        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.humid_progress, 1, 0, 1, 1)

        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 1, 2, 9, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.Weather = QLabel(self.weather_page)
        self.Weather.setObjectName(u"Weather")
        font13 = QFont()
        font13.setPointSize(35)
        self.Weather.setFont(font13)
        self.Weather.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.Weather.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.Weather, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.weather_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_4 = QGridLayout(self.settings_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 1, 0, 1, 4)

        self.frame_2 = QFrame(self.settings_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.cancel = QPushButton(self.frame_2)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setMinimumSize(QSize(90, 0))
        font14 = QFont()
        font14.setFamily(u"Segoe UI Semilight")
        font14.setPointSize(15)
        self.cancel.setFont(font14)
        self.cancel.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom:2px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(46, 164, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"	border:2px solid rgb(162, 255, 185)\n"
"}")

        self.horizontalLayout_4.addWidget(self.cancel)

        self.save = QPushButton(self.frame_2)
        self.save.setObjectName(u"save")
        self.save.setMinimumSize(QSize(90, 0))
        self.save.setFont(font14)
        self.save.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom:2px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(46, 164, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"	border:2px solid rgb(162, 255, 185)\n"
"}")

        self.horizontalLayout_4.addWidget(self.save)


        self.gridLayout_4.addWidget(self.frame_2, 15, 2, 1, 2)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 4, 0, 1, 4)

        self.dir = QLineEdit(self.settings_page)
        self.dir.setObjectName(u"dir")
        self.dir.setFont(font14)
        self.dir.setStyleSheet(u"QLineEdit{\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"	border:2px solid rgb(99, 107, 255)\n"
"}\n"
"QLineEdit:hover{\n"
"	border:2px solid rgb(46, 164, 255)\n"
"}\n"
"QLineEdit:focus{\n"
"	border:2px solid rgb(162, 255, 185)\n"
"}")

        self.gridLayout_4.addWidget(self.dir, 3, 0, 1, 3)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 14, 0, 1, 4)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 12, 0, 1, 4)

        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")
        font15 = QFont()
        font15.setPointSize(16)
        self.label_2.setFont(font15)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 8, 0, 1, 4)

        self.label_3 = QLabel(self.settings_page)
        self.label_3.setObjectName(u"label_3")
        font16 = QFont()
        font16.setFamily(u"Nirmala UI Semilight")
        font16.setPointSize(30)
        self.label_3.setFont(font16)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 4)

        self.frame_4 = QFrame(self.settings_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.light = QRadioButton(self.frame_4)
        self.light.setObjectName(u"light")
        self.light.setMaximumSize(QSize(120, 16777215))
        self.light.setFont(font)
        self.light.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(197, 197, 197);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.light)

        self.dark = QRadioButton(self.frame_4)
        self.dark.setObjectName(u"dark")
        self.dark.setFont(font)
        self.dark.setStyleSheet(u"QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(197, 197, 197);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"")
        self.dark.setChecked(True)

        self.horizontalLayout_6.addWidget(self.dark)


        self.gridLayout_4.addWidget(self.frame_4, 6, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 15, 0, 1, 2)

        self.label_5 = QLabel(self.settings_page)
        self.label_5.setObjectName(u"label_5")
        font17 = QFont()
        font17.setFamily(u"Segoe MDL2 Assets")
        font17.setPointSize(16)
        self.label_5.setFont(font17)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 4)

        self.browse = QPushButton(self.settings_page)
        self.browse.setObjectName(u"browse")
        self.browse.setFont(font14)
        self.browse.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
"	color: rgb(255, 255, 255);\n"
"	padding-bottom:2px;\n"
"}\n"
"QPushButton:hover{\n"
"	border:2px solid rgb(46, 164, 255)\n"
"}\n"
"QPushButton:pressed{\n"
"	border:2px solid rgb(162, 255, 185)\n"
"}")
        self.browse.setAutoDefault(False)
        self.browse.setFlat(False)

        self.gridLayout_4.addWidget(self.browse, 3, 3, 1, 1)

        self.grip_3 = QFrame(self.settings_page)
        self.grip_3.setObjectName(u"grip_3")
        self.grip_3.setEnabled(True)
        self.grip_3.setMaximumSize(QSize(16777215, 30))
        self.grip_3.setStyleSheet(u"")
        self.grip_3.setFrameShape(QFrame.StyledPanel)
        self.grip_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.grip_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_7 = QLabel(self.grip_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setFont(font4)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label_7)

        self.size_grip_3 = QFrame(self.grip_3)
        self.size_grip_3.setObjectName(u"size_grip_3")
        self.size_grip_3.setMinimumSize(QSize(0, 20))
        self.size_grip_3.setMaximumSize(QSize(20, 16777215))
        self.size_grip_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(98, 98, 98);\n"
"	border-radius:10px;\n"
"}")
        self.size_grip_3.setFrameShape(QFrame.StyledPanel)
        self.size_grip_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.size_grip_3)


        self.gridLayout_4.addWidget(self.grip_3, 16, 0, 1, 4)

        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.stackedWidget.raise_()
        self.titlebar.raise_()
        self.leftMenuFrame.raise_()

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.browse.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.player.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.weather.setText(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.titlebar.setToolTip(QCoreApplication.translate("MainWindow", u"Music Player", None))
#endif // QT_CONFIG(tooltip)
        self.title.setText(QCoreApplication.translate("MainWindow", u"Music Player", None))
#if QT_CONFIG(tooltip)
        self.minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize.setText("")
#if QT_CONFIG(tooltip)
        self.resize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.resize.setText("")
#if QT_CONFIG(tooltip)
        self.close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close.setText("")
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.min.setText(QCoreApplication.translate("MainWindow", u" -10 Seconds  ", None))
        self.max.setText(QCoreApplication.translate("MainWindow", u" +10 Seconds  ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By: Yashraj Ghule", None))
#if QT_CONFIG(tooltip)
        self.size_grip.setToolTip(QCoreApplication.translate("MainWindow", u"resize", None))
#endif // QT_CONFIG(tooltip)
        self.status.setText(QCoreApplication.translate("MainWindow", u"Select a Music", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"By: Yashraj Ghule", None))
#if QT_CONFIG(tooltip)
        self.size_grip_2.setToolTip(QCoreApplication.translate("MainWindow", u"resize", None))
#endif // QT_CONFIG(tooltip)
        self.visiblity.setText(QCoreApplication.translate("MainWindow", u"Visiblity 4 km", None))
        self.wind.setText(QCoreApplication.translate("MainWindow", u"Wind No wind", None))
        self.baro.setText(QCoreApplication.translate("MainWindow", u"Pressure 1010 mbar", None))
        self.pred.setText(QCoreApplication.translate("MainWindow", u"Feels like 24\u00baC", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Updated as of :time:", None))
        self.atmos.setText(QCoreApplication.translate("MainWindow", u"cloudy", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"28\u00baC", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"Pune,India", None))
        self.dew.setText(QCoreApplication.translate("MainWindow", u"Dew Point 19\u00baC", None))
        self.uvnum.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.uvtxt.setText(QCoreApplication.translate("MainWindow", u"Moderate", None))
        self.humid_3.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.humidity.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>25%</p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"UV Index", None))
        self.Weather.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Weather</p></body></html>", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.dir.setText(QCoreApplication.translate("MainWindow", u"C:/Users/Admin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Songs Folder Path", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", u"   Browse   ", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"By: Yashraj Ghule", None))
#if QT_CONFIG(tooltip)
        self.size_grip_3.setToolTip(QCoreApplication.translate("MainWindow", u"resize", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

