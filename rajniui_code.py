#Note: Add def Task_Gui(): before while True:
from rajniui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import Rajni
import sys

class MainThread(QThread):

    def __init__(self):
        super(MainThread,self).__init__()
    
    def run(self):
        Rajni.Task_Gui()

startexe=MainThread()

class Gui_start(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui=Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.start.clicked.connect(self.startTask)
        self.gui.exit.clicked.connect(self.close)

    def startTask(self):
        self.gui.label1=QtGui.QMovie("..//MidiProjectGIFS//walk-loop.gif")
        self.gui.gif_1.setMovie(self.gui.label1)
        self.gui.label1.start()

        self.gui.label2=QtGui.QMovie("..//MidiProjectGIFS//5ac3659684140aa60ceca491b48b8bb2.gif")
        self.gui.gif_2.setMovie(self.gui.label2)
        self.gui.label2.start()

        self.gui.label3=QtGui.QMovie("..//MidiProjectGIFS//Intercept_Echo_v2-3.5MB-2-1542062294.gif")
        self.gui.gif_3.setMovie(self.gui.label3)
        self.gui.label3.start()

        self.gui.label4=QtGui.QMovie("..//MidiProjectGIFS//result (1).gif")
        self.gui.gif_4.setMovie(self.gui.label4)
        self.gui.label4.start()

        startexe.start()

        timer=QTimer(self)
        timer.timeout.connect(self.showTimeLive)
        timer.start(999)
        startexe.start()

    def showTimeLive(self):
        times=QTime.currentTime()
        time=times.toString()

        dates=QDate.currentDate()
        date=dates.toString()

        labeltime="Time: "+time
        labeldate="Date: "+date
        self.gui.text_time.setStyleSheet("background-color:#3A3B3C; color:Black; font: 20pt 'MS Shell Dlg 2';")
        self.gui.text_day.setStyleSheet("background-color:#3A3B3C; color:Black; font: 20pt 'MS Shell Dlg 2';")
        
        self.gui.text_time.setText(labeltime)
        self.gui.text_time.setAlignment(QtCore.Qt.AlignCenter)
        self.gui.text_day.setText(labeldate)
        self.gui.text_day.setAlignment(QtCore.Qt.AlignCenter)

    def close(self):
        exit(GuiApp.exec())
GuiApp=QApplication(sys.argv)
rajni_gui=Gui_start()
rajni_gui.show()
exit(GuiApp.exec_())