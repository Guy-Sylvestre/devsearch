"""
    Definir les actions notificatives lors d'un post
"""
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
    print("profile Saved!")
    print('Instance:', instance)
    print("CREATED:", created)


def deleteUser(sender, instance, **kwargs):
    """
        Supprimer un utilisateur.
    """
    user = instance.user
    user.delete()
    print("Deleting user ...")

post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
