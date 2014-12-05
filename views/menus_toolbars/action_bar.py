
from functools import partial

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
		self.set_shortcuts()

	def set_shortcuts(self):
		self.view_button.setShortcut(QtCore.Qt.Key_F3)
		self.rename_button.setShortcut(QtCore.Qt.Key_F4)
		self.copy_button.setShortcut(QtCore.Qt.Key_F5)
		self.move_button.setShortcut(QtCore.Qt.Key_F6)
		self.new_file_button.setShortcut(QtCore.Qt.Key_F7)
		self.delete_button.setShortcut(QtCore.Qt.Key_F8)
		self.exit_button.setShortcut(QtCore.Qt.Key_Alt + QtCore.Qt.Key_F4)

	def buttons_listener(self):
		"""Trigger proper button actions and propagate it to observers"""
		buttons_list = [(self.view_button, "View"),
						(self.rename_button, "Rename"),
						(self.copy_button, "Copy"),
						(self.move_button, "Move"),
						(self.new_file_button, "New File"),
						(self.delete_button, "Delete"),
						(self.exit_button, "Exit")]

		for button, button_action in buttons_list:
			action_to_call = partial(self.propagate_action, button_action)
			button.clicked.connect(action_to_call)

	def attach(self, observer):
		"""Attach observers to detect action triggers
		
		Params:
		- observer: class that need to knows about action triggers e.g. pycommander_ui
		"""
		if not observer in self._observers:
			self._observers.append(observer)

	def propagate_action(self, pressed_button):
		"""Inform observers about actions that were triggered

		Params:
		- pressed_button: Defines the action that will be triggered e.g. "Move", "Copy" or "Delete"
		"""
		for action_observer in self._observers:
			action_observer.propagate_action(pressed_button)
