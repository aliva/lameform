from functools import partial

from lameform import models

from django.contrib import admin
from django.contrib.admin.helpers import ActionForm

class HasArrivedListFilter(admin.SimpleListFilter):
    title = 'arrived'
    parameter_name = 'hasarrived_param'

    def lookups(self, request, model_admin):
        return (
            ('1', 'arrived'),
            ('0', 'not arrived')
        )

    def queryset(self, request, queryset):
        if self.value() == '0':
            return queryset.filter(arrived=None)
        elif self.value() == '1':
            return queryset.all().exclude(arrived=None)

class MainAdmin(admin.ModelAdmin):
    list_display = (
        'family',
        'name',
        #'arrived',
        'has_arrived',
        'email',
        #'phone',
        'edu',
        'work',
        'date',
        'has_verified',
        #'code',
        #'server',
    )
    list_filter = (
        HasArrivedListFilter,
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

    def has_verified(self, obj):
        return obj.verify
    has_verified.short_description = 'verified'
    has_verified.boolean = True

admin.site.disable_action('delete_selected')
admin.site.register(models.Main, MainAdmin)
