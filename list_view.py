<<<<<<< Updated upstream
import os

=======
>>>>>>> Stashed changes
from PyQt4 import QtGui
from PyQt4 import QtCore


class ListView(QtGui.QListView):

	def __init__(self, current_path):
		"""Sets the current path items view as list"""
		super(ListView, self).__init__()
		self.panel_model = QtGui.QFileSystemModel()
		self.panel_model.setRootPath(current_path)
		self.setModel(self.panel_model)
		self.setRootIndex(self.panel_model.index(current_path))


