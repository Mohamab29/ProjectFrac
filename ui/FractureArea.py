import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog
from Ui_FractureArea import Ui_FractureArea
from PyQt5 import QtCore, QtGui, QtWidgets

class FractureArea():
    def __init__(self):
        self.mainWindow = QMainWindow()
        self.ui = Ui_FractureArea()
        self.ui.setupUi(self.mainWindow)
        self.setActions()

    def setActions(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)
        self.ui.homeButton.clicked.connect(self.evnHomeBtnClicked)
        self.ui.page1Button.clicked.connect(self.evnPage1BtnClicked)
        self.ui.page2Button.clicked.connect(self.evnPage2BtnClicked)
        self.ui.page3Button.clicked.connect(self.evnPage3BtnClicked)
        self.ui.loadImagesButton.clicked.connect(self.evnLoadImagesButtonClicked)

    def show(self):
        self.mainWindow.show()

    def evnHomeBtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.home)

    def evnPage1BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page1)

    def evnPage2BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page2)

    def evnPage3BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page3)
    
    def evnLoadImagesButtonClicked(self):
        fileToOpen = "Image Files (*.png *.jpg *.bmp)"
        # QFileDialog also have getSaveFileName,getSaveFileNames (with s) and more...
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", fileToOpen)
        print(res[0])

        # self.label10 = QtWidgets.QLabel(self.ui.page1)
        # self.label10.setPixmap(QtGui.QPixmap("/home/vladis/1.png"))
      


if __name__ == '__main__':
  app = QApplication(sys.argv)
  mainWindow = FractureArea()
  mainWindow.show()
  sys.exit(app.exec_())