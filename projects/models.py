"""
    Definir les tables, leurs relations ainsi que tous les attributs qui les integres
"""
from email.policy import default
from django.db import models
import uuid
from users.models import Profile

class Project(models.Model):
    """
        Definition de la table projet avec ses attributs.
        Systeme de relation: -Many to Many (table Project & Tag)
                             -One to Many (table Project & Review)
                             -One to Many (table Profile & Project)
    """
    owner =  models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="defaultjpg")
    demo_link = models.CharField(max_length=200, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True) 
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    source_link = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        """
            Afficher le titre  de la table  Projet
        """
        return self.title
    
    
class Review(models.Model):
    """
        Definition de la table Review avec ses attributs.
        Systeme de relation: -Many to One (table Review & Project)
    """
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down')
    )
    
    #owner = 
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    body = models.TextField(blank=True, null=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        """
            Afficher la value de la table Review
        """
        return self.value
    
class Tag(models.Model):
    """
        Definition de la table Tag avec ses attributs.
        Systeme de relation: -Many to may (table Tag & Project)
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        """
            Afficher le nom de la table Tag
        """
        return self.name