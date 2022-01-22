# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\history.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QHeaderView, QMessageBox, QDialog, QGroupBox, QLabel, \
    QPushButton, QVBoxLayout, QHBoxLayout, QLineEdit

from DbOps import DbOps
from utils import get_week_begin, get_week_end
from ui_settings import *


class Ui_history(object):
    def setupUi(self, history):
        history.setObjectName("history")
        history.resize(PAGE_WIDTH, HEIGHT)
        self.verticalLayout = QtWidgets.QVBoxLayout(history)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(history)
        # self.tabWidget.setGeometry(QtCore.QRect(PAGE_MARGIN, 0, PAGE_WIDTH-2*PAGE_MARGIN, HEIGHT))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_all = QtWidgets.QWidget()
        self.tab_all.setObjectName("tab_all")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_all)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget_all = QtWidgets.QTableWidget(self.tab_all)
        self.tableWidget_all.setObjectName("tableWidget_all")
        self.tableWidget_all.setColumnCount(0)
        self.tableWidget_all.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget_all, 0, 0, 1, 6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 4, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.pushButton_Aupdate = QtWidgets.QPushButton(self.tab_all)
        self.pushButton_Aupdate.setObjectName("pushButton_Aupdate")
        self.gridLayout.addWidget(self.pushButton_Aupdate, 1, 2, 1, 1)
        self.pushButton_Adelete = QtWidgets.QPushButton(self.tab_all)
        self.pushButton_Adelete.setObjectName("pushButton_Adelete")
        self.gridLayout.addWidget(self.pushButton_Adelete, 1, 3, 1, 1)
        self.tabWidget.addTab(self.tab_all, "")
        self.tab_week = QtWidgets.QWidget()
        self.tab_week.setObjectName("tab_week")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_week)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tableWidget_week = QtWidgets.QTableWidget(self.tab_week)
        self.tableWidget_week.setObjectName("tableWidget_week")
        self.tableWidget_week.setColumnCount(0)
        self.tableWidget_week.setRowCount(0)
        self.gridLayout_2.addWidget(self.tableWidget_week, 1, 0, 1, 4)
        self.pushButton_Wupdate = QtWidgets.QPushButton(self.tab_week)
        self.pushButton_Wupdate.setObjectName("pushButton_Wupdate")
        self.gridLayout_2.addWidget(self.pushButton_Wupdate, 2, 1, 1, 1)
        self.pushButton_Wdelete = QtWidgets.QPushButton(self.tab_week)
        self.pushButton_Wdelete.setObjectName("pushButton_Wdelete")
        self.gridLayout_2.addWidget(self.pushButton_Wdelete, 2, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 2, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_week)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.tab_week)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout_2.addWidget(self.dateEdit, 0, 2, 1, 1)
        self.tabWidget.addTab(self.tab_week, "")
        self.tab_search = QtWidgets.QWidget()
        self.tab_search.setObjectName("tab_search")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_search)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_search = QtWidgets.QPushButton(self.tab_search)
        self.pushButton_search.setObjectName("pushButton_search")
        self.gridLayout_3.addWidget(self.pushButton_search, 0, 3, 1, 1)
        self.tableWidget_search = QtWidgets.QTableWidget(self.tab_search)
        self.tableWidget_search.setObjectName("tableWidget_search")
        self.tableWidget_search.setColumnCount(0)
        self.tableWidget_search.setRowCount(0)
        self.gridLayout_3.addWidget(self.tableWidget_search, 1, 0, 1, 4)
        self.pushButton_Supdate = QtWidgets.QPushButton(self.tab_search)
        self.pushButton_Supdate.setObjectName("pushButton_Supdate")
        self.gridLayout_3.addWidget(self.pushButton_Supdate, 2, 1, 1, 1)
        self.comboBox_action = QtWidgets.QComboBox(self.tab_search)
        self.comboBox_action.setObjectName("comboBox_action")
        self.gridLayout_3.addWidget(self.comboBox_action, 0, 1, 1, 1)
        self.comboBox_level = QtWidgets.QComboBox(self.tab_search)
        self.comboBox_level.setObjectName("comboBox_level")
        self.gridLayout_3.addWidget(self.comboBox_level, 0, 2, 1, 1)
        self.pushButton_Sdelete = QtWidgets.QPushButton(self.tab_search)
        self.pushButton_Sdelete.setObjectName("pushButton_Sdelete")
        self.gridLayout_3.addWidget(self.pushButton_Sdelete, 2, 2, 1, 1)
        self.comboBox_part = QtWidgets.QComboBox(self.tab_search)
        self.comboBox_part.setCurrentText("")
        self.comboBox_part.setObjectName("comboBox_part")
        self.gridLayout_3.addWidget(self.comboBox_part, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_search, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(history)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(history)

        self.init_all()

    def retranslateUi(self, history):
        _translate = QtCore.QCoreApplication.translate
        history.setWindowTitle(_translate("history", "Form"))
        self.pushButton_Aupdate.setText(_translate("history", "update"))
        self.pushButton_Adelete.setText(_translate("history", "delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_all), _translate("history", "All"))
        self.pushButton_Wupdate.setText(_translate("history", "update"))
        self.pushButton_Wdelete.setText(_translate("history", "delete"))
        self.label.setText(_translate("history", "select week:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_week), _translate("history", "Week"))
        self.pushButton_search.setText(_translate("history", "Search"))
        self.pushButton_Supdate.setText(_translate("history", "update"))
        self.pushButton_Sdelete.setText(_translate("history", "delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_search), _translate("history", "Search"))

    def init_all(self):
        # initialize UI and build up connection

        # --- init UI ---
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDisplayFormat("yyyy-MM-dd")
        self.dateEdit.setDate(QDate.currentDate())
        self.pushButton_search.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search.setIcon(icon)
        part_box = [part[0] for part in DbOps.fetch_parts()]
        part_box.insert(0,'')
        self.comboBox_part.addItems(part_box)
        self.refresh_name_combobox('')

        # --- init table ---
        self.init_table()

        # --- connection ---
        self.pushButton_Adelete.clicked.connect(lambda: self.delete_record_table("all"))
        self.pushButton_Wdelete.clicked.connect(lambda: self.delete_record_table("week"))
        self.pushButton_Sdelete.clicked.connect(lambda : self.delete_record_table("search"))
        self.pushButton_Aupdate.clicked.connect(lambda: self.update_record_table("all"))
        self.pushButton_Wupdate.clicked.connect(lambda: self.update_record_table("week"))
        self.pushButton_Supdate.clicked.connect(lambda : self.update_record_table("search"))
        self.dateEdit.dateChanged.connect(self.flush_week_table)
        self.tabWidget.tabBarClicked['int'].connect(self.refresh_by_tab_click)
        # search page
        self.comboBox_part.activated[str].connect(self.refresh_name_combobox)
        self.comboBox_part.activated.connect(self.comboBox_level.clear)
        self.comboBox_action.currentTextChanged[str].connect(self.refresh_level_combobox)
        self.pushButton_search.clicked.connect(self.flush_search_table)


    def init_table(self):
        tableWidgets = [self.tableWidget_all, self.tableWidget_week, self.tableWidget_search]
        for tableWidget in tableWidgets:
            tableWidget.setColumnCount(5)
            # 水平和垂直方向设置为正好填满表格
            tableWidget.horizontalHeader().setStretchLastSection(True)
            tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            # 设置表格的表头，并设置为不可编辑
            header_labels = ['id', '动作', '难度', '数目', '日期']
            tableWidget.setHorizontalHeaderLabels(header_labels)
            tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            # 隐藏id列，不显示数据的id也就是主键，这里的主键只用来删除和修改数据时使用
            tableWidget.setColumnHidden(0, True)
            # 不显示单元格
            tableWidget.setShowGrid(False)
            # 设置表格选择行为为 只能一行一行选择
            tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # 初始化表格数据
        self.flush_table()
        self.flush_week_table()

    def refresh_by_tab_click(self, idx):
        if idx == 0:
            self.flush_table()
        elif idx == 1:
            self.flush_week_table()
        elif idx == 2:
            self.flush_search_table()

    def refresh_name_combobox(self, part):
        self.comboBox_action.clear()
        name_box = [name[0] for name in DbOps.fetch_names(part)]
        self.comboBox_action.addItems(name_box)

    def refresh_level_combobox(self, name):
        self.comboBox_level.clear()
        level_box = ['']
        if len(name)>0:
            for level in DbOps.fetch_levels(name):
                level_box.append(level[0])
        self.comboBox_level.addItems(level_box)

    def flush_table(self):
        data = DbOps.fetch_records()
        # 设置表格的行数，和数据的数量相关
        self.tableWidget_all.setRowCount(len(data))

        # 设置表格的数据
        for idx, item in enumerate(data):
            for i, word in enumerate(item):
                self.tableWidget_all.setItem(idx, i, QTableWidgetItem(str(word)))

    def flush_week_table(self):
        cur_date = self.dateEdit.date().toString(Qt.ISODate)
        begin_date, end_date = get_week_begin(cur_date), get_week_end(cur_date)
        print(cur_date, begin_date, end_date)
        data = DbOps.fetch_week_records(begin_date, end_date)
        # 设置表格的行数，和数据的数量相关
        self.tableWidget_week.setRowCount(len(data))

        # 设置表格的数据
        for idx, item in enumerate(data):
            for i, word in enumerate(item):
                self.tableWidget_week.setItem(idx, i, QTableWidgetItem(str(word)))

    def flush_search_table(self):
        if len(str(self.comboBox_action.currentText()))>0:
            if len(str(self.comboBox_level.currentText()))>0:
                data = DbOps.fetch_records_by_action(str(self.comboBox_action.currentText()), str(self.comboBox_level.currentText()))
            else:
                data = DbOps.fetch_records_by_action(str(self.comboBox_action.currentText()))

            self.tableWidget_search.setRowCount(len(data))

            # 设置表格的数据
            for idx, item in enumerate(data):
                for i, word in enumerate(item):
                    self.tableWidget_search.setItem(idx, i, QTableWidgetItem(str(word)))

    def update_record_table(self, table_name):
        if table_name == 'all':
            tableWidget = self.tableWidget_all
        elif table_name == 'week':
            tableWidget = self.tableWidget_week
        elif table_name == 'search':
            tableWidget = self.tableWidget_search
        selected_row = tableWidget.selectedItems()
        if len(selected_row) > 0:  # selected a row
            edit_row = tableWidget.row(selected_row[0])
            rid = tableWidget.item(edit_row, 0).text()
            name = tableWidget.item(edit_row, 1).text()
            level = tableWidget.item(edit_row, 2).text()
            num = tableWidget.item(edit_row, 3).text()
            rdate = tableWidget.item(edit_row, 4).text()
            # call dialog
            self.update_dialog(rid, name, level, num, rdate)
        if table_name == 'all':
            self.flush_table()
        elif table_name == 'week':
            self.flush_week_table()
        elif table_name == 'search':
            self.flush_search_table()

    def delete_record_table(self, table_name):
        if table_name == 'all':
            tableWidget = self.tableWidget_all
        elif table_name == 'week':
            tableWidget = self.tableWidget_week
        elif table_name == 'search':
            tableWidget = self.tableWidget_search
        selected_row = tableWidget.selectedItems()
        if len(selected_row) > 0:  # selected a row
            del_row = tableWidget.row(selected_row[0])
            rid = tableWidget.item(del_row, 0).text()
            # pop up confirm dialog
            if self.delete_dialog() == True:
                DbOps.delete_record_by_id(rid)
                if table_name == 'all':
                    self.flush_table()
                elif table_name == 'week':
                    self.flush_week_table()
                elif table_name == 'search':
                    self.flush_search_table()

    def update_dialog(self, rid, name, level, num, rdate):
        dialog = QDialog(self)
        dialog.setWindowTitle('Update')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        # 创建一个group盒子
        group = QGroupBox(dialog)

        # bind id for update-SQL
        self.rid = rid

        # 标签和输入框
        lb1 = QLabel('动作:', group)
        self.ed_name = QLineEdit(group)
        self.ed_name.setText(name)
        lb2 = QLabel('难度:', group)
        self.ed_level = QLineEdit(group)
        self.ed_level.setText(level)
        lb3 = QLabel('数量:', group)
        self.ed_num = QLineEdit(group)
        self.ed_num.setText(num)
        lb4 = QLabel('日期:', group)
        self.ed_date = QLineEdit(group)
        self.ed_date.setText(rdate)

        # 创建确定和取消的按钮
        ok_button = QPushButton('yes', dialog)
        cancel_button = QPushButton('cancel', dialog)

        # 创建一个垂直布局，将标签和按钮控件都添加到垂直布局里
        group_layout = QVBoxLayout()
        group_item = [lb1, self.ed_name, lb2, self.ed_level, lb3, self.ed_num, lb4, self.ed_date]
        for item in group_item:
            group_layout.addWidget(item)

        # 将垂直布局添加到groupbox中
        group.setLayout(group_layout)
        group.setFixedSize(group.sizeHint())

        # 创建一个水平布局，并将两个按钮添加到布局中
        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)

        # 创建一个最外层的dialog垂直布局，将盒子和按钮布局加到这个布局中
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(group)
        dialog_layout.addLayout(button_layout)

        # 设置这个对话框的布局
        dialog.setLayout(dialog_layout)
        dialog.setFixedSize(dialog.sizeHint())

        ok_button.clicked.connect(self.update_record)
        ok_button.clicked.connect(dialog.accept)

        # 默认选中ok按钮
        ok_button.setDefault(True)

        dialog.exec_()
        return False

    def update_record(self):
        # print(self.rid, self.ed_name.text(), self.ed_level.text(), self.ed_num.text(), self.ed_date.text())
        DbOps.update_record(self.rid, self.ed_name.text(), self.ed_level.text(), self.ed_num.text(),
                            self.ed_date.text())

    def delete_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle(u'Delete')
        dialog.setWindowFlags(dialog.windowFlags() & ~Qt.WindowContextHelpButtonHint)
        group = QGroupBox('', dialog)
        lb1 = QLabel(u'确认删除记录吗?')

        ok_button = QPushButton(u'yes', dialog)
        cancel_button = QPushButton(u'cancel', dialog)

        ok_button.clicked.connect(dialog.accept)
        ok_button.setDefault(True)
        cancel_button.clicked.connect(dialog.reject)
        group_layout = QVBoxLayout()
        group_item = [lb1]
        for item in group_item:
            group_layout.addWidget(item)
        group.setLayout(group_layout)
        group.setFixedSize(group.sizeHint())

        button_layout = QHBoxLayout()
        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(group)
        dialog_layout.addLayout(button_layout)
        dialog.setLayout(dialog_layout)
        dialog.setFixedSize(dialog.sizeHint())

        # 当点击ok是，表示确定删除返回True
        if dialog.exec_():
            return True
        # 否则返回False
        return False

    def show_hint(self, message):
        hint_msg = QMessageBox()
        hint_msg.setText(message)
        hint_msg.addButton(QMessageBox.Ok)
        hint_msg.setWindowTitle("提示")
        hint_msg.exec_()
