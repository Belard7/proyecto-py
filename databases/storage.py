import json

def save_tasks(task_list):
    tasks = [task_list.item(i).text() for i in range(task_list.count())]
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def load_tasks(task_list):
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            task_list.addItems(tasks)
    except FileNotFoundError:
        pass
