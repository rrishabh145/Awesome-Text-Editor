import sys

#PYQT5 PyQt4’s QtGui module has been split into PyQt5’s QtGui, QtPrintSupport and QtWidgets modules

from PyQt5 import QtWidgets
#PYQT5 QAction, QMainWindow, QApplication, QTextEdit, QFileDialog, QDialog

from PyQt5 import QtPrintSupport
#PYQT5 QPrintPreviewDialog, QPrintDialog

from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt

class Main(QtWidgets.QMainWindow):

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self,parent)

        self.filename = ""

        self.initUI()
    def initToolbar(self):

        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
        self.saveAction.setStatusTip("Save document")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        self.toolbar = self.addToolBar("Options")

        self.toolbar.addAction(self.newAction)
        self.toolbar.addAction(self.openAction)
        self.toolbar.addAction(self.saveAction)

        self.toolbar.addSeparator()


        # Makes the next toolbar appear underneath this one
        self.addToolBarBreak()

    def initFormatbar(self):

        self.formatbar = self.addToolBar("Format")

    def initMenubar(self):

        menubar = self.menuBar()

        file = menubar.addMenu("File")
        edit = menubar.addMenu("Edit")
        view = menubar.addMenu("View")     

    def initUI(self):
        
        self.text = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolbar()
        self.initFormatbar()
        self.initMenubar()

        # Initialize a statusbar for the window
        self.statusbar = self.statusBar()

        # x and y coordinates on the screen, width, height
        self.setGeometry(100,100,1030,800)

        self.setWindowTitle("Awesome Text Editor")

def main():

    app = QtWidgets.QApplication(sys.argv)

    main = Main()
    main.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()