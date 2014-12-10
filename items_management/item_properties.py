
import os, stat

class ItemProperties(object):

    folder_type_text = "File Folder"

    def __init__(self, file_path):
        self.file_path = file_path
        self.name = os.path.basename(self.file_path)
        self.location = os.path.dirname(self.file_path)
        self.type = os.path.splitext(self.file_path)[1]
        self.size = os.path.getsize(self.file_path)
        self.readonly = (not os.access(self.file_path, os.W_OK))
        self.isfile = os.path.isfile(self.file_path)
        self.isfolder = os.path.isdir(self.file_path)

    def get_current_dir(self):
        return "current dir: ", os.getcwd()
    
    def get_location(self):
        return self.location

    def get_extention(self):
        return self.type

    def get_type(self):
        if(self.is_file()):
            return self.get_extention()
        else:
            return self.folder_type_text

    def get_size_in_bytes(self):
        return self.size

    def is_readonly(self):
        return self.readonly

    def is_hidden(self):
        #linux method to verify if it is hidden
        #return self.file_path.startswith('.')
        return False

    def is_file(self):
        return self.isfile

    def is_folder(self):
        return self.isfolder

    def get_name(self):
        return self.name

    def set_as_readonly(self):
		os.chmod(self.file_path ,stat.S_IWRITE)
