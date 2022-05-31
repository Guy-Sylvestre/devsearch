"""
    Definir le comportement de chaque action
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm

def projects(request):
    """
        Afficher tout les enregistrements de la table Project
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


@login_required(login_url="login")
def createProject(request):
    """
        Creer un projet avec une image
    """
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    """
        Mettre a jour un projet deja existant avec une image integree
    """
    project = Project.objects.get(pk=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    """
        Supprimer un projet grace a son id
    """
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')

    context = {
        "object": project,
    }

    return render(request, 'projects/delete_template.html', context)