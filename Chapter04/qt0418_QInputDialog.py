# -*- coding: utf-8 -*-

'''
    【简介】
	PyQt5中 QInputDialog 例子
   
  
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class InputdialogDemo(QWidget):
	def __init__(self, parent=None):
		super(InputdialogDemo, self).__init__(parent)
		layout = QFormLayout()
		self.btn = QPushButton("获得列表里的选项")
		self.btn.clicked.connect(self.getItem)
		self.le = QLineEdit()
		layout.addRow(self.btn,self.le)
		self.btn1 = QPushButton("获得字符串")
		self.btn1.clicked.connect(self.gettext)
		self.le1 = QLineEdit()
		layout.addRow(self.btn1,self.le1)
		self.btn2 = QPushButton("获得整数")
		self.btn2.clicked.connect(self.getint)
		self.le2 = QLineEdit()
		layout.addRow(self.btn2,self.le2)
		self.setLayout(layout)
		self.setWindowTitle("Input Dialog demo")
		
	def getItem(self):
		items = ("C", "C++", "Java", "Python")
		item, ok = QInputDialog.getItem(self, "select input dialog",
		"语言列表", items, 0, False)
		if ok and item:
			self.le.setText(item)
	
	def gettext(self):	
		text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名:')
		if ok:
			self.le1.setText(str(text)) 

	def getint(self):
		num,ok=QInputDialog.getInt(self,"integer input dualog","输入数字")
		if ok:
			self.le2.setText(str(num))
					
if __name__ == '__main__':
	app = QApplication(sys.argv)
	demo = InputdialogDemo()
	demo.show()
	sys.exit(app.exec_())
