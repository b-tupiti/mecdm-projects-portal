from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from users.utils import isAdminUser
from django.shortcuts import redirect
from requests.models import AccountRequest
from .models import Project
from entities.models import *

def Projects(request):
    
    is_admin = isAdminUser(request)
    total_requests = AccountRequest.objects.count()
    
    projects = Project.objects.all()
   
    search_filters = {
        'donors' :  Donor.objects.all(),
        'implementors': Implementor.objects.all(),
        'partners': Partner.objects.all(),
    }
    
    context = {
        'is_admin':is_admin,
        'total_requests':total_requests,
        'projects': projects,
        'search_filters' : search_filters,
    }
    
    return render(request,'projects/projects.html', context)