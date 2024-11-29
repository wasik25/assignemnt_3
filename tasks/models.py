from django.db import models

class TaskModel(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    is_completed = models.BooleanField(default=False)
    task_assign_date = models.DateField()

    def __str__(self):
        return self.taskTitle
