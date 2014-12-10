import sys
from PyQt4 import QtGui
from PyQt4 import QtCore

from items_management.item_properties import ItemProperties

class PropertiesView(QtGui.QDialog):
    def __init__(self, parentObject, file_path):
        super(PropertiesView, self).__init__(parentObject)
        self.fileProperties = ItemProperties(file_path)
        self.init_ui()

    def init_ui(self):
        modal_heigth = 375
        modal_width = 275
        self.setFixedSize(modal_heigth, modal_width)
        self.setWindowTitle("<{0}> properties". format(self.fileProperties.get_name()))
        self.center()
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMaximizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowMinimizeButtonHint)
        
        self.create_info_components()
        self.create_buttons_components()
        self.set_layout()
        self.configure_events()

        self.show()

    def center(self):
        frameGm = self.frameGeometry()
        centerPoint = QtGui.QDesktopWidget().availableGeometry().center()
        frameGm.moveCenter(centerPoint)
        self.move(frameGm.topLeft())

    def HLine(self):
        toto = QFrame()
        toto.setFrameShape(QFrame.HLine)
        toto.setFrameShadow(QFrame.Sunken)
        return toto

    def create_info_components(self):

        self.grid = QtGui.QGridLayout(self)
        
        # Set File Info into Vbox Layout
        self.vbox = QtGui.QVBoxLayout()
        location_label = QtGui.QLabel("File location: " + str(self.fileProperties.get_location()), self)
        self.vbox.addWidget(location_label)
        self.vbox.addStretch(0.5)
        type_label = QtGui.QLabel("Type: " + str(self.fileProperties.get_type()), self)
        self.vbox.addWidget(type_label)
        self.vbox.addStretch(0.5)
        size_label = QtGui.QLabel("Size: " + str(self.fileProperties.get_size_in_bytes()), self)
        self.vbox.addWidget(size_label)
        self.vbox.addStretch(0.5)
        attributes_label = QtGui.QLabel("Attributes: ", self)
        self.vbox.addWidget(attributes_label)

        read_only_cb = QtGui.QCheckBox('&Read only', self)
        read_only_cb.setChecked(self.fileProperties.is_readonly())
        self.vbox.addWidget(read_only_cb)

        hidden_cb = QtGui.QCheckBox('&Hidden', self)
        hidden_cb.setChecked(self.fileProperties.is_hidden())
        self.vbox.addWidget(hidden_cb)

        self.vbox.addStretch()

    def create_buttons_components(self):

        # Set Buttons into Hbox Layout
        first_column = 0
        first_row = 0
        second_column = 1
        second_row = 1
        self.hbox = QtGui.QHBoxLayout()
        generate_ok_button = QtGui.QPushButton("OK", self)
        generate_ok_button.resize(generate_ok_button.sizeHint())
        self.hbox.addWidget(generate_ok_button)

        generate_cancel_button = QtGui.QPushButton("Cancel", self)
        generate_cancel_button.resize(generate_cancel_button.sizeHint())
        self.hbox.addWidget(generate_cancel_button)
        
        generate_apply_button = QtGui.QPushButton("Apply", self)
        generate_apply_button.resize(generate_apply_button.sizeHint())
        self.hbox.addWidget(generate_apply_button)
        
        self.grid.addLayout(self.vbox, first_row, first_column)
        self.grid.addLayout(self.hbox, second_row, first_column)

    def set_layout(self):
        self.setLayout(self.grid)
        
    def configure_events(self):
        pass
