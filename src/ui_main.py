import os
import sys

from PyQt5.QtGui import QIcon, QFontDatabase
from PyQt5.QtWidgets import QMainWindow, QApplication

from DbOps import DbOps
from ui_index import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('../res/main_icon.png'))


if __name__ == '__main__':
    DbOps.init_tables()
    app = QApplication(sys.argv)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    QtGui.QFontDatabase.addApplicationFont("../res/fonts/hanyishangweishoushuW.ttf")
    QtGui.QFontDatabase.addApplicationFont("../res/fonts/fangzhengheitijianti.TTF")
    # print(QtGui.QFontDatabase().families())
    my_window = MyWindow()
    my_window.setStyleSheet(open("../ui/teal_style.css", "r", encoding='utf-8').read())
    my_window.show()
    sys.exit(app.exec_())
