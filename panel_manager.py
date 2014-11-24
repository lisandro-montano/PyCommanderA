
from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelManager(QtGui.QTreeView):
	def __init__(self):
		super(PanelManager, self).__init__()
		model = QtGui.QFileSystemModel()
		model.setRootPath(QtCore.QDir.homePath())
		self.setModel(model)