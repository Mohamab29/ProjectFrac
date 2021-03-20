import sys
from PyQt5.QtWidgets import *  # imports section

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My GUI")  # add widgets, set properties
        self.resize(200, 200)

        self.btn = QPushButton("Open File", self)
        self.btn.move(40, 40);
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        file_to_open = "JPG File (*.jpg);;Can be change (*.png);;TIFF File (*.tiff)"
        # QFileDialog also have getSaveFileName,getSaveFileNames (with s) and more...
        res = QFileDialog.getOpenFileNames(self, "Open File", "/home/", file_to_open)
        print(res)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI canvas
    dlgMain.show()  # show the GUI
    sys.exit(app.exec_())  # execute the application
