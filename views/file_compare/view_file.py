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

		self.menubar = self.menuBar()
		self.file_menu = self.menubar.addMenu('&File')
		self.file_menu.addAction(self.save_action)
		self.file_menu.addAction(self.open_action)

	def save_file(self):
		"""Save the current file and update selected_file and current_file variables"""

		f = open(self.current_file, 'w')
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
