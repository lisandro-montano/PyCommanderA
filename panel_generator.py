
from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelGenerator(QtGui.QTreeView):
	def __init__(self):
		super(PanelGenerator, self).__init__()
		model = QtGui.QFileSystemModel()
		model.setRootPath(QtCore.QDir.homePath())
		self.setModel(model)