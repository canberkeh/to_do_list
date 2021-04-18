from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE

date = datetime.strptime('2018-11-10 10:55:31', '%Y-%m-%d %H:%M:%S')
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    name = models.CharField(max_length=32)
    create_date = models.DateTimeField(default=datetime.now(), blank=True)

    def str(self):
        return self.name


class ToDoListItem(models.Model):
    class ToDoListItemStatus(models.TextChoices):
        UNCOMPLETED = 'UNCOMPLETED'
        COMPLETED = 'COMPLETED'
        EXPIRED = 'EXPIRED'

    todolist = models.ForeignKey(ToDoList, on_delete=CASCADE)
    name = models.CharField(max_length=32)
    description = models.TextField()
    create_date = models.DateTimeField(default=datetime.now(), blank=True)
    deadline = models.DateTimeField()
    status = models.TextField(choices=ToDoListItemStatus.choices, default=ToDoListItemStatus.UNCOMPLETED)

    def str(self):
        return self.name
