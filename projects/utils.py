from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginationProjects(request, projects, results):
    """"
        SYSTEME DE PAGINATION
    """
    page = request.GET.get('page')
    paginator = Paginator(projects, results)
    
    try:
        projects = paginator.page(page)
    except  PageNotAnInteger:
        page = 1
        projects = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects = paginator.page(page)
        
    leftIndex = (int(page) - 1)
    
    if leftIndex < 1:
        leftIndex = 1
        
    rightIndex = (int(page) + 4)
    
    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1
        
    custom_range = range(leftIndex, rightIndex)
    
    return custom_range, projects



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