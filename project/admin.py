from django.contrib import admin
from .models import Project, ProjectCategory, Practice, Positionpractice, Usage

class ProjectCategoryAdmin(admin.ModelAdmin):
    model = ProjectCategory

class ProjectAdmin(admin.ModelAdmin):
    model = Project

class PositionpracticeAdmin(admin.ModelAdmin):
    model = Positionpractice
    list_filter = ['practice', 'project__name']
    search_fields = ['project__name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Practice)
admin.site.register(Usage)
admin.site.register(Positionpractice, PositionpracticeAdmin)
