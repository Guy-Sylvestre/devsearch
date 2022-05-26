"""
    Definir les routes du module project
"""
from django.urls import path
from . import views
 
urlpatterns = [
    path("project/<str:pk>", views.project, name="project"),

    #CRUD (Create, Read, Update and Delete)
    path("", views.projects, name="projects"),
    path("create-project/", views.createProject, name="create-project"),
    path("update-project/<str:pk>", views.updateProject, name="update-project"),
    path("delete-project/<str:pk>", views.deleteProject, name="delete-project"),
]