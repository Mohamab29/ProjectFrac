# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FractureArea(object):
    def setupUi(self, FractureArea):
        FractureArea.setObjectName("FractureArea")
        FractureArea.resize(1000, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(FractureArea.sizePolicy().hasHeightForWidth())
        FractureArea.setSizePolicy(sizePolicy)
        FractureArea.setMouseTracking(False)
        FractureArea.setAnimated(True)
        FractureArea.setTabShape(QtWidgets.QTabWidget.Rounded)
        FractureArea.setDockNestingEnabled(False)
        FractureArea.setUnifiedTitleAndToolBarOnMac(False)
        self.centralWidget = QtWidgets.QWidget(FractureArea)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Content = QtWidgets.QFrame(self.centralWidget)
        self.Content.setMinimumSize(QtCore.QSize(0, 0))
        self.Content.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.leftMenuFrame = QtWidgets.QFrame(self.Content)
        self.leftMenuFrame.setMinimumSize(QtCore.QSize(170, 0))
        self.leftMenuFrame.setMaximumSize(QtCore.QSize(150, 16777215))
        self.leftMenuFrame.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.leftMenuFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.leftMenuFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.leftMenuFrame.setObjectName("leftMenuFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.leftMenuFrame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.homeButton = QtWidgets.QPushButton(self.leftMenuFrame)
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout.addWidget(self.homeButton)
        self.page1Button = QtWidgets.QPushButton(self.leftMenuFrame)
        self.page1Button.setObjectName("page1Button")
        self.verticalLayout.addWidget(self.page1Button)
        self.page2Button = QtWidgets.QPushButton(self.leftMenuFrame)
        self.page2Button.setObjectName("page2Button")
        self.verticalLayout.addWidget(self.page2Button)
        self.page3Button = QtWidgets.QPushButton(self.leftMenuFrame)
        self.page3Button.setObjectName("page3Button")
        self.verticalLayout.addWidget(self.page3Button)
        self.horizontalLayout_2.addWidget(self.leftMenuFrame, 0, QtCore.Qt.AlignTop)
        self.pagesFrame = QtWidgets.QFrame(self.Content)
        self.pagesFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pagesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pagesFrame.setObjectName("pagesFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.pagesFrame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.pagesFrame)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QtWidgets.QWidget()
        self.home.setObjectName("home")
        self.scrollArea = QtWidgets.QScrollArea(self.home)
        self.scrollArea.setGeometry(QtCore.QRect(160, 0, 451, 461))
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContent = QtWidgets.QWidget()
        self.scrollAreaWidgetContent.setGeometry(QtCore.QRect(0, 0, 451, 461))
        self.scrollAreaWidgetContent.setObjectName("scrollAreaWidgetContent")
        self.pictureGridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContent)
        self.pictureGridLayout.setContentsMargins(0, 0, 0, 0)
        self.pictureGridLayout.setVerticalSpacing(0)
        self.pictureGridLayout.setObjectName("pictureGridLayout")
        self.image1 = QtWidgets.QLabel(self.scrollAreaWidgetContent)
        self.image1.setMaximumSize(QtCore.QSize(200, 200))
        self.image1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.image1.setMouseTracking(False)
        self.image1.setAcceptDrops(False)
        self.image1.setAutoFillBackground(False)
        self.image1.setText("")
        self.image1.setPixmap(QtGui.QPixmap("../../../fracture/1.png"))
        self.image1.setScaledContents(True)
        self.image1.setWordWrap(False)
        self.image1.setObjectName("image1")
        self.pictureGridLayout.addWidget(self.image1, 0, 0, 1, 1)
        self.image3 = QtWidgets.QLabel(self.scrollAreaWidgetContent)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image3.sizePolicy().hasHeightForWidth())
        self.image3.setSizePolicy(sizePolicy)
        self.image3.setMinimumSize(QtCore.QSize(100, 100))
        self.image3.setMaximumSize(QtCore.QSize(200, 200))
        self.image3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.image3.setText("")
        self.image3.setPixmap(QtGui.QPixmap("../../../fracture/35.png"))
        self.image3.setScaledContents(True)
        self.image3.setObjectName("image3")
        self.pictureGridLayout.addWidget(self.image3, 0, 1, 1, 1)
        self.image4 = QtWidgets.QLabel(self.scrollAreaWidgetContent)
        self.image4.setMaximumSize(QtCore.QSize(200, 200))
        self.image4.setText("")
        self.image4.setPixmap(QtGui.QPixmap("../../../fracture/22.png"))
        self.image4.setScaledContents(True)
        self.image4.setObjectName("image4")
        self.pictureGridLayout.addWidget(self.image4, 1, 1, 1, 1)
        self.image2 = QtWidgets.QLabel(self.scrollAreaWidgetContent)
        self.image2.setMaximumSize(QtCore.QSize(200, 200))
        self.image2.setText("")
        self.image2.setPixmap(QtGui.QPixmap("../../../fracture/2.png"))
        self.image2.setScaledContents(True)
        self.image2.setObjectName("image2")
        self.pictureGridLayout.addWidget(self.image2, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContent)
        self.stackedWidget.addWidget(self.home)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.loadImagesButton = QtWidgets.QPushButton(self.page1)
        self.loadImagesButton.setGeometry(QtCore.QRect(290, 440, 111, 25))
        self.loadImagesButton.setObjectName("loadImagesButton")
        self.stackedWidget.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.label2 = QtWidgets.QLabel(self.page2)
        self.label2.setGeometry(QtCore.QRect(280, 240, 67, 17))
        self.label2.setObjectName("label2")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QtWidgets.QWidget()
        self.page3.setObjectName("page3")
        self.label3 = QtWidgets.QLabel(self.page3)
        self.label3.setGeometry(QtCore.QRect(280, 230, 67, 17))
        self.label3.setObjectName("label3")
        self.stackedWidget.addWidget(self.page3)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.pagesFrame)
        self.horizontalLayout.addWidget(self.Content)
        FractureArea.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QMenuBar(FractureArea)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Open = QtWidgets.QMenu(self.menubar)
        self.menu_Open.setObjectName("menu_Open")
        FractureArea.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(FractureArea)
        self.statusbar.setObjectName("statusbar")
        FractureArea.setStatusBar(self.statusbar)
        self.action_Open = QtWidgets.QAction(FractureArea)
        self.action_Open.setObjectName("action_Open")
        self.menu_Open.addAction(self.action_Open)
        self.menubar.addAction(self.menu_Open.menuAction())

        self.retranslateUi(FractureArea)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FractureArea)

    def retranslateUi(self, FractureArea):
        _translate = QtCore.QCoreApplication.translate
        FractureArea.setWindowTitle(_translate("FractureArea", "MainWindow"))
        self.homeButton.setStatusTip(_translate("FractureArea", "Go back Home"))
        self.homeButton.setText(_translate("FractureArea", "Home"))
        self.page1Button.setStatusTip(_translate("FractureArea", "Go to Page 1"))
        self.page1Button.setText(_translate("FractureArea", "Page 1"))
        self.page2Button.setStatusTip(_translate("FractureArea", "Go to Page 2"))
        self.page2Button.setText(_translate("FractureArea", "Page 2"))
        self.page3Button.setStatusTip(_translate("FractureArea", "Go to Page 3"))
        self.page3Button.setText(_translate("FractureArea", "Page 3"))
        self.page1.setStatusTip(_translate("FractureArea", "Page 1"))
        self.loadImagesButton.setText(_translate("FractureArea", "Load Images"))
        self.page2.setStatusTip(_translate("FractureArea", "Page 2"))
        self.label2.setText(_translate("FractureArea", "page2"))
        self.page3.setStatusTip(_translate("FractureArea", "Page 3"))
        self.label3.setText(_translate("FractureArea", "page3"))
        self.menu_Open.setTitle(_translate("FractureArea", "&File"))
        self.action_Open.setText(_translate("FractureArea", "&Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FractureArea = QtWidgets.QMainWindow()
    ui = Ui_FractureArea()
    ui.setupUi(FractureArea)
    FractureArea.show()
    sys.exit(app.exec_())

