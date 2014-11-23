
from PyQt4 import QtGui
from PyQt4 import QtCore
from panel_generator import PanelGenerator

class PyCommanderUIGenerator(QtGui.QWidget):

	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.init_ui()
		self.create_components()

	def init_ui(self):
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
		left_panel = PanelGenerator()
		right_panel = PanelGenerator()

		layout_panels = QtGui.QHBoxLayout()
		layout_panels.addWidget(left_panel)
		layout_panels.addWidget(right_panel)
		self.setLayout(layout_panels)
