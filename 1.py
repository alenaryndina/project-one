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
        self.pushButton_2.clicked.connect(self.save)
        self.point = 0
        self.show()

    def run(self):
        if self.answer3.isChecked():
            self.point += 10
        if self.checkBox_9.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.checkBox_12.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.answer6.isChecked():
            self.point += 10
        if self.lineEdit.text().lower() == "Аравийский полуостров".lower():
            self.point += 10
        if self.answer8.isChecked():
            self.point += 10
        if self.checkBox_13.isChecked() and not (self.checkBox_14.isChecked() or self.checkBox_16.isChecked()):
            self.point += 10
        if self.checkBox_15.isChecked() and not (self.checkBox_14.isChecked() or self.checkBox_16.isChecked()):
            self.point += 10
        if self.answer16.isChecked():
            self.point += 10
        if self.answer18.isChecked():
            self.point += 10
        if self.lineEdit_2.text().lower() == "Енисей".lower():
            self.point += 10
        if self.answer23.isChecked():
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
            self.save()
            self.point = 0
            self.buttonGroup.setExclusive(False)
            self.buttonGroup_2.setExclusive(False)
            self.buttonGroup_3.setExclusive(False)
            self.buttonGroup_4.setExclusive(False)
            self.buttonGroup_5.setExclusive(False)
            self.answer4.setChecked(False)
            self.answer5.setChecked(False)
            self.answer6.setChecked(False)
            self.answer7.setChecked(False)
            self.answer.setChecked(False)
            self.answer1.setChecked(False)
            self.answer2.setChecked(False)
            self.answer3.setChecked(False)
            self.answer8.setChecked(False)
            self.answer12.setChecked(False)
            self.answer9.setChecked(False)
            self.answer10.setChecked(False)
            self.answer11.setChecked(False)
            self.answer13.setChecked(False)
            self.answer15.setChecked(False)
            self.answer14.setChecked(False)
            self.answer19.setChecked(False)
            self.answer21.setChecked(False)
            self.answer17.setChecked(False)
            self.answer16.setChecked(False)
            self.answer18.setChecked(False)
            self.answer22.setChecked(False)
            self.answer23.setChecked(False)
            self.answer20.setChecked(False)

            self.checkBox_9.setChecked(False)
            self.checkBox_10.setChecked(False)
            self.checkBox_11.setChecked(False)
            self.checkBox_12.setChecked(False)
            self.checkBox_13.setChecked(False)
            self.checkBox_14.setChecked(False)
            self.checkBox_15.setChecked(False)
            self.checkBox_16.setChecked(False)
            self.buttonGroup.setExclusive(True)
            self.buttonGroup_2.setExclusive(True)
            self.buttonGroup_3.setExclusive(True)
            self.buttonGroup_4.setExclusive(True)
            self.buttonGroup_5.setExclusive(True)
            self.lineEdit_2.setText("")
            self.lineEdit.setText("")

    def save(self):
        file = open("result_test.txt","w",encoding="utf-8")
        file.write(str(self.point)+"\n")
        file.write(self.textEdit_3.toPlainText())
        if self.answer.isChecked():
            file.write(self.answer.text()+"\n")
        if self.answer1.isChecked():
            file.write(self.answer1.text()+"\n")
        if self.answer2.isChecked():
            file.write(self.answer2.text()+"\n")
        if self.answer3.isChecked():
            file.write(self.answer3.text()+"\n")

        file.write("\n"+self.textEdit_4.toPlainText())
        if self.checkBox_9.isChecked():
            file.write(self.checkBox_9.text()+"\n")
        if self.checkBox_10.isChecked():
            file.write(self.checkBox_10.text()+"\n")
        if self.checkBox_11.isChecked():
            file.write(self.checkBox_11.text()+"\n")
        if self.checkBox_12.isChecked():
            file.write(self.checkBox_12.text()+"\n")


        file.write("\n"+self.textEdit_5.toPlainText())
        if self.answer4.isChecked():
            file.write(self.answer4.text()+"\n")
        if self.answer5.isChecked():
            file.write(self.answer5.text()+"\n")
        if self.answer6.isChecked():
            file.write(self.answer6.text()+"\n")
        if self.answer7.isChecked():
            file.write(self.answer7.text()+"\n")
            
        file.write("\n"+self.textEdit_6.toPlainText())
        file.write(self.lineEdit.text()+"\n")
            
            
        file.write("\n"+self.textEdit_8.toPlainText())
        if self.answer8.isChecked():
            file.write(self.answer4.text()+"\n")
        if self.answer9.isChecked():
            file.write(self.answer5.text()+"\n")
        if self.answer10.isChecked():
            file.write(self.answer6.text()+"\n")
        if self.answer11.isChecked():
            file.write(self.answer7.text()+"\n")


        file.write("\n"+self.textEdit_9.toPlainText())
        if self.checkBox_9.isChecked():
            file.write(self.checkBox_13.text()+"\n")
        if self.checkBox_10.isChecked():
            file.write(self.checkBox_14.text()+"\n")
        if self.checkBox_11.isChecked():
            file.write(self.checkBox_15.text()+"\n")
        if self.checkBox_12.isChecked():
            file.write(self.checkBox_16.text()+"\n")


        file.write("\n"+self.textEdit_11.toPlainText())
        if self.answer12.isChecked():
            file.write(self.answer4.text()+"\n")
        if self.answer13.isChecked():
            file.write(self.answer5.text()+"\n")
        if self.answer15.isChecked():
            file.write(self.answer6.text()+"\n")
        if self.answer14.isChecked():
            file.write(self.answer7.text()+"\n")

        file.write("\n"+self.textEdit_12.toPlainText())
        if self.answer17.isChecked():
            file.write(self.answer4.text()+"\n")
        if self.answer16.isChecked():
            file.write(self.answer5.text()+"\n")
        if self.answer18.isChecked():
            file.write(self.answer6.text()+"\n")
        if self.answer19.isChecked():
            file.write(self.answer7.text()+"\n")

        file.write("\n"+self.textEdit_10.toPlainText())
        file.write(self.lineEdit_2.text()+"\n")


        file.write("\n"+self.textEdit_13.toPlainText())
        if self.answer21.isChecked():
            file.write(self.answer4.text()+"\n")
        if self.answer22.isChecked():
            file.write(self.answer5.text()+"\n")
        if self.answer23.isChecked():
            file.write(self.answer6.text()+"\n")
        if self.answer20.isChecked():
            file.write(self.answer7.text()+"\n")

        file.write("\n"+self.textEdit_15.toPlainText())
        file.write(self.calendarWidget.selectedDate().toString("yyyy-MM-dd")+" "+ self.timeEdit.time().toString()+"\n")

        file.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
