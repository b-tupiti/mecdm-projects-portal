from django.shortcuts import render, redirect
from users.utils import isAdminUser
from requests.models import AccountRequest
from .models import *
from entities.models import *
from .utils import *
from utils.utils import paginateItems, generateSingleSpreadsheet
from django.http import HttpResponse
from django.core import serializers

def Projects(request):
    
    is_admin = isAdminUser(request)
    total_requests = AccountRequest.objects.count()
    
    search_filters = getProjectFilters()
    
    filtered_projects, selected = searchProjects(request)
    
    custom_range, projects = paginateItems(request, filtered_projects, 5)
    
    context = {
        'is_admin':is_admin,
        'total_requests':total_requests,
        'projects': projects,
        'custom_range':custom_range,
        'search_filters' : search_filters,
        
        'selected' : selected,
        
        'serialized_projects' : serializers.serialize('json', filtered_projects,  use_natural_foreign_keys=True),
    }
    
    return render(request,'projects/projects.html', context)



def ExportProjects(request):
    
    if request.method == "POST":
        
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="exported_projects.xls"'

        data = request.POST.get('data')
        
        items, col_titles = createRowItemsFromJSON(data)
        
        generateSingleSpreadsheet(
            response,               
            'Generated Projects',   
            items,                  
            col_titles,             
        )

        return response
    
    else:
        return redirect('projects')
