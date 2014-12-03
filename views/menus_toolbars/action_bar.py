

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
		"""Create buttons required for actions bar
		Apply click focus to ensure tab only works with panels
		"""
		self.view_button = QtGui.QPushButton("F3 - View")
		self.view_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.rename_button = QtGui.QPushButton("F4 - Rename")
		self.rename_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.copy_button = QtGui.QPushButton("F5 - Copy")
		self.copy_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.move_button = QtGui.QPushButton("F6 - Move")
		self.move_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.new_file_button = QtGui.QPushButton("F7 - New File")
		self.new_file_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.delete_button = QtGui.QPushButton("F8 - Delete")
		self.delete_button.setFocusPolicy(QtCore.Qt.ClickFocus)
		self.exit_button = QtGui.QPushButton("Alt + F4 - Exit")
		self.exit_button.setFocusPolicy(QtCore.Qt.ClickFocus)
