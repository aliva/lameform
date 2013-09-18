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
    search_fields = (
        'name',
        'family',
        'email',
    )
    actions = (
        'person_arrived',
    )
    
    def person_arrived(self, request, queryset):
        for item in queryset:
            item.mark_arrived()
    person_arrived.short_description = 'arrived'

admin.site.disable_action('delete_selected')   
admin.site.register(models.Main, MainAdmin)