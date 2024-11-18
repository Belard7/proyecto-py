from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QDateEdit, QDialogButtonBox
from PyQt5.QtCore import QDate

class AddListDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nueva Lista")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()

        self.label = QLabel("Nombre de la Lista:")
        layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_list_name(self):
        return self.line_edit.text().strip()


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Nueva Tarea")
        self.setMinimumWidth(300)

        layout = QVBoxLayout()

        self.name_label = QLabel("Nombre de la Tarea:")
        layout.addWidget(self.name_label)

        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        self.date_label = QLabel("Fecha de Vencimiento:")
        layout.addWidget(self.date_label)

        self.date_input = QDateEdit()
        self.date_input.setCalendarPopup(True)
        self.date_input.setDate(QDate.currentDate())
        layout.addWidget(self.date_input)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttons.accepted.connect(self.accept)
        self.buttons.rejected.connect(self.reject)
        layout.addWidget(self.buttons)

        self.setLayout(layout)

    def get_task_data(self):
        return self.name_input.text().strip(), self.date_input.date()
