from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def load(self): pass

    @abstractmethod
    def save(self, tasks): pass
