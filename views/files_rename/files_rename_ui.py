import sys

from PyQt4 import QtGui
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QVBoxLayout, QWidget, QPushButton, QTableView,\
    QLineEdit, QStandardItemModel, QHBoxLayout, QStandardItem

class FilesRenameUI(QWidget):
    def __init__(self):
        super(FilesRenameUI, self).__init__()

        indexes_list = [1, 2, 3, 4, 5]
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle('PyMultipleRenameA')

        self.names = QLineEdit()
        self.names.setObjectName("Name")
        self.names.setText("[N]")

        self.extension = QLineEdit()
        self.extension.setObjectName("Extension")
        self.extension.setText("[E]")

        self.current_names_label = QtGui.QLabel("Current items name")
        self.new_names_label = QtGui.QLabel("New items name")


        header_labels = ['Name']
        self.model = QStandardItemModel(self)
        self.model.setHeaderData(0, Qt.Horizontal, header_labels[0])
        self.append_selected_files(indexes_list)
        self.current_names = QTableView()
        self.current_names.setModel(self.model)

        self.cancel_button = QPushButton()
        self.cancel_button.setObjectName("cancel")
        self.cancel_button.setText("Cancel")

        self.rename_button = QPushButton()
        self.rename_button.setObjectName("rename")
        self.rename_button.setText("Rename")

        self.fields = QHBoxLayout()
        self.fields.addWidget(self.names)
        self.fields.addWidget(self.extension)

        self.buttons = QHBoxLayout()
        self.buttons.addWidget(self.cancel_button)
        self.buttons.addWidget(self.rename_button)

        self.panel_v_layout = QVBoxLayout()
        self.panel_v_layout.addLayout(self.fields)
        self.panel_v_layout.addWidget(self.current_names)
        self.panel_v_layout.addLayout(self.buttons)

        self.setLayout(self.panel_v_layout)

    def append_selected_files(self, indexes_list):
        for index in indexes_list:
            item = QStandardItem(index)
            self.model.appendRow(item)

app = QtGui.QApplication(sys.argv)
form = FilesRenameUI()
form.show()
app.exec_()
	