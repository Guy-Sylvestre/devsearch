"""
    admin.py permet d'afficher dans la partie administration du systeme les tables que nous declarons
"""
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)