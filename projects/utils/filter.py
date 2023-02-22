from projects.models import Donor, Implementor, Partner, Risk, ProjectType, StatusCategory, Status
import json


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

def filterProjectsForReport(data, report_type):
    
    projects = json.loads(data)
    
    # grab donors from each project
    donors_lists = [project['fields']['donors'] for project in projects]  

    # extend all donors list to a donors list so that it becomes a list of strings
    donors = []
    for _list in donors_lists:
        donors.extend(_list)

    # remove duplicate donors
    donors = list(set(donors))
    
    donor_objs = []
    for donor in donors:
        donor_objs.append({
            'name': donor,
            'project_count': 0,
            'total_funding': 0,
        })
    
    
    for project in projects:
        for donor in donor_objs:
            if donor.get('name') in project['fields']['donors']:
                donor['project_count'] = donor.get('project_count') + 1
                if project['fields']['budget_total']:
                    donor['total_funding'] = donor.get('total_funding') + float(project['fields']['budget_total'])
    
    return donor_objs