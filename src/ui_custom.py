import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QApplication, \
    QListWidget


class TodoQListWidgetItem(QListWidgetItem):
    def __init__(self, content, num):
        super().__init__()
        self.widget = QWidget()
        # decoration
        self.label_arrow = QLabel()
        self.label_arrow.setText("")
        self.label_arrow.setPixmap(QtGui.QPixmap("../res/arrow.png").scaled(24,24))

        # display planning content
        self.label_content = QLabel()
        self.label_content.setText(content)
        # display planning num.scaled(16,16
        self.lineEdit_num = QLineEdit()
        self.lineEdit_num.setText(num)
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
        self.hbox.addWidget(self.pushButton_done)
        self.hbox.addWidget(self.pushButton_delete)
        self.hbox.addStretch(1)
        # 设置widget的布局
        self.widget.setLayout(self.hbox)
        # 设置自定义的QListWidgetItem的sizeHint，不然无法显示
        self.setSizeHint(self.widget.sizeHint())


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#
#     # 主窗口
#     w = QWidget()
#     w.setWindowTitle("QListWindow")
#     # 新建QListWidget
#     listWidget = QListWidget(w)
#     listWidget.resize(300, 300)
#
#     # 新建两个自定义的QListWidgetItem(customQListWidgetItem)
#     item1 = TodoQListWidgetItem("引体向上 标准", "100")
#     item2 = TodoQListWidgetItem("俯卧撑 钻石", "24")
#
#     # 在listWidget中加入两个自定义的item
#     listWidget.addItem(item1)
#     listWidget.setItemWidget(item1, item1.widget)
#     listWidget.addItem(item2)
#     # listWidget.setItemWidget(item2, item2.widget)
#
#     # 绑定点击槽函数 点击显示对应item中的name
#     listWidget.itemClicked.connect(lambda item: print(item.nameLabel.text()))
#
#     w.show()
#     sys.exit(app.exec_())