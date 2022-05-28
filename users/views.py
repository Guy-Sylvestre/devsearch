"""
    Definir le comportement de chaque action
"""
from django.shortcuts import render


def profiles(request):
    return render(request, "users/profiles.html")