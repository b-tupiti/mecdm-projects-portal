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


class StatusAdmin(admin.ModelAdmin):
    pass 
admin.site.register(Status, StatusAdmin)


class StatusCategoryAdmin(admin.ModelAdmin):
    pass 
admin.site.register(StatusCategory, StatusCategoryAdmin)
