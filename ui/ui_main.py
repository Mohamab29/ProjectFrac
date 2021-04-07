# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 717)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Top_Bar = QtWidgets.QFrame(self.centralwidget)
        self.Top_Bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.Top_Bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.Top_Bar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Top_Bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Bar.setObjectName("Top_Bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Top_Bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_toggle = QtWidgets.QFrame(self.Top_Bar)
        self.frame_toggle.setMaximumSize(QtCore.QSize(100, 40))
        self.frame_toggle.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_Toggle = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_Toggle.sizePolicy().hasHeightForWidth())
        self.btn_Toggle.setSizePolicy(sizePolicy)
        self.btn_Toggle.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.btn_Toggle.setObjectName("btn_Toggle")
        self.verticalLayout_2.addWidget(self.btn_Toggle)
        self.horizontalLayout.addWidget(self.frame_toggle)
        self.frame_top = QtWidgets.QFrame(self.Top_Bar)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 70))
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.horizontalLayout.addWidget(self.frame_top)
        self.verticalLayout.addWidget(self.Top_Bar)
        self.Content = QtWidgets.QFrame(self.centralwidget)
        self.Content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Content.setObjectName("Content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.Content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(100, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_top_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_top_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_menus.setObjectName("frame_top_menus")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_top_menus)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_page_predict = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_predict.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_page_predict.setFont(font)
        self.btn_page_predict.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_predict.setStyleSheet("QPushButton {\n"
"    color: rgb(200, 200, 200);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.btn_page_predict.setAutoRepeat(False)
        self.btn_page_predict.setObjectName("btn_page_predict")
        self.verticalLayout_4.addWidget(self.btn_page_predict)
        self.btn_page_results = QtWidgets.QPushButton(self.frame_top_menus)
        self.btn_page_results.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_page_results.setFont(font)
        self.btn_page_results.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_results.setStyleSheet("QPushButton {\n"
"    color: rgb(200, 200, 200);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.btn_page_results.setObjectName("btn_page_results")
        self.verticalLayout_4.addWidget(self.btn_page_results)
        self.verticalLayout_3.addWidget(self.frame_top_menus, 0, QtCore.Qt.AlignTop)
        self.frame_bottom_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_bottom_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_bottom_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bottom_menus.setObjectName("frame_bottom_menus")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_bottom_menus)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.btn_page_help = QtWidgets.QPushButton(self.frame_bottom_menus)
        self.btn_page_help.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_page_help.setFont(font)
        self.btn_page_help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_page_help.setStyleSheet("QPushButton {\n"
"    color: rgb(200, 200, 200);\n"
"    background-color: rgb(35, 35, 35);\n"
"    border: 0px solid;\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"    background-color: rgb(55, 55, 55);\n"
"}\n"
"")
        self.btn_page_help.setObjectName("btn_page_help")
        self.verticalLayout_15.addWidget(self.btn_page_help)
        self.verticalLayout_3.addWidget(self.frame_bottom_menus, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.Content)
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.main_page_predict = QtWidgets.QWidget()
        self.main_page_predict.setObjectName("main_page_predict")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_page_predict)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_main_page_predict = QtWidgets.QFrame(self.main_page_predict)
        self.frame_main_page_predict.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_page_predict.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_page_predict.setObjectName("frame_main_page_predict")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_main_page_predict)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_main_page_predict_picture = QtWidgets.QFrame(self.frame_main_page_predict)
        self.frame_main_page_predict_picture.setMinimumSize(QtCore.QSize(2, 0))
        self.frame_main_page_predict_picture.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_page_predict_picture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_page_predict_picture.setObjectName("frame_main_page_predict_picture")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_main_page_predict_picture)
        self.gridLayout.setContentsMargins(-1, -1, -1, 7)
        self.gridLayout.setObjectName("gridLayout")
        self.label_selected_picture = QtWidgets.QLabel(self.frame_main_page_predict_picture)
        self.label_selected_picture.setStyleSheet("QLabel {color: rgb(130, 130, 130)}")
        self.label_selected_picture.setScaledContents(True)
        self.label_selected_picture.setObjectName("label_selected_picture")
        self.gridLayout.addWidget(self.label_selected_picture, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalLayout_3.addWidget(self.frame_main_page_predict_picture)
        self.frame_main_page_predict_frame_list = QtWidgets.QFrame(self.frame_main_page_predict)
        self.frame_main_page_predict_frame_list.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_main_page_predict_frame_list.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_main_page_predict_frame_list.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main_page_predict_frame_list.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main_page_predict_frame_list.setLineWidth(0)
        self.frame_main_page_predict_frame_list.setObjectName("frame_main_page_predict_frame_list")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_main_page_predict_frame_list)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_images = QtWidgets.QLabel(self.frame_main_page_predict_frame_list)
        self.label_images.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_images.setFont(font)
        self.label_images.setStyleSheet("QLabel {color: rgb(255, 255, 255)}")
        self.label_images.setObjectName("label_images")
        self.verticalLayout_11.addWidget(self.label_images, 0, QtCore.Qt.AlignHCenter)
        self.images_import_list = QtWidgets.QListWidget(self.frame_main_page_predict_frame_list)
        self.images_import_list.setMinimumSize(QtCore.QSize(150, 0))
        self.images_import_list.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.images_import_list.setFrameShape(QtWidgets.QFrame.Panel)
        self.images_import_list.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.images_import_list.setLineWidth(1)
        self.images_import_list.setMidLineWidth(0)
        self.images_import_list.setProperty("showDropIndicator", True)
        self.images_import_list.setDragEnabled(False)
        self.images_import_list.setObjectName("images_import_list")
        self.verticalLayout_11.addWidget(self.images_import_list)
        self.horizontalLayout_3.addWidget(self.frame_main_page_predict_frame_list)
        self.verticalLayout_7.addWidget(self.frame_main_page_predict)
        self.frame_pages_buttons = QtWidgets.QFrame(self.main_page_predict)
        self.frame_pages_buttons.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_pages_buttons.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_buttons.setObjectName("frame_pages_buttons")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_pages_buttons)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_pages_buttons_load_clear_images = QtWidgets.QFrame(self.frame_pages_buttons)
        self.frame_pages_buttons_load_clear_images.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_buttons_load_clear_images.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_buttons_load_clear_images.setObjectName("frame_pages_buttons_load_clear_images")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_pages_buttons_load_clear_images)
        self.verticalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.btn_load_images = QtWidgets.QPushButton(self.frame_pages_buttons_load_clear_images)
        self.btn_load_images.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_load_images.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_load_images.setAutoFillBackground(False)
        self.btn_load_images.setStyleSheet("QPushButton {\n"
"    color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_load_images.setAutoDefault(False)
        self.btn_load_images.setDefault(False)
        self.btn_load_images.setFlat(False)
        self.btn_load_images.setObjectName("btn_load_images")
        self.verticalLayout_10.addWidget(self.btn_load_images)
        self.btn_clear_images = QtWidgets.QPushButton(self.frame_pages_buttons_load_clear_images)
        self.btn_clear_images.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.btn_clear_images.setFont(font)
        self.btn_clear_images.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_clear_images.setToolTip("")
        self.btn_clear_images.setStatusTip("")
        self.btn_clear_images.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_clear_images.setObjectName("btn_clear_images")
        self.verticalLayout_10.addWidget(self.btn_clear_images)
        self.horizontalLayout_8.addWidget(self.frame_pages_buttons_load_clear_images)
        self.frame_pages_buttons_check_uncheck_images = QtWidgets.QFrame(self.frame_pages_buttons)
        self.frame_pages_buttons_check_uncheck_images.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_buttons_check_uncheck_images.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_buttons_check_uncheck_images.setObjectName("frame_pages_buttons_check_uncheck_images")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_pages_buttons_check_uncheck_images)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.btn_check_all = QtWidgets.QPushButton(self.frame_pages_buttons_check_uncheck_images)
        self.btn_check_all.setEnabled(False)
        self.btn_check_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_check_all.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_check_all.setObjectName("btn_check_all")
        self.verticalLayout_12.addWidget(self.btn_check_all)
        self.btn_uncheck_all = QtWidgets.QPushButton(self.frame_pages_buttons_check_uncheck_images)
        self.btn_uncheck_all.setEnabled(False)
        self.btn_uncheck_all.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_uncheck_all.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_uncheck_all.setObjectName("btn_uncheck_all")
        self.verticalLayout_12.addWidget(self.btn_uncheck_all)
        self.horizontalLayout_8.addWidget(self.frame_pages_buttons_check_uncheck_images)
        self.frame_pages_buttons_delete = QtWidgets.QFrame(self.frame_pages_buttons)
        self.frame_pages_buttons_delete.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_buttons_delete.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_buttons_delete.setObjectName("frame_pages_buttons_delete")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_pages_buttons_delete)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.btn_delete_selected_images = QtWidgets.QPushButton(self.frame_pages_buttons_delete)
        self.btn_delete_selected_images.setEnabled(False)
        self.btn_delete_selected_images.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_delete_selected_images.setObjectName("btn_delete_selected_images")
        self.verticalLayout_14.addWidget(self.btn_delete_selected_images)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_pages_buttons_delete)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_14.addWidget(self.pushButton_3)
        self.horizontalLayout_8.addWidget(self.frame_pages_buttons_delete)
        self.frame_pages_buttons_predict_button = QtWidgets.QFrame(self.frame_pages_buttons)
        self.frame_pages_buttons_predict_button.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_pages_buttons_predict_button.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages_buttons_predict_button.setObjectName("frame_pages_buttons_predict_button")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_pages_buttons_predict_button)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.btn_predict = QtWidgets.QPushButton(self.frame_pages_buttons_predict_button)
        self.btn_predict.setEnabled(False)
        self.btn_predict.setMinimumSize(QtCore.QSize(0, 56))
        self.btn_predict.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_predict.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.btn_predict.setObjectName("btn_predict")
        self.verticalLayout_13.addWidget(self.btn_predict)
        self.horizontalLayout_8.addWidget(self.frame_pages_buttons_predict_button)
        self.verticalLayout_7.addWidget(self.frame_pages_buttons)
        self.stackedWidget.addWidget(self.main_page_predict)
        self.page_results = QtWidgets.QWidget()
        self.page_results.setObjectName("page_results")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_results)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.page_results)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(4)
        self.gridLayout_4.setVerticalSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_selected_picture_4 = QtWidgets.QLabel(self.frame_3)
        self.label_selected_picture_4.setStyleSheet("QLabel {color: rgb(130, 130, 130)}")
        self.label_selected_picture_4.setScaledContents(True)
        self.label_selected_picture_4.setObjectName("label_selected_picture_4")
        self.gridLayout_4.addWidget(self.label_selected_picture_4, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_6.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel {color: rgb(255, 255, 255)}")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.listWidget = QtWidgets.QListWidget(self.frame_4)
        self.listWidget.setStyleSheet("background-color: rgb(43, 43, 43);")
        self.listWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_9.addWidget(self.listWidget)
        self.horizontalLayout_6.addWidget(self.frame_4)
        self.verticalLayout_6.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.page_results)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_17.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_6)
        self.pushButton.setEnabled(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_17.addWidget(self.pushButton)
        self.horizontalLayout_5.addWidget(self.frame_6)
        self.frame_8 = QtWidgets.QFrame(self.frame)
        self.frame_8.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_5.setEnabled(False)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout_19.addWidget(self.pushButton_5)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_8)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_19.addWidget(self.pushButton_4)
        self.horizontalLayout_5.addWidget(self.frame_8)
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setEnabled(False)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_18.addWidget(self.pushButton_7)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_6.setEnabled(False)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_18.addWidget(self.pushButton_6)
        self.horizontalLayout_5.addWidget(self.frame_7)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_9.setEnabled(False)
        self.pushButton_9.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayout_16.addWidget(self.pushButton_9)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_8.setEnabled(False)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"    color: rgb(100, 100, 100);\n"
"}\n"
"QPushButton:hover {\n"
"    color: rgb(85, 170, 255);\n"
"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.verticalLayout_16.addWidget(self.pushButton_8)
        self.horizontalLayout_5.addWidget(self.frame_5)
        self.verticalLayout_6.addWidget(self.frame)
        self.stackedWidget.addWidget(self.page_results)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.page_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #FFF;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.stackedWidget.addWidget(self.page_3)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.Content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "FractureArea"))
        self.btn_Toggle.setText(_translate("MainWindow", "TOGGLE"))
        self.btn_page_predict.setText(_translate("MainWindow", "Predict"))
        self.btn_page_results.setText(_translate("MainWindow", "Results"))
        self.btn_page_help.setText(_translate("MainWindow", "Help"))
        self.label_selected_picture.setText(_translate("MainWindow", "Please load and select image."))
        self.label_images.setText(_translate("MainWindow", "Images: 0 Checked: 0"))
        self.btn_load_images.setText(_translate("MainWindow", "Load Images"))
        self.btn_clear_images.setText(_translate("MainWindow", "Clear Image list"))
        self.btn_check_all.setText(_translate("MainWindow", "Check All"))
        self.btn_uncheck_all.setText(_translate("MainWindow", "Uncheck All"))
        self.btn_delete_selected_images.setText(_translate("MainWindow", "Delete selected Images"))
        self.pushButton_3.setText(_translate("MainWindow", "Button"))
        self.btn_predict.setText(_translate("MainWindow", "Predict"))
        self.label_selected_picture_4.setText(_translate("MainWindow", "No results"))
        self.label_2.setText(_translate("MainWindow", "Images: 0 Checked: 0"))
        self.pushButton_2.setText(_translate("MainWindow", "Save Images and CSVs"))
        self.pushButton.setText(_translate("MainWindow", "Clear Image list"))
        self.pushButton_5.setText(_translate("MainWindow", "Save Images"))
        self.pushButton_4.setText(_translate("MainWindow", "Save CSVs"))
        self.pushButton_7.setText(_translate("MainWindow", "Check All"))
        self.pushButton_6.setText(_translate("MainWindow", "Uncheck All"))
        self.pushButton_9.setText(_translate("MainWindow", "Delete selected Images"))
        self.pushButton_8.setText(_translate("MainWindow", "Button"))
        self.label.setText(_translate("MainWindow", "PAGE 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
