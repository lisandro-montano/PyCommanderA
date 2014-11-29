import sys

from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView
from icons_view import IconsView
from details_view import DetailsView
from panel_toolbar import PanelToolbar

from PyQt4.QtGui import QItemDelegate, QPen, QStyle, QBrush
from PyQt4.QtCore import SIGNAL, QEvent, Qt

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

	def file_data(self, index, data):
		index_item = self.panel.panel_model.index(index.row(),0,index.parent())

		if (data == "Name"):
			self.panel.panel_model.filePath(index_item)

		elif data == "Path":
			self.panel.panel_model.fileName(index_item)

		elif data == "Info":
			self.panel.panel_model.fileInfo(index_item)

		elif data == "Type":
			self.panel.panel_model.fileInfo(index_item)

	def isFileFolder(self, index):
		"""Returns 1 if file and returns 0 if folder"""
		file_type = self.file_data(index, "Type")
		if sub_string(str(file_type)).find('Folder') >= 0:
			return 0
		elif sub_string(str(file_type)).find("File") > 0:
			return 1

	def propagate_dir(self, new_dir):
		"""Detect changes in directory and propagate them to proper instances"""
		self.current_path = new_dir
		self.panel_toolbar.update_path(self.current_path)
		self.panel.update_path(self.current_path)

def sub_string(string):
	return string[-6:]
