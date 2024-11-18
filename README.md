UNIVERSIDAD GERARDO BARRIOS SAN MIGUEL
FACULTAD DE CIENCIA Y TECNOLOGÍA






ASIGNATURA:
PROGRAMACION COMPUTACIONAL III
DOCENTE:
WILLIAN GIRON
Actividad:
AVANCES
Estudiantes:
Jimmy Abelardo Rivas Lazo


Planteamiento del Problema
En la vida diaria, es común tener múltiples actividades, proyectos y compromisos, lo que puede generar desorganización, estrés y olvidos importantes.
La falta de una herramienta para organizar y gestionar estas tareas de manera simple y eficiente representa un problema para personas que buscan mejorar su productividad personal y laboral.

La solución propuesta es una Aplicación de Lista de Tareas (To-Do List) que permita a los usuarios crear, gestionar y priorizar sus actividades

 Funcionalidad Principal
La funcionalidad principal del proyecto es ofrecer una interfaz de consola donde el usuario pueda:

Añadir nuevas tareas.
Ver la lista de tareas pendientes.
Marcar tareas como completadas.
Eliminar tareas completadas o no deseadas.
El proyecto se desarrollará en Python utilizando listas o diccionarios para almacenar las tareas y el estado de cada una de ellas (pendiente o completada).
En un futuro, esta estructura básica permitirá añadir opciones de prioridad o fechas límite a cada tarea.


Avances del Proyecto
Hasta el momento, se ha logrado desarrollar una versión inicial del programa que cubre las funcionalidades básicas:

Añadir tarea: Permite al usuario agregar una nueva tarea a la lista.
Ver lista de tareas: Muestra todas las tareas pendientes y completadas con sus respectivos estados.
Marcar como completada: Permite al usuario actualizar el estado de una tarea como "completada".
Eliminar tarea: El usuario puede eliminar tareas que ya no sean relevantes o hayan sido completadas.



Objetivos Faltantes y Plan de Desarrollo
Para completar el proyecto y ofrecer una aplicación más robusta, se han identificado los siguientes objetivos pendientes:

Persistencia de Datos (30%): Implementar un sistema para guardar y cargar la lista de tareas al iniciar o cerrar la aplicación, utilizando un archivo de texto o un sistema de base de datos como SQLite. 
Esto permitirá que el usuario pueda cerrar la aplicación y conservar su lista de tareas al volver a abrirla.

Tecnologías: Librería pickle para guardar en archivos o SQLite para una solución más avanzada.

Clasificación y Filtrado de Tareas (20%): Implementar la opción de añadir prioridad o fecha límite a las tareas, permitiendo clasificarlas y filtrarlas. Esto ayudará a los usuarios a ver qué tareas son más urgentes.

Método: Añadir un campo de prioridad en cada tarea y modificar las funciones para ordenar o filtrar la lista según prioridad.
Notificaciones (10%): Crear un sistema de notificaciones para recordar al usuario tareas pendientes. Esto podría realizarse mediante notificaciones en la interfaz o mensajes en la terminal.

Tecnologías: Librería time y threading para alertas temporales o librerías de notificación como plyer.


