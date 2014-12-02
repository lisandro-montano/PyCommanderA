

from PyQt4 import QtGui
from PyQt4 import QtCore

class ActionBar(QtGui.QDockWidget):

	def __init__(self):
		"""Initialize action bar and proper buttons
		Set all buttons in the action bar and
		display layout properly
		"""
		super(ActionBar, self).__init__()
		self.create_buttons()
		
		self.buttons_bar = QtGui.QWidget()
		self.buttons_layout = QtGui.QHBoxLayout()

		self.buttons_layout.addWidget(self.view_button)
		self.buttons_layout.addWidget(self.rename_button)
		self.buttons_layout.addWidget(self.copy_button)
		self.buttons_layout.addWidget(self.move_button)
		self.buttons_layout.addWidget(self.new_file_button)
		self.buttons_layout.addWidget(self.delete_button)
		self.buttons_layout.addWidget(self.exit_button)
		self.buttons_bar.setLayout(self.buttons_layout)
		self.setWidget(self.buttons_bar)
		self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

	def create_buttons(self):
		"""Create buttons required for actions bar"""
		self.view_button = QtGui.QPushButton("F3 - View")
		self.rename_button = QtGui.QPushButton("F4 - Rename")
		self.copy_button = QtGui.QPushButton("F5 - Copy")
		self.move_button = QtGui.QPushButton("F6 - Move")
		self.new_file_button = QtGui.QPushButton("F7 - New File")
		self.delete_button = QtGui.QPushButton("F8 - Delete")
		self.exit_button = QtGui.QPushButton("Alt + F4 - Exit")
