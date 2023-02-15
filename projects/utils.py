from .models import *
from django.db.models import Q
import json

def searchProjects(request):
    
    query = Q()
    
    keywords = ''
    if request.GET.get('keywords'):
        keywords = request.GET.get('keywords')
        query.add(Q(title__icontains=keywords),Q.AND)
     
    selected_status = ''
    if request.GET.get('status'):
        selected_status = request.GET.get('status')
        query.add(Q(status__status__icontains=selected_status),Q.AND)
        
    selected_category = ''
    if request.GET.get('category'):
        selected_category = request.GET.get('category')
        query.add(Q(status__category__name__icontains=selected_category),Q.AND)
        
    selected_donor = ''
    if request.GET.get('donor'):
        selected_donor = request.GET.get('donor')
        donor = Donor.objects.filter(name__iexact=selected_donor)
        query.add(Q(donors__in=donor),Q.AND)
        
    selected_implementor = ''
    if request.GET.get('implementor'):
        selected_implementor = request.GET.get('implementor')
        implementor = Implementor.objects.filter(name__iexact=selected_implementor)
        query.add(Q(implementors__in=implementor),Q.AND)
        
    selected_partner = ''
    if request.GET.get('partner'):
        selected_partner = request.GET.get('partner')
        partner = Partner.objects.filter(name__iexact=selected_partner)
        query.add(Q(partners__in=partner),Q.AND)
        
    selected_type = ''
    if request.GET.get('type'):
        selected_type = request.GET.get('type')
        query.add(Q(type__name__icontains=selected_type),Q.AND)
        
    selected_risk = ''
    if request.GET.get('risk'):
        selected_risk = request.GET.get('risk')
        query.add(Q(risk_rate__rate__icontains=selected_risk),Q.AND)
    
    projects = Project.objects.filter(query)
    
    tags = ''
    if request.GET.get('tags'):
        # split tags
        tags = request.GET.get('tags').replace(" ","").split(',')
        # filter first tag
        projects = projects.filter(tags__in=Tag.objects.filter(name__icontains=tags[0]))
        # chain consecutive tags in list
        for tag in tags[1:]:
            projects = projects.filter(tags__in=Tag.objects.filter(name__icontains=tag))
        
        tags = ','.join(str(tag) for tag in tags)  

   
    selected = {
        'keywords' : keywords,
        'tags' : tags,
        'selected_status': selected_status,
        'selected_category': selected_category,
        'selected_donor': selected_donor,
        'selected_implementor': selected_implementor, 
        'selected_partner': selected_partner, 
        'selected_type': selected_type, 
        'selected_risk': selected_risk, 
    }

    return projects, selected

def getProjectFilters():
    search_filters = {
        'donors' :  Donor.objects.all(),
        'implementors': Implementor.objects.all(),
        'partners': Partner.objects.all(),
        'risks': Risk.objects.all(),
        'types': ProjectType.objects.all(),
        'categories': StatusCategory.objects.all(),
        'statuses': Status.objects.all(),
    }
    return search_filters

def getDataForExcel():
    
    # grab queryset
    projects = Project.objects.all()
    
    # traverse queryset, generate dictionary from each object, append to list
    projects_list = []
    for project in projects:
        projects_list.append(
            { 
                'id': str(project.id),
                'title' : str(project.title),
                'description' : str(project.description),
                'risk_rate' : str(project.risk_rate),
                'type' : str(project.type),
                'status' : str(project.status),
                'donors' : ','.join(str(item) for item in [item for item in project.donors.values_list('name', flat=True)]),
                'implementors' : ','.join(str(item) for item in [item for item in project.implementors.values_list('name', flat=True)]),
                'partners' : ','.join(str(item) for item in [item for item in project.partners.values_list('name', flat=True)]),
                'tags' : ','.join(str(item) for item in [item for item in project.tags.values_list('name', flat=True)]),
            }
        )
    
    # return list 
    return projects_list
       
def createRowItemsFromJSON(data):
    
    data = json.loads(data)
    
    col_headers = [
        'Id', 
        'Title',
        'Description',
        'Risk Rate',
        'Type',
        'Status',
        'Donors',
        'Implementing Agencies',
        'Partner Organisations\\Acreddited Entites',
        'Tags'
        ]
    
    project_list = []
    for project in data:
        print(project)
        project_list.append([
            project['pk'],
            project['fields']['title'],
            project['fields']['description'],
            project['fields']['risk_rate'],
            project['fields']['type'],
            project['fields']['status'],
            ', '.join(item for item in project['fields']['donors']),
            ', '.join(item for item in project['fields']['implementors']),
            ', '.join(item for item in project['fields']['partners']),
            ', '.join(item for item in project['fields']['tags']),
        ])
        
    return col_headers, project_list   
        

       
       
       
       
       
    

    
    
    
    
    