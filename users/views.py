"""
    Definir le comportement de chaque action
"""
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Profile


def loginPage(request):


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

    }

    return render(request, "users/login_register.html", context)


def logoutUser(request):
    logout(request)
    messages.error(request, "User was logged out")
    return redirect("login")



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
