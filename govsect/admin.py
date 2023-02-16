from django.contrib import admin
from .models import * 

class GovernanceTypeAdmin(admin.ModelAdmin):
    pass 
admin.site.register(GovernanceType, GovernanceTypeAdmin)

class SectorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sector,SectorAdmin)
