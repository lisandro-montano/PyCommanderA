

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
		self._observers = []
		
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
		self.buttons_listener()

	def create_buttons(self):
		"""Create buttons required for actions bar
		Apply no focus to ensure tab only works with panels
		"""
		self.view_button = QtGui.QPushButton("F3 - View")
		self.view_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.rename_button = QtGui.QPushButton("F4 - Rename")
		self.rename_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.copy_button = QtGui.QPushButton("F5 - Copy")
		self.copy_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.move_button = QtGui.QPushButton("F6 - Move")
		self.move_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.new_file_button = QtGui.QPushButton("F7 - New File")
		self.new_file_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.delete_button = QtGui.QPushButton("F8 - Delete")
		self.delete_button.setFocusPolicy(QtCore.Qt.NoFocus)
		self.exit_button = QtGui.QPushButton("Alt + F4 - Exit")
		self.exit_button.setFocusPolicy(QtCore.Qt.NoFocus)

	def buttons_listener(self):
		self.connect(self.copy_button, QtCore.SIGNAL('clicked()'), self.propagate_action)

	def attach(self, observer):
		"""Attach observers to detect action triggers"""
		if not observer in self._observers:
			self._observers.append(observer)

	def propagate_action(self, pressed_button):
		"""Inform observers about actions that were triggered

		Params:
		- item_action: defines the action that will be triggered e.g. "Move", "Copy" or "Delete"
		"""
		for panel_observer in self._observers:
			panel_observer.propagate_action(pressed_button)
		print pressed_button
