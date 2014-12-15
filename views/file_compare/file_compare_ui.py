from PyQt4 import QtGui
from PyQt4 import QtCore
from views.file_compare.view_file import ViewFile

class FileCompareUI(QtGui.QMainWindow):

	def __init__(self, left_files_list, right_files_list):
		"""Initializes and creates the UI components for file comparison window"""
		super(FileCompareUI, self).__init__()
		self.init_ui()
		self.get_items(left_files_list, right_files_list)
		self.create_panels()
		#self.compare_buttons()
		self.setCentralWidget(self.compare_panels)
		#self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.compare_buttons)
		self.show()

	def init_ui(self):
		"""Initializes the UI for File Comparison Window"""
		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.setPalette(palette)
		self.setFixedSize(1200, 600)
		self.setWindowTitle('PyCompareA')

	def get_items(self, left_files_list, right_files_list):
		self.left_file = ""
		self.right_file = ""
		for item_path, item_name, item_type in left_files_list:
			if item_type == "File":
				self.left_file = item_path
				break

		for item_path, item_name, item_type in right_files_list:
			if item_type == "File":
				self.right_file = item_path
				break

		if self.left_file == "" or self.right_file == "":
			reply = QtGui.QMessageBox.question(self, "PyCompareA",
            	  	"You haven't selected any file in one or both panels, please select again\n", 
              		QtGui.QMessageBox.Ok, QtGui.QMessageBox.Ok)
			if reply == QtGui.QMessageBox.Ok:
				self.close()

	def create_panels(self):
		"""Draws both panels for file comparison"""
		self.compare_panels = QtGui.QDockWidget()
		self.panel_container =QtGui.QWidget()
		self.panel_layout = QtGui.QHBoxLayout()	

		self.left_compare_panel = ViewFile(self.left_file)
		self.right_compare_panel = ViewFile(self.right_file)
		
		self.panel_layout.addWidget(self.left_compare_panel)
		self.panel_layout.addWidget(self.right_compare_panel)
		self.panel_container.setLayout(self.panel_layout)

		self.compare_panels.setWidget(self.panel_container)
		