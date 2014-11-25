
from PyQt4 import QtGui
from PyQt4 import QtCore


class ListView(QtGui.QListView):

	def __init__(self, currentPath):
		"""Sets the currentPath items view as list"""
		super(ListView, self).__init__()
		panel_model = QtGui.QFileSystemModel()
		panel_model.setRootPath(currentPath)
		self.setModel(panel_model)
		self.setRootIndex(panel_model.index(currentPath))

	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def on_treeView_clicked(self, index):
		indexItem = self.model.index(index.row(), 0, index.parent())

		fileName = self.model.fileName(indexItem)
		fileName = self.model.filePath(indexItem)

		#self.selected_items.
		print 'selected item index found at %s with data: %s' % (indexItem.toString(), fileName.toString(), fileName.toString())