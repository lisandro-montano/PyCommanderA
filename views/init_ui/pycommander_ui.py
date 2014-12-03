from PyQt4 import QtGui
from PyQt4 import QtCore
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
		panels = PanelManager()
		action_bar = ActionBar()

		self.setCentralWidget(panels)
		self.addDockWidget(QtCore.Qt.DockWidgetArea(8), action_bar)

		self.show()
