from PyQt5.QtWidgets import QWidget

from ui_home import Ui_home
from ui_sidebar import Ui_sidebar
from ui_history import Ui_history
from ui_analysis import Ui_analysis
from ui_settings import Ui_settings

class Home(QWidget, Ui_home):
    def __init__(self):
        super(Home, self).__init__()
        self.setupUi(self)

class Sidebar(QWidget, Ui_sidebar):
    def __init__(self):
        super(Sidebar, self).__init__()
        self.setupUi(self)

class History(QWidget, Ui_history):
    def __init__(self):
        super(History, self).__init__()
        self.setupUi(self)


class Analysis(QWidget, Ui_analysis):
    def __init__(self):
        super(Analysis, self).__init__()
        self.setupUi(self)

class Settings(QWidget, Ui_settings):
    def __init__(self):
        super(Settings, self).__init__()
        self.setupUi(self)