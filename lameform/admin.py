from django.contrib import admin
from lameform import models

class MainAdmin(admin.ModelAdmin):
    list_display = (
        'family',
        'name',
        'email',
        'phone',
        'edu',
        'work',
        #'date',
        'verify',
        #'code',
        #'server',
    )
    order_by = (
        'family',
        'name',
    )

admin.site.register(models.Main, MainAdmin)