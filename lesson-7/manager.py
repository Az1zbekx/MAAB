from task import Task

class TaskManager:
    def __init__(self, storage):
        self.storage = storage
        self.tasks = self.storage.load()

    def add_task(self, task):
        if any(t.task_id == task.task_id for t in self.tasks):
            raise ValueError("Task ID already exists.")
        self.tasks.append(task)

    def view_tasks(self):
        return self.tasks

    def update_task(self, task_id, **kwargs):
        for task in self.tasks:
            if task.task_id == task_id:
                task.title = kwargs.get('title', task.title)
                task.description = kwargs.get('description', task.description)
                task.due_date = kwargs.get('due_date', task.due_date)
                task.status = kwargs.get('status', task.status)
                return True
        return False

    def delete_task(self, task_id):
        initial_len = len(self.tasks)
        self.tasks = [t for t in self.tasks if t.task_id != task_id]
        return len(self.tasks) < initial_len

    def filter_tasks(self, status):
        return [t for t in self.tasks if t.status.lower() == status.lower()]

    def save_tasks(self):
        self.storage.save(self.tasks)

    def load_tasks(self):
        self.tasks = self.storage.load()
