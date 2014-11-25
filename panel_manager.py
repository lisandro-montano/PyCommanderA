
from PyQt4 import QtGui
from PyQt4 import QtCore

from panel_view import PanelView

class PanelManager(QtGui.QSplitter):

	def __init__(self):
		"""Initialize the ListView panels for PyCommanderA"""
		super(PanelManager, self).__init__()
		left_panel = PanelView()
		right_panel = PanelView()

		self.addWidget(left_panel)
		self.addWidget(right_panel)
