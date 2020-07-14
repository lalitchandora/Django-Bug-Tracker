from django.shortcuts import render
from .models import Bug
from projects_app.models import Project

def list_bugs(request,id):
    query_bugs = Bug.objects.filter(project_id=id)
    project_name = query_bugs[0].project_id.name
    context = {
        'bugs_list': query_bugs,
        'project_name': project_name
    }
    return render(request, 'bugs_app/bugs.html', context)