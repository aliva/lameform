from functools import partial

from lameform import models

from django.contrib import admin
from django.contrib.admin.helpers import ActionForm

class MainAdmin(admin.ModelAdmin):
    list_display = (
        'family',
        'name',
        'arrived',
        'email',
        #'phone',
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
        'phone',
    )
    actions = (
        'person_arrived',
    )
    
    action_form = partial(ActionForm, initial={'action': 'person_arrived'})
    
    def person_arrived(self, request, queryset):
        for item in queryset:
            item.mark_arrived()
    person_arrived.short_description = 'arrived'

admin.site.disable_action('delete_selected')   
admin.site.register(models.Main, MainAdmin)