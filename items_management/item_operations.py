import os

from PyQt4 import QtGui

class ItemOperations(object):
    def __init__(self):
        super(ItemOperations, self).__init__()

    def rename_item(self, current_item_path, current_item_name,new_name):
        if current_item_name != new_name:
            os.rename(current_item_path, self.create_new_item_path(current_item_path, current_item_name, new_name))

    def create_new_item_path(self, current_path, name, new_name):
        """Returns the new item path.

        Params:
        - panel: list_view object
        - current_path: the current complete item path
        - name: the older item name
        - new_name: the new item name

        e.g. new_item_path(<item_current-complete_path>, <current_item_name>, <item_new_name>)
             returns "<new_item_name_complete_path>"
        e.g. new_item_path("C:\example.txt", "example.txt", "anotherName.txt")
             returns "C:\anotherName.txt"
        """
        path = self.sub_string(current_path, "right", -len(name))
        return path + new_name

    def sub_string(self, string, side, quantity):
        """Returns a substring according to the side and letter quantity send.

        Params:
        - string: the string from where the substring will be obtained
        - side: the string side from where the position counter will start
        - quantity: number of sites the position counter will move to obtain the substring

        e.g. sub_string("text example", "left", 6)
             returns "text e"
        e.g. sub_string("text example", "left", -6)
             returns "xample"
        e.g. sub_string("text example", "right", -2)
             returns "text examp"
        e.g. sub_string("text example", "right", 2)
             returns "te"
        """
        STRING_LEFT_SIDE = "left"
        STRING_RIGHT_SIDE = "right"
        if side == STRING_LEFT_SIDE:
            return string[quantity:]
        elif side == STRING_RIGHT_SIDE:
            return string[:quantity]