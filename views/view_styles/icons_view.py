
from PyQt4 import QtGui
from PyQt4 import QtCore

from views.view_styles.list_view import ListView

class IconsView(ListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(IconsView, self).__init__(currentPath)
