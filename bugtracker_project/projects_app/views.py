from django.shortcuts import render, redirect
from .forms import ProjectForm

def home(request):
    return render(request,'projects_app/base.html')

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