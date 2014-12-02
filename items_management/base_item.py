
from PyQt4 import QtGui
from PyQt4 import QtCore

class BaseItem(QtGui.QFileSystemModel):
	def __init__(self, current_path):
		"""Create Base Item based on """
		super(BaseItem, self).__init__()
		self.setRootPath(current_path)