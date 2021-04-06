from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog,QMessageBox,QDesktopWidget,QFrame
from ui_functions import *
import sys
import subprocess
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main2 import Ui_MainWindow
from dialog import Ui_Dialog
from PIL import Image


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.imageListPathDict = {}
        self.setActions()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setActions(self):
        self.ui.btn_page_1.clicked.connect(self.evnPage1BtnClicked)
        self.ui.btn_page_2.clicked.connect(self.evnPage2BtnClicked)
        self.ui.btn_page_3.clicked.connect(self.evnPage3BtnClicked)
        self.ui.btn_Toggle.clicked.connect(self.evnBtnToggleClicked)
        self.ui.btn_load_images.clicked.connect(self.evnLoadImagesButtonClicked)
        self.ui.btn_clear_images.clicked.connect(self.evnClearImagesButtonClicked)
        self.ui.images_import_list.itemClicked.connect(self.evnImageListItemClicked)
        self.ui.images_import_list.itemDoubleClicked.connect(self.evnImageListItemDoubleClicked)


    def imageLabelFrame(self,frame1,frame2,lineWidth):
        self.ui.label_selected_picture.setFrameShape(frame1)
        self.ui.label_selected_picture.setFrameShadow(frame2)
        self.ui.label_selected_picture.setLineWidth(lineWidth)
    

    def evnImageListItemClicked(self, item):
        self.ui.label_selected_picture.setPixmap(QtGui.QPixmap(self.imageListPathDict[item.text()]))
        self.imageLabelFrame(QFrame.StyledPanel,QFrame.Sunken,3)
        
        if not self.isAtLeastOneItemChecked():
            self.toggleButtonAndChangeStyle(self.ui.btn_uncheck_all,False)
        else:
            self.toggleButtonAndChangeStyle(self.ui.btn_uncheck_all,True)

        if self.isAtLeastOneItemNotChecked():
            self.toggleButtonAndChangeStyle(self.ui.btn_check_all,True)
        else:
            self.toggleButtonAndChangeStyle(self.ui.btn_check_all,False)


    def evnImageListItemDoubleClicked(self, item):
        self.openImage(self.imageListPathDict[item.text()])

    def evnPage1BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_1)

    def evnPage2BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)

    def evnPage3BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)

    def evnBtnToggleClicked(self):
        UIFunctions.toggleMenu(self, 250, True)

    def evnLoadImagesButtonClicked(self):
        fileToOpen = "Image Files (*.png *.jpg *.bmp)"
        # QFileDialog also have getSaveFileName,getSaveFileNames (with s) and more...
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", fileToOpen)

        if (len(res[0]) > 0):
            # self.ui.label_selected_picture.setText("Please select image.")
            self.ui.btn_clear_images.setEnabled(True)
            self.changeButtonToEnableStyle(self.ui.btn_clear_images)
            self.renderInputPictureList(res[0])



    def evnClearImagesButtonClicked(self):
        if(self.imageListPathDict and self.showDialog('Are you sure?')):
            self.ui.btn_clear_images.setEnabled(False)
            self.ui.images_import_list.clear()
            self.imageListPathDict = {}
            self.ui.label_images.setText(f"Images: {self.ui.images_import_list.count()}")
            self.imageLabelFrame(0,0,0)
            self.ui.label_selected_picture.setText("Please load and select image.")
            self.changeButtonToDisableStyle(self.ui.btn_clear_images)


        self.toggleButtonAndChangeStyle(self.ui.btn_uncheck_all,False)


        
    def showDialog(self, message):
        msgBox = QMessageBox()
        
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText(message)
        msgBox.setWindowTitle("Clear all images")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        qr = msgBox.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        msgBox.move(qr.center())

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            return True
        else: return False

    def openImage(self, path):
        image = Image.open(path, 'r')
        image.show()

    def renderInputPictureList(self, pictures_input_path):
        for i in range(len(pictures_input_path)):
            if pictures_input_path[i].split('/')[-1] not in self.imageListPathDict:
                self.imageListPathDict[pictures_input_path[i].split('/')[-1]] = pictures_input_path[i]
                listItem = QtWidgets.QListWidgetItem()
                listItem.setCheckState(QtCore.Qt.Checked)
                listItem.setText(pictures_input_path[i].split('/')[-1])
                self.setListItemItemStyle(listItem)
                self.ui.images_import_list.addItem(listItem)
        self.ui.label_images.setText(f"Images: {self.ui.images_import_list.count()}")

        self.toggleButtonAndChangeStyle(self.ui.btn_uncheck_all,True)


    def setListItemItemStyle(self, item):
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)


    def isAtLeastOneItemChecked(self):
        for index in range(self.ui.images_import_list.count()):
            if self.ui.images_import_list.item(index).checkState() == 2:
                return True
        return False

    def isAtLeastOneItemNotChecked(self):
        for index in range(self.ui.images_import_list.count()):
            if self.ui.images_import_list.item(index).checkState() == 0:
                return True
        return False

    def isNoItemChecked(self):
        for index in range(self.ui.images_import_list.count()):
            if self.ui.images_import_list.item(index).checkState() == 2:
                return False
        return True

    def changeButtonToEnableStyle(self,btn):
       btn.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(160, 160, 160);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(85, 170, 255);\n"
                                        "}")
    def changeButtonToDisableStyle(self,btn):
       btn.setStyleSheet("QPushButton {\n"
                                        "    color: rgb(100, 100, 100);\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    color: rgb(85, 170, 255);\n"
                                        "}")


    def toggleButtonAndChangeStyle(self,btn,term):
        if(not term):
            btn.setEnabled(False)
            self.changeButtonToDisableStyle(btn)
        elif(term):
            btn.setEnabled(True)
            self.changeButtonToEnableStyle(btn)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
