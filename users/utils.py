from .models import UserProfile
from django.contrib.auth.models import User

import secrets
import string

def isAdminUser(request):
    
    is_admin = False
    
    try:
        user = User.objects.get(id=request.user.id)  
        profile = UserProfile.objects.get(user=user) 
        if profile.user_type == 'ADMIN':
            is_admin = True
    except:
        print('User does not have a profile')
        
    return is_admin

def generatePassword():
    generatedPassword = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for i in range(8))
    return generatedPassword



