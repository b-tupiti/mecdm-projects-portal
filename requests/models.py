from django.db import models
import uuid

class AccountRequest(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=500)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    occupation = models.CharField(max_length=200,blank=True,null=True)
    organization = models.CharField(max_length=200,blank=True,null=True)
    reason_for_request = models.TextField()
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    
    class Meta:
        ordering = ['-created']
