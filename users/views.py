"""
    Definir le comportement de chaque action
"""
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.shortcuts import render, redirect
from .models import Profile


def loginPage(request):
    """
        Systeme de loging
    """
    
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


    return render(request, "users/login.html")


def logoutUser(request):
    """
        Systeme de deconnexion
    """
    logout(request)
    messages.error(request, "User was logged out")
    return redirect("login")


def registerUser(request):
    """
        Creer un utilisateur
    """

    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created!")

            login(request, user)
            return redirect("profiles")
        else:
            messages.success(request, "An error has occurred during Registration")

    context = {
        "form": form,
    }

    return render(request, "users/register.html", context)


def profiles(request):
    """
        Afficher tout les profiles
    """
    profiles = Profile.objects.all()
    context = {
        "profiles": profiles
    }
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    """
        Acceder au profile d'un utilisateur
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
