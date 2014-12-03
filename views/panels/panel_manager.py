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
		self.left_panel = PanelView()
		self.left_panel.setAccessibleName("left")
		self.right_panel = PanelView()
		self.right_panel.setAccessibleName("right")

		panel_splitter.addWidget(self.left_panel)
		panel_splitter.addWidget(self.right_panel)

		self.setWidget(panel_splitter)
		self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
		self.setTabOrder(self.left_panel.panel, self.right_panel.panel)

		self.left_panel.panel.setFocus()
