from django.shortcuts import render
from django.http import HttpResponse
from .models import Project


def projects(request)-> str:
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'projects/projects.html', context)

def project(request, pk) -> str:
    projectObject = Project.objects.get(id=pk) 
    context = {
        'project': projectObject
    }
    return render(request, 'projects/single-project.html', context)