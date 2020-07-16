from django.shortcuts import render, redirect, reverse
from .models import Bug
from projects_app.models import Project
from .forms import AddBugForm

def list_bugs(request,id):
    query_bugs = Bug.objects.filter(project_id=id)
    project = Project.objects.filter(id = id)[0]

    context = {
        'bugs_list': query_bugs,
        'project': project
    }
    return render(request, 'bugs_app/bugs.html', context)

def bug_add(request,project_id):

    if request.method == "POST":
        form = AddBugForm(request.POST)
        if form.is_valid():
            project = Project.objects.filter(id=project_id)[0]

            bug = form.save(commit = False)
            bug.project_id = project
            bug.save()
            a = reverse('bug_list', args=[project_id])
            
            return redirect(a)
            
    else:
        form = AddBugForm()
        
    context = {
        'form': form
    }

    return render(request,'bugs_app/addbugs.html', context)

def bug_delete(request,project_id,bug_id):
    project = Project.objects.filter(id = project_id)[0]
    bug = Bug.objects.filter(project_id = project,id = bug_id)[0]
    bug.delete()
    return redirect(reverse('bug_list', args=[project_id]))
