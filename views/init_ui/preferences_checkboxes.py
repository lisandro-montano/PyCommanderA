from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import QSettings

#class CheckBox(QtGui.QWidget):
class PreferencesCheckboxes(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        """In this interface the user can set the view preferences as listView or detailedView

		Params:
		- parent: receives the parent reference
		"""
        super(PreferencesCheckboxes, self).__init__(parent)

        self.options_section = QtGui.QDockWidget()
        self.options_container =QtGui.QWidget()
        self.options_layout = QtGui.QVBoxLayout()

        self.detailed_view = QtGui.QCheckBox('Detailed View', self)
        self.list_view = QtGui.QCheckBox('List View', self)
        
        self.checkbox1 = QtGui.QCheckBox('Extension', self)
        self.checkbox2 = QtGui.QCheckBox('Size', self)
        self.checkbox3 = QtGui.QCheckBox('Date', self)

        button_ok = QtGui.QPushButton('OK', self)
        button_cancel = QtGui.QPushButton('Cancel', self)

        #Button Events
        button_cancel.clicked.connect(self.close)
        button_ok.clicked.connect(self.save_preferences)

        self.buttons_container =QtGui.QWidget()
        self.buttons_layout = QtGui.QHBoxLayout()
        self.buttons_layout.addWidget(button_ok)
        self.buttons_layout.addWidget(button_cancel)
        self.buttons_container.setLayout(self.buttons_layout)

        self.options_layout.addWidget(self.list_view)
        self.options_layout.addWidget(self.detailed_view)
        self.options_layout.addWidget(self.checkbox1)
        self.options_layout.addWidget(self.checkbox2)
        self.options_layout.addWidget(self.checkbox3)
        self.options_layout.addWidget(self.buttons_container)

        self.options_container.setLayout(self.options_layout)

        self.options_section.setWidget(self.options_container)
        self.options_section.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)
        self.setCentralWidget(self.options_section)

        #Checkbox events
        self.list_view.stateChanged.connect(self.list_view_checked)
        self.detailed_view.stateChanged.connect(self.detailed_view_checked)

        self.setFixedSize(300, 250)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Select Options')
        self.show()

    def save_preferences(self):
        """Save the user view preferences in a settings.ini file"""
        settings = QSettings('settings.ini', QtCore.QSettings.IniFormat, self)
        settings.setValue("detailed_view", self.detailed_view.isChecked())
        settings.setValue("list_view", self.list_view.isChecked())
        settings.setValue("item_extension", self.checkbox1.isChecked())
        settings.setValue("item_size", self.checkbox2.isChecked())
        settings.setValue("item_date", self.checkbox3.isChecked())
        self.close()

    def list_view_checked(self, state):
        """Based on the received state, this method sets the list and detailed view check box check or unchecked
        and enable/disable the checkboxes related to the wanted columns enabled for detailed view.

        Params:
        - state: receives the list view QEvent e.g. "QtCore.Qt.Checked"
        """
        if state == QtCore.Qt.Checked:
            self.detailed_view.setChecked(False)
            self.checkbox1.setEnabled(False)
            self.checkbox2.setEnabled(False)
            self.checkbox3.setEnabled(False)
        elif state == QtCore.Qt.Unchecked:
            self.list_view.setChecked(False)
            self.detailed_view.setChecked(True)
            self.checkbox1.setEnabled(True)
            self.checkbox2.setEnabled(True)
            self.checkbox3.setEnabled(True)

    def detailed_view_checked(self, state):
        """Based on the received state, this method sets the list and detailed view check box check or unchecked
        and enable/disable the checkboxes related to the wanted columns enabled for detailed view.

        Params:
        - state: receives the detailed view QEvent e.g. "QtCore.Qt.Checked"
        """
        if state == QtCore.Qt.Checked:
            self.list_view.setChecked(False)
            self.checkbox1.setEnabled(True)
            self.checkbox2.setEnabled(True)
            self.checkbox3.setEnabled(True)
        elif state == QtCore.Qt.Unchecked:
            self.list_view.setChecked(True)
            self.detailed_view.setChecked(False)
            self.checkbox1.setEnabled(False)
            self.checkbox2.setEnabled(False)
            self.checkbox3.setEnabled(False)