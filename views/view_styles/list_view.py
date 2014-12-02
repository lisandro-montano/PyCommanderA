
from PyQt4 import QtGui
from PyQt4 import QtCore
from items_management.file_operations import rename_dialog
from PyQt4.QtGui import QAbstractItemView, QListView
from PyQt4.QtCore import Qt

class ListView(QtGui.QListView):
	def __init__(self, current_path):
		"""Sets the current path items view as list"""
		super(ListView, self).__init__()
		self.selected_items = []
		self.removed = 0
		self.panel_model = QtGui.QFileSystemModel()
		self.panel_model.setRootPath(current_path)
		self.setModel(self.panel_model)
		self.setRootIndex(self.panel_model.index(current_path))
		self.setSelectionMode(QAbstractItemView.MultiSelection)

		# Obtaining the selected item using mouse right click event
		self.clicked.connect(self.panel_list_selection)

	def update_path(self, new_path):
		"""Update panel root index to modify after path changes
		Triggered by:
		- Toolbar combo box
		- Path editable field
		- Double click on panel folders
		"""
		self.setRootIndex(self.panel_model.index(new_path))

	def mousePressEvent(self, event):
		"""Redefining the QListView mousePressEvent"""
		self._mouse_button = event.button()
		super(ListView, self).mousePressEvent(event)

	def keyPressEvent(self, key_event):
		# Maintain original functionality by calling QListView's version
		QListView.keyPressEvent(self, key_event)
		if (key_event.key()==Qt.Key_Space):
			self.verify_selected_items()

		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) == 1:
			rename_dialog(self,self.selectedIndexes()[0])

		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) == 0:
			rename_dialog(self,self.currentIndex())

		if key_event.key() == Qt.Key_F4 and len(self.selectedIndexes()) > 1:
			#Unselect all the files and enable the rename current index file
			self.selectionModel().clearSelection()
			rename_dialog(self,self.currentIndex())

	def verify_selected_items(self):
		#Verify if the selected items are equal to selected_items array
		items_selected_list = self.selectedIndexes()
		if (self.selected_items != items_selected_list):
			self.selected_items = items_selected_list

	@QtCore.pyqtSlot(QtCore.QModelIndex)
	def panel_list_selection(self, index):
		"""According to the mouse event the action is performed"""
		mouse_right_click_event = 2
		mouse_left_click_event = 1

		# If right click retrieve the item information
		if self._mouse_button == mouse_right_click_event:
			try:
				if self.selected_items.index(index) >= 0:
					self.selectionModel().select(index, QtGui.QItemSelectionModel.Deselect)
			except:
				self.selectionModel().select(index, QtGui.QItemSelectionModel.Select)

		#If left click show a message about the event
		elif self._mouse_button == mouse_left_click_event:
			#If the left clicked item was already selected the prompt is launched
			if len(self.selected_items)== 1 and index == self.selected_items[0]:
				#File changed and unselected
				rename_dialog(self, index)
			
			#If not all the right selected items are removed from the list, and is selected the left clicked item"
			elif len(self.selected_items)>= 1:
				#Remove all the already selected items
				self.selectionModel().clearSelection()
				#Select the left clicked item
				self.selectionModel().select(index, QtGui.QItemSelectionModel.Select)

		self.verify_selected_items()


