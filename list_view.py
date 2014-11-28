import os

from PyQt4 import QtGui
from PyQt4 import QtCore

from PyQt4.QtGui import QAbstractItemView, QListView
from PyQt4.QtCore import QEvent,Qt, SIGNAL


class ListView(QtGui.QListView):

	def __init__(self, current_path):
		"""Sets the current path items view as list"""
		super(ListView, self).__init__()
		self._observer = 0
		self.panel_model = QtGui.QFileSystemModel()
		self.panel_model.setRootPath(current_path)
		self.setModel(self.panel_model)
		self.setRootIndex(self.panel_model.index(current_path))
		self.setSelectionMode(QAbstractItemView.MultiSelection)

	def update_path(self, new_path):
		"""Updating the QListView path"""
		self.setRootIndex(self.panel_model.index(new_path))

	def mousePressEvent(self, event):
		"""Redefining the QListView mousePressEvent"""
		self._mouse_button = event.button()
		super(ListView, self).mousePressEvent(event)
