from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk):
    projectObject = Project.objects.get(id=pk) 
    context = {
        'project': projectObject
    }
    return render(request, 'projects/single-project.html', context)


def createProject(request):
    form = ProjectForm()
    context = {
        "form": form
    }
    return render (request, 'projects/project_form.html', context)