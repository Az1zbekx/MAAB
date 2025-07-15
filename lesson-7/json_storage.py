import json
from task import Task
from storage import Storage
class JSONStorage(Storage):
    def __init__(self, filename):
        self.filename = filename

    def save(self, tasks):
        with open(self.filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=2)

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return [Task.from_dict(d) for d in data]
        except FileNotFoundError:
            return []
