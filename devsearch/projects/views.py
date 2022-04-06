from django.shortcuts import render
from django.http import HttpResponse


def projects(request)-> str:
    return render(request, 'projects/projects.html')

def project(request, pk) -> str:
    return render(request, 'projects/single-project.html')