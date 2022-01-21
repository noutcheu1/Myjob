from django.db import models
from core.interface import *
from django.contrib.auth.models import User
import json

# Create your models here.

class Metier(models.Model):
    """
    Description: Model Description
    """
    nom = models.CharField(max_length=200)
    domaine =models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nom}-:{self.domaine}"

    class Meta:
        abstract=False

class Travail(models.Model):
    travail_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self) :
        return "{}".format(self.travail_text)

class Choix(models.Model):
    travail = models.ForeignKey(Travail, on_delete=models.CASCADE)
    choix_text = models.CharField(max_length=200)
    nbre_place = models.IntegerField(default=0)
    def __str__(self):
       return "{}".format(self.choix_text)
       
class ProfilUser(Profil):
    """
    Description: Model Description
    """
    work= (('developpeur',"dev Android"), ("developpeur", "DEV WEb"), ("DATA SCIENTIST","DATA SCIENTIST"))
    metier = models.CharField(max_length=200)
    birthday = models.DateField(auto_now_add=False)
    metier = models.CharField(max_length=200, choices=work)
    cv = models.FileField(verbose_name='User_Cv', upload_to="Cv_doc", null=True)
    

    def __str__(self):
        return f"{self.user.username}-:{self.metier}"

    class Meta:
        abstract = False


class Formation(models.Model):
    """
    Description: Model Description
    """

   
    date_debut =models.DateField()
    date_fin = models.DateField()
    nom = models.CharField(max_length=200)
    lieux = models.CharField(max_length=200)
    description = models.TextField()
    profiluser = models.ForeignKey(ProfilUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} || {self.lieux}:{self.date_debut}-{self.date_fin}"
        
    class Meta:
        abstract = False


class Competence(models.Model):
    """
    Description: Model Description
    """
    niveau = models.CharField(max_length=2000)
    description = models.TextField()
    nom = models.CharField(max_length=200)    
    profiluser = models.ForeignKey(ProfilUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} || {self.description} -{self.niveau}"

    class Meta:
        abstract = False


class Experience(models.Model):
    """
    Description: Model Description
    """
    experiences_users = models.ForeignKey(ProfilUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="experiences_user")

    date_de_debut = models.DateField()
    date_de_fin = models.DateField()
    title = models.CharField(max_length=200)
    Description =models.TextField()
    lieux = models.CharField(max_length=200)
    type_contrat = models.CharField(max_length=50,  choices=CONTRAT_TYPE)

    class Meta:
        abstract = False

    def __str__(self):
        return f"{self.title} || {self.lieux}:{self.date_de_debut}-{self.date_de_fin}"


class ProfilRetruteur(Profil):
    """
    Description: Model Description
    """
    web_site = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"

    class Meta:
    	abstract = False


class Job(models.Model):
    """
    Description: Model Description
    """
    WORK_LOC = STATES_LOCATION
    WORK_STATUE= (("draft", "en attente"), ("bad", "refuser"), ("poster", "ok"), ("close", "fermer"))
    metier = models.CharField(max_length=200)
    profilretruteur = models.ForeignKey(ProfilRetruteur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    type_contrat = models.CharField(max_length=50)
    salaire_min =  models.PositiveIntegerField(default=0)
    date_debut = models.DateField(auto_now_add=True)
    date_fin = models.DateField()
    description = models.TextField()
    salaire_max = models.PositiveIntegerField(default=0)
    Job_statue = models.CharField(max_length=150, choices=WORK_STATUE)
    work_location =  models.CharField(max_length=200)
    nombres_experiences = models.PositiveIntegerField(default=0)
    nbre_place = models.PositiveIntegerField(default=1)

   


    def __str__(self):
        return f"{self.titre} {self.salaire_max}"

    class Meta:
        abstract = False
        ordering = ('date_debut', 'date_fin', 'Job_statue')


class Postuler(models.Model):
    """
    Description: Model Description
    """
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    motivation_letter =  models.TextField()
    date_post = models.DateField(auto_now_add=True)
    response_status = models.CharField(max_length=200, choices=RESPONSE_STATUS)
    
    def set_retruter(self, pk, job):
        poste = Postuler.objects.get(user_id=pk.id, job_id=job)
        print(poste,'de user')
        poste.response_status = 'Retruter'
        print(poste,'de user after')
        poste.save()

    
    
    def __str__(self):
            return f" {self.user_id} a Postuler a {self.job_id} {self.response_status}"

    class Meta:
        abstract = False
        ordering = ('date_post','id')
        
"""
class Retruter(Retruter):
  
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ProfilUser, on_delete=models.CASCADE)
    user_retruteur_id = models.ForeignKey(ProfilRetruteur, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)

    class Meta:
        abstract = False
"""