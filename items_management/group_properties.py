__author__ = 'Elmer Alvarado'

import os, stat

class GroupProperties(object):

    group_type = "Multiple Types"
    total_size = 0.00
    is_readonly = True
    is_hidden = True
    def __init__(self, list_files):
        self.list_files = list_files
        self.get_all_properties()

    def get_current_dir(self):
        return "current dir: ", os.getcwd()

    def get_location(self):
        return os.path.dirname(self.list_files[0])

    def get_type(self):
        return self.group_type

    def get_size_in_bytes(self):
        return self.total_size


    def is_readonly(self):
        return True

    def is_hidden(self):
        return False

    def get_number_of_files(self):
        pass

    def get_number_of_folders(self):
        pass

    def set_as_readonly(self):
		pass

    def set_as_hidden(self):
		pass

    def get_all_properties(self):
        for file in self.list_files:
            # sum the file size
            self.total_size += os.path.getsize(file)

            # Verify that all files are
            if(not os.access(file, os.W_OK)):
                self.is_readonly = False


