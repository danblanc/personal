from django.db import models
import datetime as dt
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

class Types(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 10)

    def __str__(self):
        return self.name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    img_tec = models.ImageField(upload_to = 'core')
    img_proj = models.ImageField(upload_to = 'core')
    url = models.URLField(null = True)
    desc = models.CharField(max_length = 250)
    type = models.ForeignKey(Types, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.desc

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length = 250)
    intro =  models.TextField()
    url = models.URLField(null = True)
    date = models.DateTimeField(default=dt.datetime.now())

    def __str__(self):
        return self.title