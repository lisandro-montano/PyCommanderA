import os

from PyQt4 import QtGui

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

		self.current_panel = self.left_panel
		self.target_panel = self.right_panel

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
			self.current_panel = self.left_panel
			self.target_panel = self.right_panel
		elif self.right_panel.panel.hasFocus():
			self.current_panel = self.right_panel
			self.target_panel = self.left_panel

		self.origin_full_paths = self.get_current_panel_paths()

		if action == "Copy" or action == "Move":
			self.target_path = self.get_target_panel_path(self.target_panel)

		self.execute_action(action)

	def get_current_panel_paths(self):
		"""Obtain an array that includes all selected paths in the origin panel
		if no item is selected, the current index will be returned as only item in the array

		Params:
		- current_panel: PanelView object that is currently focused and where the actions will be originated
		- current_panel_paths: returns the selected item paths from the current_panel in order to perform actions
		  on them
		"""
		current_panel_var = self.current_panel.panel
		current_panel_paths = []
		if len(self.current_panel.panel.selected_items) == 0:
			item_path = str(current_panel_var.model().get_item_data(current_panel_var.currentIndex(), "Path"))
			item_name = str(current_panel_var.model().get_item_data(current_panel_var.currentIndex(), "Name"))
			item_type = str(current_panel_var.model().get_item_type(current_panel_var.currentIndex()))
			current_panel_paths.append((item_path, item_name, item_type))
		else:
			for index in current_panel_var.selected_items:
				item_path = str(current_panel_var.model().get_item_data(index, "Path"))
				item_name = str(current_panel_var.model().get_item_data(index, "Name"))
				item_type = str(current_panel_var.model().get_item_type(index))
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
		CREATE_FILES = "New File"
		RENAME_ITEMS = "Rename"

		if action == COPY_ITEMS:
			self.panel_operations.copy_items(self.origin_full_paths, self.target_path)
		if action == MOVE_ITEMS:
			self.panel_operations.move_items(self.origin_full_paths, self.target_path)
		if action == DELETE_ITEMS:
			self.confirm_items_deletion()
		if action == CREATE_FILES:
			self.new_file_dialog()
		if action == RENAME_ITEMS:
			self.rename_item_key_event()

	def confirm_items_deletion(self):
		"""Launch confirmation message to ensure the user really wants to delete selected files"""
		self.files_to_delete = []
		for item_path, item_name, item_type in self.origin_full_paths:
			self.files_to_delete.append(item_name)
		message = ", ".join(self.files_to_delete)
		
		reply = QtGui.QMessageBox.question(self, "PyCommanderA",
            "Are you sure you want to delete?\n" + message, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
		if reply == QtGui.QMessageBox.Yes:
			self.panel_operations.delete_items(self.origin_full_paths)

	def new_file_dialog(self):
		"""Create new file in the current path if it does not exist"""
		new_file_name, ok_button_pressed = QtGui.QInputDialog.getText(self, 'Create New File', 'Introduce New File name:')
		current_path = self.current_panel.current_path

		#Verify if there is no file with the same introduced name in the current path
		if ok_button_pressed and os.path.isfile(current_path + new_file_name) == False:
			self.panel_operations.create_new_file(new_file_name, current_path)

		#if there is a file name with the same name introduced, an error message is displayed
		elif ok_button_pressed != False:
			QtGui.QMessageBox.information(self, "Error Message",
									"There is a file with the same introduced name. No new file was created.")

	def rename_item_key_event(self):
		"""With the following ifs are capture the F4 key events execute the corresponding actions"""
		if len(self.current_panel.panel.selectedIndexes()) == 1:
			#When there is only one selected item, the selected item will be renamed
			self.current_panel.panel.rename_dialog(self.selectedIndexes()[0])

		if len(self.current_panel.panel.selectedIndexes()) == 0 or len(self.current_panel.panel.selectedIndexes()) > 1:
			#When there is no selected item, the item that has the cursor over will be renamed
			self.current_panel.panel.selectionModel().clearSelection()
			self.current_panel.panel.rename_dialog(self.current_panel.panel.currentIndex())