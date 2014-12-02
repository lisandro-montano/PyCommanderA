import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from views.view_styles.list_view import ListView
from views.view_styles.icons_view import IconsView
from views.view_styles.detailed_view import DetailedView
from views.menus_toolbars.panel_toolbar import PanelToolbar

from PyQt4.QtGui import QItemDelegate, QPen, QStyle, QBrush

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the current path and creates the panels with current path as initial path
		Default View = List View
		"""
		super(PanelView, self).__init__()
		self.current_path = QtCore.QDir.rootPath()
		self.LIST_VIEW = 1
		self.ICONS_VIEW = 2
		self.DETAILED_VIEW = 3

		self.set_list_type(self.LIST_VIEW)
		
		self.panel_toolbar = PanelToolbar(self.current_path)
		self.panel_layout = QtGui.QVBoxLayout()
		self.panel_layout.addWidget(self.panel_toolbar)
		self.panel_layout.addWidget(self.panel)
		self.setLayout(self.panel_layout)

		self.panel_toolbar.attach(self)

	def set_list_type(self, type):
		"""Defines the view type
		- List view
		- Icon view
		- Detailed view
		"""
		if type == self.LIST_VIEW:
			self.panel = ListView(self.current_path)
		elif type == self.ICONS_VIEW:
			self.panel = IconsView(self.current_path)
		elif type == self.DETAILED_VIEW:
			self.panel = DetailsView(self.current_path)
		return self.panel

	def propagate_dir(self, new_dir):
		"""Detect changes in directory/path and propagate them to proper instances
		- Updates current_path
		- Updates toolbar for proper panel
		- Updates panel view
		"""
		self.current_path = new_dir
		self.panel_toolbar.update_path(self.current_path)
		self.panel.update_path(self.current_path)
