import os

from PyQt4 import QtGui
from PyQt4 import QtCore

class ViewFile(QtGui.QMainWindow):

	def __init__(self, file_to_open):
		"""Initializes and opens the file in the panel

		Params:
		file_to_open : file that will be opened in this panel e.g. E:\Test.text
		current_file : created to save the full path of current opened file_name
		selected_file: created to save the content of the file opened
		"""
		super(ViewFile, self).__init__()
		self.selected_file = open(file_to_open).read()
		self.current_file = file_to_open
		self.create_menubar()

		self.file_name = QtGui.QLabel(self.current_file)
		self.view_file = QtGui.QTextEdit(self)
		self.view_file.setText(self.selected_file)

		self.panel_layout = QtGui.QVBoxLayout()
		self.panel_layout.addWidget(self.file_name)
		self.panel_layout.addWidget(self.view_file)
		self.panel_container = QtGui.QWidget()
		self.panel_container.setLayout(self.panel_layout)
		self.setCentralWidget(self.panel_container)
		
	def create_menubar(self):
		"""Create a menubar with save and open options for each panel"""

		self.save_action = QtGui.QAction('Save', self)
		self.save_action.setStatusTip('Save current file')
		self.save_action.triggered.connect(self.save_file)

		self.open_action = QtGui.QAction('Open', self)
		self.open_action.setStatusTip('Open a new file')
		self.open_action.triggered.connect(self.open_file)

		self.save_as_action = QtGui.QAction('Save As', self)
		self.save_as_action.setStatusTip('Save file with a different name')
		self.save_as_action.triggered.connect(self.save_as_dialog)

		self.menubar = self.menuBar()
		self.file_menu = self.menubar.addMenu('&File')
		self.file_menu.addAction(self.open_action)
		self.file_menu.addAction(self.save_action)
		self.file_menu.addAction(self.save_as_action)

	def save_file(self):
		"""Save the current file and update selected_file and current_file variables"""

		f = open(self.current_file, 'w')
		self.verify_compare_spaces()
		self.selected_file = self.view_file.toPlainText()
		f.write(self.selected_file)
		self.view_file.setText(self.selected_file)
		f.close()


	def open_file(self):
		"""Open a new file with QFileDialog window, update selected_file and current_file 
		after selecting the new file
		"""
		
		self.new_file_name = QtGui.QFileDialog.getOpenFileName(self, 'Open file', self.current_file)

		f = open(self.new_file_name, 'r')

		with f:        
			self.selected_file = f.read()
			self.current_file = self.new_file_name
			self.file_name.setText(self.current_file)
			self.view_file.setText(self.selected_file)

	def highlight_section(self, section, color):
		"""Define the sections to be highlighted in red or green

		Params:
		section : line to be highlighted with specific color (red or green)
		color   : defines the highlight color depending on extra content or missing content
		"""
		
		cursor = self.view_file.textCursor()
		# Setup the desired format for matches
		format = QtGui.QTextCharFormat()
		if color == "red":
			format.setBackground(QtGui.QBrush(QtGui.QColor(255, 0, 0, 127)))
			regex = QtCore.QRegExp(section)
		else:
			format.setBackground(QtGui.QBrush(QtGui.QColor(0, 255, 0, 127)))
			regex = QtCore.QRegExp('\S' + section)
		# Process the displayed document
		pos = 0
		index = regex.indexIn(self.view_file.toPlainText(), pos)
		while (index != -1):
			# Select the matched text and apply the desired format
			cursor.setPosition(index)
			cursor.movePosition(QtGui.QTextCursor.EndOfLine, 1)
			cursor.mergeCharFormat(format)
			# Move to the next match
			pos = index + regex.matchedLength()
			index = regex.indexIn(self.view_file.toPlainText(), pos)

	def remove_highlight(self):
		"""Remove all background color prior to any reload or re-comparison in order
		to avoid confusion
		"""
		
		self.view_file.setTextBackgroundColor(QtGui.QColor(0, 0, 0, 0))

	def save_as_dialog(self):
		"""Save file with a different name in the same location"""

		new_full_name, ok_button_pressed = QtGui.QInputDialog.getText(self, 'Save as:', 'File name:',
                                                  QtGui.QLineEdit.Normal, self.current_file)

		#Verify if there is no file with the same introduced name in the current path
		if ok_button_pressed and os.path.isfile(new_full_name) == False:
			self.create_new_file(new_full_name)

		#if there is a file name with the same name introduced, an error message is displayed
		elif ok_button_pressed != False:
			QtGui.QMessageBox.information(self, "Error Message",
									      "There is a file with the same name. No new file was created.")

	def create_new_file(self, new_full_name):
		"""Create new file in the current path if it does not exist

		Params:
		- new_file_name: Receives the new file name
		- current_path: Receives the current panel root path
		"""
		try:
			file = open(new_full_name, 'w')
			self.verify_compare_spaces()
			self.selected_file = self.view_file.toPlainText()
			file.write(self.selected_file)
			self.view_file.setText(self.selected_file)
			self.current_file = new_full_name
			self.file_name.setText(self.current_file)
			file.close()
		except:
			QtGui.QMessageBox.information(self, "Error Message", 
										  "There was a problem creating the file. Action was not completed.")

	def verify_compare_spaces(self):
		"""In order to save changes, we need to remove indicators of comparison. 
		This function removes +, - and 2 spaces at the beginning of each line
		"""
		self.remove_spaces = []
		self.current_text = ""
		self.current_text = self.view_file.toPlainText()
		for line in self.current_text.split('\n'):
			if str(line).startswith("- ") or str(line).startswith("+ ") or str(line).startswith("  "):
				line.replace(line[:2], '')
			self.remove_spaces.append(str(line))
		self.selected_file = '\n'.join(self.remove_spaces)
		self.view_file.setText(self.selected_file)
		self.remove_highlight()
