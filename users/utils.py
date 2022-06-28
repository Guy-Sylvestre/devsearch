from django.db.models import Q
from .models import Profile, Skill



def  searchProfiles(request):
    """
        Ajouter un systeme de recherche de profile avance qui peut:
            -Faire une recherche par nom
            -Faire une recherche par titre
            -Faire une recherche par competence
        Afficher tous les profiles des utilisateurs enregistres dans la base de donnees
    """
    
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
        
    profiles = Profile.objects.distinct().filter(
                Q(name__icontains=search_query) |
                Q(short_intro__icontains=search_query) |
                Q(skill__in=skills)
    )
    
    return profiles, search_query 