from PyQt4 import QtGui
from PyQt4 import QtCore

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
		- action: string that defines the action that will be performed in the panels or panel items e.g. Move
		          an item from left panel to right panel, Copy and item from right to left panel
		          Possible values : View, Rename, Copy, Move, Delete, New File and Exit 
		"""
		self.panel_operations = PanelOperations()
		self.item_operations = ItemOperations()
		self.origin_full_paths = []
		self.target_path = ""

		if self.left_panel.panel.hasFocus():
			current_panel = self.left_panel
			target_panel = self.right_panel
		elif self.right_panel.panel.hasFocus():
			current_panel = self.right_panel
			target_panel = self.left_panel	

		self.origin_full_paths = self.get_current_panel_paths(current_panel)

		if action == "Copy" or action == "Move":
			self.target_path = self.get_target_panel_path(target_panel)

		self.execute_action(action)

	def get_current_panel_paths(self, current_panel):
		"""Obtain an array that includes all selected paths in the origin panel
		if no item is selected, the current index will be returned as only item in the array

		Params:
		- current_panel: PanelView object that is currently focused and where the actions will be originated
		- current_panel_paths: retuns the selected item paths from the current_panel in order to perform actions
		                       on them
		"""
		current_panel_paths = []
		if len(current_panel.panel.selected_items) == 0:
			item_path = str(current_panel.panel.model().get_item_data(current_panel.panel.currentIndex(), "Path"))
			item_name = str(current_panel.panel.model().get_item_data(current_panel.panel.currentIndex(), "Name"))
			item_type = str(current_panel.panel.model().get_item_type(current_panel.panel.currentIndex()))
			current_panel_paths.append((item_path, item_name, item_type))
		else:
			for index in current_panel.panel.selected_items:
				item_path = str(current_panel.panel.model().get_item_data(index, "Path"))
				item_name = str(current_panel.panel.model().get_item_data(index, "Name"))
				item_type = str(current_panel.panel.model().get_item_type(index))
				current_panel_paths.append((item_path, item_name, item_type))

		return current_panel_paths

	def get_target_panel_path(self, target_panel):
		"""Obtain the target panel path in order to perform move or copy actions

		Params:
		- target_panel: panel where item(s) will be moved or copied to e.g. left_panel
		- target_panel_path: this path will be obtained from the path_edit field in the 
		                     target panel e.g /Users/username/Documents 
		"""
		target_panel_path = str(target_panel.panel_toolbar.path_edit.text())
		
		return target_panel_path

	def execute_action(self, action):
		"""Execute the panel_operations action depending on the button that was pressed
		and sending required params

		Params:
		- action: action from button pressed that will trigger proper panel_operation method e.g. "Copy"
		"""
		COPY_ITEMS = "Copy"
		MOVE_ITEMS = "Move"
		DELETE_ITEMS = "Delete"

		if action == COPY_ITEMS:
			self.panel_operations.copy_items(self.origin_full_paths, self.target_path)
		if action == MOVE_ITEMS:
			self.panel_operations.move_items(self.origin_full_paths, self.target_path)
		if action == DELETE_ITEMS:
			self.confirm_items_deletion()

	def confirm_items_deletion(self):
		"""Launch confirmation message to ensure the user really wants to delete selecte files"""
		self.files_to_delete = []
		for item_path, item_name, item_type in self.origin_full_paths:
			self.files_to_delete.append(item_name)
		message = ", ".join(self.files_to_delete)
		
		reply = QtGui.QMessageBox.question(self, "PyCommanderA",
            "Are you sure you want to delete?\n" + message, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			self.panel_operations.delete_items(self.origin_full_paths)
