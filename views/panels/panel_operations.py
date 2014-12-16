import shutil
import os

from PyQt4 import QtGui

class PanelOperations(object):
    def __init__(self):
        super(PanelOperations, self).__init__()

    def copy_items(self, origin_full_paths, target_path):
    	"""Copy items from origin_full_paths to target_path

    	Params:
    	- origin_full_paths: List of item paths, names and item type to determine the method for copying it
    	- target_path: Path where all items from origint_paths will be copied to e.g "c:\"
    	"""
        for item_path, item_name, item_type in origin_full_paths:
            if item_type == "File":
                shutil.copy2(item_path, target_path)
            else:
                shutil.copytree(item_path, target_path + item_name, symlinks = False, ignore = None)

    def move_items(self, origin_full_paths, target_path):
        """Move items from origin_full_paths to target_path

		Params:
		- origin_full_paths: List of item paths, names and item type to determine the method for moving it
		- target_path: Path where all items from origint_paths will be copied to e.g "c:\"
		"""
        for item_path, item_name, item_type in origin_full_paths:
            shutil.move(item_path, target_path)

    def delete_items(self, origin_full_paths):
        """Delete items from origin_full_paths

        Params:
        - origin_full_paths: List of item paths, names and item type to delete
        """
        for item_path, item_name, item_type in origin_full_paths:
            if item_type == "File":
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)

    def create_new_file(self, new_file_name, current_path):
        """Create new file in the current path if it does not exist

        Params:
        - new_file_name: Receives the new file name
        - current_path: Receives the current panel root path
        """
        try:
            file = open(current_path + new_file_name, 'w')
            file.close()

        except:
            print "Error"
