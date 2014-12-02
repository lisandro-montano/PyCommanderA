import os

from PyQt4 import QtGui

class ItemOperations(object):
    def __init__(self):
        super(ItemOperations, self).__init__()

    def item_data(self, panel, index, data):
        """Returns the item information according to the required data requested.

        Params:
        - panel: list_view object
        - index: selected item index
        - data: item data type requested
        """
        index_item = panel.model().index(index.row(), 0, index.parent())

        if (data == "Name"):
            return panel.model().fileName(index_item)

        elif data == "Path":
            return panel.model().filePath(index_item)

        elif data == "Info":
            return panel.model().fileInfo(index_item)

        elif data == "Type":
            return panel.model().type(index_item)

    def get_item_type(self, panel, index):
        """Returns 1 if the item is File and returns 0 if the item is Folder

        Params:
        - panel: list_view object
        - index: selected item index
        """
        file_type = self.item_data(panel, index, "Type")
        if self.sub_string(str(file_type), "left", -6).find('Folder') >= 0:
            return 'Folder'
        elif self.sub_string(str(file_type), "left", -4).find("File") >= 0:
            return "File"

    def rename_dialog(self, panel, index):
        """Launch an input dialog where the current item name to be renamed is displayed
        Actions:
        - After press Ok button the item is renamed if the name was modified.
        - After press Cancel button the item name is not changed.

        Params:
        - panel: list_view object
        - index: selected item index
        """
        current_file_name = str(self.item_data(panel, index, "Name"))
        current_file_path = str(self.item_data(panel, index, "Path"))
        current_type = self.get_item_type(panel, index)
        new_name, ok = QtGui.QInputDialog.getText(panel, 'Rename %s Dialog' % current_type,
                                              'Modify the %s name:' % current_type,
                                              QtGui.QLineEdit.Normal, current_file_name)

        #If the
        if ok and current_file_name != new_name:
            os.rename(current_file_path, self.new_item_path(current_file_path, current_file_name, new_name))

    def new_item_path(self, current_path, name, new_name):
        """Returns the new item path.

        Params:
        - panel: list_view object
        - current_path: the current complete item path
        - name: the older item name
        - new_name: the new item name
        """
        path = self.sub_string(current_path, "right", -len(name))
        return path + new_name

    def sub_string(self, string, side, quantity):
        """Returns a substring according to the side and letter quantity send.

        Params:
        - string: the string from where the substring will be obtained
        - side: the string side from where the position counter will start
        - quantity: number of sites the position counter will move to obtain the substring
        """
        if side == "left":
            return string[quantity:]
        elif side == "right":
            return string[:quantity]