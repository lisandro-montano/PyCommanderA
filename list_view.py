import os

from PyQt4 import QtGui
from PyQt4 import QtCore


class ListView(QtGui.QListView):

	def __init__(self, currentPath):
		"""Sets the currentPath items view as list"""
		super(ListView, self).__init__()
		self.panel_model = QtGui.QFileSystemModel()
		self.panel_model.setRootPath(currentPath)
		self.setModel(self.panel_model)
		self.setRootIndex(self.panel_model.index(currentPath))

