from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView
from icons_view import IconsView
from details_view import DetailsView
from panel_toolbar import PanelToolbar

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the current path and defines the panels"""
		super(PanelView, self).__init__()
		self.current_path = QtCore.QDir.rootPath()
		self.type_list = 1
		self.selected_items = []

		self.set_list_type(self.type_list)
		
		self.panel_toolbar = PanelToolbar(self.current_path)
		
		self.panel_layout = QtGui.QVBoxLayout()
		self.panel_layout.addWidget(self.panel_toolbar)
		self.panel_layout.addWidget(self.panel)
		self.setLayout(self.panel_layout)

		self.panel_toolbar.attach(self)

		self.panel.clicked.connect(self.panel_list_selection)

	def set_list_type(self, type):
		"""Changes the list type view"""
		if type == 1:
			self.panel = ListView(self.current_path)
		elif type == 2:
			self.panel = IconsView(self.current_path)
		elif type == 3:
			self.panel = DetailsView(self.current_path)
		return self.panel

	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def panel_list_selection(self, index):
		index_item = self.panel.panel_model.index(index.row(),0,index.parent())

		file_path = self.panel.panel_model.filePath(index_item)
		file_type = self.panel.panel_model.type(index_item)

		if sub_string(str(file_type)).find('Folder') >= 0:
			print "Is folder"

		if sub_string(str(file_type)).find("File") > 0:
			print "Is file"

		print(index.row())
		print(file_path)

	def propagate_dir(self, new_dir):
		self.current_path = new_dir
		self.panel_toolbar.path_edit.setText(self.current_path)
		self.panel.setRootIndex(self.panel.panel_model.index(self.current_path))

def sub_string(string):
	return string[-6:]