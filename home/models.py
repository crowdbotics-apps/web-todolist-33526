from django.conf import settings
from django.db import models


class TodoList(models.Model):
    "Generated Model"
    todo = models.CharField(
        max_length=256,
    )
    description = models.TextField()
    duedate = models.DateTimeField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="todolist_user",
    )
