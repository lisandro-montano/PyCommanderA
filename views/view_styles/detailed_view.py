
from PyQt4 import QtGui
from PyQt4 import QtCore

from views.view_styles.list_view import ListView

class DetailedView(ListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(DetailedView, self).__init__(currentPath)