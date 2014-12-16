import difflib

from PyQt4 import QtGui
from PyQt4 import QtCore
from views.file_compare.view_file import ViewFile

RED_COLOR = "red"
GREEN_COLOR = "green"

class FileCompareUI(QtGui.QMainWindow):

	def __init__(self, left_files_list, right_files_list):
		"""Initializes and creates the UI components for file comparison window

		Params:
		left_files_list  : list of files selected on the left panel
		right_files_list : list of files selected on the right panel

		The first available file will be selected, if none is encountered, an error message
		is displayed and compare window is closed
		"""
		super(FileCompareUI, self).__init__()
		self.init_ui()
		self.get_items(left_files_list, right_files_list)
		self.create_panels()
		self.create_buttons_bar()
		self.setCentralWidget(self.compare_panels)
		self.addDockWidget(QtCore.Qt.DockWidgetArea(8), self.buttons_container)
		self.show()
		self.connect(self.compare_button, QtCore.SIGNAL('clicked()'), 
					 self.compare_files)
		self.connect(self.reload_button, QtCore.SIGNAL('clicked()'), 
					 self.reload_files)

	def init_ui(self):
		"""Initializes the UI for File Comparison Window"""

		palette = QtGui.QPalette()
		palette.setColor(QtGui.QPalette.Background,QtCore.Qt.gray)

		self.setPalette(palette)
		self.setFixedSize(1200, 600)
		self.setWindowTitle('PyCompareA')

	def get_items(self, left_files_list, right_files_list):
		"""Goes through all available items and picks the first file of each panel,
		if no file is found in any panel, the comparison is stopped and panel closed
		"""

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
		self.compare_panels.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

	def create_buttons_bar(self):
		"""Create buttons to run comparison again or to reload current files and discard changes"""

		self.buttons_container = QtGui.QDockWidget()
		self.buttons_bar = QtGui.QWidget()
		self.buttons_layout = QtGui.QHBoxLayout()
		self.compare_button = QtGui.QPushButton("F3 - Compare")
		self.compare_button.setShortcut(QtCore.Qt.Key_F3)
		self.reload_button = QtGui.QPushButton("Reload Files")
		self.buttons_layout.addWidget(self.compare_button)
		self.buttons_layout.addWidget(self.reload_button)
		self.buttons_bar.setLayout(self.buttons_layout)
		self.buttons_container.setWidget(self.buttons_bar)
		self.buttons_container.setFeatures(QtGui.QDockWidget.NoDockWidgetFeatures)

	def compare_files(self):
		"""Runs the comparison between panels using difflib functionalities

		Result is analyzed, highlighted and posted in the right panel to denote the differences
		Red is used for extra lines and green is used for the ones that need to be addDockWidget
		- symbol is shown in front of extra lines and + symbol in front of missing ones
		"""

		self.right_compare_panel.remove_highlight()
		self.current_left_array = []
		self.current_right_array = []
		self.current_left_text = ""
		self.current_right_text = ""
		self.current_left_text = self.left_compare_panel.view_file.toPlainText()
		self.current_right_text = self.right_compare_panel.view_file.toPlainText()
		for line in self.current_left_text.split('\n'):
			self.current_left_array.append(str(line))
		for line in self.current_right_text.split('\n'):
			if str(line).startswith("- ") or str(line).startswith("+ ") or str(line).startswith("  "):
				line.replace(line[:2], '')
			self.current_right_array.append(str(line))

		d = difflib.Differ()
		self.compare_result = list(d.compare(self.current_right_array, self.current_left_array))
		self.remove_question_marks()
		self.compare_result_string = '\n'.join(self.compare_result)
		self.right_compare_panel.view_file.setText(self.compare_result_string)
		for line in self.compare_result:
			if line.startswith("- "):
				self.right_compare_panel.highlight_section(line, RED_COLOR)
			if line.startswith("+ "):
				self.right_compare_panel.highlight_section(line, GREEN_COLOR)

	def remove_question_marks(self):
		"""difflib creates extra lines with ? at the beggining when remove and add operations are 
		required simultaneously. This section will be removed because it is not required and can 
		be confusing for the final user
		"""
		
		for line in self.compare_result:
			if line.startswith("? "):
				self.compare_result.remove(line)

	def reload_files(self):
		"""Function to reload current files and remove highlighted parts in order to 
		start new comparisons
		"""

		self.left_compare_panel.view_file.setText(self.left_compare_panel.selected_file)
		self.right_compare_panel.view_file.setText(self.right_compare_panel.selected_file)
		self.left_compare_panel.file_name.setText(self.left_compare_panel.current_file)
		self.right_compare_panel.file_name.setText(self.right_compare_panel.current_file)
		self.left_compare_panel.remove_highlight()
		self.right_compare_panel.remove_highlight()
	