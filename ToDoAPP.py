
import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QFrame, QWidget,
    QLineEdit, QComboBox, QToolButton, QStyle, QInputDialog, QCalendarWidget, QMenu, QAction, QDialog
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QDate

class ToDoAppModern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas ")
        self.setGeometry(200, 100, 800, 600)

        self.init_ui()
        self.load_styles()

    def init_ui(self):
        # Contenedor principal
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout()
        main_widget.setLayout(main_layout)

        # Barra lateral (Sidebar)
        sidebar = QFrame()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(200)
        sidebar_layout = QVBoxLayout()
        sidebar.setLayout(sidebar_layout)

        # Elementos de la barra lateral
        sidebar_label = QLabel("My Lists")
        sidebar_label.setFont(QFont("Arial", 14, QFont.Bold))
        sidebar_label.setAlignment(Qt.AlignCenter)
        sidebar_layout.addWidget(sidebar_label)

        self.lists_widget = QListWidget()
        self.lists_widget.setObjectName("listsWidget")
        self.lists_widget.addItems(["My Day", "Important", "Planned", "Tasks"])
        sidebar_layout.addWidget(self.lists_widget)

        add_list_button = QPushButton("New List")
        add_list_button.clicked.connect(self.add_new_list)
        sidebar_layout.addWidget(add_list_button)

        sidebar_layout.addStretch()

        # Vista principal (Main View)
        main_view = QFrame()
        main_view_layout = QVBoxLayout()
        main_view.setLayout(main_view_layout)
        main_view.setObjectName("mainView")

        # Título de la vista principal
        title_label = QLabel("My Day")
        title_label.setFont(QFont("Arial", 18, QFont.Bold))
        title_label.setAlignment(Qt.AlignLeft)
        main_view_layout.addWidget(title_label)

        # Fecha
        date_label = QLabel(QDate.currentDate().toString("dddd, d MMMM"))
        date_label.setFont(QFont("Arial", 12))
        date_label.setAlignment(Qt.AlignLeft)
        main_view_layout.addWidget(date_label)

        # Lista de tareas
        self.tasks_widget = QListWidget()
        self.tasks_widget.setObjectName("tasksWidget")
        main_view_layout.addWidget(self.tasks_widget)

        # Botón para agregar tareas (que se convertirá en el formulario)
        self.add_task_button = QPushButton("Add Task")
        self.add_task_button.setObjectName("addTaskButton")
        self.add_task_button.setFont(QFont("Arial", 14))
        self.add_task_button.clicked.connect(self.show_task_form)
        main_view_layout.addWidget(self.add_task_button)

        # Contenedor del formulario para agregar tareas (invisible al inicio)
        self.task_form = QFrame()
        self.task_form.setObjectName("taskForm")
        self.task_form.setHidden(True)
        form_layout = QVBoxLayout()
        self.task_form.setLayout(form_layout)

        # Campo para el nombre de la tarea
        self.task_name_input = QLineEdit()
        self.task_name_input.setPlaceholderText("Task name")
        form_layout.addWidget(self.task_name_input)

        # Selector de lista
        self.list_selector_layout = QHBoxLayout()
        list_label = QLabel("Select List:")
        self.list_selector = QComboBox()
        self.list_selector.addItems(["My Day", "Important", "Planned", "Tasks"])
        self.list_selector_layout.addWidget(list_label)
        self.list_selector_layout.addWidget(self.list_selector)
        form_layout.addLayout(self.list_selector_layout)

        # Opciones adicionales con íconos
        options_layout = QHBoxLayout()

        # Botón de calendario
        calendar_button = QToolButton()
        calendar_button.setIcon(QIcon("resources/icons/calendario.png"))
        calendar_button.setToolTip("Set due date")
        calendar_button.clicked.connect(self.show_calendar)
        options_layout.addWidget(calendar_button)

        # Botón de recordatorio
        reminder_button = QToolButton()
        reminder_button.setIcon(QIcon("resources/icons/reminder.png"))
        reminder_button.setToolTip("Add reminder")
        reminder_button.clicked.connect(self.show_reminder_menu)
        options_layout.addWidget(reminder_button)

        # Botón de repetición
        repeat_button = QToolButton()
        repeat_button.setIcon(self.style().standardIcon(QStyle.SP_BrowserReload))
        repeat_button.setToolTip("Set repeat option")
        repeat_button.clicked.connect(self.show_repeat_menu)
        options_layout.addWidget(repeat_button)

        form_layout.addLayout(options_layout)

        # Botón para guardar la tarea
        save_button = QPushButton("Save Task")
        save_button.setObjectName("saveTaskButton")
        save_button.clicked.connect(self.save_task)
        form_layout.addWidget(save_button)

        main_view_layout.addWidget(self.task_form)
        main_layout.addWidget(sidebar)
        main_layout.addWidget(main_view)

    def load_styles(self):
        with open("resources/styles.qss", "r") as file:
            self.setStyleSheet(file.read())

    def show_task_form(self):
        """Muestra el formulario para agregar tareas."""
        self.add_task_button.setHidden(True)
        self.task_form.setHidden(False)

    def save_task(self):
        """Guarda la tarea y vuelve al estado inicial."""
        task_name = self.task_name_input.text().strip()
        if not task_name:
            return

        selected_list = self.list_selector.currentText()
        formatted_task = f"{task_name} ({selected_list})"
        self.tasks_widget.addItem(formatted_task)

        self.task_name_input.clear()
        self.list_selector.setCurrentIndex(0)

        self.task_form.setHidden(True)
        self.add_task_button.setHidden(False)

    def add_new_list(self):
        # Funcionalidad para agregar nuevas listas
        new_list_name, ok = QInputDialog.getText(self, "New List", "Enter list name:")
        if ok and new_list_name:
            self.lists_widget.addItem(new_list_name)
            self.update_list_selector(new_list_name)

    def update_list_selector(self, new_list_name):
        """Actualiza el QComboBox con la nueva lista."""
        self.list_selector.addItem(new_list_name)

    def show_calendar(self):
        """Muestra un calendario para seleccionar una fecha."""
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Due Date")
        dialog.setModal(True)
        dialog.setFixedSize(400, 350)

        dialog_layout = QVBoxLayout(dialog)
        calendar = QCalendarWidget(dialog)

        selected_date = [None]

        calendar.clicked.connect(lambda date: self.task_name_input.setText(date.toString("d MMM yyyy")))

        dialog_layout.addWidget(calendar)
        
        def set_selected_date(date):
            selected_date[0] = date.toString("d MMM yyyy")
        
        calendar.clicked.connect(set_selected_date)
        dialog_layout.addWidget(calendar)

        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: self.save_date_and_close(dialog, selected_date))
        buttons_layout.addWidget(save_button)

        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.close)
        buttons_layout.addWidget(close_button)

        dialog_layout.addLayout(buttons_layout)

        dialog.exec_()
    
    
    def save_date_and_close(self, dialog, selected_date):
    
        if selected_date[0]:
            self.task_name_input.setText(selected_date[0])  # Coloca la fecha en el campo de texto
        dialog.close()

    def show_reminder_menu(self):
        """Muestra un menú de opciones para recordatorios."""
        menu = QMenu(self)
        menu.addAction("Remind me at a specific time")
        menu.addAction("Remind me tomorrow")
        menu.addAction("Remind me in a week")
        menu.exec_(self.cursor().pos())

    def show_repeat_menu(self):
        """Muestra un menú para las opciones de repetición."""
        menu = QMenu(self)
        menu.addAction("Repeat daily")
        menu.addAction("Repeat weekly")
        menu.addAction("Repeat annually")
        menu.exec_(self.cursor().pos())


# Ejecutar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoAppModern()
    window.show()
    sys.exit(app.exec_())