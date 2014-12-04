import shutil

from PyQt4 import QtGui

class PanelOperations(object):
    def __init__(self):
        super(PanelOperations, self).__init__()

    def copy_items(self, origin_paths, target_path):
    	"""Copy items from origin_paths to target_path

    	Params:
    	- origin_paths: List of item paths and item type to determine the method for copying it
    	- target_path: Path where all items from origint_paths will be copied to e.g "c:\"
    	"""
    	for item_path, item_type in origin_paths:
    		if item_type == "File":
    			shutil.copy2(item_path, target_path)
    		else:
				shutil.copytree(item_path, target_path, symlinks = False, ignore = None)