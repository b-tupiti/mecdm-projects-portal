from django.shortcuts import render
from users.utils import isAdminUser
from requests.models import AccountRequest
from .models import *
from entities.models import *
from .utils import searchProjects, getProjectFilters
from utils.utils import paginateItems

def Projects(request):
    
    is_admin = isAdminUser(request)
    total_requests = AccountRequest.objects.count()
    
    search_filters = getProjectFilters()
    
    projects, selected = searchProjects(request)
    custom_range, projects = paginateItems(request, projects, 5)
    
    context = {
        'is_admin':is_admin,
        'total_requests':total_requests,
        'projects': projects,
        'custom_range':custom_range,
        'search_filters' : search_filters,
        
        'selected' : selected,
    }
    
    return render(request,'projects/projects.html', context)