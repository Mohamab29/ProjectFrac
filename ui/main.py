from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QDesktopWidget, QFrame
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_main import Ui_MainWindow
from PIL import Image
from functools import partial


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


def isAtLeastOneItemChecked(list):
    for index in range(list.count()):
        if list.item(index).checkState() == 2:
            return True
    return False


def isAtLeastOneItemNotChecked(list):
    for index in range(list.count()):
        if list.item(index).checkState() == 0:
            return True
    return False


def isNoItemChecked(list):
    for index in range(list.count()):
        if list.item(index).checkState() == 2:
            return False
    return True


def numOfCheckedItems(list):
    counter = 0
    for index in range(list.count()):
        if list.item(index).checkState() == 2:
            counter = counter + 1
    return counter


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.animation = QtCore.QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.imageListPathDict = {}
        self.predictedImageListPathDict = {}
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
        self.ui.btn_toggle.clicked.connect(self.evnBtnToggleClicked)

        self.ui.btn_predict_page_load_images.clicked.connect(self.evnLoadImagesButtonClicked)
        self.ui.btn_predict_page_clear_images.clicked.connect(self.evnClearImagesButtonClickedPagePredict)
        self.ui.btn_predict_page_check_all.clicked.connect(self.evnCheckAllButtonClickedPagePredict)
        self.ui.btn_predict_page_uncheck_all.clicked.connect(self.evnUncheckAllButtonClickedPagePredict)
        self.ui.btn_predict_page_delete_selected_images.clicked.connect(self.evnDeleteSelectedImagesButtonClickedPagePredict)
        self.ui.btn_predict_page_predict.clicked.connect(self.evnPredictButtonClicked)

        self.ui.images_predict_page_import_list.itemClicked.connect(self.evnImageListItemClickedPagePredict)
        self.ui.images_predict_page_import_list.itemDoubleClicked.connect(partial(self.evnImageListItemDoubleClicked, self.imageListPathDict))
        self.ui.images_predict_page_import_list.currentItemChanged.connect(
            partial(self.evnCurrentItemChanged, self.ui.label_predict_page_selected_picture))

        self.ui.btn_results_page_clear_images.clicked.connect(self.evnClearImagesButtonClickedPageResults)
        self.ui.btn_results_page_check_all.clicked.connect(self.evnCheckAllButtonClickedPageResults)
        self.ui.btn_results_page_uncheck_all.clicked.connect(self.evnUncheckAllButtonClickedPageResults)
        self.ui.btn_results_page_delete_selected_images.clicked.connect(self.evnDeleteSelectedImagesButtonClickedPageResults)

        self.ui.images_results_page_import_list.itemClicked.connect(self.evnImageListItemClickedPageResults)
        self.ui.images_results_page_import_list.itemDoubleClicked.connect(partial(self.evnImageListItemDoubleClicked, self.predictedImageListPathDict))
        # self.ui.images_results_page_import_list.currentItemChanged.connect(
        #     partial(self.evnCurrentItemChanged, self.ui.label_predict_page_selected_picture))

    def evnPredictButtonClicked(self):
        checked_items = []

        for index in range(self.ui.images_predict_page_import_list.count()):
            if self.ui.images_predict_page_import_list.item(index).checkState() == 2:
                list_item = self.ui.images_predict_page_import_list.item(index)
                checked_items.append(self.imageListPathDict[list_item.text()])

        # test(checked_items)

    def imageLabelFrame(self, label, frame1, frame2, lineWidth):
        print(label)

        label.setFrameShape(frame1)
        label.setFrameShadow(frame2)
        label.setLineWidth(lineWidth)

    def evnCurrentItemChanged(self, label, item):
        if item:
            label.setPixmap(QtGui.QPixmap(self.imageListPathDict[item.text()]))
            self.imageLabelFrame(label, QFrame.StyledPanel, QFrame.Sunken, 3)

    def sharedTermsPagePredict(self):
        list = self.ui.images_predict_page_import_list

        self.updateNumOfImages(list)

        if not isAtLeastOneItemChecked(list):
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, False)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, True)

        if isAtLeastOneItemNotChecked(list):
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_check_all, True)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_check_all, False)

        if numOfCheckedItems(list):
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, True)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, True)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, False)

    def sharedTermsPageResults(self):
        list = self.ui.images_results_page_import_list

        self.updateNumOfImages(list)

        if not isAtLeastOneItemChecked(list):
            toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, False)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, True)

        if isAtLeastOneItemNotChecked(list):
            toggleButtonAndChangeStyle(self.ui.btn_results_page_check_all, True)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_results_page_check_all, False)

        if numOfCheckedItems(list):
            toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, True)
        else:
            toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, False)

    def evnImageListItemClickedPagePredict(self):
        self.sharedTermsPagePredict()

    def evnImageListItemClickedPageResults(self):
        self.sharedTermsPageResults()

    def evnImageListItemDoubleClicked(self, dic, item):
        if item:
            openImage(dic[item.text()])

    def evnPage1BtnClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.frame_predict_page)

    def evnPageResultsClicked(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.frame_results_page)

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
                self.ui.images_predict_page_import_list.addItem(list_item)
                toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, True)
                toggleButtonAndChangeStyle(self.ui.btn_predict_page_clear_images, True)
                toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, True)
                toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, True)

                ################################################################################################
                self.predictedImageListPathDict[pictures_input_path[i].split('/')[-1]] = pictures_input_path[i]
                list_item2 = QtWidgets.QListWidgetItem()
                list_item2.setCheckState(QtCore.Qt.Checked)
                list_item2.setText(pictures_input_path[i].split('/')[-1])
                setListItemItemStyle(list_item2)
                self.ui.images_results_page_import_list.addItem(list_item2)

                toggleButtonAndChangeStyle(self.ui.btn_results_page_clear_images, True)
                toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, True)
                toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, True)

                ################################################################################################

        if len(self.ui.images_predict_page_import_list.selectedItems()) == 0:
            label = self.ui.label_predict_page_selected_picture
            self.imageLabelFrame(label, 0, 0, 0)
            label.setText("Please select image to view on the screen.")
        self.updateNumOfImages(self.ui.images_predict_page_import_list)

    def evnDeleteSelectedImagesButtonClickedPagePredict(self):
        checked_items = []

        if showDialog('Delete the selected images', 'Are you sure?'):
            for index in range(self.ui.images_predict_page_import_list.count()):
                if self.ui.images_predict_page_import_list.item(index).checkState() == 2:
                    list_item = self.ui.images_predict_page_import_list.item(index)
                    checked_items.append(list_item)

            for item in checked_items:
                self.ui.images_predict_page_import_list.takeItem(self.ui.images_predict_page_import_list.row(item))
                self.imageListPathDict.pop(item.text())

            self.sharedTermsPagePredict()

            if not len(self.ui.images_predict_page_import_list):
                label = self.ui.label_predict_page_selected_picture
                label.setText("Please load and select image.")
                self.imageLabelFrame(label, 0, 0, 0)
                toggleButtonAndChangeStyle(self.ui.btn_predict_page_clear_images, False)

    def evnDeleteSelectedImagesButtonClickedPageResults(self):
        checked_items = []

        if showDialog('Delete the selected images', 'Are you sure?'):
            for index in range(self.ui.images_results_page_import_list.count()):
                if self.ui.images_results_page_import_list.item(index).checkState() == 2:
                    list_item = self.ui.images_results_page_import_list.item(index)
                    checked_items.append(list_item)

            for item in checked_items:
                self.ui.images_results_page_import_list.takeItem(self.ui.images_results_page_import_list.row(item))
                self.predictedImageListPathDict.pop(item.text())

            self.sharedTermsPageResults()

            if not len(self.ui.images_results_page_import_list):
                label = self.ui.label_results_page_selected_picture
                label.setText("Please load and select image.")
                self.imageLabelFrame(label, 0, 0, 0)
                toggleButtonAndChangeStyle(self.ui.btn_results_page_clear_images, False)

    def evnClearImagesButtonClickedPagePredict(self):
        if self.imageListPathDict and showDialog('Clear all images', 'Are you sure?'):
            btn = self.ui.btn_predict_page_clear_images
            btn.setEnabled(False)
            self.ui.images_predict_page_import_list.clear()
            self.imageListPathDict = {}
            self.imageLabelFrame(self.ui.label_predict_page_images, 0, 0, 0)
            self.ui.label_predict_page_selected_picture.setText("Please load and select image.")
            changeButtonToDisableStyle(btn)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, False)
            self.updateNumOfImages(self.ui.images_predict_page_import_list)

    def evnClearImagesButtonClickedPageResults(self):
        if self.predictedImageListPathDict and showDialog('Clear all images', 'Are you sure?'):
            self.ui.btn_results_page_clear_images.setEnabled(False)
            self.ui.images_results_page_import_list.clear()
            self.predictedImageListPathDict = {}
            self.imageLabelFrame(self.ui.label_results_page_images, 0, 0, 0)
            self.ui.label_results_page_selected_picture.setText("Please load and select image.")
            changeButtonToDisableStyle(self.ui.btn_results_page_clear_images)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, False)
            self.updateNumOfImages(self.ui.images_results_page_import_list)

    def evnCheckAllButtonClickedPagePredict(self):
        if showDialog('Check all images', 'Are you sure?'):
            for index in range(self.ui.images_predict_page_import_list.count()):
                if self.ui.images_predict_page_import_list.item(index).checkState() == 0:
                    self.ui.images_predict_page_import_list.item(index).setCheckState(2)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, True)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, True)
            self.updateNumOfImages(self.ui.images_predict_page_import_list)

    def evnUncheckAllButtonClickedPagePredict(self):
        if showDialog('Uncheck all images', 'Are you sure?'):
            for index in range(self.ui.images_predict_page_import_list.count()):
                if self.ui.images_predict_page_import_list.item(index).checkState() == 2:
                    self.ui.images_predict_page_import_list.item(index).setCheckState(0)

            toggleButtonAndChangeStyle(self.ui.btn_predict_page_check_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_predict, False)
            toggleButtonAndChangeStyle(self.ui.btn_predict_page_delete_selected_images, False)
            self.updateNumOfImages(self.ui.images_predict_page_import_list)


    def evnCheckAllButtonClickedPageResults(self):
        if showDialog('Check all images', 'Are you sure?'):
            for index in range(self.ui.images_results_page_import_list.count()):
                if self.ui.images_results_page_import_list.item(index).checkState() == 0:
                    self.ui.images_results_page_import_list.item(index).setCheckState(2)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_check_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, True)
            self.updateNumOfImages(self.ui.images_results_page_import_list)

    def evnUncheckAllButtonClickedPageResults(self):
        if showDialog('Uncheck all images', 'Are you sure?'):
            for index in range(self.ui.images_results_page_import_list.count()):
                if self.ui.images_results_page_import_list.item(index).checkState() == 2:
                    self.ui.images_results_page_import_list.item(index).setCheckState(0)

            toggleButtonAndChangeStyle(self.ui.btn_results_page_check_all, True)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_uncheck_all, False)
            toggleButtonAndChangeStyle(self.ui.btn_results_page_delete_selected_images, False)
            self.updateNumOfImages(self.ui.images_results_page_import_list)

    def updateNumOfImages(self, list):
        self.ui.label_predict_page_images.setText(
            f"Images: {list.count()} Checked: {numOfCheckedItems(list)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
