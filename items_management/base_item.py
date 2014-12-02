
from PyQt4 import QtGui
from PyQt4 import QtCore

class BaseItem(QtGui.QFileSystemModel):
	def __init__(self, current_path):
		"""Create BaseItem to handle all item_operations"""
		super(BaseItem, self).__init__()
		self.setRootPath(current_path)