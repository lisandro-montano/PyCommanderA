
from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelView(QtGui.QListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(PanelView, self).__init__()
		currentPath = QtCore.QDir.homePath()
		panel_model = QtGui.QFileSystemModel()
		panel_model.setRootPath(currentPath)
		self.setModel(panel_model)
		self.setRootIndex(panel_model.index(currentPath))
		self.setMinimumSize(600, 450)