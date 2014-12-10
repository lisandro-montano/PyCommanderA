from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelToolbar(QtGui.QWidget):
	def __init__(self, current_path):
		"""Create panel toolbar including:
		- Combo box to list computer drives depending on the OS
		- Editable line to allow user to modify the path through the keyboard

		Params:
		- current_path: receives the path to be set as current e.g. "C:\" and defaults it
		in the combo box and path_edit
		"""
		super(PanelToolbar, self).__init__()
		self._observers = []
		self.dir_combo = self.get_volume_list()
		self.path_edit = QtGui.QLineEdit(self)
		self.path_edit.setText(current_path)
		self.configure_toolbar()

		#Signal that detects changes in combo box
		self.connect(self.dir_combo, QtCore.SIGNAL('currentIndexChanged(const QString &)'),
					 self.propagate_dir)

		#Signal that detects changes in path field
		self.connect(self.path_edit, QtCore.SIGNAL('returnPressed()'), 
					 self.propagate_dir)

	def configure_toolbar(self):
		"""Configures combo box and path editable field in QVBoxLayout
		to display it on top of panel
		"""

		self.panel_bar_layout = QtGui.QVBoxLayout()
		self.panel_bar_layout.addWidget(self.dir_combo)
		self.panel_bar_layout.addWidget(self.path_edit)
		self.setLayout(self.panel_bar_layout)
		self.dir_combo.setFocusPolicy(QtCore.Qt.NoFocus)
		self.path_edit.setFocusPolicy(QtCore.Qt.ClickFocus)

	def get_volume_list(self):
		"""Obtain volumes list from computer and add them to combo box"""
		dir_combo = QtGui.QComboBox(self)
		volumes_list = QtCore.QDir.drives()
		for x in xrange(len(volumes_list)):
			dir_combo.addItem(volumes_list[x].absolutePath())
		dir_combo.setFixedWidth(60)
		return dir_combo

	def attach(self, observer):
		"""Attach observers to detect directory/path changes"""
		if not observer in self._observers:
			self._observers.append(observer)

	def propagate_dir(self, new_dir = ""):
		"""Inform observers about changes in directory path
		If path is not retrieved, get the one from the Path field

		Params:
		- new_dir: modified path obtained from combo box, path_edit or panel in order
		to modify current panel list of items e.g "/Users" "C:\Users"
		"""
		if new_dir == "":
			new_dir = self.path_edit.text()
		#Detect if path_edit is properly finished in order to avoid problems while moving
		#or copying items 
		if new_dir[-1] != "/" and new_dir[-1] != "'\'":
			new_dir = new_dir + "/"
		
		for panel_observer in self._observers:
			panel_observer.propagate_dir(new_dir)

	def update_path(self, new_path):
		"""Update path in the toolbar when changed
		- Update combo box drive if changed from path field
		- Update path field if changed from combo box or panel

		Params:
		- new_path: modified path obtained from combo box, path_edit or panel in order
		to modify current panel list of items e.g "/Users" "C:\Users"
		"""
		self.path_edit.setText(new_path)
		new_path_dir = new_path[0] + ":/"
		if new_path_dir != self.dir_combo.currentText():
			combo_current_index = self.dir_combo.findText(new_path_dir)
			self.dir_combo.setCurrentIndex(combo_current_index)
			

