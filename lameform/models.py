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
    date = models.DateTimeField()
    verify = models.SmallIntegerField()
    code = models.TextField(blank=True, null=True, default='')
    server = models.TextField(blank=True, null=True, default='')
    arrived = models.DateTimeField(blank=True, null=True, default=None)
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
