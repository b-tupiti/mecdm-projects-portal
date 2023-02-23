from django.shortcuts import render, redirect
from users.utils import isAdminUser
from requests.models import AccountRequest
from .models import *
from entities.models import *
from .utils.search import searchProjects
from .utils.generator import generateReport, createRowItemsFromJson, generateSingleSpreadsheet, filterForReportType
from .utils.filter import getProjectFilters
from utils.utils import paginateItems
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import json
from .utils.utils import *
from django.contrib import messages



def Projects(request):
    
    is_admin = isAdminUser(request)
    total_requests = AccountRequest.objects.count()
    
    search_filters = getProjectFilters()
    
    filtered_projects, selected = searchProjects(request)
    
    custom_range, projects = paginateItems(request, filtered_projects, 5)
    
    # for options in the generate report category
    report_options = {
        'donors' : 'donors',
        'implementors' : 'implementors',
        'status' : 'status',
    }
    
    context = {
        'is_admin':is_admin,
        'total_requests':total_requests,
        'projects': projects,
        'custom_range':custom_range,
        'search_filters' : search_filters,
        
        'selected' : selected,
        
        # serializing the filtered projects so that it can be returned via a post request from either the Generate Report or Extract Data buttons
        'serialized_projects' : serializers.serialize('json', filtered_projects,  use_natural_foreign_keys=True),
        
        'report_by': report_options,
    }
    
    return render(request,'projects/projects.html', context)



def SingleProject(request, pk):
    
    project = Project.objects.get(id=pk)
    documents = Document.objects.filter(project=project)
    
    context = {
        'project':project,
        'documents': documents,
    }
    
    return render(request,'projects/project.html', context)


def ExportProjects(request):
    
    if request.method == "POST":
        
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="exported_projects.xls"'

        data = request.POST.get('data')
        
        items, col_titles = createRowItemsFromJson(data)
        
        generateSingleSpreadsheet(
            response,               
            'Generated Projects',   
            items,                  
            col_titles,             
        )
        
        return response
    
    else:
        return redirect('projects')




def GenerateReport(request):
    """
    generates a summary report based on the option selected by the user.
    options: By Donor, By Implementing Agency, By Status Category
    """
    if request.method == "POST":
        
        if request.POST.get('filter_group'):

            if request.POST.get('data') is not None:
                
                # get POST data
                filter_group = request.POST.get('filter_group')
                projects = json.loads(request.POST.get('data'))
                
                # prepare data
                data = prepareDataForReport(filter_group, projects)
                
                # generate report and saving it to response object
                response = HttpResponse(content_type='application/ms-excel')
                generateReport(filter_group, data, response)
                
                # name the file
                filename = "generated-report-by_"+filter_group
                response['Content-Disposition'] = 'attachment; filename="'+filename+'.xls"'
                
                return response
                
            else:
                messages.error(request, 'No projects to apply filter on')
                return redirect('projects')
        else:
            messages.info(request, 'Select an option to generate a report by')
            
    return redirect('projects')
   