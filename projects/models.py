from django.db import models
from entities.models import *
from govsect.models import *
import uuid


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,null=True)
    goals_objectives = models.TextField(blank=True,null=True)
    outcomes_outputs = models.TextField(blank=True,null=True)
    lessons_learned = models.TextField(blank=True,null=True)
    financial_notes = models.TextField(blank=True,null=True)
    milestones = models.TextField(blank=True,null=True)
    
    internal_comments = models.TextField(blank=True,null=True)
    external_comments = models.TextField(blank=True,null=True)
    status_notes = models.TextField(blank=True,null=True)
    
    start_date = models.DateField(blank=True,null=True)
    completion_date = models.DateField(blank=True,null=True)
    cn_submitted_date = models.DateField(blank=True,null=True)
    
    budget_total = models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    co_budget_total = models.DecimalField(max_digits=20,decimal_places=2,blank=True,null=True)
    
    risk_rate = models.ForeignKey('Risk', null=True, blank=True, on_delete=models.SET_NULL)
    type = models.ForeignKey('ProjectType', null=True, blank=True, on_delete=models.SET_NULL)
    status = models.ForeignKey('Status', null=True, blank=True, on_delete=models.SET_NULL)
    scope = models.ForeignKey('Scope', null=True, blank=True, on_delete=models.SET_NULL)
    
    gfmis_codes = models.CharField(max_length=100, blank=True, null=True)
    num_beneficiaries = models.IntegerField(blank=True, null=True)
    tonnes_co2_avoided = models.IntegerField(blank=True, null=True)
    
    contacts = models.TextField(null=True,blank=True)
    
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
    
    def __str__(self):
        return self.title
    
    
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