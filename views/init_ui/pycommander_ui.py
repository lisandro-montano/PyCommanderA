from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QObjectCleanupHandler
from preferences_checkboxes import PreferencesCheckboxes
from views.panels.panel_manager import PanelManager
from views.menus_toolbars.action_bar import ActionBar

class PyCommanderUIGenerator(QtGui.QMainWindow):

	def __init__(self):
		"""Initializes and creates the UI components for PyCommanderA"""
		super(PyCommanderUIGenerator, self).__init__()
		self.init_ui()
		self.create_components()

	def init_ui(self):
		"""Initializes the UI for PyCommanderA"""
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.setPalette(palette)
		self.resize(1500, 800)
		self.move(100, 100)
		self.setWindowTitle('PyCommanderA')

	def create_components(self):
		"""Draw all required components for PyCommanderA:
		   - Menu
		   - Toolbars
		   - Panels
		   - Action buttons
		"""

		#Defining the Main Menu
		self.create_menu()

		#Defining the panel manager
		self.panels = PanelManager()

		#Defining the action bar
		self.action_bar = ActionBar()
		self.action_bar.attach(self)

		self.setCentralWidget(self.panels)
		self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.action_bar)

		self.show()

	def create_menu(self):
		"""This method creates the required menu options for the Main Window"""

		#Defining the Close option for the menu
		close_action = QtGui.QAction('Close', self)
		close_action.setShortcut('Ctrl+Q')
		close_action.setStatusTip('Close Bar')
		close_action.triggered.connect(self.close)

		#Defining the Main Menu options
		#Adding the Close option to the File menu option
		menu_bar = self.menuBar()
		file_menu = menu_bar.addMenu('&File')
		file_menu.addAction(close_action)

		#Defining the Settings option for the menu
		settings = QtGui.QAction('Preferences', self)
		settings.setShortcut('Ctrl+S')
		settings.setStatusTip('Open preferences')
		settings.triggered.connect(self.show_checkbox)

		#Adding the Settings option to the Preferences menu option
		settings_action = menu_bar.addMenu('&Settings')
		settings_action.addAction(settings)

	def propagate_action(self, pressed_button):
		"""Triggers action related to the pressed button on the focused panel

		Params:
		- pressed_button: Defines the action that will be triggered e.g. "Move", "Copy" or "Delete"
		"""
		self.panels.get_focused_panel(pressed_button)

	def show_checkbox(self):
		checkbox_dialog = PreferencesCheckboxes(parent=self)
		checkbox_dialog.attach(self)

	def set_user_preferences(self):
		self.panels.left_panel.set_user_preferences()
		QObjectCleanupHandler().add(self.panels.right_panel.layout())
		self.panels.right_panel.set_user_preferences()
