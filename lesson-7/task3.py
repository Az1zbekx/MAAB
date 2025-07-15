from dataclasses import dataclass
@dataclass
class Task:
    task_id: str
    title: str
    description: str
    due_date: str
    status: str

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Task(**data)
