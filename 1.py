import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPixmap


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 900)
        self.setWindowTitle('PyQT')
        self.pixmap = QPixmap("1.jpg")
        self.label.setPixmap(self.pixmap)
        self.show()
        self.pushButton.clicked.connect(self.run)
        self.point = 0

    def run(self):
        if self.radioButton_8.isChecked():
            self.point += 10
        if self.checkBox_9.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.checkBox_12.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.radioButton_3.isChecked():
            self.point += 10
        if self.lineEdit.text().lowers == "Аравийский полуостров".lower():
            self.point += 10
        self.pushButton.setText(str(self.point))
        self.point = 0


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
