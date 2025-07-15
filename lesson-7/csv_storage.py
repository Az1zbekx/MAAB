import csv
from task import Task
from storage import Storage
class CSVStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=Task('', '', '', '', '').to_dict().keys())
            writer.writeheader()
            for task in tasks:
                writer.writerow(task.to_dict())

    def load(self):
        tasks = []
        try:
            with open(self.filename, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    tasks.append(Task.from_dict(row))
        except FileNotFoundError:
            pass
        return tasks
