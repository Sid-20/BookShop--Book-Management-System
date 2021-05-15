# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BookShop.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MyBook=sqlite3.connect('Book_Store.db')
        curBook=MyBook.cursor()
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l1.setFont(font)
        self.l1.setAlignment(QtCore.Qt.AlignCenter)
        self.l1.setObjectName("l1")
        self.horizontalLayout_2.addWidget(self.l1)
        self.edit1 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit1.setObjectName("edit1")
        self.horizontalLayout_2.addWidget(self.edit1)
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.btn1.clicked.connect(self.findprice)
        
        self.horizontalLayout_2.addWidget(self.btn1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.l2 = QtWidgets.QLabel(self.centralwidget)
        self.l2.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l2.setFont(font)
        self.l2.setAlignment(QtCore.Qt.AlignCenter)
        self.l2.setObjectName("l2")
        self.horizontalLayout_3.addWidget(self.l2)
        spacerItem = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.edit2 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.edit2.setAlignment(QtCore.Qt.AlignCenter)
        self.edit2.setObjectName("edit2")
        self.horizontalLayout_3.addWidget(self.edit2)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.l3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l3.setFont(font)
        self.l3.setAlignment(QtCore.Qt.AlignCenter)
        self.l3.setObjectName("l3")
        self.horizontalLayout_4.addWidget(self.l3)
        self.edit3 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit3.setObjectName("edit3")
        self.horizontalLayout_4.addWidget(self.edit3)
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.btn2.clicked.connect(self.findTotal)
        self.horizontalLayout_4.addWidget(self.btn2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.l4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.l4.setFont(font)
        self.l4.setAlignment(QtCore.Qt.AlignCenter)
        self.l4.setObjectName("l4")
        self.horizontalLayout_5.addWidget(self.l4)
        self.edit4 = QtWidgets.QLineEdit(self.centralwidget)
        self.edit4.setAlignment(QtCore.Qt.AlignCenter)
        self.edit4.setObjectName("edit4")
        self.horizontalLayout_5.addWidget(self.edit4)
        spacerItem1 = QtWidgets.QSpacerItem(400, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 611, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l1.setText(_translate("MainWindow", "BOOK TITLE:"))
        self.btn1.setText(_translate("MainWindow", "FIND PRICE"))
        self.l2.setText(_translate("MainWindow", "PRICE:"))
        self.l3.setText(_translate("MainWindow", " QUANTITY: "))
        self.btn2.setText(_translate("MainWindow", "FIND TOTAL"))
        self.l4.setText(_translate("MainWindow", " TOTAL:    "))

    def findprice(self):
        MyBook=sqlite3.connect('Book_Store.db')
        curBook=MyBook.cursor()
        txt=self.edit1.text()
        
        SQL1="SELECT Price FROM Books WHERE Title='"+txt+"'"
        curBook.execute(SQL1)
        self.pr=curBook.fetchone()
        if self.pr!=None:
            self.edit2.setText(str(self.pr))
        else:
            print("Title Not found")

    def findTotal(self):
        self.qty=float(self.edit3.text())
        txt2=self.pr*self.qty
        self.edit4.setText(str(txt2))
        

    
        
        
        
        
  


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())