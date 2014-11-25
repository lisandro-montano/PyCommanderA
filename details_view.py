
from PyQt4 import QtGui
from PyQt4 import QtCore

from list_view import ListView

class DetailsView(ListView):

	def __init__(self):
		"""Sets the currentPath and defines the panels"""
		super(DetailsView, self).__init__(currentPath)