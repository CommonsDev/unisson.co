from django.contrib import admin

# Register your models here.
from django_mailman.models import List

class MailingListAdmin(admin.ModelAdmin):
    model = List
    
admin.site.register(List, MailingListAdmin)