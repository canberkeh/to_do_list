from enum import Enum

class ToDoListItemStatus(Enum):
    UNCOMPLETED = 'UNCOMPLETED'
    COMPLETED = 'COMPLETED'
    EXPIRED = 'EXPIRED'

    @classmethod
    def choices(cls):
        print(tuple((i.name, i.value) for i in cls))
        return tuple((i.name, i.value) for i in cls)
