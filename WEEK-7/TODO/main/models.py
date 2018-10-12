from django.db import models

class Owner(models.Model):
    name = models.CharField('Owner', max_length=50)
    def __str__(self):
        return self.name

class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_created = models.DateTimeField('Created', '', auto_now_add=True)
    task_due_on = models.DateTimeField('Due on')
    task_owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    task_done = models.NullBooleanField('Done')
    def __str__(self):
        return self.task_title

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.email

