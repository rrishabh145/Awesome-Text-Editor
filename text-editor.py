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

        self.newAction = QtWidgets.QAction(QtGui.QIcon("icons/new.png"),"New",self)
        self.newAction.setStatusTip("Create a new document from scratch.")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        self.openAction = QtWidgets.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
        self.openAction.setStatusTip("Open existing document")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        self.saveAction = QtWidgets.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
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

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction) 
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)



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

        self.text.setTabStopWidth(33)
        self.setWindowIcon(QtWidgets.QIcon("icons/icon.png"))
        self.text.cursorPositionChanged.connect(self.cursorPosition)

    def new(self):

        spawn = Main(self)
        spawn.show()

    def open(self):

        # Get filename and show only .writer files
        self.filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.writer)")

        if self.filename:
            with open(self.filename,"rt") as file:
                    self.text.setText(file.read())

    def save(self):

        # Only open dialog if there is no filename yet
        if not self.filename:
            self.filename = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')

        # Append extension if not there yet
        if not self.filename.endswith(".writer"):
            self.filename += ".writer"

        # We just store the contents of the text file along with the
        # format in html, which Qt does in a very nice way for us
            with open(self.filename,"wt") as file:
                file.write(self.text.toHtml())

    def preview(self):

    # Open preview dialog
        preview = QtWidgets.QPrintPreviewDialog()

    # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def print(self):

        # Open printing dialog
        dialog = QtWidgets.QPrintDialog()

        if dialog.exec_() == QtWidgets.QDialog.Accepted:
            self.text.document().print_(dialog.printer())


    

    def bulletList(self):

        cursor = self.text.textCursor()

        # Insert bulleted list
        cursor.insertList(QtWidgets.QTextListFormat.ListDisc)

    def numberList(self):

        cursor = self.text.textCursor()

        # Insert list with numbers
        cursor.insertList(QtWidgets.QTextListFormat.ListDecimal)

    def cursorPosition(self):

        cursor = self.text.textCursor()

        # Mortals like 1-indexed things
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusbar.showMessage("Line: {} | Column: {}".format(line,col))
        
    def main():

        app = QtWidgets.QApplication(sys.argv)

        main = Main()
        main.show()

        sys.exit(app.exec_())

    if __name__ == "__main__":
        main()