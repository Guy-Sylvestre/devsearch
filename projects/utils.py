from .models import Project, Tag
from django.db.models import Q



def searchProject(request):
    """
        Ajouter un systeme de recherche de projets avance qui peut:
            -Faire une recherche par nom du projet
            -Faire une recherche par le proprietaire du projet
            -Faire une recherche par technologie
        Afficher tout les enregistrements de la table Project
    """
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
        
    tags = Tag.objects.filter(name__icontains=search_query)
        
    projects = Project.objects.distinct().filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(owner__name__icontains=search_query) |
                Q(tags__in=tags)
    )

    return projects, search_query