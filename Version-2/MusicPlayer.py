import json
import os
import sys
from config import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import *
import rerun
import requests

from themes import MPDark, MPLight


class activate(QMainWindow):
    def __init__(self):
        super(activate, self).__init__()
        if load_theme == "dark":
            self.ui = MPDark.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.dark.setChecked(True)
        else:
            self.ui = MPLight.Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.light.setChecked(True)
        self.media = QMediaPlayer(self)
        self.ui.dir.setText(load_path)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.close.clicked.connect(lambda: sys.exit())
        self.ui.toggle.clicked.connect(self.toggle)
        self.anim = QPropertyAnimation(self.ui.leftMenuFrame, QByteArray(b"maximumWidth"))
        self.GLOBAL_STATE = 0
        self.geo = self.geometry()
        self.file = load_path
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.ui.close.clicked.connect(lambda: sys.exit())
        self.grip = QSizeGrip(self.ui.size_grip)
        # self.grip.setStyleSheet("QSizeGrip { width: 10px; height: 10px; margin: 5px; background-color:transparent; }")
        self.grip.setToolTip("Resize")
        self.ui.listWidget.addItems(os.listdir(load_path))
        self.ui.volume.setMaximum(200)
        self.ui.play.clicked.connect(lambda: print(self.ui.listWidget.currentItem().text()))
        self.ui.minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.resize.clicked.connect(self.maximize_restore)
        self.ui.volume.valueChanged.connect(self.setvol)
        self.ui.play.clicked.connect(self.play)
        self.ui.pause.clicked.connect(self.stop)
        self.ui.max.clicked.connect(self.seekpten)
        self.ui.min.clicked.connect(self.seekmten)
        self.ui.weather.clicked.connect(self.weather)
        self.ui.settings.clicked.connect(self.settings)
        self.ui.player.clicked.connect(self.player)
        self.ui.volume.setValue(10)
        self.ui.save.clicked.connect(self.save)
        self.ui.browse.clicked.connect(self.browse)
        self.getWeather()

        def moveWindow(event):
            if self.returnStatus() == 1:
                self.maximize_restore()
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.titlebar.mouseMoveEvent = moveWindow
        self.show()

    def toggle(self):
        if self.ui.leftMenuFrame.maximumWidth() <= 60:
            # self.anim.setStartValue(self.ui.leftMenuFrame.width())
            self.anim.setEndValue(170)
        else:
            # self.anim.setStartValue(170)
            self.anim.setEndValue(60)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        self.anim.setDuration(300)
        self.anim.start()

    def weather(self):
        self.ui.player_frame.setStyleSheet("")
        self.ui.setting_frame.setStyleSheet("")
        self.ui.weather_frame.setStyleSheet("background-color: rgb(39, 44, 53);\n"
                                            "border:none;\n"
                                            "border-left:3px solid rgb(0, 85, 255);")
        self.ui.stackedWidget.setCurrentIndex(1)

    def settings(self):
        self.ui.player_frame.setStyleSheet("")
        self.ui.weather_frame.setStyleSheet("")
        self.ui.setting_frame.setStyleSheet("background-color: rgb(39, 44, 53);\n"
                                            "border:none;\n"
                                            "border-left:3px solid rgb(0, 85, 255);")
        self.ui.stackedWidget.setCurrentIndex(2)

    def player(self):
        self.ui.weather_frame.setStyleSheet("")
        self.ui.setting_frame.setStyleSheet("")
        self.ui.player_frame.setStyleSheet("background-color: rgb(39, 44, 53);\n"
                                           "border:none;\n"
                                           "border-left:3px solid rgb(0, 85, 255);")
        # self.ui.stackedWidget.setCurrentIndex(0)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def maximize_restore(self):
        status = self.GLOBAL_STATE
        if status == 0:
            # self.showMaximized()
            self.GLOBAL_STATE = 1
            self.geo = self.geometry()
            self.animate(QRect(0, 0, 1366, 728))
            self.ui.resize.setToolTip("Restore")
        else:
            self.GLOBAL_STATE = 0
            self.showNormal()
            self.animate(self.geo)
            self.ui.resize.setToolTip("Maximize")

    def returnStatus(self):
        return self.GLOBAL_STATE

    def play(self):
        self.media.setMedia(QMediaContent(self.file + self.ui.listWidget.currentItem().text()))
        self.ui.status.setText(self.ui.listWidget.currentItem().text())
        self.media.play()

    def stop(self):
        self.media.stop()

    def setvol(self):
        self.media.setVolume(self.ui.volume.value())

    def seekpten(self):
        self.media.setPosition(self.media.position()+10000)

    def seekmten(self):
        self.media.setPosition(self.media.position()-10000)

    def animate(self, geometry):
        self.geo.anim = QPropertyAnimation(self, QByteArray(b"geometry"))
        self.geo.anim.setDuration(200)
        self.geo.anim.setEndValue(geometry)  # QRect(0,0,1366,728))
        self.geo.anim.setEasingCurve(QEasingCurve.Linear)
        self.geo.anim.start()

    def save(self):
        self.diag = QMessageBox(self)
        self.diag.setIcon(self.diag.Icon.Information)
        self.diag.setText("<h3>Reload Required!</h3>")
        self.diag.addButton(self.diag.StandardButton.Ok)
        self.diag.setWindowTitle("Alert")
        self.diag.show()
        self.diag.button(self.diag.StandardButton.Ok).clicked.connect(self.reload)

    def reload(self):
        fh = open("config.py", "w")
        if self.ui.dark.isChecked():
            fh.write(f"load_theme = \"{'dark'}\"\nload_path = \"{self.ui.dir.text()}\"")
        else:
            fh.write(f"load_theme = \"{'light'}\"\nload_path = \"{self.ui.dir.text()}\"")
        self.destroy(True, True)
        fh.close()
        rerun.rerun()
        sys.exit()

    def browse(self):
        self.fdg = QFileDialog.getExistingDirectory(self, "Select Folder", load_path)
        self.ui.dir.setText(self.fdg + "/")

    def getWeather(self):
        api = "gw0brHCdajgtm1Y7pbodIwzaRSziExm1"
        url = f"https://dataservice.accuweather.com/currentconditions/v1/204843?apikey={api}&q&details=true"
        data = json.loads(requests.get(url).content)[0]
        print("Temperature:", data["Temperature"]["Metric"]["Value"])
        print("WeatherText:", data["WeatherText"])
        print("Visiblity:", data["Visibility"]["Metric"]["Value"])
        print("Dew Point:",data["DewPoint"]["Metric"]["Value"])
        print("Pressure:",data["Pressure"]["Metric"]["Value"])
        print("Wind:",data["Wind"]["Speed"]["Metric"]["Value"],"Km/h ",data["Wind"]["Direction"]["English"])
        print("Humidity:",data["RelativeHumidity"])
        print("UV Index:",data["UVIndex"],data["UVIndexText"])
        self.ui.uvnum.setText(str(data["UVIndex"]))
        self.ui.uvtxt.setText(data["UVIndexText"])
        self.ui.stackedWidget.setCurrentIndex(1)
        progress = int(data["UVIndex"]*10)
        uvidx = (100-progress)/100
        self.ui.uv_progress.setStyleSheet(f"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{uvidx} rgba(226, 226, 226,50), stop:{uvidx+0.001} rgba(119, 255, 221, 255));border-radius:50px;")
        self.ui.baro.setText("Pressure: "+str(data["Pressure"]["Metric"]["Value"]))
        self.ui.dew.setText("Dew Point: "+str(data["DewPoint"]["Metric"]["Value"]))
        self.ui.wind.setText("Wind :"+str(str(data["Wind"]["Speed"]["Metric"]["Value"])+"Km/h "))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    win = activate()
    sys.exit(app.exec_())
