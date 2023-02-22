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

