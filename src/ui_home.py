# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\home.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QPoint, QDate, Qt
from PyQt5.QtWidgets import QCompleter, QMessageBox

from DbOps import DbOps
from utils import is_date_valid
from ui_custom import TodoQListWidgetItem
from ui_macro import *

class Ui_home(object):
    def setupUi(self, home):
        home.setObjectName("home")
        home.resize(PAGE_WIDTH, HEIGHT)
        self.verticalLayout = QtWidgets.QVBoxLayout(home)
        # self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.dateEdit = QtWidgets.QDateEdit(home)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout.addWidget(self.dateEdit)

        self.lineEdit_Aname = QtWidgets.QLineEdit(home)
        self.lineEdit_Aname.setObjectName("lineEdit_Aname")
        self.horizontalLayout.addWidget(self.lineEdit_Aname)
        self.lineEdit_Alevel = QtWidgets.QLineEdit(home)
        self.lineEdit_Alevel.setObjectName("lineEdit_Alevel")
        self.horizontalLayout.addWidget(self.lineEdit_Alevel)
        self.lineEdit_num = QtWidgets.QLineEdit(home)
        self.lineEdit_num.setObjectName("lineEdit_num")
        self.horizontalLayout.addWidget(self.lineEdit_num)

        # self.lineEdit_date = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        # self.lineEdit_date.setObjectName("lineEdit_date")
        # self.horizontalLayout.addWidget(self.lineEdit_date)

        self.pushButton_complete = QtWidgets.QPushButton(home)
        self.pushButton_complete.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/completed.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_complete.setIcon(icon)
        self.pushButton_complete.setObjectName("pushButton_complete")
        self.horizontalLayout.addWidget(self.pushButton_complete)
        self.pushButton_todo = QtWidgets.QPushButton(home)
        self.pushButton_todo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../res/todo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_todo.setIcon(icon1)
        self.pushButton_todo.setObjectName("pushButton_todo")
        self.horizontalLayout.addWidget(self.pushButton_todo)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(home)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.sizeHint()
        self.verticalLayout.addWidget(self.listWidget)

        self.retranslateUi(home)
        QtCore.QMetaObject.connectSlotsByName(home)
        self.init_all()

    def retranslateUi(self, home):
        _translate = QtCore.QCoreApplication.translate
        home.setWindowTitle(_translate("home", "Form"))

    def init_all(self):
        # ----- customization ----
        # self.lineEdit_date.setText(str(datetime.date.today()))
        # auto-complete
        sql = "select distinct AName from actions;"
        data = DbOps.execute_sql(sql)
        name_list = [name[0] for name in data]
        name_completer = QCompleter(name_list, self)
        self.lineEdit_Aname.setCompleter(name_completer)
        sql = "select distinct Alevel from actions;"
        data = DbOps.execute_sql(sql)
        level_list = [name[0] for name in data]
        level_completer = QCompleter(level_list, self)
        self.lineEdit_Alevel.setCompleter(level_completer)

        # dateEdit
        self.dateEdit.setCalendarPopup(True)
        self.refresh_date()

        # Load QlistWidgetItem from DB
        for todo_item in DbOps.fetch_todos():
            content = todo_item[0] + " " + todo_item[1]
            item = TodoQListWidgetItem(content, str(todo_item[2]))
            item.pushButton_done.clicked.connect(self.complete_todo_record)
            item.pushButton_delete.clicked.connect(self.delete_todo_record)
            self.listWidget.addItem(item)
            self.listWidget.setItemWidget(item, item.widget)  # Sets the widget to be displayed in the given item

        # signal & connection
        self.pushButton_complete.clicked.connect(self.add_complete_record)
        self.pushButton_todo.clicked.connect(self.add_todo_record)

    def refresh_date(self):
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QDate.currentDate())

    def is_line_all_valid(self):
        flag = True
        if len(self.lineEdit_Aname.text()) == 0 or len(self.lineEdit_Alevel.text()) == 0 \
                or len(self.lineEdit_num.text()) == 0:
            flag = False
        # str_date = self.lineEdit_date.text()
        str_date = self.dateEdit.date().toString(Qt.ISODate)
        if not is_date_valid(str_date):
            flag = False
        return flag

    def add_complete_record(self):
        # create record
        record = []
        if self.is_line_all_valid():
            record.append(self.lineEdit_Aname.text())  # name
            record.append(self.lineEdit_Alevel.text())  # level
            record.append(self.lineEdit_num.text())  # num
            # record.append(self.lineEdit_date.text())
            record.append(self.dateEdit.date().toString(Qt.ISODate))
            # print(record)
            DbOps.insert_record(record)
            # clear text
            self.lineEdit_Aname.clear()
            self.lineEdit_Alevel.clear()
            self.lineEdit_num.clear()
        else:
            print("> incomplete record.")

    def add_todo_record(self):
        if self.is_line_all_valid():
            record = []
            record.append(self.lineEdit_Aname.text())  # name
            record.append(self.lineEdit_Alevel.text())  # level
            record.append(self.lineEdit_num.text())  # num
            print(record)
            if DbOps.insert_todo(record):
                # add item widget
                content = self.lineEdit_Aname.text() + " " + self.lineEdit_Alevel.text()
                item = TodoQListWidgetItem(content, self.lineEdit_num.text())
                # add connection
                item.pushButton_done.clicked.connect(self.complete_todo_record)
                item.pushButton_delete.clicked.connect(self.delete_todo_record)
                self.listWidget.addItem(item)
                self.listWidget.setItemWidget(item, item.widget)  # Sets the widget to be displayed in the given item
                # clear text
                self.lineEdit_Aname.clear()
                self.lineEdit_Alevel.clear()
                self.lineEdit_num.clear()
            else:
                QMessageBox.about(self, "TODO Exists", "已有该项的计划了，别贪心哦~")
        else:
            print("> incomplete record.")

    def complete_todo_record(self):
        # retrieve button
        button = self.sender()
        # calculate the coordinates of button relative to listWidget
        button_position = button.mapToGlobal(QPoint(0, 0)) - self.listWidget.mapToGlobal(QPoint(0, 0))
        # get the custom item widget
        todo_item_idx = self.listWidget.indexAt(button_position)
        # print(todo_item_idx.row())

        # create record
        todo_item = self.listWidget.takeItem(todo_item_idx.row())
        content = todo_item.label_content.text().split()
        record = content.copy()
        record.append(todo_item.lineEdit_num.text())
        record.append(str(datetime.date.today()))
        # print(content,record)
        # insert record
        DbOps.insert_record(record)
        # delete todo_item in db
        DbOps.delete_todo(content)


    def delete_todo_record(self):
        # retrieve button
        button = self.sender()
        # calculate the coordinates of button relative to listWidget
        button_position = button.mapToGlobal(QPoint(0, 0)) - self.listWidget.mapToGlobal(QPoint(0, 0))
        # get the custom item widget
        todo_item_idx = self.listWidget.indexAt(button_position)
        todo_item = self.listWidget.takeItem(todo_item_idx.row())
        content = todo_item.label_content.text().split()
        # delete todo_item in db
        DbOps.delete_todo(content)

    # def relink_item_button(self):
    #     lineEdit = self.sender()
    #     pos = lineEdit.mapToGlobal(QPoint(0, 0)) - self.listWidget.mapToGlobal(QPoint(0, 0))
    #     todo_item_idx = self.listWidget.indexAt(pos)
    #     print(todo_item_idx.row())
    #     todo_item = self.listWidget.itemFromIndex(todo_item_idx)
    #     todo_item.pushButton_done.clicked.connect(self.complete_todo_record)
    #     todo_item.pushButton_delete.clicked.connect(self.delete_todo_record)
