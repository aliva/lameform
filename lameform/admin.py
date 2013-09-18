from django.contrib import admin
from lameform import models

class MainAdmin(admin.ModelAdmin):
    list_display = (
        'family',
        'name',
        'arrived',
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
    actions = (
        'person_arriaved',
    )
    
    def person_arriaved(self, request, queryset):
        for item in queryset:
            item.mark_arrived()
    person_arriaved.short_description = 'arrived'

admin.site.disable_action('delete_selected')   
admin.site.register(models.Main, MainAdmin)