import sys
import task
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QTextEdit)


class Tasks(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def add_task(self):
        task.add(self.name_task_e.text(), self.body_task_e.toPlainText())
        self.name_task_e.clear()
        self.body_task_e.clear()

    def initUI(self):
        #Создаем окно
        self.resize(500, 300)
        self.move(300, 300)
        self.setWindowTitle('Заметки')

        # Создаем кнопку
        btn1 = QPushButton('Добавить заметку', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(30, 130)
        btn1.clicked.connect(self.add_task)

        # Создаем кнопку
        btn2 = QPushButton('Удалить заметку', self)
        btn2.resize(btn2.sizeHint())
        btn2.move(30, 170)

        # Создаем кнопку
        btn3 = QPushButton('Найти заметку', self)
        btn3.resize(btn3.sizeHint())
        btn3.move(30, 210)

        #Создаем текствое поле
        name_task = QLabel('Название заметки:', self)
        body_task = QLabel('Тело заметки:', self)
        name_task.move(30, 50)
        body_task.move(30, 70)

        self.name_task_e = QLineEdit(self)
        self.body_task_e = QTextEdit(self)
        self.name_task_e.move(160, 50)
        self.body_task_e.move(160, 70)



        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    tasks = Tasks()
    sys.exit(app.exec_())