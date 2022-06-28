"""
    Definir le comportement de chaque action
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project, Tag
from .forms import ProjectForm
from django.db.models import Q
from django.contrib import messages
from .utils import searchProject

def projects(request):
    """
        Ajouter un systeme de recherche de projets
        Afficher tout les enregistrements de la table Project
    """
    projects, search_query = searchProject(request)

    context = {
        'projects': projects,
        "search_query": search_query
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
    profile = request.user.profile
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            messages.success(request, f"{project} was created succefully!")
            return redirect('account')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


@login_required(login_url="login")
def updateProject(request, pk):
    """
        Mettre a jour un projet deja existant avec une image integree
    """
    profile = request.user.profile
    project = profile.project_set.get(pk=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f"{project} was updated succefully!")
            return redirect('account')

    context = {
        "form": form
    }

    return render (request, 'projects/project_form.html', context)


@login_required(login_url="login")
def deleteProject(request, pk):
    """
        Supprimer un projet grace a son id
    """
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f"{project} was deleted succefully!")
        return redirect('account')

    context = {
        "object": project,
    }

    return render(request, 'projects/delete_template.html', context)