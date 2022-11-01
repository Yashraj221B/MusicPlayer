# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musicFrameITfblh.ui'
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
        MainWindow.resize(693, 553)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(35, 39, 47);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 75))
        self.frame_3.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(4, 4, 4, 4)
        self.label_7 = QLabel(self.frame_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(45, 45))
        self.label_7.setMaximumSize(QSize(45, 45))
        self.label_7.setStyleSheet(u"padding:10px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_7.setPixmap(QPixmap(u":/leftNavigation/Assets/Light/Music.png"))
        self.label_7.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_7)

        self.label_9 = QLabel(self.frame_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 55))
        self.label_9.setMaximumSize(QSize(16777215, 55))
        self.label_9.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.label_9.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_9)

        self.pushButton_3 = QPushButton(self.frame_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(45, 45))
        self.pushButton_3.setMaximumSize(QSize(55, 55))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 97, 102);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(71, 72, 76);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/mediaControls/Assets/Light/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(25, 25))

        self.horizontalLayout_4.addWidget(self.pushButton_3)

        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(55, 45))
        self.label_8.setMaximumSize(QSize(55, 55))
        self.label_8.setStyleSheet(u"font: 11pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.horizontalLayout_4.addWidget(self.label_8)


        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 1)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 60))
        self.frame_6.setMaximumSize(QSize(16777215, 75))
        self.frame_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(4)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(45, 45))
        self.label_13.setMaximumSize(QSize(45, 45))
        self.label_13.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding:10px;")
        self.label_13.setPixmap(QPixmap(u":/leftNavigation/Assets/Light/Music.png"))
        self.label_13.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_6)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 55))
        self.label_14.setMaximumSize(QSize(16777215, 55))
        self.label_14.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.label_14.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.label_14)

        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(55, 55))
        self.pushButton_5.setMaximumSize(QSize(55, 55))
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 97, 102);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(71, 72, 76);\n"
"}")
        self.pushButton_5.setIcon(icon)
        self.pushButton_5.setIconSize(QSize(25, 25))

        self.horizontalLayout_6.addWidget(self.pushButton_5)

        self.label_15 = QLabel(self.frame_6)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(55, 55))
        self.label_15.setMaximumSize(QSize(55, 55))
        self.label_15.setStyleSheet(u"font: 11pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.horizontalLayout_6.addWidget(self.label_15)


        self.gridLayout.addWidget(self.frame_6, 5, 0, 1, 1)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 60))
        self.frame_2.setMaximumSize(QSize(16777215, 75))
        self.frame_2.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(45, 45))
        self.label_10.setMaximumSize(QSize(45, 45))
        self.label_10.setStyleSheet(u"padding:10px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label_10.setPixmap(QPixmap(u":/leftNavigation/Assets/Light/Music.png"))
        self.label_10.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 55))
        self.label_12.setMaximumSize(QSize(16777215, 55))
        self.label_12.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.label_12.setWordWrap(True)

        self.horizontalLayout_3.addWidget(self.label_12)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(55, 55))
        self.pushButton_4.setMaximumSize(QSize(55, 55))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 97, 102);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(71, 72, 76);\n"
"}")
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(55, 55))
        self.label_11.setMaximumSize(QSize(55, 55))
        self.label_11.setStyleSheet(u"font: 11pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.horizontalLayout_3.addWidget(self.label_11)


        self.gridLayout.addWidget(self.frame_2, 4, 0, 1, 1)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 60))
        self.frame_4.setMaximumSize(QSize(16777215, 75))
        self.frame_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_5.setSpacing(4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(4, 4, 4, 4)
        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(45, 45))
        self.label_4.setMaximumSize(QSize(45, 45))
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);\n"
"padding:10px;")
        self.label_4.setPixmap(QPixmap(u":/leftNavigation/Assets/Light/Music.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label_4)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 55))
        self.label_6.setMaximumSize(QSize(16777215, 55))
        self.label_6.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.label_6.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(55, 55))
        self.pushButton_2.setMaximumSize(QSize(55, 55))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 97, 102);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(71, 72, 76);\n"
"}")
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 25))

        self.horizontalLayout_5.addWidget(self.pushButton_2)

        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(55, 55))
        self.label_5.setMaximumSize(QSize(55, 55))
        self.label_5.setStyleSheet(u"font: 11pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.horizontalLayout_5.addWidget(self.label_5)


        self.gridLayout.addWidget(self.frame_4, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 60))
        self.frame_5.setMaximumSize(QSize(16777215, 75))
        self.frame_5.setStyleSheet(u"background-color: rgba(255, 255, 255, 50);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(45, 45))
        self.label.setMaximumSize(QSize(45, 45))
        self.label.setStyleSheet(u"padding:10px;\n"
"background-color: rgba(255, 255, 255, 0);")
        self.label.setPixmap(QPixmap(u":/leftNavigation/Assets/Light/Music.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 55))
        self.label_2.setMaximumSize(QSize(16777215, 55))
        self.label_2.setStyleSheet(u"font: 12pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(55, 55))
        self.pushButton.setMaximumSize(QSize(55, 55))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(95, 97, 102);\n"
"}\n"
"QPushButton::pressed{\n"
"	background-color: rgb(71, 72, 76);\n"
"}")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setFlat(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(55, 55))
        self.label_3.setMaximumSize(QSize(55, 55))
        self.label_3.setStyleSheet(u"font: 11pt \"Nirmala UI\";\n"
"color: rgb(255, 255, 255);\n"
"padding:5px;")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.gridLayout.addWidget(self.frame_5, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 693, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_7.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Imagine Dragon - Radioactive", None))
        self.pushButton_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"04:30", None))
        self.label_13.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Imagine Dragon - Radioactive", None))
        self.pushButton_5.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"04:30", None))
        self.label_10.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Imagine Dragon - Radioactive", None))
        self.pushButton_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"04:30", None))
        self.label_4.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Imagine Dragon - Radioactive", None))
        self.pushButton_2.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"04:30", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Imagine Dragon - Radioactive ", None))
        self.pushButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"04:30", None))
    # retranslateUi


import sys
class activate(QMainWindow):
    def __init__(self):
        super(activate,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.gridLayout.setAlignment(Qt.AlignTop)
        self.show()

app = QApplication(sys.argv)
win = activate()
sys.exit(app.exec_())
