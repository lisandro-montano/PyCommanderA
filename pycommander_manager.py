
import sys
from PyQt4 import QtGui
from pycommander_ui import PyCommanderUIGenerator

def main():
	"""Initialize application and generate UI for PyCommanderA"""

	app = QtGui.QApplication(sys.argv)

	PyCommanderA_ui = PyCommanderUIGenerator()
	PyCommanderA_ui.show()

	sys.exit(app.exec_())


if __name__ == '__main__':
    main()