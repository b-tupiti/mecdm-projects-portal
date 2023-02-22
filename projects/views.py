from django.shortcuts import render, redirect
from users.utils import isAdminUser
from requests.models import AccountRequest
from .models import *
from entities.models import *
from .utils.search import searchProjects
from .utils.generator import generateReport, createRowItemsFromJson, generateSingleSpreadsheet, filterProjectsForReport
from .utils.filter import getProjectFilters
from utils.utils import paginateItems
from django.http import HttpResponse, JsonResponse
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
        
        # serializing the filtered projects so that it can be returned via a post request from either the Generate Report or Extract Data buttons
        'serialized_projects' : serializers.serialize('json', filtered_projects,  use_natural_foreign_keys=True),
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
    
    if request.method == "POST":
        
        if request.POST.get('generate-report'):
            
            # the type of report to be generated and the projects to generate report for
            report_type = request.POST.get('generate-report')
            data = request.POST.get('data')
            
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="report.xls"'
            
            results = filterProjectsForReport(data, report_type)
            
            generateReport(
                results,
                response,
            )
            
            return response
            
        else:
            return HttpResponse('<p>Select a category for generating reports in the dropdown </p>')
        
    return redirect('projects')
   