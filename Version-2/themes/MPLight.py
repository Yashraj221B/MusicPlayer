# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'music-player-beta-light.ui'
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
        MainWindow.resize(663, 558)
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
        self.titlebar = QFrame(self.centralwidget)
        self.titlebar.setObjectName(u"titlebar")
        self.titlebar.setMaximumSize(QSize(16777215, 33))
        self.titlebar.setStyleSheet(u"background-color: rgb(130, 121, 255);")
        self.titlebar.setFrameShape(QFrame.StyledPanel)
        self.titlebar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.titlebar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, -1)
        self.title = QLabel(self.titlebar)
        self.title.setObjectName(u"title")
        self.title.setMinimumSize(QSize(0, 20))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.titlebar)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(45, 20))
        self.minimize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(67, 255, 64);\n"
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
        self.resize.setMinimumSize(QSize(45, 20))
        self.resize.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(251, 226, 36);\n"
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
        self.close.setMinimumSize(QSize(45, 20))
        self.close.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgb(186, 28, 28);\n"
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
        font1 = QFont()
        font1.setPointSize(40)
        self.stackedWidget.setFont(font1)
        self.stackedWidget.setStyleSheet(u"background-color: rgb(255, 249, 249)")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.gridLayout_2 = QGridLayout(self.home)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.max = QPushButton(self.home)
        self.max.setObjectName(u"max")
        font2 = QFont()
        font2.setPointSize(15)
        self.max.setFont(font2)
        self.max.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.max, 5, 1, 1, 1)

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
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"")

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

        self.volume = QSlider(self.home)
        self.volume.setObjectName(u"volume")
        self.volume.setStyleSheet(u"QSlider::groove:horizontal{\n"
"	border-radius:10px;\n"
"	background-color: rgb(0, 85, 255);\n"
"	border:px solid rgb(255, 255, 255);\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	height:21px;\n"
"	width:16px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:3px solid rgb(255, 64, 64);\n"
"	border-radius:10px;\n"
"}\n"
"QSlider::handle:hover{\n"
"	background-color: rgb(255, 248, 57)\n"
"}\n"
"QSlider::handle:pressed{\n"
"	background-color: rgb(154, 150, 34);\n"
"}")
        self.volume.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.volume, 3, 0, 1, 2)

        self.min = QPushButton(self.home)
        self.min.setObjectName(u"min")
        self.min.setFont(font2)
        self.min.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.min, 5, 0, 1, 1)

        self.status = QLabel(self.home)
        self.status.setObjectName(u"status")
        font4 = QFont()
        font4.setFamily(u"Palatino Linotype")
        font4.setPointSize(15)
        self.status.setFont(font4)
        self.status.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.status.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.status, 2, 0, 1, 2)

        self.pause = QPushButton(self.home)
        self.pause.setObjectName(u"pause")
        self.pause.setFont(font2)
        self.pause.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.pause, 4, 1, 1, 1)

        self.play = QPushButton(self.home)
        self.play.setObjectName(u"play")
        self.play.setFont(font2)
        self.play.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	border:none;\n"
"	background-color:rgb(153, 65, 156);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(214, 91, 218);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgb(149, 79, 255);\n"
"}")

        self.gridLayout_2.addWidget(self.play, 4, 0, 1, 1)

        self.listWidget = QListWidget(self.home)
        self.listWidget.setObjectName(u"listWidget")
        font5 = QFont()
        font5.setFamily(u"Palatino Linotype")
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setWeight(50)
        self.listWidget.setFont(font5)
        self.listWidget.setStyleSheet(u"QListWidget {	\n"
"	background-color: rgb(255, 255, 255);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(44, 49, 60);\n"
"	border:3px solid rgb(61, 69, 85);\n"
"	font: 10pt \"Palatino Linotype\";\n"
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
"QHeaderView::section{\n"
"	Background-color: rgb(39, 44, 54);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 60);\n"
"	border-style: none;\n"
" "
                        "   border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QListWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.listWidget, 1, 0, 1, 2)

        self.stackedWidget.addWidget(self.home)
        self.weather_page = QWidget()
        self.weather_page.setObjectName(u"weather_page")
        self.weather_page.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.weather_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.Weather = QLabel(self.weather_page)
        self.Weather.setObjectName(u"Weather")
        self.Weather.setFont(font1)
        self.Weather.setStyleSheet(u"")
        self.Weather.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.Weather, 0, 0, 1, 1)

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
        self.wind = QLabel(self.frame)
        self.wind.setObjectName(u"wind")
        font7 = QFont()
        font7.setFamily(u"Nirmala UI Semilight")
        font7.setPointSize(14)
        self.wind.setFont(font7)
        self.wind.setStyleSheet(u"")
        self.wind.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.wind, 9, 0, 1, 1)

        self.baro = QLabel(self.frame)
        self.baro.setObjectName(u"baro")
        self.baro.setFont(font7)
        self.baro.setStyleSheet(u"")
        self.baro.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.baro, 7, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 9, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.frame_5 = QFrame(self.frame_3)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(150, 150))
        self.frame_5.setMaximumSize(QSize(150, 150))
        self.frame_5.setStyleSheet(u"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.752 rgb(202, 202, 202) stop:0.755 rgb(38, 43, 53));\n"
"border-radius:75px;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setMaximumSize(QSize(135, 135))
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:66px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(24, 89, 81, 21))
        self.label_4.setFont(font7)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.humid = QLabel(self.frame_8)
        self.humid.setObjectName(u"humid")
        self.humid.setGeometry(QRect(16, 22, 101, 61))
        font8 = QFont()
        font8.setFamily(u"Nirmala UI Semilight")
        font8.setPointSize(41)
        self.humid.setFont(font8)
        self.humid.setStyleSheet(u"")
        self.humid.setAlignment(Qt.AlignCenter)
        self.humid.setMargin(-10)

        self.gridLayout_8.addWidget(self.frame_8, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_3, 1, 2, 9, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_3, 4, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_8, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer, 8, 0, 1, 1)

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
        self.time.setStyleSheet(u"")
        self.time.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.time, 3, 0, 1, 1)

        self.atmos = QLabel(self.frame_6)
        self.atmos.setObjectName(u"atmos")
        self.atmos.setFont(font7)
        self.atmos.setStyleSheet(u"")
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
        font9 = QFont()
        font9.setFamily(u"Nirmala UI Semilight")
        font9.setPointSize(45)
        self.temp.setFont(font9)
        self.temp.setAutoFillBackground(False)
        self.temp.setStyleSheet(u"")
        self.temp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.temp)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_10)


        self.gridLayout_9.addWidget(self.frame_7, 0, 0, 1, 1)

        self.city = QLabel(self.frame_6)
        self.city.setObjectName(u"city")
        font10 = QFont()
        font10.setFamily(u"Nirmala UI Semilight")
        font10.setPointSize(16)
        font10.setUnderline(False)
        font10.setStrikeOut(False)
        font10.setKerning(True)
        self.city.setFont(font10)
        self.city.setAutoFillBackground(False)
        self.city.setStyleSheet(u"")
        self.city.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.city, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_6, 0, 0, 1, 3)

        self.pred = QLabel(self.frame)
        self.pred.setObjectName(u"pred")
        self.pred.setFont(font7)
        self.pred.setStyleSheet(u"")
        self.pred.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.pred, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 3, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_7, 7, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(270, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 5, 1, 1, 1)

        self.dew = QLabel(self.frame)
        self.dew.setObjectName(u"dew")
        self.dew.setFont(font7)
        self.dew.setStyleSheet(u"")
        self.dew.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.dew, 5, 0, 1, 1)

        self.visiblity = QLabel(self.frame)
        self.visiblity.setObjectName(u"visiblity")
        self.visiblity.setFont(font7)
        self.visiblity.setStyleSheet(u"")
        self.visiblity.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_7.addWidget(self.visiblity, 3, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_4, 2, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.weather_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.gridLayout_4 = QGridLayout(self.settings_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.settings_page)
        self.label_3.setObjectName(u"label_3")
        font11 = QFont()
        font11.setFamily(u"Nirmala UI Semilight")
        font11.setPointSize(30)
        self.label_3.setFont(font11)
        self.label_3.setStyleSheet(u"")
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
        self.light.setFont(font2)
        self.light.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(44, 49, 60);\n"
"	border: 3px solid rgb(44, 49, 60);	\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.light)

        self.dark = QRadioButton(self.frame_4)
        self.dark.setObjectName(u"dark")
        self.dark.setFont(font2)
        self.dark.setStyleSheet(u"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	color: rgb(255, 255, 255);\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(255, 255, 255);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(44, 49, 60);\n"
"	border: 3px solid rgb(44, 49, 60);	\n"
"}\n"
"")
        self.dark.setChecked(True)

        self.horizontalLayout_6.addWidget(self.dark)


        self.gridLayout_4.addWidget(self.frame_4, 6, 0, 1, 4)

        self.browse = QPushButton(self.settings_page)
        self.browse.setObjectName(u"browse")
        font12 = QFont()
        font12.setFamily(u"Segoe UI Semilight")
        font12.setPointSize(15)
        self.browse.setFont(font12)
        self.browse.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
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

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_7, 12, 0, 1, 4)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 1, 0, 1, 4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 15, 0, 1, 2)

        self.dir = QLineEdit(self.settings_page)
        self.dir.setObjectName(u"dir")
        self.dir.setFont(font12)
        self.dir.setStyleSheet(u"QLineEdit{\n"
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

        self.label_2 = QLabel(self.settings_page)
        self.label_2.setObjectName(u"label_2")
        font13 = QFont()
        font13.setPointSize(16)
        self.label_2.setFont(font13)
        self.label_2.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_2, 5, 0, 1, 4)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_9, 4, 0, 1, 4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_8, 8, 0, 1, 4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_5, 14, 0, 1, 4)

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
        self.cancel.setFont(font12)
        self.cancel.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
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
        self.save.setFont(font12)
        self.save.setStyleSheet(u"QPushButton{\n"
"	border:2px solid rgb(0, 85, 255);\n"
"	border-radius:15px;	\n"
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

        self.label_5 = QLabel(self.settings_page)
        self.label_5.setObjectName(u"label_5")
        font14 = QFont()
        font14.setFamily(u"Segoe MDL2 Assets")
        font14.setPointSize(16)
        self.label_5.setFont(font14)
        self.label_5.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.label_5, 2, 0, 1, 4)

        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 2, 1, 1)

        self.leftMenuFrame = QFrame(self.centralwidget)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setMaximumSize(QSize(60, 16777215))
        self.leftMenuFrame.setStyleSheet(u"background-color: rgb(130, 121, 255);")
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
        self.toggle.setFont(font2)
        self.toggle.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(icons/icon_menu.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:rgb(130, 121, 255);\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
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
        self.player_frame.setStyleSheet(u"background-color: rgb(130, 121, 255);\n"
"border:none;\n"
"border-left:5px solid rgb(91, 91, 91);")
        self.player_frame.setFrameShape(QFrame.StyledPanel)
        self.player_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.player_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player = QPushButton(self.player_frame)
        self.player.setObjectName(u"player")
        self.player.setMinimumSize(QSize(0, 54))
        self.player.setFont(font2)
        self.player.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(icons/cil-home.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
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
        self.weather_frame.setStyleSheet(u"background-color: rgb(130, 121, 255);")
        self.weather_frame.setFrameShape(QFrame.StyledPanel)
        self.weather_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.weather_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.weather = QPushButton(self.weather_frame)
        self.weather.setObjectName(u"weather")
        self.weather.setMinimumSize(QSize(0, 54))
        self.weather.setFont(font2)
        self.weather.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(icons/weather.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 18px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 55px;\n"
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
        self.settings.setFont(font2)
        self.settings.setStyleSheet(u"QPushButton {	\n"
"	background-image:url(icons/cil-settings.png);\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 50px;\n"
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
        self.max.setText(QCoreApplication.translate("MainWindow", u" +10 Seconds  ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"By: Yashraj Ghule", None))
#if QT_CONFIG(tooltip)
        self.size_grip.setToolTip(QCoreApplication.translate("MainWindow", u"resize", None))
#endif // QT_CONFIG(tooltip)
        self.min.setText(QCoreApplication.translate("MainWindow", u" -10 Seconds  ", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"Select a Music", None))
        self.pause.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.Weather.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Weather</p></body></html>", None))
        self.wind.setText(QCoreApplication.translate("MainWindow", u"Wind No wind", None))
        self.baro.setText(QCoreApplication.translate("MainWindow", u"Pressure 1010 mbar", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Humidity", None))
        self.humid.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>25%</p></body></html>", None))
        self.time.setText(QCoreApplication.translate("MainWindow", u"Updated as of :time:", None))
        self.atmos.setText(QCoreApplication.translate("MainWindow", u"cloudy", None))
        self.temp.setText(QCoreApplication.translate("MainWindow", u"28\u00baC", None))
        self.city.setText(QCoreApplication.translate("MainWindow", u"Pune,India", None))
        self.pred.setText(QCoreApplication.translate("MainWindow", u"Feels like 24\u00baC", None))
        self.dew.setText(QCoreApplication.translate("MainWindow", u"Dew Point 19\u00baC", None))
        self.visiblity.setText(QCoreApplication.translate("MainWindow", u"Visiblity 4 km", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.light.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.dark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.browse.setText(QCoreApplication.translate("MainWindow", u"   Browse   ", None))
        self.dir.setText(QCoreApplication.translate("MainWindow", u"C:/Users/Admin", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.cancel.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Songs Folder Path", None))
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.player.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.weather.setText(QCoreApplication.translate("MainWindow", u"Weather", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi

