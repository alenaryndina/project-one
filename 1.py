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
        if self.radioButton_8.isChecked():
            self.point += 10
        if self.checkBox_9.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.checkBox_12.isChecked() and not (self.checkBox_10.isChecked() or self.checkBox_11.isChecked()):
            self.point += 10
        if self.radioButton_3.isChecked():
            self.point += 10
        if self.lineEdit.text().lower() == "Аравийский полуостров".lower():
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
        if self.lineEdit_2.text().lower() == "Енисей".lower():
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
            self.save()
            self.point = 0
            self.buttonGroup.setExclusive(False)
            self.buttonGroup_2.setExclusive(False)
            self.buttonGroup_3.setExclusive(False)
            self.buttonGroup_4.setExclusive(False)
            self.buttonGroup_5.setExclusive(False)
            self.radioButton.setChecked(False)
            self.radioButton_2.setChecked(False)
            self.radioButton_3.setChecked(False)
            self.radioButton_4.setChecked(False)
            self.radioButton_5.setChecked(False)
            self.radioButton_6.setChecked(False)
            self.radioButton_7.setChecked(False)
            self.radioButton_8.setChecked(False)
            self.radioButton_9.setChecked(False)
            self.radioButton_10.setChecked(False)
            self.radioButton_11.setChecked(False)
            self.radioButton_12.setChecked(False)
            self.radioButton_13.setChecked(False)
            self.radioButton_14.setChecked(False)
            self.radioButton_15.setChecked(False)
            self.radioButton_16.setChecked(False)
            self.radioButton_21.setChecked(False)
            self.radioButton_22.setChecked(False)
            self.radioButton_23.setChecked(False)
            self.radioButton_24.setChecked(False)
            self.radioButton_25.setChecked(False)
            self.radioButton_26.setChecked(False)
            self.radioButton_27.setChecked(False)
            self.radioButton_28.setChecked(False)

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
        if self.radioButton_5.isChecked():
            file.write(self.radioButton_5.text()+"\n")
        if self.radioButton_6.isChecked():
            file.write(self.radioButton_6.text()+"\n")
        if self.radioButton_7.isChecked():
            file.write(self.radioButton_7.text()+"\n")
        if self.radioButton_8.isChecked():
            file.write(self.radioButton_8.text()+"\n")

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
        if self.radioButton.isChecked():
            file.write(self.radioButton.text()+"\n")
        if self.radioButton_2.isChecked():
            file.write(self.radioButton_2.text()+"\n")
        if self.radioButton_3.isChecked():
            file.write(self.radioButton_3.text()+"\n")
        if self.radioButton_4.isChecked():
            file.write(self.radioButton_4.text()+"\n")
            
        file.write("\n"+self.textEdit_5.toPlainText())
        if self.radioButton.isChecked():
            file.write(self.radioButton.text()+"\n")
        if self.radioButton_2.isChecked():
            file.write(self.radioButton_2.text()+"\n")
        if self.radioButton_3.isChecked():
            file.write(self.radioButton_3.text()+"\n")
        if self.radioButton_4.isChecked():
            file.write(self.radioButton_4.text()+"\n")
            
            
        file.write("\n"+self.textEdit_5.toPlainText())
        if self.radioButton.isChecked():
            file.write(self.radioButton.text()+"\n")
        if self.radioButton_2.isChecked():
            file.write(self.radioButton_2.text()+"\n")
        if self.radioButton_3.isChecked():
            file.write(self.radioButton_3.text()+"\n")
        if self.radioButton_4.isChecked():
            file.write(self.radioButton_4.text()+"\n")

        file.close()


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())
