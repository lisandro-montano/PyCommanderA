import sys

from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import QSettings, QObjectCleanupHandler

from views.view_styles.list_view import ListView
from views.view_styles.icons_view import IconsView
from views.view_styles.detailed_view import DetailedView
from views.menus_toolbars.panel_toolbar import PanelToolbar

from PyQt4.QtGui import QItemDelegate, QPen, QStyle, QBrush

class PanelView(QtGui.QWidget):

	def __init__(self):
		"""Sets the current path and creates the panels with current path as initial path
		Default View = List View
		"""
		super(PanelView, self).__init__()
		self.current_path = QtCore.QDir.rootPath()
		self.LIST_VIEW = 1
		self.ICONS_VIEW = 2
		self.DETAILED_VIEW = 3
		self.user_view_preferences_list = []

		self.panel_toolbar = PanelToolbar(self.current_path)
		self.set_user_preferences()

	def set_list_type(self, type):
		"""Defines the view type
		- List view
		- Icon view
		- Detailed view
		"""
		if type == self.LIST_VIEW:
			self.panel = ListView(self.current_path)
		elif type == self.ICONS_VIEW:
			self.panel = IconsView(self.current_path)
		elif type == self.DETAILED_VIEW:
			self.panel = DetailedView(self.current_path, self.user_view_preferences_list)

	def propagate_dir(self, new_dir):
		"""Detect changes in directory/path and propagate them to proper instances
		- Updates current_path
		- Updates toolbar for proper panel
		- Updates panel view

		Params:
		- new_dir: modified path obtained from combo box, path_edit or panel in order
		to modify current panel list of items e.g "/Users" "C:\Users"
		"""
		self.current_path = new_dir
		self.panel_toolbar.update_path(self.current_path)
		self.panel.update_path(self.current_path)

	def set_user_preferences(self):
		settings = QSettings("settings.ini", QtCore.QSettings.IniFormat, self)
		settings.beginGroup("user_preferences")
		self.user_view_preferences_list.append(["list_view", settings.value("list_view","r").toBool()])
		self.user_view_preferences_list.append(["detailed_view", settings.value("detailed_view","r").toBool()])
		self.user_view_preferences_list.append(["item_extension", settings.value("item_extension","r").toBool()])
		self.user_view_preferences_list.append(["item_size", settings.value("item_size","r").toBool()])
		self.user_view_preferences_list.append(["item_date", settings.value("item_date","r").toBool()])
		settings.endGroup()

		try:
			QObjectCleanupHandler().add(self.panel_layout.layout())
		except:
			print "First time the layout is not added yet"

		self.panel_layout = QtGui.QVBoxLayout()
		self.panel_layout.addWidget(self.panel_toolbar)

		try:
			QObjectCleanupHandler().add(self.panel)
		except:
			print "First time the panel is not defined yet"

		if self.user_view_preferences_list[0][1] == True:
			self.set_list_type(self.LIST_VIEW)
		elif self.user_view_preferences_list[1][1] == True:
			self.set_list_type(self.DETAILED_VIEW)

		self.panel_layout.addWidget(self.panel)
		self.setLayout(self.panel_layout)
		self.user_view_preferences_list = []

		self.panel_toolbar.attach(self)
		self.panel.attach(self)

		# Obtaining the selected item using mouse click event
		self.panel.clicked.connect(self.panel.panel_list_selection)

		# Obtaining the selected item using mouse double click event
		self.panel.doubleClicked.connect(self.panel.update_panel_current_path)