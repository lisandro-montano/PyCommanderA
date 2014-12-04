from PyQt4 import QtGui
from PyQt4 import QtCore
import warnings

from views.panels.panel_view import PanelView
from views.panels.panel_operations import PanelOperations
from items_management.item_operations import ItemOperations

class PanelManager(QtGui.QDockWidget):

	def __init__(self):
		"""Initialize the panels for PyCommanderA
		Create 2 panels (left_panel and right_panel)
		Set them properly in a splitter
		"""
		super(PanelManager, self).__init__()
		panel_splitter = QtGui.QSplitter()
		self.left_panel = PanelView()
		self.left_panel.setAccessibleName("left")
		self.right_panel = PanelView()
		self.right_panel.setAccessibleName("right")

		panel_splitter.addWidget(self.left_panel)
		panel_splitter.addWidget(self.right_panel)

		self.setWidget(panel_splitter)
		self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
		self.setTabOrder(self.left_panel.panel, self.right_panel.panel)

		self.left_panel.panel.setFocus()

	def get_focused_panel(self, action):
		"""Obtains the panel that has focus first and sends the action, current_panel 
		and target_panel to execute the action

		Params:
		- action: defines the action that will be performed in the panels or panel items e.g. Move
		          an item from left panel to right panel, Copy and item from right to left panel
		"""
		self.panel_operations = PanelOperations()
		self.item_operations = ItemOperations()

		if self.left_panel.panel.hasFocus():
			current_panel = self.left_panel
			target_panel = self.right_panel
		elif self.right_panel.panel.hasFocus():
			current_panel = self.right_panel
			target_panel = self.left_panel	
		else:
			print "Please, select a panel to perform the action"

		self.origin_paths = self.get_current_panel_paths(current_panel)

		if action == "Copy" or action == "Move":
			self.target_path = self.get_target_panel_path(target_panel)

	def get_current_panel_paths(self, current_panel):
		"""Obtain an array that includes all selected paths in the origin panel
		if no item is selected, the current index will be returne as only item in the array

		Params:
		- current_panel: panel that is currently focused and where the actions will be originated
		"""
		current_panel_paths = []
		if len(current_panel.panel.selected_items) == 0:
			item_path = str(current_panel.panel.model().get_item_data(current_panel.panel.currentIndex(), "Path"))
			item_type = str(current_panel.panel.model().get_item_type(current_panel.panel.currentIndex()))
			current_panel_paths.append((item_path, item_type))
		else:
			for index in current_panel.panel.selected_items:
				item_path = str(current_panel.panel.model().get_item_data(index, "Path"))
				item_type = str(current_panel.panel.model().get_item_type(index))
				current_panel_paths.append((item_path, item_type))

		return current_panel_paths

	def get_target_panel_path(self, target_panel):
		"""Obtain the target panel path in order to perform move or copy actions

		Params:
		- target_panel: panel where item(s) will be moved or copied to e.g. left_panel 
		"""
		target_panel_full_path = str(target_panel.panel.model().get_item_data(target_panel.panel.currentIndex(), "Path"))
		target_panel_name = str(target_panel.panel.model().get_item_data(target_panel.panel.currentIndex(), "Name"))

		target_panel_path = self.item_operations.sub_string(target_panel_full_path, "right", -len(target_panel_name))
		
		return target_panel_path

		
			