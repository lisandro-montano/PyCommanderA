import sys

from PyQt4 import QtGui
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QVBoxLayout, QWidget, QPushButton, QTextEdit, QDockWidget


class FilesRenameUI(QDockWidget):
    def __init__(self):
        super(FilesRenameUI, self).__init__()

        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle('Rename multiple files')
        self.panel_splitter = QtGui.QSplitter()

        self.current_names_label = QtGui.QLabel("Current items name")
        self.new_names_label = QtGui.QLabel("New items name")

        self.current_names = QTextEdit()
        self.current_names.setObjectName("Current selected items name")
        self.current_names.setText("Current names")

        self.new_names = QTextEdit()
        self.new_names.setObjectName("New selected items name")
        self.new_names.setText("New names")

        self.cancel_button = QPushButton()
        self.cancel_button.setObjectName("cancel")
        self.cancel_button.setText("Cancel")

        self.rename_button = QPushButton()
        self.rename_button.setObjectName("rename")
        self.rename_button.setText("Rename")

        self.panel_1 = QWidget()
        self.panel_h_layout1 = QVBoxLayout()
        self.panel_h_layout1.addWidget(self.current_names_label)
        self.panel_h_layout1.addWidget(self.current_names)
        self.panel_h_layout1.addWidget(self.cancel_button)

        self.panel_2 = QWidget()
        self.panel_h_layout2 = QVBoxLayout()
        self.panel_h_layout2.addWidget(self.new_names_label)
        self.panel_h_layout2.addWidget(self.new_names)
        self.panel_h_layout2.addWidget(self.rename_button)

        self.panel_1.setLayout(self.panel_h_layout1)
        self.panel_2.setLayout(self.panel_h_layout2)

        self.panel_splitter.addWidget(self.panel_1)
        self.panel_splitter.addWidget(self.panel_2)

        self.setWidget(self.panel_splitter)

        self.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

app = QtGui.QApplication(sys.argv)
form = FilesRenameUI()
form.show()
app.exec_()
	