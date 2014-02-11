from django.contrib import admin
# Register your models here.
from django_mailman.models import List
from .models import WorkGroup
from cms.admin.placeholderadmin import PlaceholderAdmin

class MailingListAdmin(admin.ModelAdmin):
    model = List

class WorkGroupAdmin(admin.ModelAdmin):
    model= WorkGroup

admin.site.register(WorkGroup, WorkGroupAdmin)
admin.site.register(List, MailingListAdmin)