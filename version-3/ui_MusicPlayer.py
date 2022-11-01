# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MusicPlayerDHDniO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(635, 575)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(5, 5, 5, 5)
        self.AppWindow = QFrame(self.centralwidget)
        self.AppWindow.setObjectName(u"AppWindow")
        self.AppWindow.setEnabled(True)
        self.AppWindow.setMinimumSize(QSize(625, 565))
        self.AppWindow.setStyleSheet(u"#AppWindow{\n"
"	background-color: ;\n"
"	background-color: rgb(67, 75, 90);\n"
"	border:1px solid rgb(32, 36, 43);\n"
"}\n"
"#topBar{\n"
"	background-color:rgb(35, 39, 47);\n"
"}\n"
"#leftBar{\n"
"	background-color:;\n"
"	background-color: rgb(35, 39, 47);\n"
"	border:none;\n"
"}\n"
"#bottomBar{\n"
"	background-color: rgb(35, 39, 47);\n"
"}\n"
"#title{\n"
"	padding-left:10px;\n"
"	color:rgb(225,225,225);\n"
"	font: 15pt \"Segoe UI\";\n"
"}\n"
"#appNav QPushButton{\n"
"	border-radius:8px;\n"
"}\n"
"#appNav QPushButton::hover{\n"
"	background-color: rgb(87, 99, 118);\n"
"}\n"
"#appNav QPushButton::pressed{\n"
"	background-color:rgb(0, 117, 206);\n"
"}\n"
"#appNav QPushButton#close::pressed{\n"
"	background-color:rgb(255, 0, 200);\n"
"}\n"
"#leftBar QPushButton{\n"
"	text-align:left;\n"
"	padding-left:40px;\n"
"	padding-bottom:5px;\n"
"	background-position:left centre;\n"
"	background-repeat:no-repeat;\n"
"	height:45px;\n"
"	/*border:none;\n"
"	border-left:8px solid transparent;\n"
"	border-right:8px solid trans"
                        "parent;*/\n"
"	background-color: transparent;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 15pt \"Nirmala UI Semilight\";\n"
"}\n"
"#leftBar QPushButton::hover{\n"
"	background-color: rgb(94, 107, 127);\n"
"}\n"
"#leftBar QPushButton::pressed{\n"
"	background-color: rgb(64, 115, 255);\n"
"}\n"
"#toggle{\n"
"	border:none;\n"
"	border-left:15px solid transparent;\n"
"	background-image: url(:/leftNavigation/Assets/Light/menu.png);\n"
"}\n"
"#music{\n"
"	border:none;\n"
"	border-left:14px solid transparent;\n"
"	background-image: url(:/leftNavigation/Assets/Light/Music.png);\n"
"}\n"
"#settings{\n"
"	border:none;\n"
"	border-left:16px solid transparent;\n"
"	border-right:10px solid transparent;\n"
"	background-image: url(:/leftNavigation/Assets/Light/settings.png);\n"
"}\n"
"QToolTip{\n"
"	position:5px 10px;\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(60, 68, 81);\n"
"	font: 10pt \"Segoe UI\";\n"
"	border:none;\n"
"	border-left:5px solid rgb(190, 190, 190);\n"
"}\n"
"QListWidget {\n"
"	background-colo"
                        "r:;\n"
"	background-color: rgb(71, 80, 95);\n"
"	border:2px solid rgb(142, 159, 190);\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"    outline: 0;\n"
"	font: 12pt \"Segoe UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QListWidget::item:selected {\n"
"	background-color: rgb(5, 180, 255);\n"
"	color: rgb(225, 225, 255);\n"
"}\n"
"QListWidget::item:selected:active {\n"
"	background-color: rgb(5, 180, 255);\n"
"}\n"
"\n"
"QListWidget::item:hover {\n"
"	background-color: rgb(138, 155, 185);\n"
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
"    subcontrol-position"
                        ": right;\n"
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
"     background: none;\n"
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
"    border-bottom-right-radius: "
                        "7px;\n"
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
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }	\n"
"#frame_2 QPushButton{\n"
"	background-color: rgb(60, 65, 94);\n"
"	border:2px solid rgb(226, 226, 226);\n"
"	padding-left:2px;\n"
"}\n"
"#frame_2 QPushButton::hover{\n"
"	background-color: rgb(96, 104, 150);\n"
"}\n"
"#frame_2 QPushButton::pressed{\n"
"	background-color: rgb(35, 37, 54);\n"
"}\n"
"#frame_3 QPushButton{\n"
"	background-color: rgb(60, 65, 94);\n"
"	border:2px solid rgb(226, 226, 226);\n"
"	border-radius:20px;\n"
"}\n"
"#frame_3 QPushButto"
                        "n::hover{\n"
"	background-color: rgb(96, 104, 150);\n"
"}\n"
"#frame_3 QPushButton::pressed{\n"
"	background-color: rgb(35, 37, 54);\n"
"}\n"
"#play{\n"
"	border-radius:27px;\n"
"}\n"
"#next{\n"
"	border-radius:20px;\n"
"}\n"
"#previous{\n"
"	border-radius:20px;\n"
"}\n"
"#frame_5 QLabel{\n"
"	background-color: rgb(110, 124, 148);\n"
"	padding:5px 10px;\n"
"	color: rgb(255, 255, 255);\n"
"	font: 8pt \"Segoe UI Semibold\";\n"
"	border-radius:5px;\n"
"}\n"
"QSlider::groove:horizontal{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:0.114, x2:0.5, y2:0.978312, stop:0.253534 rgba(0, 0, 0, 0), stop:0.260645 rgba(154, 155, 158, 255), stop:0.632422 rgba(159, 160, 161, 255), stop:0.63902 rgba(0, 0, 0, 0));\n"
"}\n"
"QSlider::handle:horizontal{\n"
"	height:20px;\n"
"	width:20px;\n"
"	background-color: rgb(3, 179, 255);\n"
"	border-radius:10px;\n"
"}\n"
"QSlider::handle:hover{\n"
"	background-color: rgb(2, 142, 202);\n"
"}\n"
"QSlider::handle:pressed{\n"
"	background-color: rgb(93,"
                        " 29, 255);\n"
"}\n"
"#song{\n"
"	font: 15pt \"Segoe UI Semibold\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(33, 33, 33);\n"
"	padding-bottom:3px;\n"
"	border-radius:15px;\n"
"}\n"
"#settings_page QLabel{\n"
"	font: 18pt \"Nirmala UI\";\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#settings_page QLineEdit{\n"
"	font: 12pt \"Nirmala UI\";\n"
"	background-color: rgb(226, 226, 226);\n"
"	padding:3px;\n"
"}\n"
"#settings_page QRadioButton{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Nirmala UI\";\n"
"}\n"
"#settings_page QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"#settings_page QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"#settings_page QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"#settings_page QPushButton{\n"
"	background-color: rgb"
                        "(97, 113, 144);\n"
"	color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(29, 146, 255);\n"
"	font: 14pt \"Segoe UI\";\n"
"	border-radius:10px;\n"
"}\n"
"#settings_page QPushButton::hover{\n"
"	background-color: rgb(119, 139, 176);\n"
"}\n"
"#settings_page QPushButton::pressed{\n"
"	background-color: rgb(74, 86, 109);\n"
"}\n"
"#settings_page QPushButton::disabled{\n"
"	color: rgb(181, 181, 181);\n"
"	border:2px solid rgb(29, 115, 190)\n"
"}\n"
"#size_grip{\n"
"	padding:3px;\n"
"	background-color: rgb(84, 94, 113);\n"
"	border-radius:10px;\n"
"}\n"
"#size_grip::hover{\n"
"	background-color: rgb(104, 116, 139);\n"
"}\n"
"#designer{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 10pt \"Segoe UI Semibold\";\n"
"}")
        self.AppWindow.setFrameShape(QFrame.StyledPanel)
        self.AppWindow.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.AppWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.topBar = QFrame(self.AppWindow)
        self.topBar.setObjectName(u"topBar")
        self.topBar.setStyleSheet(u"")
        self.topBar.setFrameShape(QFrame.StyledPanel)
        self.topBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.topBar)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(self.topBar)
        self.title.setObjectName(u"title")
        self.title.setStyleSheet(u"")

        self.horizontalLayout_2.addWidget(self.title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.appNav = QFrame(self.topBar)
        self.appNav.setObjectName(u"appNav")
        self.appNav.setStyleSheet(u"")
        self.appNav.setFrameShape(QFrame.StyledPanel)
        self.appNav.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.appNav)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.minimize = QPushButton(self.appNav)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(30, 30))
        self.minimize.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/topNavigation/Assets/Light/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize.setIcon(icon)

        self.horizontalLayout.addWidget(self.minimize)

        self.maximize = QPushButton(self.appNav)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMinimumSize(QSize(30, 30))
        self.maximize.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/topNavigation/Assets/Light/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximize.setIcon(icon1)

        self.horizontalLayout.addWidget(self.maximize)

        self.close = QPushButton(self.appNav)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(30, 30))
        self.close.setToolTipDuration(-1)
        self.close.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u"Assets/Light/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.close.setIcon(icon2)

        self.horizontalLayout.addWidget(self.close)


        self.horizontalLayout_2.addWidget(self.appNav)


        self.gridLayout.addWidget(self.topBar, 0, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.AppWindow)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFocusPolicy(Qt.ClickFocus)
        self.stackedWidget.setStyleSheet(u"")
        self.music_page = QWidget()
        self.music_page.setObjectName(u"music_page")
        self.music_page.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.music_page)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.listWidget = QListWidget(self.music_page)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"")
        self.listWidget.setDragEnabled(False)
        self.listWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerItem)

        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 2)

        self.frame_5 = QFrame(self.music_page)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setHorizontalSpacing(10)
        self.gridLayout_8.setVerticalSpacing(0)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.position = QSlider(self.frame_5)
        self.position.setObjectName(u"position")
        self.position.setMinimumSize(QSize(0, 20))
        self.position.setMaximumSize(QSize(16777215, 20))
        self.position.setStyleSheet(u"")
        self.position.setTracking(True)
        self.position.setOrientation(Qt.Horizontal)
        self.position.setTickPosition(QSlider.NoTicks)
        self.position.setTickInterval(0)

        self.gridLayout_8.addWidget(self.position, 0, 1, 1, 1)

        self.totalPos = QLabel(self.frame_5)
        self.totalPos.setObjectName(u"totalPos")
        self.totalPos.setMinimumSize(QSize(48, 0))
        self.totalPos.setStyleSheet(u"")
        self.totalPos.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.totalPos, 0, 2, 1, 1)

        self.currentPos = QLabel(self.frame_5)
        self.currentPos.setObjectName(u"currentPos")
        self.currentPos.setMinimumSize(QSize(48, 0))
        self.currentPos.setAlignment(Qt.AlignCenter)

        self.gridLayout_8.addWidget(self.currentPos, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 3, 0, 1, 1)

        self.song = QLabel(self.music_page)
        self.song.setObjectName(u"song")
        self.song.setStyleSheet(u"")
        self.song.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.song, 1, 0, 1, 1)

        self.frame = QFrame(self.music_page)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(4)
        self.gridLayout_7.setVerticalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_4 = QSpacerItem(36, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 0, 1, 2, 1)

        self.play = QPushButton(self.frame_2)
        self.play.setObjectName(u"play")
        self.play.setMinimumSize(QSize(55, 55))
        self.play.setMaximumSize(QSize(55, 55))
        self.play.setCursor(QCursor(Qt.PointingHandCursor))
        self.play.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/mediaControls/Assets/Light/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play.setIcon(icon3)
        self.play.setIconSize(QSize(30, 30))

        self.gridLayout_7.addWidget(self.play, 0, 3, 2, 1, Qt.AlignVCenter)

        self.next = QPushButton(self.frame_2)
        self.next.setObjectName(u"next")
        self.next.setMinimumSize(QSize(40, 40))
        self.next.setMaximumSize(QSize(40, 40))
        self.next.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/mediaControls/Assets/Light/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon4)
        self.next.setIconSize(QSize(20, 20))

        self.gridLayout_7.addWidget(self.next, 0, 4, 2, 1, Qt.AlignVCenter)

        self.previous = QPushButton(self.frame_2)
        self.previous.setObjectName(u"previous")
        self.previous.setMinimumSize(QSize(40, 40))
        self.previous.setMaximumSize(QSize(40, 40))
        self.previous.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/mediaControls/Assets/Light/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.previous.setIcon(icon5)

        self.gridLayout_7.addWidget(self.previous, 0, 2, 2, 1, Qt.AlignVCenter)

        self.horizontalSpacer_3 = QSpacerItem(35, 27, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 6, 2, 1)


        self.gridLayout_6.addWidget(self.frame_2, 0, 1, 1, 1)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(150, 0))
        self.frame_3.setMaximumSize(QSize(150, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.volume_button = QPushButton(self.frame_3)
        self.volume_button.setObjectName(u"volume_button")
        self.volume_button.setMinimumSize(QSize(40, 40))
        self.volume_button.setMaximumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/mediaControls/Assets/Light/volume_down.png", QSize(), QIcon.Normal, QIcon.Off)
        self.volume_button.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.volume_button, 0, Qt.AlignVCenter)

        self.volume = QSlider(self.frame_3)
        self.volume.setObjectName(u"volume")
        self.volume.setMinimumSize(QSize(100, 20))
        self.volume.setMaximumSize(QSize(16777215, 20))
        self.volume.setStyleSheet(u"")
        self.volume.setMaximum(50)
        self.volume.setValue(15)
        self.volume.setTracking(True)
        self.volume.setOrientation(Qt.Horizontal)
        self.volume.setInvertedAppearance(False)

        self.horizontalLayout_4.addWidget(self.volume)


        self.gridLayout_6.addWidget(self.frame_3, 0, 2, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame, 2, 0, 1, 2)

        self.stackedWidget.addWidget(self.music_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"")
        self.gridLayout_9 = QGridLayout(self.settings_page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setVerticalSpacing(15)
        self.gridLayout_9.setContentsMargins(-1, 10, -1, 9)
        self.apply = QPushButton(self.settings_page)
        self.apply.setObjectName(u"apply")
        self.apply.setEnabled(True)
        self.apply.setMinimumSize(QSize(100, 0))
        self.apply.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.apply, 8, 1, 1, 1)

        self.frame_6 = QFrame(self.settings_page)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.label_2, 0, 0, 1, 1)

        self.dark_theme = QRadioButton(self.frame_6)
        self.dark_theme.setObjectName(u"dark_theme")
        self.dark_theme.setStyleSheet(u"")
        self.dark_theme.setChecked(True)

        self.gridLayout_10.addWidget(self.dark_theme, 1, 0, 1, 1)

        self.light_theme = QRadioButton(self.frame_6)
        self.light_theme.setObjectName(u"light_theme")
        self.light_theme.setStyleSheet(u"")

        self.gridLayout_10.addWidget(self.light_theme, 2, 0, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_5, 1, 2, 2, 1)


        self.gridLayout_9.addWidget(self.frame_6, 3, 0, 2, 2)

        self.frame_8 = QFrame(self.settings_page)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.path = QLineEdit(self.frame_8)
        self.path.setObjectName(u"path")
        self.path.setLayoutDirection(Qt.LeftToRight)
        self.path.setStyleSheet(u"")
        self.path.setMaxLength(1000)
        self.path.setEchoMode(QLineEdit.Normal)
        self.path.setDragEnabled(True)
        self.path.setClearButtonEnabled(False)

        self.gridLayout_11.addWidget(self.path, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_8)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.pushButton, 1, 1, 1, 1)

        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label, 0, 0, 1, 2)


        self.gridLayout_9.addWidget(self.frame_8, 0, 0, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(492, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_9.addItem(self.horizontalSpacer_2, 8, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_2, 7, 0, 1, 2)

        self.frame_7 = QFrame(self.settings_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.custom = QRadioButton(self.frame_7)
        self.custom.setObjectName(u"custom")

        self.gridLayout_12.addWidget(self.custom, 2, 1, 1, 1)

        self.label_3 = QLabel(self.frame_7)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_12.addWidget(self.label_3, 0, 1, 1, 3)

        self.windows = QRadioButton(self.frame_7)
        self.windows.setObjectName(u"windows")
        self.windows.setChecked(True)

        self.gridLayout_12.addWidget(self.windows, 1, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_7, 1, 3, 4, 1)


        self.gridLayout_9.addWidget(self.frame_7, 5, 0, 1, 2)

        self.stackedWidget.addWidget(self.settings_page)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)

        self.leftBar = QFrame(self.AppWindow)
        self.leftBar.setObjectName(u"leftBar")
        self.leftBar.setMinimumSize(QSize(0, 0))
        self.leftBar.setMaximumSize(QSize(55, 16777215))
        self.leftBar.setStyleSheet(u"")
        self.leftBar.setFrameShape(QFrame.StyledPanel)
        self.leftBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftBar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle_frame = QFrame(self.leftBar)
        self.toggle_frame.setObjectName(u"toggle_frame")
        self.toggle_frame.setFrameShape(QFrame.StyledPanel)
        self.toggle_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.toggle_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toggle = QPushButton(self.toggle_frame)
        self.toggle.setObjectName(u"toggle")
        self.toggle.setMinimumSize(QSize(0, 40))
        self.toggle.setMaximumSize(QSize(16777208, 55))
        self.toggle.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.toggle, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.toggle_frame)

        self.music_frame = QFrame(self.leftBar)
        self.music_frame.setObjectName(u"music_frame")
        self.music_frame.setStyleSheet(u"#music_frame{\n"
"	border:none;\n"
"	border-left:4px solid rgb(0, 0, 255);\n"
"	border-right:3px solid rgb(67, 75, 90);\n"
"}")
        self.music_frame.setFrameShape(QFrame.StyledPanel)
        self.music_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.music_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.music = QPushButton(self.music_frame)
        self.music.setObjectName(u"music")
        self.music.setMinimumSize(QSize(0, 40))
        self.music.setMaximumSize(QSize(16777215, 55))

        self.horizontalLayout_3.addWidget(self.music)


        self.verticalLayout_2.addWidget(self.music_frame)

        self.verticalSpacer = QSpacerItem(20, 244, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settings_frame = QFrame(self.leftBar)
        self.settings_frame.setObjectName(u"settings_frame")
        self.settings_frame.setStyleSheet(u"")
        self.settings_frame.setFrameShape(QFrame.StyledPanel)
        self.settings_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.settings_frame)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.settings = QPushButton(self.settings_frame)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 40))
        self.settings.setMaximumSize(QSize(16777215, 55))
        self.settings.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.settings, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.settings_frame)


        self.gridLayout.addWidget(self.leftBar, 1, 0, 1, 1)

        self.bottomBar = QFrame(self.AppWindow)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMaximumSize(QSize(16777215, 25))
        self.bottomBar.setStyleSheet(u"")
        self.bottomBar.setFrameShape(QFrame.StyledPanel)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 2, 15, 2)
        self.designer = QLabel(self.bottomBar)
        self.designer.setObjectName(u"designer")
        self.designer.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.designer)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_6)


        self.gridLayout.addWidget(self.bottomBar, 2, 0, 1, 2)

        self.stackedWidget.raise_()
        self.topBar.raise_()
        self.leftBar.raise_()
        self.bottomBar.raise_()

        self.gridLayout_5.addWidget(self.AppWindow, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Music Player", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"MusicPlayer", None))
#if QT_CONFIG(tooltip)
        self.minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize.setText("")
#if QT_CONFIG(tooltip)
        self.maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximize.setText("")
#if QT_CONFIG(tooltip)
        self.close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close.setText("")
#if QT_CONFIG(tooltip)
        self.position.setToolTip(QCoreApplication.translate("MainWindow", u"Position", None))
#endif // QT_CONFIG(tooltip)
        self.totalPos.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.currentPos.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.song.setText(QCoreApplication.translate("MainWindow", u"Music Player", None))
#if QT_CONFIG(tooltip)
        self.play.setToolTip(QCoreApplication.translate("MainWindow", u"Play", None))
#endif // QT_CONFIG(tooltip)
        self.play.setText("")
#if QT_CONFIG(shortcut)
        self.play.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.next.setToolTip(QCoreApplication.translate("MainWindow", u"Next", None))
#endif // QT_CONFIG(tooltip)
        self.next.setText("")
#if QT_CONFIG(tooltip)
        self.previous.setToolTip(QCoreApplication.translate("MainWindow", u"Previous", None))
#endif // QT_CONFIG(tooltip)
        self.previous.setText("")
#if QT_CONFIG(tooltip)
        self.volume_button.setToolTip(QCoreApplication.translate("MainWindow", u"Volume", None))
#endif // QT_CONFIG(tooltip)
        self.volume_button.setText("")
        self.apply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Theme", None))
        self.dark_theme.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.light_theme.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.path.setText("")
        self.path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Music Location", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Where to Look for Music", None))
        self.custom.setText(QCoreApplication.translate("MainWindow", u"Custom (Preview)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Title Bar", None))
        self.windows.setText(QCoreApplication.translate("MainWindow", u"Windows", None))
#if QT_CONFIG(tooltip)
        self.toggle.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.toggle.setText(QCoreApplication.translate("MainWindow", u"Toggle", None))
#if QT_CONFIG(tooltip)
        self.music.setToolTip(QCoreApplication.translate("MainWindow", u"music", None))
#endif // QT_CONFIG(tooltip)
        self.music.setText(QCoreApplication.translate("MainWindow", u"Music", None))
#if QT_CONFIG(tooltip)
        self.settings.setToolTip(QCoreApplication.translate("MainWindow", u"settings", None))
#endif // QT_CONFIG(tooltip)
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.designer.setText(QCoreApplication.translate("MainWindow", u"By: Yashraj Ghule", None))
    # retranslateUi

