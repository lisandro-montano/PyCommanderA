from PyQt4 import QtGui
from PyQt4 import QtCore

from views.panels.panel_view import PanelView

class PanelManager(QtGui.QDockWidget):

	def __init__(self):
		"""Initialize the panels for PyCommanderA
		Create 2 panels (left_panel and right_panel)
		Set them properly in a splitter
		"""
		super(PanelManager, self).__init__()
		panel_splitter = QtGui.QSplitter()
		left_panel = PanelView()
		left_panel.setAccessibleName("left")
		right_panel = PanelView()
		right_panel.setAccessibleName("right")

		panel_splitter.addWidget(left_panel)
		panel_splitter.addWidget(right_panel)

		self.setWidget(panel_splitter)
		self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
		self.setTabOrder(left_panel.panel, right_panel.panel)
