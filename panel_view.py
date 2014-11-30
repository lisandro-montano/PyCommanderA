import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView
from icons_view import IconsView
from details_view import DetailsView
from panel_toolbar import PanelToolbar

from PyQt4.QtGui import QItemDelegate, QPen, QStyle, QBrush

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the current path and defines the panels"""
		super(PanelView, self).__init__()
		self.current_path = QtCore.QDir.rootPath()
		self.type_list = 1

		self.set_list_type(self.type_list)
		
		self.panel_toolbar = PanelToolbar(self.current_path)
		self.panel_layout = QtGui.QVBoxLayout()
		self.panel_layout.addWidget(self.panel_toolbar)
		self.panel_layout.addWidget(self.panel)
		self.setLayout(self.panel_layout)

		self.panel_toolbar.attach(self)

	def set_list_type(self, type):
		"""Changes the list type view"""
		if type == 1:
			self.panel = ListView(self.current_path)
		elif type == 2:
			self.panel = IconsView(self.current_path)
		elif type == 3:
			self.panel = DetailsView(self.current_path)
		return self.panel

	def propagate_dir(self, new_dir):
		"""Detect changes in directory and propagate them to proper instances"""
		self.current_path = new_dir
		self.panel_toolbar.update_path(self.current_path)
		self.panel.update_path(self.current_path)

