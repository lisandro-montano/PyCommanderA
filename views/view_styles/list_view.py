from PyQt4 import QtGui
from PyQt4 import QtCore

from view_operations import ViewOperations

class ListView(ViewOperations):
	def __init__(self, current_path):
		"""Sets the current path items view as list

		Params:
		- current_path: receives the path to be set as current e.g. "C:\"
		"""
		super(ListView, self).__init__(current_path)
		self.hide_list_columns()

	def hide_list_columns(self):
	 	#Hiding the not required columns
	 	self.setColumnWidth(self.NAME_COLUMN, self.NAME_COLUMN_WIDTH)
		self.hideColumn(self.SIZE_COLUMN)
		self.hideColumn(self.DATE_COLUMN)
		self.hideColumn(self.KIND_COLUMN)
