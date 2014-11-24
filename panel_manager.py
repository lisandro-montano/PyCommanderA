
from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelManager(QtGui.QListView):
	def __init__(self):
		super(PanelManager, self).__init__()
		panel_model = QtGui.QFileSystemModel()
		panel_model.setRootPath(QtCore.QDir.currentPath())
		self.setModel(panel_model)
		self.setRootIndex(panel_model.index(QtCore.QDir.homePath()))