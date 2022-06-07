"""
    Definir les actions notificatives lors d'un post
"""
from cgi import print_arguments
from .models import Profile
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    """
        Creer un profile
    """
    print("Profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
        )
    print("------------------------------------- createProfile ------------------------------------")
    print("profile Saved!")
    print('Instance:', instance)
    print("CREATED:", created)
    print("-------------------------------------------------------------------------")
    
    
def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()
    
    print("------------------------------ updateUser -------------------------------------------")
    print("profile Saved!")
    print('Instance:', instance)
    print("CREATED:", created)
    print("-------------------------------------------------------------------------")


def deleteUser(sender, instance, **kwargs):
    """
        Supprimer un utilisateur.
    """
    user = instance.user
    user.delete()
    print("------------------------------- deleteUser ------------------------------------------")
    print("Deleting user ... ")
    print("-------------------------------------------------------------------------")

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)
