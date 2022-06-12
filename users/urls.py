"""
    Definir les routes du module users
"""
from django.urls import path
from . import views
 
urlpatterns = [
    # Loging, logout and register
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("register/", views.registerUser, name="register"),
    
    # Display profile and detail profile url
    path("", views.profiles, name="profiles"),
    path("profile/<str:pk>/", views.userProfile, name="user-profile"),
    
    # Displaya and edit account url
    path("account/", views.userAccount, name="account"),
    path("edit-account/", views.editAccount, name="edit-account"),
    
    # Create, update and delete skill url
    path("create-skill/", views.createSkill, name="create-skill"),
    path("update-skill/<str:pk>/", views.updateSkill, name="update-skill"),
    path("delete-skill/<str:pk>/", views.deleteSKill, name="delete-skill"),
]

