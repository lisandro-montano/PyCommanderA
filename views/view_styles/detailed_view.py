from PyQt4 import QtGui
from PyQt4 import QtCore

from view_operations import ViewOperations

class DetailedView(ViewOperations):
	def __init__(self, current_path, user_preferences_list):
		"""Sets the current path items view as list

		Params:
		- current_path: receives the path to be set as current e.g. "C:\"
		"""
		super(DetailedView, self).__init__(current_path)
		self.show_hide_list_columns(user_preferences_list)

	def show_hide_list_columns(self, user_preferences_list):
		self.setColumnWidth(self.name_column, self.name_column_width)
	 	#Hiding or showing the columns based on user's preferences
	 	if user_preferences_list[2][1] == False:
			self.hideColumn(self.kind_column)
		if user_preferences_list[2][1] == True:
			self.showColumn(self.kind_column)
		if user_preferences_list[3][1] == False:
			self.hideColumn(self.size_column)
		if user_preferences_list[3][1] == True:
			self.showColumn(self.size_column)
		if user_preferences_list[4][1] == False:
			self.hideColumn(self.date_column)
		if user_preferences_list[4][1] == True:
			self.showColumn(self.date_column)
