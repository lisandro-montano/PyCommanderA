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
	 	self.setColumnWidth(self.name_column, self.name_column_width)
		self.hideColumn(self.size_column)
		self.hideColumn(self.date_column)
		self.hideColumn(self.kind_column)
