def prepareDataForReport(filter_group, projects):
    items = getFilterItems(filter_group, projects)
    
    
    objs = [{'filtered_by': item, 'project_count': 0, 'total_funding': 0, 'projects': []} for item in items]

    data = organizeDataForExcel(filter_group, objs, projects)
    
    return data
   

def organizeDataForExcel(filter_group, objs, projects):
    # loops through each project, get all projects that match filter,
    for project in projects:
        for obj in objs:
            if obj.get('filtered_by') in project['fields'][filter_group]:
                obj['projects'].append(project)
                obj['project_count'] = obj.get('project_count') + 1
                if project['fields']['budget_total']:
                    obj['total_funding'] = obj.get('total_funding') + float(project['fields']['budget_total'])
    
    return objs
    
def getFilterItems(filter_group, projects):
    
    # handles the filter_group 'status'. status key is a list [status, status_category], this grabs the status_category
    if filter_group == 'status':
         items = [project['fields'][filter_group][1] for project in projects]
    # handles filter_group keys 'donors' and 'implementors'   
    else:
        items_lists = [project['fields'][filter_group] for project in projects]
        items = []
        for _list in items_lists:
            items.extend(_list)

    # removes duplicate items 
    items = list(set(items))
    
    return items
    
    