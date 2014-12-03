
from PyQt4 import QtGui
from item_operations import ItemOperations
from PyQt4 import QtCore

class BaseItem(QtGui.QFileSystemModel):
	def __init__(self, current_path):
		"""Create BaseItem to handle all item_operations

		Params:
		- current_path: receives the path to be set as current e.g. "C:\"
		"""
		super(BaseItem, self).__init__()
		self.setRootPath(current_path)
		self.item_operations = ItemOperations()

	def get_item_data(self, index, data):
		"""Returns the item information according to the required data requested.

		Params:
		- panel: list_view object
		- index: selected item index
		- data: item data type requested

		e.g. item_date(<list_view_object>, <folder_selected_index>, "Name")
		     returns "<folder_name>"
		"""
		TABLE_VIEW_COLUMN_NUMBER = 0
		index_item = self.index(index.row(), TABLE_VIEW_COLUMN_NUMBER, index.parent())

		if data == "Name":
			return self.fileName(index_item)

		elif data == "Path":
			return self.filePath(index_item)

		elif data == "Info":
			return self.fileInfo(index_item)

		elif data == "Type":
			return self.type(index_item)

	def get_item_type(self, index):
		"""Returns the item type, returns "File" or "Folder"

		Params:
		- panel: list_view object
		- index: selected item index

		e.g. item_date(<list_view_object>, <file_selected_index>)
		     returns "File"
		"""
		file_type = self.get_item_data(index, "Type")
		if self.item_operations.sub_string(str(file_type), "left", -6).find('Folder') >= 0:
			return 'Folder'
		elif self.item_operations.sub_string(str(file_type), "left", -4).find("File") >= 0:
			return "File"

