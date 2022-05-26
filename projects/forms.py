"""
    Gener un formulaire a l'aide de la table deja creer
"""
from django.forms import ModelForm, widgets
from django import forms
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
        fields = ['title', 'featured_image', 'description',
                    'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    'class': 'input'
                }
            )
            
        # self.fields['title'].widget.attrs.update(
        #         {
        #             'class': 'input'
        #         }
        #     )

        # self.fields['description'].widget.attrs.update(
        #         {
        #             'class': 'input'
        #         }
        #     )