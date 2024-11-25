import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QLabel, QFrame, QWidget,
    QLineEdit, QComboBox, QToolButton, QStyle, QInputDialog, QCalendarWidget, QMenu, QAction, QDialog,
    QListWidgetItem, QCheckBox
)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt, QDate, QSize


class ToDoAppModern(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(200, 100, 800, 600)
        
        self.tasks_dict = { "My Day": [], "Important": [], "Planned": [], "Tasks": [] }

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
        self.lists_widget.itemClicked.connect(self.change_list)


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
        self.title_label = QLabel("My Day")
        self.title_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.title_label.setAlignment(Qt.AlignLeft)
        main_view_layout.addWidget(self.title_label)

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
        """Guarda la tarea con un círculo como botón de completado."""
        task_name = self.task_name_input.text().strip()
        if not task_name:
            return

        selected_list = self.list_selector.currentText()
        formatted_task = f"{task_name} - {selected_list}"

        # Crear un nuevo QListWidgetItem
        task_item = QListWidgetItem()

        # Crear un contenedor horizontal para el checkbox y la etiqueta
        container_widget = QWidget()
        container_layout = QHBoxLayout()
        container_layout.setContentsMargins(0, 0, 0, 0)

        # Crear el checkbox
        checkbox = QCheckBox()
        checkbox.setToolTip("Mark as completed")
        checkbox.stateChanged.connect(lambda: self.toggle_task_completion(checkbox))

        # Crear la etiqueta para la tarea
        task_label = QLabel(formatted_task)
        task_label.setFont(QFont("Arial", 12))

        # Agregar checkbox y etiqueta al contenedor
        container_layout.addWidget(checkbox)
        container_layout.addWidget(task_label)
        container_layout.addStretch()
        container_widget.setLayout(container_layout)

        # tamano del widget
        task_item.setSizeHint(QSize(400, 50))  
        self.tasks_widget.addItem(task_item)
        self.tasks_widget.setItemWidget(task_item, container_widget)

        if selected_list not in self.tasks_dict:
            self.tasks_dict[selected_list] = []
        self.tasks_dict[selected_list].append(formatted_task)
        # Reiniciar el formulario
        self.task_name_input.clear()
        self.list_selector.setCurrentIndex(0)
        self.task_form.setHidden(True)
        self.add_task_button.setHidden(False)

        self.update_main_view(selected_list)
    
    def update_main_view(self, selected_list):
        self.tasks_widget.clear()
        self.title_label.setText(selected_list)

        tasks = self.tasks_dict.get(selected_list, [])
        for task in tasks:
            task_item = QListWidgetItem(task)
            self.tasks_widget.addItem(task_item)

    def change_list(self, item):
        selected_list = item.text()
        self.update_main_view(selected_list)


    def toggle_task_completion(self, checkbox):
        """Marca o desmarca la tarea como completada."""
        parent_widget = checkbox.parentWidget()
        label = parent_widget.findChild(QLabel)
        if label:
            if checkbox.isChecked():
                label.setStyleSheet("color: grey;")
            else:
                label.setStyleSheet("color: white;")

    

    def add_new_list(self):
        """Agrega una nueva lista a la barra lateral."""
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
        dialog_layout.addWidget(calendar)

        selected_date = [None]

        def set_selected_date(date):
            selected_date[0] = date.toString("d MMM yyyy")

        calendar.clicked.connect(set_selected_date)

        buttons_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        save_button.clicked.connect(lambda: self.append_date_to_task(dialog, selected_date))
        buttons_layout.addWidget(save_button)

        close_button = QPushButton("Close")
        close_button.clicked.connect(dialog.close)
        buttons_layout.addWidget(close_button)

        dialog_layout.addLayout(buttons_layout)
        dialog.exec_()

    def append_date_to_task(self, dialog, selected_date):
        """Agrega la fecha seleccionada al nombre de la tarea."""
        if selected_date[0]:
            current_text = self.task_name_input.text().strip()
            if current_text:
                self.task_name_input.setText(f"{current_text} ({selected_date[0]})")
            else:
                self.task_name_input.setText(f"({selected_date[0]})")
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
