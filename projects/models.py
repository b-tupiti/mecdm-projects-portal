from django.db import models
from entities.models import *
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    donors = models.ManyToManyField(Donor, verbose_name="Donor Agencies",  blank=True)
    implementors = models.ManyToManyField(Implementor, verbose_name="Implementing Agencies", blank=True)
    partners = models.ManyToManyField(Partner, verbose_name="Accreditted Entities\\Partner Organizations",  blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
