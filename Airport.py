import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class Airport:
    def __init__(self):
        self.employees = []

    def hire_employee(self, employee):
        self.employees.append(employee)
        print(f"{employee.get_full_name()} был принят на работу в качестве {employee.post} с окладом в рразмере {employee.salary} рублей")

    def fire_employee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)
            print(f"{employee.get_full_name()} было отказано")
        else:
            print("Сотрудник не найден")


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Анкета Airline'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Создаем поля для ввода информации о сотруднике
        first_name_label = QLabel('Имя:')
        self.first_name_edit = QLineEdit()
        last_name_label = QLabel('Фамилия:')
        self.last_name_edit = QLineEdit()
        post_label = QLabel('Должность:')
        self.post_edit = QLineEdit()
        salary_label = QLabel('Зарплата:')
        self.salary_edit = QLineEdit()

        # Создаем кнопки для найма и увольнения сотрудника
        hire_button = QPushButton('Принят')
        hire_button.clicked.connect(self.hire_employee)
        fire_button = QPushButton('Отказно')
        fire_button.clicked.connect(self.fire_employee)

        # Создаем вертикальный макет и добавляем в него элементы управления
        layout = QVBoxLayout()
        layout.addWidget(first_name_label)
        layout.addWidget(self.first_name_edit)
        layout.addWidget(last_name_label)
        layout.addWidget(self.last_name_edit)
        layout.addWidget(post_label)
        layout.addWidget(self.post_edit)
        layout.addWidget(salary_label)
        layout.addWidget(self.salary_edit)
        layout.addWidget(hire_button)
        layout.addWidget(fire_button)

        self.setLayout(layout)
        self.show()

    def hire_employee(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()
        post = self.post_edit.text()
        salary = self.salary_edit.text()

        employee = Employee(first_name, last_name, post, salary)
        company.hire_employee(employee)

    def fire_employee(self):
        first_name = self.first_name_edit.text()
        last_name = self.last_name_edit.text()

        for employee in company.employees:
            if employee.first_name == first_name and employee.last_name == last_name:
                company.fire_employee(employee)
                break

class Employee:
    def __init__(self, first_name, last_name, post, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.post = post
        self.salary = salary

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


if __name__ == '__main__':
    company = Airport()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
