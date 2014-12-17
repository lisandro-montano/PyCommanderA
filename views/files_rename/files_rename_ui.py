import sys

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QVBoxLayout, QWidget, QPushButton, QTableView, QDockWidget, QLineEdit, QStandardItemModel


class FilesRenameUI(QDockWidget):
    def __init__(self, indexes_list):
        super(FilesRenameUI, self).__init__()

        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle('Rename multiple files')
        self.panel_splitter = QtGui.QSplitter()

        self.names = QLineEdit()
        self.names.setObjectName("Name")
        self.names.setText("[N]")

        self.extension = QLineEdit()
        self.extension.setObjectName("Extension")
        self.extension.setText("[E]")

        self.current_names_label = QtGui.QLabel("Current items name")
        self.new_names_label = QtGui.QLabel("New items name")

        self.model1 = QStandardItemModel(self)
        self.current_names = QTableView()
        self.current_names.setModel(self.model1)

        self.model2 = QStandardItemModel(self)
        self.new_names = QTableView()
        self.new_names.setModel(self.model2)
        self.new_names.append_selected_files(indexes_list)

        self.cancel_button = QPushButton()
        self.cancel_button.setObjectName("cancel")
        self.cancel_button.setText("Cancel")

        self.rename_button = QPushButton()
        self.rename_button.setObjectName("rename")
        self.rename_button.setText("Rename")

        self.panel_1 = QWidget()
        self.panel_h_layout1 = QVBoxLayout()
        self.panel_h_layout1.addWidget(self.names)
        self.panel_h_layout1.addWidget(self.current_names_label)
        self.panel_h_layout1.addWidget(self.current_names)
        self.panel_h_layout1.addWidget(self.cancel_button)

        self.panel_2 = QWidget()
        self.panel_h_layout2 = QVBoxLayout()
        self.panel_h_layout2.addWidget(self.extension)
        self.panel_h_layout2.addWidget(self.new_names_label)
        self.panel_h_layout2.addWidget(self.new_names)
        self.panel_h_layout2.addWidget(self.rename_button)

        self.panel_1.setLayout(self.panel_h_layout1)
        self.panel_2.setLayout(self.panel_h_layout2)

        self.panel_splitter.addWidget(self.panel_1)
        self.panel_splitter.addWidget(self.panel_2)

        self.setWidget(self.panel_splitter)

        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

    def append_selected_files(self, indexes_list):
        for index in indexes_list:
            self.new_names.model().appendRow(index)

app = QtGui.QApplication(sys.argv)
form = FilesRenameUI()
form.show()
app.exec_()
	