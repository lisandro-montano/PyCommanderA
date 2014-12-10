from PyQt4 import QtCore

class Settings(QtCore.QSettings):
    def __init__(self):
        """Initializes the Settings class"""
        super(Settings, self).__init__()