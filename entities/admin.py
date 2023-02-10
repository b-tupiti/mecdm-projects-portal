from django.contrib import admin
from .models import Donor, Partner, Implementor

admin.site.register(Donor)
admin.site.register(Partner)
admin.site.register(Implementor)
