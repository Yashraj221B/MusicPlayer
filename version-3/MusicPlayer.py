from ui_MusicPlayer import *
from PySide2.QtMultimedia import QMediaContent, QMediaPlayer
from grips import *
import time
import os
import sys


class activate(QMainWindow):
    def __init__(self):
        super(activate, self).__init__()
        self.sliderstate = True
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.player = QMediaPlayer(self)
        # self.ui.topBar.hide()
        self.ui.volume.setValue(10)
        self.ui.volume.valueChanged.connect(self.volume)
        self.ui.play.clicked.connect(self.play)

        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(100)
        effect.setColor(QColor(0, 0, 0, 50))
        self.ui.AppWindow.setGraphicsEffect(effect)

        self.player.positionChanged.connect(self.setPos)
        # self.player.stateChanged.connect(self.setPos)
        self.load_files("D:/YASH FILES/SONGS")
        self.ui.position.sliderPressed.connect(self.changeFalse)
        self.ui.position.sliderReleased.connect(self.changeTrue)
        self.ui.position.sliderMoved.connect(self.changePos)
        self.player.stateChanged.connect(self.state)
        self.ui.volume_button.clicked.connect(self.muteStatus)
        self.ui.close.clicked.connect(self.appExit)
        self.ui.minimize.clicked.connect(self.appMinimize)
        self.ui.maximize.clicked.connect(self.appMaximize)
        self.volume()

        self.hide_grips = True
        self.setContentsMargins(10, 10, 10, 10)
        self.left_grip = PyGrips(self, "left", self.hide_grips)
        self.right_grip = PyGrips(self, "right", self.hide_grips)
        self.top_grip = PyGrips(self, "top", self.hide_grips)
        self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
        self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
        self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
        self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
        self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        self.ui.music.clicked.connect(self.music)
        self.ui.settings.clicked.connect(self.settings)

        def moveWindow(event):
            if event.buttons() == Qt.LeftButton:
                # if self.pos().x()<0 and self.pos().y()<0:
                #     self.move(0,0)
                # elif self.pos().x()<0:
                #     self.move(0,self.pos().y())
                # elif self.pos().y()<0:
                #     self.move(self.pos().x(),0)
                if self.isMaximized():
                    self.ui.gridLayout_5.setContentsMargins(5, 5, 5, 5)
                    icon = QIcon()
                    icon.addFile(":/topNavigation/Assets/Light/maximize.png",
                                 QSize(), QIcon.Normal, QIcon.Off)
                    self.ui.maximize.setIcon(icon)
                    self.left_grip.show()
                    self.right_grip.show()
                    self.top_grip.show()
                    self.bottom_grip.show()
                    self.top_left_grip.show()
                    self.top_right_grip.show()
                    self.bottom_left_grip.show()
                    self.bottom_right_grip.show()
                    self.showNormal()
                self.showNormal()
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.topBar.mouseMoveEvent = moveWindow
        self.ui.toggle.clicked.connect(self.toggle)
        self.show()

    def music(self):
        self.ui.music_frame.setStyleSheet(u"#music_frame{\n"
                                          "	border:none;\n"
                                          "	border-left:4px solid rgb(0, 0, 255);\n"
                                          "	border-right:3px solid rgb(67, 75, 90);\n"
                                          "}")
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.settings_frame.setStyleSheet("")

    def settings(self):
        self.ui.settings_frame.setStyleSheet(u"#settings_frame{\n"
                                             "	border:none;\n"
                                             "	border-left:4px solid rgb(0, 0, 255);\n"
                                             "	border-right:3px solid rgb(67, 75, 90);\n"
                                             "}")
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.music_frame.setStyleSheet("")

    def toggle(self):
        self.anim = QPropertyAnimation(self.ui.leftBar, b"maximumWidth")
        self.anim.setStartValue(55)
        self.anim.setEndValue(150)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.setDuration(200)
        if self.ui.leftBar.maximumWidth() <= 60:
            self.anim.setDirection(self.anim.Forward)
            self.anim.start()
        else:
            self.anim.setDirection(self.anim.Backward)
            self.anim.start()

    def resizeEvent(self, event):
        self.left_grip.setGeometry(5, 10, 10, self.height())
        self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
        self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
        self.bottom_grip.setGeometry(
            5, self.height() - 15, self.width() - 10, 10)
        self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
        self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
        self.bottom_right_grip.setGeometry(
            self.width() - 20, self.height() - 20, 15, 15)

    def appExit(self):
        effect = QGraphicsOpacityEffect(self, opacity=1)
        self.ui.AppWindow.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setDuration(100)
        self.anim.start()
        self.anim.stateChanged.connect(lambda: sys.exit(0))

    def appMinimize(self):
        effect = QGraphicsOpacityEffect(self, opacity=1)
        self.ui.AppWindow.setGraphicsEffect(effect)
        self.anim = QPropertyAnimation(self, b"windowOpacity")
        self.anim.setStartValue(1.0)
        self.anim.setEndValue(0.0)
        self.anim.setDuration(100)
        self.anim.start()
        self.anim.stateChanged.connect(self.mainMinimize)

    def appMaximize(self):
        if self.isMaximized():
            self.setContentsMargins(10, 10, 10, 10)
            self.ui.gridLayout_5.setContentsMargins(5, 5, 5, 5)
            icon = QIcon()
            icon.addFile(":/topNavigation/Assets/Light/maximize.png",
                         QSize(), QIcon.Normal, QIcon.Off)
            self.ui.maximize.setIcon(icon)
            self.left_grip.show()
            self.right_grip.show()
            self.top_grip.show()
            self.bottom_grip.show()
            self.top_left_grip.show()
            self.top_right_grip.show()
            self.bottom_left_grip.show()
            self.bottom_right_grip.show()
            self.showNormal()
        else:
            self.ui.gridLayout_5.setContentsMargins(0, 0, 0, 0)
            self.setContentsMargins(0, 0, 0, 0)
            icon = QIcon()
            icon.addFile(":/topNavigation/Assets/Light/restore.png",
                         QSize(), QIcon.Normal, QIcon.Off)
            self.ui.maximize.setIcon(icon)
            self.left_grip.hide()
            self.right_grip.hide()
            self.top_grip.hide()
            self.bottom_grip.hide()
            self.top_left_grip.hide()
            self.top_right_grip.hide()
            self.bottom_left_grip.hide()
            self.bottom_right_grip.hide()
            self.showMaximized()

    def mainMinimize(self):
        self.showMinimized()
        self.setWindowOpacity(1.0)
        effect = QGraphicsDropShadowEffect(self)
        effect.setBlurRadius(30)
        effect.setColor(QColor(0, 0, 0, 50))
        self.ui.AppWindow.setGraphicsEffect(effect)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def load_files(self, path):
        files = os.listdir(path)
        self.ui.listWidget.addItems(files)

    def volume(self):
        self.player.setVolume(self.ui.volume.value())
        if self.ui.volume.value() < 50:
            self.player.setMuted(False)
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_down.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(False)

        if self.ui.volume.value() > 50:
            self.player.setMuted(False)
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_up.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(False)

        if self.ui.volume.value() == 0:
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_off.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(True)

    def play(self):
        print(self.player.state())
        if self.player.state() == self.player.State.StoppedState:
            print("s1 was called!")
            try:
                self.player.setMedia(QMediaContent(
                    "D:/YASH FILES/SONGS"+"/"+self.ui.listWidget.currentItem().text()))
                self.player.play()
            except:
                print("Error Occured at s1")

        elif self.player.state() == self.player.State.PlayingState:
            if self.player.currentMedia().canonicalUrl().toString().lower() == str("D:/YASH FILES/SONGS/"+self.ui.listWidget.currentItem().text()).lower():
                print("s2.1 was called!")
                self.player.pause()

            else:
                print("s2.2 was called!")
                self.player.setMedia(QMediaContent(
                    "D:/YASH FILES/SONGS"+"/"+self.ui.listWidget.currentItem().text()))
                self.player.play()

        elif self.player.state() == self.player.State.PausedState:
            if self.player.currentMedia().canonicalUrl().toString().lower() == str("D:/YASH FILES/SONGS/"+self.ui.listWidget.currentItem().text()).lower():
                print("s3.1 was called!")
                self.player.play()

            else:
                print("s3.2 was called!")
                self.player.setMedia(QMediaContent(
                    "D:/YASH FILES/SONGS"+"/"+self.ui.listWidget.currentItem().text()))
                self.player.play()

    def setPos(self):
        self.ui.totalPos.setText(
            str(time.strftime("%M:%S", time.gmtime(self.player.duration()/1000))))
        duration = str(time.strftime(
            "%M:%S", time.gmtime(self.player.position()/1000)))
        self.ui.currentPos.setText(duration)
        self.ui.position.setMaximum(self.player.duration())
        if self.sliderstate:
            self.ui.position.setValue(self.player.position())

    def changePos(self):
        self.player.setPosition(self.ui.position.value())

    def changeTrue(self):
        self.sliderstate = True

    def changeFalse(self):
        self.sliderstate = False

    def muteStatus(self):
        if self.player.isMuted() and self.ui.volume.value() == 0:
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_down.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(False)
            self.ui.volume.setValue(15)
            self.player.setVolume(10)

        elif self.player.isMuted():
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_down.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(False)
        else:
            icon = QIcon()
            icon.addFile(":/mediaControls/Assets/Light/volume_off.png")
            self.ui.volume_button.setIcon(icon)
            self.player.setMuted(True)

    def state(self):
        if self.player.state() == self.player.State.StoppedState:
            icon = QIcon()
            icon.addFile(u":/mediaControls/Assets/Light/pause.png",
                         QSize(), QIcon.Normal, QIcon.Off)
            self.ui.play.setIcon(icon)
            self.ui.play.setIconSize(QSize(30, 30))

        elif self.player.state() == self.player.State.PlayingState:
            icon = QIcon()
            icon.addFile(u":/mediaControls/Assets/Light/play.png",
                         QSize(), QIcon.Normal, QIcon.Off)
            self.ui.play.setIcon(icon)
            self.ui.play.setIconSize(QSize(30, 30))

        elif self.player.state() == self.player.State.PausedState:
            icon = QIcon()
            icon.addFile(u":/mediaControls/Assets/Light/pause.png",
                         QSize(), QIcon.Normal, QIcon.Off)
            self.ui.play.setIcon(icon)
            self.ui.play.setIconSize(QSize(30, 30))

    def setPos(self):
        self.ui.totalPos.setText(
            str(time.strftime("%M:%S", time.gmtime(self.player.duration()/1000))))
        duration = str(time.strftime(
            "%M:%S", time.gmtime(self.player.position()/1000)))
        self.ui.currentPos.setText(duration)
        self.ui.position.setMaximum(self.player.duration())
        if self.sliderstate:
            self.ui.position.setValue(self.player.position())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = activate()
    sys.exit(app.exec_())
