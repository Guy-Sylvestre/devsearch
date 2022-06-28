"""
    Definir le comportement de chaque action
"""
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, ProfileForm, SkillForm
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Profile
from .utils import searchProfiles


def loginPage(request):
    """
        Systeme de loging
    """ 
    page = "login"

    if request.user.is_authenticated:
        return redirect("profiles")
        
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Username does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "Username OR password is incorrect")

    context = {
        "page": page,
    }

    return render(request, "users/login.html", context)


def logoutUser(request):
    """
        Systeme de deconnexion
    """
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("login")


def registerUser(request):
    """
        Creer un utilisateur
    """
    page = "register"

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect("edit-account")
        else:
            messages.success(request, "An error has occurred during Registration")

    context = {
        "form": form,
        "page": page,
    }

    return render(request, "users/register.html", context)


def profiles(request):
    """
        Ajouter un systeme de recherche de profile
        Afficher tout les enregistrements de la table Project
    """
    profiles, search_query = searchProfiles(request)
    
    context = {
        "profiles": profiles,
        "search_query": search_query
    }
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    """
        Acceder au profile d'un utilisateur grace a son id
        Afficher aussi grace a son id tous les projets et competence relative a l'utilisateur selectionne
        Le tout sans onglet de modifications
    """
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {
        "profile": profile,
        "topSkills": topSkills,
        "otherSkills": otherSkills
    }

    return render(request,  "users/user-profile.html", context)


@login_required(login_url="login")
def userAccount(request):
    """
        Acceder au profile de l'utilsateur connecte
        Afficher tous les  projets et competences qui lui sont propre
        Le tout avec onglet de modifications
    """
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context = {
        "profile": profile,
        "skills": skills,
        "projects": projects,
    }
    
    return render(request, "users/account.html", context)


@login_required(login_url="login")
def editAccount(request):
    """
        Acceder a la modifications des informations personnel de l'utilisateur s'il est connecte
    """
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
    
    context = {
        "form": form,
    }
    
    return render(request, "users/profile_form.html", context)


@login_required(login_url="login")
def createSkill(request):
    """
        Ajouter de nouvelle competences a l'utilisateur connecter
    """
    profile = request.user.profile
    form = SkillForm()
    
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, f"{skill} was added succefully!")
            return redirect("account")
    
    context = {
        "form": form,
    }
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def updateSkill(request, pk):
    """
        Mettre a jour une competence precise de l'utilisateur
    """
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, f"{skill} was updated succefully!")
            return redirect("account")
    
    context = {
        "form": form,
    }
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def deleteSKill(request, pk):
    """
        Supprimer une competence precise de l'utilisateur
    """
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request, f"{skill} was deleted succefully!")
        return redirect('account')

    context = {
        "object": skill,
    }

    return render(request, 'users/delete_template.html', context)