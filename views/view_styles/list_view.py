
from PyQt4 import QtGui
from PyQt4 import QtCore
from items_management.item_operations import ItemOperations
from items_management.base_item import BaseItem
from PyQt4.QtGui import QAbstractItemView, QTableView
from PyQt4.QtCore import Qt

class ListView(QtGui.QTableView):
	def __init__(self, current_path):
		"""Sets the current path items view as list"""
		super(ListView, self).__init__()
		self.item_operations=ItemOperations()
		self.selected_items = []
		self.removed = 0
		self.panel_model = BaseItem(current_path)
		self.setModel(self.panel_model)
		self.setRootIndex(self.panel_model.index(current_path))
		self.setSelectionMode(QAbstractItemView.MultiSelection)
		self.set_list_format()

		# Obtaining the selected item using mouse click event
		self.clicked.connect(self.panel_list_selection)

	def set_list_format(self):
		"""Set the list format and hide the not required columns"""
		NAME_COLUMN = 0
		NAME_COLUMN_WIDTH = 250
		SIZE_COLUMN = 1
		KIND_COLUMN = 2
		DATE_COLUMN = 3

		self.verticalHeader().setVisible(False)
		#To remove the table lines
		self.setGridStyle(Qt.NoPen)

		#Hiding the not required columns
		self.setColumnWidth(NAME_COLUMN, NAME_COLUMN_WIDTH)
		self.hideColumn(SIZE_COLUMN)
		self.hideColumn(DATE_COLUMN)
		self.hideColumn(KIND_COLUMN)

	def update_path(self, new_path):
		"""Update panel root index to modify after path changes
		Triggered by:
		- Toolbar combo box
		- Path editable field
		- Double click on panel folders

		Params:
		- new_path: receives the new path e.g. "C:\example_dir\"
		"""
		self.setRootIndex(self.panel_model.index(new_path))
		self.panel_model.setRootPath(new_path)

	def mousePressEvent(self, event):
		"""Redefining the QTableView mousePressEvent

		Params:
		- event: receives the mouse press event
		"""
		self._mouse_button = event.button()
		super(ListView, self).mousePressEvent(event)

	def keyPressEvent(self, key_event):
		"""Redefining the QTableView required key press events

		Params:
		- key_event: receives the key press event
		"""
		QTableView.keyPressEvent(self, key_event)

		#According to the item selection status it's selected/unselected
		#with the space bar
		if (key_event.key()==Qt.Key_Space):
			self.update_selected_items()

		#With the following ifs are capture the F4 key events execute the
		#corresponding actions
		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) == 1:
			#When there is only one selected item, the selected item will be renamed
			ItemOperations.rename_dialog(self,self.selectedIndexes()[0])

		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) == 0:
			#When there is no selected item, the item that has the cursor over will be renamed
			self.item_operations.rename_dialog(self,self.currentIndex())

		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) > 1:
			#When there are more than one selected item, all of them will be unselected
			#and the item where the cursor is over will be renamed
			self.selectionModel().clearSelection()
			self.item_operations.rename_dialog(self,self.currentIndex())

	def update_selected_items(self):
		"""The current selected items indexes are saved in self.selected_items list"""
		items_selected_list = self.selectedIndexes()
		if (self.selected_items != items_selected_list):
			self.selected_items = items_selected_list

	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def panel_list_selection(self, index):
		"""This method helps to perform the correct action, according to the mouse event"""
		MOUSE_RIGHT_CLICK_EVENT = 2
		MOUSE_LEFT_CLICK_EVENT = 1

		# If right click event is performed retrieve the item information
		if self._mouse_button == MOUSE_RIGHT_CLICK_EVENT:
			self.update_item_selection_status(index)

		#If left click show a message about the event
		elif self._mouse_button == MOUSE_LEFT_CLICK_EVENT:
			#If the left clicked item was already selected the prompt is launched
			if len(self.selected_items)== 1 and index == self.selected_items[0]:
				#File changed and unselected
				self.item_operations.rename_dialog(self, index)
			
			#If not all the right selected items are removed from the list, and is selected the left clicked item"
			elif len(self.selected_items)>= 1:
				#Remove all the already selected items
				self.selectionModel().clearSelection()
				#Select the left clicked item
				self.change_item_selection_status(index, "Select")

		self.update_selected_items()

	def update_item_selection_status(self, index):
		"""This method select/deselect an item base on the index sent

		Params:
		- index: receives the item index which will be selected or deselected
		"""
		try:
			if self.selected_items.index(index) >= 0:
				self.change_item_selection_status(index, "Deselect")
		except:
			self.change_item_selection_status(index, "Select")

	def change_item_selection_status(self, index, change_status_item):
		"""This method changes an item selection status

		Params:
		- index: receives the item index which will be selected or deselected.
		- change_status_item: lets the method know which status will the item have.
		"""
		if change_status_item == "Select":
			self.selectionModel().select(index, QtGui.QItemSelectionModel.Select)
		elif change_status_item == "Deselect":
			self.selectionModel().select(index, QtGui.QItemSelectionModel.Deselect)
