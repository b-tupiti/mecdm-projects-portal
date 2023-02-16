from django.db import models
import uuid

class GovernanceType(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name



class Sector(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def natural_key(self):
        return self.name 
    
    def __str__(self):
        return self.name