class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

    def __str__(self):
        return f"{self.description} (дедлайн: {self.deadline}; статус: {"выполнено" if self.status else "не выполнено"})"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Задача {task} добавлена')

    def mark_done(self, task_index):
        task = self.tasks[task_index]
        print(f'Задача {task} отмечена выполненной')
        task.status = True

    def get_current_tasks(self):
        return [task for task in self.tasks if not task.status]

    def __iter__(self):
        return iter(self.tasks)


manager = TaskManager()

while True:
    description = input("Введите название задачи (или 'выход' для завершения ввода): ")
    if description.lower() == "выход":
        break
    deadline = input("Введите дедлайн задачи: ")
    task = Task(description, deadline)
    manager.add_task(task)

print("Список задач:")
for i, task in enumerate(manager, start=1):
    print(f"{i}. {task}")

while True:
    try:
        manager.mark_done(int(input("Введите номер выполненной задачи (или букву для выхода): ")) - 1)
        print("Ваш список задач:")
        for i, task in enumerate(manager, start=1):
            print(f"{i}. {task}")
        continue
    except:
        print('Увидимся, жидкий гомо!')
        break

# for task in manager.get_current_tasks():
#    print(task)
