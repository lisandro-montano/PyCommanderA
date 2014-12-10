from PyQt4 import QtGui
from PyQt4 import QtCore

from view_operations import ViewOperations

class DetailedView(ViewOperations):
	def __init__(self, current_path):
		"""Sets the current path items view as list

		Params:
		- current_path: receives the path to be set as current e.g. "C:\"
		"""
		super(DetailedView, self).__init__(current_path)