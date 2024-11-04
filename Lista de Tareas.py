import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel, QListWidgetItem
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Configuración inicial de la ventana
        self.setWindowTitle("Lista de Tareas")
        self.setGeometry(100, 100, 400, 300)
        
        # Layout principal
        self.layout = QVBoxLayout()
        
        # Lista de tareas
        self.task_list = QListWidget()
        
        # Campo de texto para añadir nueva tarea
        self.new_task_input = QLineEdit()
        self.new_task_input.setPlaceholderText("Escribe una nueva tarea aquí...")
        
        # Botones
        self.add_task_button = QPushButton("Agregar Tarea")
        self.add_task_button.clicked.connect(self.add_task)
        
        self.complete_task_button = QPushButton("Marcar como Completada")
        self.complete_task_button.clicked.connect(self.complete_task)
        
        self.delete_task_button = QPushButton("Eliminar Tarea")
        self.delete_task_button.clicked.connect(self.delete_task)
        
        # Organizar botones en un layout horizontal
        button_layout = QHBoxLayout()
        button_layout.addWidget(self.add_task_button)
        button_layout.addWidget(self.complete_task_button)
        button_layout.addWidget(self.delete_task_button)
        
        # Agregar widgets al layout principal
        self.layout.addWidget(QLabel("Lista de Tareas:"))
        self.layout.addWidget(self.task_list)
        self.layout.addWidget(self.new_task_input)
        self.layout.addLayout(button_layout)
        
        # Configurar el layout para la ventana
        self.setLayout(self.layout)
    
    def add_task(self):
        """Añadir una nueva tarea a la lista."""
        task_text = self.new_task_input.text().strip()
        if task_text:
            # Añadir tarea a la lista con el texto ingresado
            item = QListWidgetItem(task_text)
            self.task_list.addItem(item)
            self.new_task_input.clear()
    
    def complete_task(self):
        """Marcar la tarea seleccionada como completada."""
        current_item = self.task_list.currentItem()
        if current_item:
            # Cambiar el estilo del texto para indicar que está completada
            current_item.setForeground(QColor("gray"))
            font = current_item.font()
            font.setStrikeOut(True)  # Tachar el texto
            current_item.setFont(font)
    
    def delete_task(self):
        """Eliminar la tarea seleccionada."""
        current_row = self.task_list.currentRow()
        if current_row >= 0:
            # Eliminar la tarea de la lista
            self.task_list.takeItem(current_row)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
