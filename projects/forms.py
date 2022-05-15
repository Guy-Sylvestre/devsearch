"""
    Gener un formulaire a l'aide de la table deja creer
"""
from django.forms import ModelForm
from .models import Project

class ProjectForm(ModelForm):
    """
        Creation du formulaire avec le model ModelForm de django
    """
    class Meta:
        """
            Definir le nom de la table ciblee (model) et ses differents champs (fields)
        """
        model = Project
        fields = '__all__'