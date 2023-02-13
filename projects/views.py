from django.shortcuts import render
from users.utils import isAdminUser
from requests.models import AccountRequest
from .models import *
from entities.models import *
from .utils import searchProjects, getProjectFilters


def Projects(request):
    
    is_admin = isAdminUser(request)
    total_requests = AccountRequest.objects.count()
    
    search_filters = getProjectFilters()
    
    projects, selected = searchProjects(request)
    
    
    context = {
        'is_admin':is_admin,
        'total_requests':total_requests,
        'projects': projects,
        'search_filters' : search_filters,
        
        'selected' : selected,
    }
    
    return render(request,'projects/projects.html', context)