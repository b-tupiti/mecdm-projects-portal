from django.db import models
import uuid



class Donor(models.Model):
    name = models.CharField(max_length=300)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name
   
   
    
class Partner(models.Model):
    name = models.CharField(max_length=300)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name
    
    
    
class Implementor(models.Model):
    name = models.CharField(max_length=300)
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name


