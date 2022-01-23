import sys

from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QApplication, \
    QListWidget, QSpacerItem, QSizePolicy
from ui_macro import *


class TodoQListWidgetItem(QListWidgetItem):
    def __init__(self, content, num):
        super().__init__()
        self.widget = QWidget()
        # decoration
        self.label_arrow = QLabel()
        self.label_arrow.setText("")
        self.label_arrow.setPixmap(QtGui.QPixmap("../res/arrow.png").scaled(24, 24))

        # display planning content
        self.label_content = QLabel()
        self.label_content.setText(content)
        # display planning num.scaled(16,16
        self.lineEdit_num = QLineEdit()
        # self.lineEdit_num.setAlignment(QtCore.Qt.AlignCenter)
        str_num = num.split(".")[0]
        width = self.lineEdit_num.fontMetrics().width(str_num)
        self.lineEdit_num.setMaximumWidth(width*3)
        self.lineEdit_num.setText(str_num)
        # button
        self.pushButton_done = QPushButton()
        self.pushButton_done.setText("")
        icon_done = QtGui.QIcon()
        icon_done.addPixmap(QtGui.QPixmap("../res/done.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_done.setIcon(icon_done)
        self.pushButton_delete = QPushButton()
        self.pushButton_delete.setText("")
        icon_delete = QtGui.QIcon()
        icon_delete.addPixmap(QtGui.QPixmap("../res/delete.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon_delete)

        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.label_arrow)
        self.hbox.addWidget(self.label_content)
        self.hbox.addWidget(self.lineEdit_num)
        self.hbox.addStretch(1)
        self.hbox.addWidget(self.pushButton_done)
        self.hbox.addWidget(self.pushButton_delete)
        # 设置widget的布局
        self.widget.setLayout(self.hbox)
        # self.widget.setSizePolicy(QSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding))
        # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        self.setSizeHint(self.widget.sizeHint())

        # --- custom theme ---
        # since I haven't find a way to change custom QListWidgetIem style in styleshee
        widget_qss = """
                        margin-left: 14px; margin-right: 14px; margin-top: 7px; margin-bottom: 7px;
                        background-color: white; 
                        border-radius: 10px;
                    """
        self.widget.setStyleSheet(widget_qss)
        button_qss = """
                        margin: 4px;
                        padding: 8px;
                    """
        self.pushButton_delete.setStyleSheet(button_qss)
        self.pushButton_done.setStyleSheet(button_qss)
        label_qss = """
                        font-size: 30px;
                        font: bold;
                    """
        self.label_content.setStyleSheet(label_qss)
        lineEdit_qss = """
                        margin: 0px;
                        border-radius: 0px;
                    """
        self.lineEdit_num.setStyleSheet(lineEdit_qss)
