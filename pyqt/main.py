import sys
import task
# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QLineEdit, QTextEdit, QDialog, QVBoxLayout)


class Tasks(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def add_task(self):
        task.add(self.name_task_e.text(), self.body_task_e.toPlainText())
        self.name_task_e.clear()
        self.body_task_e.clear()

    def del_task(self):
        task.delete(self.name_task_e.text())
        self.name_task_e.clear()
        self.body_task_e.clear()

    def all_task(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Дополнительное окно")
        self.dialog.setGeometry(100, 100, 400, 300)
        
        result = task.all()
        print(result)
        result_str = ''
        for t in result:
            name = t['name']
            body = t['body']
            date = t['date']
            result_str += f'Название: {name}\nЗаметка: {body}\nВремя: {date}\n----------------------\n\n'
        
        layout = QVBoxLayout()
        layout.addWidget(QLabel(result_str))
        self.dialog.setLayout(layout)
        
        self.dialog.show()

    def initUI(self):
        #Создаем окно
        self.resize(500, 300)
        self.move(300, 300)
        self.setWindowTitle('Заметки')

        # Создаем кнопку
        btn1 = QPushButton('Добавить заметку', self)
        btn1.resize(btn1.sizeHint())
        btn1.move(30, 100)
        btn1.clicked.connect(self.add_task)

        # Создаем кнопку
        btn2 = QPushButton('Удалить заметку', self)
        btn2.resize(btn2.sizeHint())
        btn2.move(30, 140)
        btn2.clicked.connect(self.del_task)

        # Создаем кнопку
        btn3 = QPushButton('Найти заметку', self)
        btn3.resize(btn3.sizeHint())
        btn3.move(30, 180)

        # Создаем кнопку
        btn4 = QPushButton('Все заметки', self)
        btn4.resize(btn4.sizeHint())
        btn4.move(30, 220)
        btn4.clicked.connect(self.all_task)

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