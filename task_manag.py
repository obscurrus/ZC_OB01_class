class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def __str__(self):
        return "{} (дедлайн: {}; статус: {})".format(self.description, self.deadline,
                                                     "выполнено" if self.status else "не выполнено")


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Задача {task} добавлена')

    def mark_done(self, task_index):
        task = self.tasks[task_index]
        task.status = True
        print(f'Задача {task} отмечена выполненной')

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.status]

    def __iter__(self):
        return iter(self.tasks)


manager = TaskManager()

task1 = Task("Купить молоко", "2023-03-10")
task2 = Task("Сдать проект", "2023-03-20")
task3 = Task("Позвонить родителям", "2023-03-15")

manager.add_task(task1)
manager.add_task(task2)
manager.add_task(task3)

print("Список текущих задач:")
for task in manager.get_current_tasks():
    print(task)

manager.mark_done(0)

print("Список текущих задач после выполнения задачи:")
for task in manager.get_current_tasks():
    print(task)
