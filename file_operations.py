import sys, os

from PyQt4 import QtGui

def file_data(panel, index, data):
    index_item = panel.model().index(index.row(),0,index.parent())

    if (data == "Name"):
        return panel.model().fileName(index_item)

    elif data == "Path":
        return panel.model().filePath(index_item)

    elif data == "Info":
        return panel.model().fileInfo(index_item)

    elif data == "Type":
        return panel.model().fileInfo(index_item)

def isFileFolder(panel, index):
    """Returns 1 if file and returns 0 if folder"""
    file_type = panel.file_data(index, "Type")
    if panel.sub_string(str(file_type,"left",-6)).find('Folder') >= 0:
        return 0
    elif panel.sub_string(str(file_type,"left", -4)).find("File") >= 0:
        return 1

def rename_dialog(panel, index):
    current_file_name = str(file_data(panel,index,"Name"))
    current_file_path = str(file_data(panel,index,"Path"))
    text, ok = QtGui.QInputDialog.getText(panel, 'Rename Dialog', 'Modify the file/folder name:',
                                          QtGui.QLineEdit.Normal, current_file_name)

    if ok and current_file_path != text:
        os.rename(current_file_path,rename_replace_path(current_file_path,current_file_name,text))

def rename_replace_path(current_path,name,new_name):
    """This method structure the new file path considering the new name introduced"""
    temp = sub_string(current_path,"right",-len(name))
    return temp + new_name

def sub_string(string,side,quantity):
    if side == "left":
        return string[quantity:]
    elif side == "right":
        return string[:quantity]