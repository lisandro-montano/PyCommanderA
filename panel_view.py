
from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(PanelView, self).__init__()
		self.currentPath = QtCore.QDir.homePath()
		self.type_list = 1
		self.selected_items = []
		self.panel = ListView(self.currentPath)
		v_layout = QtGui.QVBoxLayout()
		v_layout.addWidget(self.panel)
		self.setLayout(v_layout)

	def change_list_type(self, type):
		"""Changes the list type view"""
		if type == 1:
			self.panel = ListView(self.currentPath)
		elif type == 2:
			self.panel = IconsView(self.currentPath)
		elif type == 3:
			self.panel = DetailsView(self.currentPath)



class IconsView(ListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(IconsView, self).__init__(currentPath)


class DetailsView(ListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(DetailsView, self).__init__(currentPath)