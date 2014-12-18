from PyQt4 import QtGui
from PyQt4 import QtCore
from items_management.base_item import BaseItem
from PyQt4.QtGui import QAbstractItemView, QTableView
from PyQt4.QtCore import Qt

#Constants
MOUSE_RIGHT_CLICK_EVENT = 2
MOUSE_LEFT_CLICK_EVENT = 1
TABLE_VIEW_COLUMN_NUMBER = 0
TABLE_VIEW_ROW_NUMBER = 0

class ViewOperations(QtGui.QTableView):
    def __init__(self, current_path):
        """Sets the current path items view as list

		Params:
		- current_path: receives the path to be set as current e.g. "C:\"
		"""
        super(ViewOperations, self).__init__()
        self._observers = []
        self.selected_items = []
        self.panel_model = BaseItem(current_path)
        self.setModel(self.panel_model)
        self.setRootIndex(self.panel_model.index(current_path))
        self.setSelectionMode(QAbstractItemView.MultiSelection)
        TABLE_VIEW_PARENT = self.selectionModel().currentIndex().parent()
        self.set_list_format()
        self.model().index(TABLE_VIEW_ROW_NUMBER, TABLE_VIEW_COLUMN_NUMBER, TABLE_VIEW_PARENT)

    def set_list_format(self):
        """Set the list format and hide the not required columns"""
        self.name_column = 0
        self.name_column_width = 250
        self.size_column = 1
        self.kind_column = 2
        self.date_column = 3

        self.verticalHeader().setVisible(False)

        #To remove the table lines
        self.setGridStyle(Qt.NoPen)

        #Disable tab key navigation for table items to have it available only at panel level
        self.setTabKeyNavigation(False)

    def update_path(self, new_path):
        """Update panel root index to modify after path changes	Triggered by:
        - Toolbar combo box
        - Path editable field
        - Double click on panel folders

        Params:
        - new_path: receives the new path e.g. "C:\example_dir\"
        """
        self.setRootIndex(self.panel_model.index(new_path))
        self.panel_model.setRootPath(new_path)
        self.setFocus()

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def update_panel_current_path(self, index):
        """This method update the view's path, if the event was left, only if the item is a Folder

        Params:
        - index: receives the item index over which the actions will be performed (QIndex)
        """
        if self.panel_model.get_item_type(index) == "Folder":
            new_path = self.panel_model.get_item_data(index, "Path")
            for panel_observer in self._observers:
                panel_observer.propagate_dir(new_path)

    def mousePressEvent(self, event):
        """Redefining the QTableView mousePressEvent

        Params:
        - event: receives the mouse press event
        """
        self._mouse_button = event.button()
        super(ViewOperations, self).mousePressEvent(event)

    def keyPressEvent(self, key_event):
        """Redefining the QTableView required key press events

        Params:
        - key_event: receives the key press event
        """
        QTableView.keyPressEvent(self, key_event)

        #According to the item selection status it's selected/unselected with the space bar
        if key_event.key() == Qt.Key_Space:
            self.update_selected_items()

    def update_selected_items(self):
        """The current selected items indexes are saved in self.selected_items list"""
        items_selected_list = self.selectedIndexes()
        if self.selected_items != items_selected_list:
            self.selected_items = items_selected_list

    @QtCore.pyqtSlot(QtCore.QModelIndex)
    def panel_list_selection(self, index):
        """This method helps to perform the correct action, according to the mouse event

        Params:
        - index: receives the item index over which the actions will be performed
        """

        # If right click event is performed retrieve the item information
        if self._mouse_button == MOUSE_RIGHT_CLICK_EVENT:
            self.update_item_selection_status(index)
        #If left click show a message about the event
        elif self._mouse_button == MOUSE_LEFT_CLICK_EVENT:
        	#If the left clicked item was already selected the prompt is launched
        	if len(self.selected_items) == 1 and index == self.selected_items[0]:
        		#File changed and unselected
        		self.rename_dialog(index)

        	#If not all the right selected items are removed from the list, and is selected the left clicked item
        	elif len(self.selected_items) >= 1:
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
        self.update_selected_items()

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

    def rename_dialog(self, index):
        """Launch an input dialog where the current item name to be renamed is displayed

        Actions:
        - After press Ok button the item is renamed if the name was modified.
        - After press Cancel button the item name is not changed.

        Params:
        - index: selected item index
        """
        current_type = self.model().get_item_type(index)
        current_item_name = str(self.model().get_item_data(index, "Name"))
        new_name, ok_button_pressed = QtGui.QInputDialog.getText(self, 'Rename %s Dialog' % current_type,
                                                  'Modify the %s name:' % current_type,
                                                  QtGui.QLineEdit.Normal, current_item_name)

        if ok_button_pressed == True:
            self.model().rename_item(index, new_name, current_item_name)

    def attach(self, observer):
        """Attach observers to detect directory/path changes"""
        if not observer in self._observers:
            self._observers.append(observer)
