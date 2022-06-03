"""
    CReation de formulaire a l'aide de la table native de Django
"""
from dataclasses import fields
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


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