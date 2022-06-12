"""
    CReation de formulaire a l'aide de la table native de Django
"""
from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Skill


class CustomUserCreationForm(UserCreationForm):
    """
        Creation de systeme de creation de compte
    """
    class Meta:
        """
            Utilisation native de la table User de django et de quelque attributs de ca table tel que:
            -username
            -password1
            -password2
            -email
            -first_name
            -last_name
        """
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name"
        }


    def __init__(self, *args, **kwargs):
        """
            Styliser le formulaire avec une class deja definit.
            Pour la class deja definit c'est: input.
            Le style etant repetitif, nous la parcourons avec un for
        """
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input'
                }
            )
            
            

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "email", "username", "location", "bio", "short_intro",
                    "profile_image", "social_github", "social_linkedin", "social_twitter",
                    "social_youtube", "social_website"
                  ]
        
    def __init__(self, *args, **kwargs):
        """
            Styliser le formulaire avec une class deja definit.
            Pour la class deja definit c'est: input.
            Le style etant repetitif, nous la parcourons avec un for
        """
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input'
                }
            )
            
            

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]
        
    def __init__(self, *args, **kwargs):
        """
            Styliser le formulaire avec une class deja definit.
            Pour la class deja definit c'est: input.
            Le style etant repetitif, nous la parcourons avec un for
        """
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input'
                }
            )