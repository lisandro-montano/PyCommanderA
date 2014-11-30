import sys

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

def sub_string(string,side,quantity):
    if side == "left":
        return string[quantity:]
    elif side == "right":
        return string[:quantity]