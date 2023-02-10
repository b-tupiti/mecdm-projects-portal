from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin)


class RiskAdmin(admin.ModelAdmin):
    pass
admin.site.register(Risk, RiskAdmin)


class ProjectTypeAdmin(admin.ModelAdmin):
    pass 
admin.site.register(ProjectType, ProjectTypeAdmin)
