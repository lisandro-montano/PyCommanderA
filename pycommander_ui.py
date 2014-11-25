
from PyQt4 import QtGui
from PyQt4 import QtCore
from panel_manager import PanelManager

class PyCommanderUIGenerator(QtGui.QWidget):

	def __init__(self):
		"""Initializes and creates the UI components for PyCommanderA"""
		QtGui.QWidget.__init__(self)
		self.init_ui()
		self.create_components()

	def init_ui(self):
		"""Initializes the UI for PyCommanderA"""
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.setPalette(palette)
		self.resize(1500, 750)
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

		layout_panels = QtGui.QVBoxLayout()

		"""Adds the ListView panels for PyCommanderA"""
		layout_panels.addWidget(panels)

		"""Displays the QVBoxLayout"""
		self.setLayout(layout_panels)
