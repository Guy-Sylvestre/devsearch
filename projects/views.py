"""
    Definition du comportement de chaque action
"""
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

def projects(request):
    """
        Afficher toute les enregistrement de la table Project
    """
    projects = Project.objects.all()

    context = {
        'projects': projects
    }

    return render(request, 'projects/projects.html', context)

def project(request, pk):
    """
        Acceder au detail d'un project bien preci
    """
    projectObject = Project.objects.get(id=pk) 

    context = {
        'project': projectObject
    }

    return render(request, 'projects/single-project.html', context)


def createProject(request):
    """
        Creer un projet
    """
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


def updateProject(request, pk):
    """
        Mettre a jour un project deja existant
    """
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


def deleteProject(request, pk):
    """
        Supprimer un project grace a son id
    """
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        "object": project,
    }

    return render(request, 'projects/delete_template.html', context)