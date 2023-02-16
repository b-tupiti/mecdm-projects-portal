from django.db import models
from entities.models import *
from govsect.models import *
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    
    risk_rate = models.ForeignKey('Risk', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('ProjectType', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.SET_NULL)
    scope = models.ForeignKey('Scope', null=True, blank=True, on_delete=models.SET_NULL)
    
    donors = models.ManyToManyField(Donor, verbose_name="Donor Agencies",  blank=True)
    implementors = models.ManyToManyField(Implementor, verbose_name="Implementing Agencies", blank=True)
    partners = models.ManyToManyField(Partner, verbose_name="Accreditted Entities\\Partner Organizations",  blank=True)
    locations = models.ManyToManyField('Location', verbose_name="Project Locations",  blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    
    governance_type = models.ForeignKey(GovernanceType, verbose_name="Government or Non-government", null=True, on_delete=models.SET_NULL)
    sectors = models.ManyToManyField(Sector)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    
    
    
class ProjectType(models.Model):
    name = models.CharField(max_length=200)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name


class Risk(models.Model):
    rate = models.CharField(max_length=1)
    description = models.CharField(max_length=50)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
        
    def natural_key(self):
        return self.rate + ' - ' + self.description
    
    def __str__(self):
        return self.rate
    
    
class Status(models.Model):
    status = models.CharField(max_length=400, unique=True)
    category = models.ForeignKey('StatusCategory', null=True, blank=True, on_delete=models.SET_NULL)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def natural_key(self):
        return self.status 
    
    def __str__(self):
        return self.status
    

class StatusCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name
    
    
class Scope(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name
    

class Location(models.Model):
    name = models.CharField(max_length=400, unique=True)
    lattitude = models.FloatField(blank=True,null=True)
    longitude = models.FloatField(blank=True,null=True)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name