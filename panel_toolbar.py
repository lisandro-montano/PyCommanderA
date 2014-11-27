from PyQt4 import QtGui
from PyQt4 import QtCore


class PanelToolbar(QtGui.QWidget):
	def __init__(self, current_path):
		"""Create panel toolbar"""
		super(PanelToolbar, self).__init__()
		self._observers = []

		self.dir_combo = self.get_volume_list()

		self.path_edit = QtGui.QLineEdit(self)
		self.path_edit.setText(current_path)

		self.panel_bar_layout = QtGui.QVBoxLayout()
		self.panel_bar_layout.addWidget(self.dir_combo)
		self.panel_bar_layout.addWidget(self.path_edit)
		self.setLayout(self.panel_bar_layout)

		self.connect(self.dir_combo, QtCore.SIGNAL('currentIndexChanged(const QString &)'),
					 self.propagate_dir)

	def get_volume_list(self):
		dir_combo = QtGui.QComboBox(self)
		volumes_list = QtCore.QDir.drives()
		for x in xrange(len(volumes_list)):
			dir_combo.addItem(volumes_list[x].absolutePath())
		dir_combo.setFixedWidth(60)
		return dir_combo

	def attach(self, observer):
		if not observer in self._observers:
			self._observers.append(observer)

	def propagate_dir(self, new_dir):
		for panel_observer in self._observers:
			panel_observer.propagate_dir(new_dir)
