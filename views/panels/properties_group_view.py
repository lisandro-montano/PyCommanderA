__author__ = 'Elmer Alvarado'

import sys
from PyQt4 import QtGui, QtCore
from items_management.group_properties import GroupProperties

class PropertiesGroupView(QtGui.QDialog):

    def __init__(self, parent_object, list_files):
        super(PropertiesGroupView, self).__init__(parent_object)
        self.group_properties = GroupProperties(list_files)
        self.init_ui()

    def init_ui(self):
        heigth = 380
        width = 280
        self.setFixedSize(heigth, width)
        self.setWindowTitle("General Properties")
        #self.center()
        self.show()
        self.create_info_components()
        self.create_buttons_components()

    def create_info_components(self):

        self.grid = QtGui.QGridLayout(self)

        # Set File Info into Vbox Layout
        self.vbox = QtGui.QVBoxLayout()
        location_label = QtGui.QLabel("File location: " + str(self.group_properties.get_location()), self)
        self.vbox.addWidget(location_label)
        self.vbox.addStretch(0.5)
        type_label = QtGui.QLabel("Type: " + str(self.group_properties.get_type()), self)
        self.vbox.addWidget(type_label)
        self.vbox.addStretch(0.5)
        size_label = QtGui.QLabel("Size: " + str(self.group_properties.get_size_in_bytes()), self)
        self.vbox.addWidget(size_label)
        self.vbox.addStretch(0.5)
        attributes_label = QtGui.QLabel("Attributes: ", self)
        self.vbox.addWidget(attributes_label)

        read_only_cb = QtGui.QCheckBox('&Read only', self)
        read_only_cb.setChecked(self.group_properties.is_readonly())
        self.vbox.addWidget(read_only_cb)

        hidden_cb = QtGui.QCheckBox('&Hidden', self)
        hidden_cb.setChecked(self.group_properties.is_hidden())
        self.vbox.addWidget(hidden_cb)

        self.vbox.addStretch()

    def create_buttons_components(self):

        #Set Buttons into Hbox Layout
        first_column = 0
        first_row = 0
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
