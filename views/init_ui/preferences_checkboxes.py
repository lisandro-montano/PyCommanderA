import sys
import inspect
from PyQt4 import QtGui, QtCore

#class CheckBox(QtGui.QWidget):
class PreferencesCheckboxes(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        super(PreferencesCheckboxes, self).__init__(parent)

        self.options_section = QtGui.QDockWidget()
        self.options_container =QtGui.QWidget()
        self.options_layout = QtGui.QVBoxLayout() 
        
        checkbox1 = QtGui.QCheckBox('Extension', self)
        checkbox2 = QtGui.QCheckBox('Size', self)
        checkbox3 = QtGui.QCheckBox('Date', self)

        button_ok = QtGui.QPushButton('OK', self)
        button_cancel = QtGui.QPushButton('Cancel', self)
        button_cancel.clicked.connect(self.close)

        self.buttons_container =QtGui.QWidget()
        self.buttons_layout = QtGui.QHBoxLayout()
        self.buttons_layout.addWidget(button_ok)
        self.buttons_layout.addWidget(button_cancel)
        self.buttons_container.setLayout(self.buttons_layout)

        self.options_layout.addWidget(checkbox1)
        self.options_layout.addWidget(checkbox2)
        self.options_layout.addWidget(checkbox3)
        self.options_layout.addWidget(self.buttons_container)

        self.options_container.setLayout(self.options_layout)

        self.options_section.setWidget(self.options_container)
        self.options_section.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.setCentralWidget(self.options_section)

        self.setFixedSize(300, 150)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Select Options')
        self.show()