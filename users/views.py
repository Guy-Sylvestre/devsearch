"""
    Definir le comportement de chaque action
"""
from multiprocessing import context
import profile
from django.shortcuts import render
from .models import Profile



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
