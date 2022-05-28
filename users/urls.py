"""
    Definir les routes du module users
"""
from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.profiles, name="profiles"),
]