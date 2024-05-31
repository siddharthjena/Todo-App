from django.db import models

# Create your models here.
class TodoList(models.Model):
    task = models.CharField(max_length=250)
    task_status = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return  self.task
    

class Task_History(models.Model):
    date = models.DateTimeField(default=0)
    completed = models.IntegerField(default=0)
    incompleted =  models.IntegerField(default=0)

    def __str__(self):
        return self.completed