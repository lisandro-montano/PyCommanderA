import os

from PyQt4 import QtGui
from PyQt4 import QtCore

class ViewFile(QtGui.QMainWindow):

	def __init__(self, file_to_open):
		"""Initializes and opens the file in the panel"""
		super(ViewFile, self).__init__()
		self.selected_file = open(file_to_open).read()
		self.current_file = file_to_open
		self.create_menubar()

		self.view_file = QtGui.QTextEdit(self)
		self.view_file.setText(self.selected_file)
		self.setCentralWidget(self.view_file)
		self.compare_files()

	def create_menubar(self):
		save_action = QtGui.QAction('Save', self)
		save_action.setShortcut('Ctrl+S')
		save_action.setStatusTip('Save current file')
		save_action.triggered.connect(self.save_file)

		menubar = self.menuBar()
		file_menu = menubar.addMenu('&File')
		file_menu.addAction(save_action)

	def save_file(self):
		f = open(self.current_file, 'w')
		filedata = self.view_file.toPlainText()
		f.write(filedata)
		f.close()

	def compare_files(self):
		cursor = self.view_file.textCursor()
		# Setup the desired format for matches
		format = QtGui.QTextCharFormat()
		format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
		# Setup the regex engine
		pattern = "PyCommander"
		regex = QtCore.QRegExp(pattern)
		# Process the displayed document
		pos = 0
		index = regex.indexIn(self.view_file.toPlainText(), pos)
		while (index != -1):
			# Select the matched text and apply the desired format
			cursor.setPosition(index)
			cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
			cursor.mergeCharFormat(format)
			# Move to the next match
			pos = index + regex.matchedLength()
			index = regex.indexIn(self.view_file.toPlainText(), pos)
		
        