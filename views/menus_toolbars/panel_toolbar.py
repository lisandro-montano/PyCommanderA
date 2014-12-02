from PyQt4 import QtGui
from PyQt4 import QtCore

class PanelToolbar(QtGui.QWidget):
	def __init__(self, current_path):
		"""Create panel toolbar including:
		- Combo box to list computer drives depending on the OS
		- Editable line to allow user to modify the path through the keyboard
		"""
		super(PanelToolbar, self).__init__()
		self._observers = []

		self.dir_combo = self.get_volume_list()

		self.path_edit = QtGui.QLineEdit(self)
		self.path_edit.setText(current_path)

		self.panel_bar_layout = QtGui.QVBoxLayout()
		self.panel_bar_layout.addWidget(self.dir_combo)
		self.panel_bar_layout.addWidget(self.path_edit)
		self.setLayout(self.panel_bar_layout)
		self.dir_combo.setFocusPolicy(QtCore.Qt.NoFocus)
		self.path_edit.setFocusPolicy(QtCore.Qt.ClickFocus)

		#Signal that detects changes in combo box
		self.connect(self.dir_combo, QtCore.SIGNAL('currentIndexChanged(const QString &)'),
					 self.propagate_dir)

		#Signal that detects changes in path field
		self.connect(self.path_edit, QtCore.SIGNAL('returnPressed()'), 
					 self.propagate_dir)

	def get_volume_list(self):
		"""Obtain volumes list and add them to combo box"""
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
		"""
		if new_dir == "":
			new_dir = self.path_edit.text()
		for panel_observer in self._observers:
			panel_observer.propagate_dir(new_dir)

	def update_path(self, new_path):
		"""Update path in the toolbar when changed
		- Update combo box drive if changed from path field
		- Update path field if changed from combo box or panel
		"""
		self.path_edit.setText(new_path)
