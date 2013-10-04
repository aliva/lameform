import datetime

from django.db import models
from django.utils.timezone import utc

class Main(models.Model):
    name = models.TextField()
    family = models.TextField()
    email = models.EmailField()
    phone = models.TextField(blank=True, null=True, default='')
    edu = models.TextField()
    work = models.TextField(blank=True, null=True, default='')
    date = models.DateTimeField()
    verify = models.SmallIntegerField()
    code = models.TextField()
    server = models.TextField()
    arrived = models.DateTimeField(blank=True, null=True, default=None)

    class Meta:
        ordering = (
            'family',
            'name',
        )

    def __str__(self):
        return self.email

    def mark_arrived(self):
        if self.arrived != None:
            return
        self.arrived = datetime.datetime.utcnow().replace(tzinfo=utc)
        self.save()
