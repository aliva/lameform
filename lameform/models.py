import datetime

from django.db import models
from django.utils.timezone import utc

class Main(models.Model):
    name = models.TextField()
    family = models.TextField()
    email = models.EmailField(blank=True, null=True, default='')
    phone = models.TextField(blank=True, null=True, default='')
    edu = models.TextField(blank=True, null=True, default='')
    work = models.TextField(blank=True, null=True, default='')
    date = models.DateTimeField(default=datetime.datetime(2013, 9, 21, 12, 30).replace(tzinfo=utc))
    verify = models.SmallIntegerField(default=0)
    code = models.TextField(blank=True, null=True, default='')
    server = models.TextField(blank=True, null=True, default='')
    arrived = models.BooleanField(default=True)
    arrive_time = models.DateTimeField(blank=True, null=True)
    registered_on_site = models.BooleanField()

    registered_on_site.verbose_name = 'net reg'

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
