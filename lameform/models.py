from django.db import models

class Main(models.Model):
    name = models.TextField()
    family = models.TextField()
    email = models.EmailField()
    phone = models.TextField()
    edu = models.TextField()
    work = models.TextField()
    date = models.DateTimeField()
    verify = models.SmallIntegerField()
    code = models.TextField()
    server = models.TextField()
