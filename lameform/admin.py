from django.contrib import admin
from lameform import models

class MainAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Main, MainAdmin)