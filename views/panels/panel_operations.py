import shutil
import os

from PyQt4 import QtGui

class PanelOperations(object):
    def __init__(self):
        super(PanelOperations, self).__init__()

    def copy_items(self, origin_paths, target_path):
    	"""Copy items from origin_paths to target_path

    	Params:
    	- origin_paths: List of item paths, names and item type to determine the method for copying it
    	- target_path: Path where all items from origint_paths will be copied to e.g "c:\"
    	"""
    	for item_path, item_name, item_type in origin_paths:
    		if item_type == "File":
    			shutil.copy2(item_path, target_path)
    		else:
				shutil.copytree(item_path, target_path + item_name, symlinks = False, ignore = None)

    def move_items(self, origin_paths, target_path):
        """Move items from origin_paths to target_path

		Params:
		- origin_paths: List of item paths, names and item type to determine the method for moving it
		- target_path: Path where all items from origint_paths will be copied to e.g "c:\"
		"""
        for item_path, item_name, item_type in origin_paths:
            shutil.move(item_path, target_path)

    def delete_items(self, origin_paths):
        """Delete items from origin_paths

        Params:
        - origin_paths: List of item paths, names and item type to delete
        """
        for item_path, item_name, item_type in origin_paths:
            if item_type == "File":
                os.remove(item_path)
            else:
                shutil.rmtree(item_path)
