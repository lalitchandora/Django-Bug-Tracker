from django.shortcuts import render, redirect
from .forms import ProjectForm
from .models import Project

def home(request):
    project_list = Project.objects.all()
    context = {
        'projects': project_list,
    }
    return render(request, 'projects_app/home.html', context)

def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProjectForm()    
    
    context = {
        'form': form
    }
    return render(request, 'projects_app/add_project.html',context)