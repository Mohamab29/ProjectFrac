from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDesktopWidget, QFrame
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_MainWindow
from PIL import Image


def changeButtonToDisableStyle(btn):
    btn.setStyleSheet("QPushButton {\n"
                      "    color: rgb(100, 100, 100);\n"
                      "}\n"
                      "QPushButton:hover {\n"
                      "    color: rgb(85, 170, 255);\n"
                      "}")


def changeButtonToEnableStyle(btn):
    btn.setStyleSheet("QPushButton {\n"
                      "    color: rgb(200, 200, 200);\n"
                      "}\n"
                      "QPushButton:hover {\n"
                      "    color: rgb(85, 170, 255);\n"
                      "}")


def toggleButtonAndChangeStyle(btn, term):
    if not term:
        btn.setEnabled(False)
        changeButtonToDisableStyle(btn)
    elif term:
        btn.setEnabled(True)
        changeButtonToEnableStyle(btn)


def setListItemItemStyle(item):
    font = QtGui.QFont()
    font.setBold(True)
    font.setWeight(75)
    item.setFont(font)
    brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
    brush.setStyle(QtCore.Qt.NoBrush)
    item.setForeground(brush)


def openImage(path):
    image = Image.open(path, 'r')
    image.show()


def showDialog(title, message):
    msg_box = QMessageBox()

    msg_box.setIcon(QMessageBox.Information)
    msg_box.setText(message)
    msg_box.setWindowTitle(title)
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    qr = msg_box.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    msg_box.move(qr.center())

    return_value = msg_box.exec()
    if return_value == QMessageBox.Ok:
        return True
    else:
        return False


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.animation = QtCore.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.imageListPathDict = {}
        self.setActions()
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setActions(self):
        self.ui.btn_page_predict.clicked.connect(self.evnPage1BtnClicked)
        self.ui.btn_page_results.clicked.connect(self.evnPageResultsClicked)
        self.ui.btn_Toggle.clicked.connect(self.evnBtnToggleClicked)
        self.ui.btn_load_images.clicked.connect(self.evnLoadImagesButtonClicked)
        self.ui.btn_clear_images.clicked.connect(self.evnClearImagesButtonClicked)
        self.ui.images_import_list.itemClicked.connect(self.evnImageListItemClicked)
        self.ui.images_import_list.itemDoubleClicked.connect(self.evnImageListItemDoubleClicked)
        self.ui.btn_check_all.clicked.connect(self.evnCheckAllButtonClicked)
        self.ui.btn_uncheck_all.clicked.connect(self.evnUncheckAllButtonClicked)
        self.ui.images_import_list.currentItemChanged.connect(self.evnCurrentItemChanged)
        self.ui.btn_delete_selected_images.clicked.connect(self.evnDeleteSelectedImagesButtonClicked)
        self.ui.btn_predict.clicked.connect(self.evnPredictButtonClicked)

    def evnPredictButtonClicked(self):
        checked_items = []

        for index in range(self.ui.images_import_list.count()):
            if self.ui.images_import_list.item(index).checkState() == 2:
                list_item = self.ui.images_import_list.item(index)
                checked_items.append(self.imageListPathDict[list_item.text()])

        # test(checked_items)

    def imageLabelFrame(self, frame1, frame2, lineWidth):
        self.ui.label_selected_picture.setFrameShape(frame1)
        self.ui.label_selected_picture.setFrameShadow(frame2)
        self.ui.label_selected_picture.setLineWidth(lineWidth)

    def evnCurrentItemChanged(self, item):
        if item:
            self.ui.label_selected_picture.setPixmap(QtGui.QPixmap(self.imageListPathDict[item.text()]))
            self.imageLabelFrame(QFrame.StyledPanel, QFrame.Sunken, 3)

    def sharedTerms(self):
        self.updateNumOfImages()

        if not self.isAtLeastOneItemChecked():
            toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, False)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, True)

        if self.isAtLeastOneItemNotChecked():
            toggleButtonAndChangeStyle(self.ui.btn_check_all, True)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_check_all, False)

        if self.numOfCheckedItems():
            toggleButtonAndChangeStyle(self.ui.btn_predict, True)
            toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, True)

        else:
            toggleButtonAndChangeStyle(self.ui.btn_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, False)

    def evnImageListItemClicked(self):
        self.sharedTerms()

    def evnImageListItemDoubleClicked(self, item):
        openImage(self.imageListPathDict[item.text()])

    def evnPage1BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.main_page_predict)

    def evnPageResultsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_results)

    def evnBtnToggleClicked(self):
        self.toggleMenu(250, True)

    def toggleMenu(self, maxWidth, enable):
        if enable:
            # GET WIDTH
            width = self.ui.frame_left_menu.width()
            max_extend = maxWidth
            standard = 100

            # SET MAX WIDTH
            if width == 100:
                width_extended = max_extend
            else:
                width_extended = standard

            # ANIMATION
            self.animation.setDuration(400)
            self.animation.setStartValue(width)
            self.animation.setEndValue(width_extended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def evnLoadImagesButtonClicked(self):
        file_to_open = "Image Files (*.png *.jpg *.bmp)"
        # QFileDialog also have getSaveFileName,getSaveFileNames (with s) and more...
        res = QFileDialog.getOpenFileNames(None, "Open File", "/", file_to_open)

        if len(res[0]) > 0:
            self.renderInputPictureList(res[0])

    def renderInputPictureList(self, pictures_input_path):
        for i in range(len(pictures_input_path)):
            if pictures_input_path[i].split('/')[-1] not in self.imageListPathDict:
                self.imageListPathDict[pictures_input_path[i].split('/')[-1]] = pictures_input_path[i]
                list_item = QtWidgets.QListWidgetItem()
                list_item.setCheckState(QtCore.Qt.Checked)
                list_item.setText(pictures_input_path[i].split('/')[-1])
                setListItemItemStyle(list_item)
                self.ui.images_import_list.addItem(list_item)
                toggleButtonAndChangeStyle(self.ui.btn_predict, True)
                toggleButtonAndChangeStyle(self.ui.btn_clear_images, True)
                toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, True)
                toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, True)

        if len(self.ui.images_import_list.selectedItems()) == 0:
            self.imageLabelFrame(0, 0, 0)
            self.ui.label_selected_picture.setText("Please select image to view on the screen.")

        self.updateNumOfImages()

    def evnDeleteSelectedImagesButtonClicked(self):
        checked_items = []

        if showDialog('Delete the selected images', 'Are you sure?'):
            for index in range(self.ui.images_import_list.count()):
                if self.ui.images_import_list.item(index).checkState() == 2:
                    list_item = self.ui.images_import_list.item(index)
                    checked_items.append(list_item)

            for item in checked_items:
                self.ui.images_import_list.takeItem(self.ui.images_import_list.row(item))
                self.imageListPathDict.pop(item.text())

            self.sharedTerms()

            if not len(self.ui.images_import_list):
                self.ui.label_selected_picture.setText("Please load and select image.")
                self.imageLabelFrame(0, 0, 0)
                toggleButtonAndChangeStyle(self.ui.btn_clear_images, False)

    def evnClearImagesButtonClicked(self):
        if self.imageListPathDict and showDialog('Clear all images', 'Are you sure?'):
            self.ui.btn_clear_images.setEnabled(False)
            self.ui.images_import_list.clear()
            self.imageListPathDict = {}
            self.imageLabelFrame(0, 0, 0)
            self.ui.label_selected_picture.setText("Please load and select image.")
            changeButtonToDisableStyle(self.ui.btn_clear_images)
            toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, False)
            self.updateNumOfImages()

    def evnCheckAllButtonClicked(self):
        if showDialog('Check all images', 'Are you sure?'):
            for index in range(self.ui.images_import_list.count()):
                if self.ui.images_import_list.item(index).checkState() == 0:
                    self.ui.images_import_list.item(index).setCheckState(2)
            toggleButtonAndChangeStyle(self.ui.btn_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_predict, True)
            toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, True)
            self.updateNumOfImages()

    def evnUncheckAllButtonClicked(self):
        if showDialog('Uncheck all images', 'Are you sure?'):
            for index in range(self.ui.images_import_list.count()):
                if self.ui.images_import_list.item(index).checkState() == 2:
                    self.ui.images_import_list.item(index).setCheckState(0)

            toggleButtonAndChangeStyle(self.ui.btn_check_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_delete_selected_images, False)
            self.updateNumOfImages()

    def updateNumOfImages(self):
        self.ui.label_images.setText(
            f"Images: {self.ui.images_import_list.count()} Checked: {self.numOfCheckedItems()}")

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

    def numOfCheckedItems(self):
        counter = 0
        for index in range(self.ui.images_import_list.count()):
            if self.ui.images_import_list.item(index).checkState() == 2:
                counter = counter + 1
        return counter


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
