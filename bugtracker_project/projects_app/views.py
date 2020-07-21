from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import ProjectForm
from .models import Project

def home(request):
    project_list = Project.objects.all()
    page = request.GET.get('page',1)

    paginator = Paginator(project_list,2)
    try:
        project_list = paginator.page(page)
    except PageNotAnInteger:
        project_list = paginator.page(1)
    except EmptyPage:
        project_list = paginator.page(paginator.num_pages)
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