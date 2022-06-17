from django.db import models


# class SubTasks(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     status = models.BooleanField(default=False)


class Todo(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    status = models.BooleanField(default=False)
