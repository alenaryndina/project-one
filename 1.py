import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QInputDialog, QMessageBox
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
        self.pushButton.clicked.connect(self.run)
        self.point = 0
        self.show()

    def run(self):
        if self.radioButton_8.isChecked():
            self.point += 10
        if self.checkBox_9.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.checkBox_12.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.radioButton_3.isChecked():
            self.point += 10
        if self.lineEdit.text().lower == "Аравийский полуостров".lower():
            self.point += 10
        if self.radioButton_9.isChecked():
            self.point += 10
        if self.checkBox_13.isChecked() and not (self.checkBox_14.isChecked() or self.checkBox_16.isChecked()):
            self.point += 10
        if self.checkBox_15.isChecked() and not (self.checkBox_14.isChecked() or self.checkBox_16.isChecked()):
            self.point += 10
        if self.radioButton_16.isChecked():
            self.point += 10
        if self.radioButton_25.isChecked():
            self.point += 10
        if self.lineEdit_2.text().lower == "Енисей".lower():
            self.point += 10
        if self.radioButton_27.isChecked():
            self.point += 10
        date = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        time = self.timeEdit.time().toString()
        if date == "2018-12-11" and time == "06:00:00":
            self.point += 100
        result = ""
        if 0 <= self.point <= 50:
            result = 'Вы набрали ' + str(self.point) + " баллов (оценка - 1)"
        if 50 < self.point <= 90:
            result = 'Вы набрали ' + str(self.point) + " баллов (оценка -2 )"
        if 90 < self.point <= 100:
            result = 'Вы набрали ' + str(self.point) + " баллов (оценка -3 )"
        if 100 < self.point <= 140:
            result = 'Вы набрали ' + str(self.point) + " баллов (оценка -4 )"
        if 140 < self.point <= 200:
            result = 'Вы набрали ' + str(self.point) + " баллов (оценка -5 )"
        print(result)

        buttonReply = QMessageBox.question(self, 'Результат теста', result,
                                           QMessageBox.Yes)
        if buttonReply == QMessageBox.Yes:
            self.point = 0


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
