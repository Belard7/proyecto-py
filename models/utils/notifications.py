from plyer import notification

def notify_task(task):
    notification.notify(
        title='Recordatorio de Tarea',
        message=task,
        timeout=10
    )
