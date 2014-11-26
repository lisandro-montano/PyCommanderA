

from PyQt4 import QtGui
from PyQt4 import QtCore

class ActionBar(QtGui.QToolBar):

	def __init__(self):
		"""Create action buttons for PyCommanderA"""
		super(ActionBar, self).__init__()

		"""Create separators to distribute toolbar properly"""
		spacer1 = QtGui.QWidget()
		spacer2 = QtGui.QWidget()
		spacer3 = QtGui.QWidget()
		spacer4 = QtGui.QWidget()
		spacer5 = QtGui.QWidget()		
		spacer6 = QtGui.QWidget()
		spacer7 = QtGui.QWidget()
		spacer8 = QtGui.QWidget()
		spacer9 = QtGui.QWidget()
		spacer10 = QtGui.QWidget()
		spacer11 = QtGui.QWidget()
		spacer12 = QtGui.QWidget()
		spacer_left = QtGui.QWidget()
		spacer_right = QtGui.QWidget()
		spacer1.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer2.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer3.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer4.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer5.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer6.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer7.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer8.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer9.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer10.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer11.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer12.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer_left.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		spacer_right.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)


		"""Add toolbar options"""
		self.addWidget(spacer_left)
		self.addAction("F3 - View") 
		self.addWidget(spacer1)
		self.addSeparator()
		self.addWidget(spacer2)
		self.addAction("F4 - Rename")
		self.addWidget(spacer3)
		self.addSeparator()
		self.addWidget(spacer4)
		self.addAction("F5 - Copy")
		self.addWidget(spacer5)
		self.addSeparator()
		self.addWidget(spacer6)
		self.addAction("F6 - Move")
		self.addWidget(spacer7)
		self.addSeparator()
		self.addWidget(spacer8)
		self.addAction("F7 - New File")
		self.addWidget(spacer9)
		self.addSeparator()
		self.addWidget(spacer10)
		self.addAction("F8 - Delete")
		self.addWidget(spacer11)
		self.addSeparator()
		self.addWidget(spacer12)
		self.addAction("Alt + F4 - Exit")
		self.addWidget(spacer_right)
		self.setMovable(0) 
	