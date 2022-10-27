from django.db import models
# Create your models here.

class Study(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 250)
    start = models.IntegerField()
    end = models.IntegerField()
    place = models.CharField(max_length = 250)
    description = models.TextField()

    def __str__(self):
        return self.title

class Work(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 250)
    start = models.IntegerField()
    end = models.CharField(max_length = 50)
    place = models.CharField(max_length = 250)
    tasks = models.JSONField()

    def __str__(self):
        return self.title