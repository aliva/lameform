from functools import partial

from lameform import models

from django.contrib import admin
from django.contrib.admin.helpers import ActionForm

class MainAdmin(admin.ModelAdmin):
    list_display = (
        'family',
        'name',
        'has_arrived',
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

    def has_arrived(self, obj):
        if obj.arrived == None:
            return False
        else:
            return True
    has_arrived.short_description = 'arrived'
    has_arrived.boolean = True

admin.site.disable_action('delete_selected')
admin.site.register(models.Main, MainAdmin)
