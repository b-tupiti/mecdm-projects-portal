from django.db import models
from django.contrib.auth.models import User
import uuid

class UserProfile(models.Model):
    
    class UserType(models.TextChoices):
        SECURE = "SECURE", "SECURE"
        ADMIN = "ADMIN", "ADMIN"
        
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    first_name = models.CharField(max_length=200,blank=True,null=True)
    last_name = models.CharField(max_length=200,blank=True,null=True)
    user_type = models.CharField(max_length=7, choices=UserType.choices, default=UserType.SECURE)
    
    
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.username
    
    class Meta:
        ordering = ['-user_type', 'username']
