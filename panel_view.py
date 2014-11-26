
from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView
from icons_view import IconsView
from details_view import DetailsView

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(PanelView, self).__init__()
		self.currentPath = QtCore.QDir.homePath()
		self.type_list = 1
		self.selected_items = []
		self.set_list_type(self.type_list)
		v_layout = QtGui.QVBoxLayout()
		v_layout.addWidget(self.panel)
		self.setLayout(v_layout)
		QtCore.QObject.connect(self.panel.selectionModel(), QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'), self.panel_list_selection)

	def set_list_type(self, type):
		"""Changes the list type view"""
		if type == 1:
			self.panel = ListView(self.currentPath)
		elif type == 2:
			self.panel = IconsView(self.currentPath)
		elif type == 3:
			self.panel = DetailsView(self.currentPath)
		return self.panel

	@QtCore.pyqtSlot("QItemSelection, QItemSelection")
	def panel_list_selection(self, selected, deselected):
		index_item = selected.index(index.row(),0,index.parent())

		file_name = self.panel.setRootIndex.fileName(index_item)
		file_path = self.panel.setRootIndex.filePath(index_item)

		print(selected)
		print(deselected)