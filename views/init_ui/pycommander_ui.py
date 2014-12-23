from PyQt4 import QtGui
from PyQt4 import QtCore
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

		#Defining the menu options
		closeAction = QtGui.QAction('Close', self)
		closeAction.setShortcut('Ctrl+Q')
		closeAction.setStatusTip('Close Bar')
		closeAction.triggered.connect(self.close)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(closeAction)

		check_box = QtGui.QAction('Preferences', self)
		check_box.setShortcut('Ctrl+S')
		check_box.setStatusTip('Open preferences')
		check_box.triggered.connect(self.show_checkbox)

		settingsMenu = menubar.addMenu('&Settings')
		settingsMenu.addAction(check_box)

		#Defining the panel manager
		self.panels = PanelManager()

		#Defining the action bar
		self.action_bar = ActionBar()
		self.action_bar.attach(self)

		self.setCentralWidget(self.panels)
		self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.action_bar)

		self.show()

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
		self.panels.right_panel.set_user_preferences()
