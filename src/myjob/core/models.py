from django.db import models
from core.interface import *
from django.contrib.auth.models import User
import json

# Create your models here.

class Metier(Metier):
    """
    Description: Model Description
    """
    nom = models.CharField(max_length=200)
    domaine =models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.nom}-:{self.domaine}"

    class Meta:
        abstract=False



class ProfilUser(ProfilUser):
    """
    Description: Model Description
    """
    work= (('developpeur',"dev Android"), ("developpeur", "DEV WEb"), ("DATA SCIENTIST","DATA SCIENTIST"))
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    birthday = models.DateField(auto_now_add=False)
    metier = models.CharField(max_length=200, choices=work)
    cv = models.FileField(verbose_name='User_Cv', upload_to="Cv_doc", null=True)


    def __str__(self):
        return f"{self.user.username}-:{self.metier}"

    class Meta:
        abstract = False


class Formation(Formation):
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


class Competence(Competence):
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


class Experience(Experience):
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


class ProfilRetruteur(ProfilRetruteur):
    """
    Description: Model Description
    """
    web_site = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username}"

    class Meta:
    	abstract = False


class Job(Job):
    """
    Description: Model Description
    """
    WORK_LOC = STATES_LOCATION
    WORK_STATUE= (("draft", "en attente"), ("bad", "refuser"), ("poster", "ok"))
    metier = models.ForeignKey(Metier, on_delete=models.CASCADE)
    profilretruteur = models.ForeignKey(ProfilRetruteur, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    type_contrat = models.CharField(max_length=50,  choices=CONTRAT_TYPE)
    salaire_min =  models.PositiveIntegerField(default=0)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField()
    description = models.TextField()
    salaire_max = models.PositiveIntegerField(default=0)
    Job_statue = models.CharField(max_length=150, choices=WORK_STATUE)
    work_location =  models.CharField(max_length=200, choices=WORK_LOC)
    nombres_experiences = models.PositiveIntegerField(default=0)
   




    def __str__(self):
        return f"{self.titre} || {self.salaire_min} < {self.salaire_max}:{self.date_debut}-{self.date_fin} {self.Job_statue}"

    class Meta:
        abstract = False
        ordering = ('date_debut', 'date_fin', 'Job_statue')


class Postuler(Postuler):
    """
    Description: Model Description
    """
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    motivation_letter =  models.TextField()
    date_post = models.DateField(auto_now_add=True)
    response_status = models.CharField(max_length=200, choices=RESPONSE_STATUS)
    user_retruteur_id = models.ForeignKey(ProfilRetruteur, on_delete=models.CASCADE)
    
    @classmethod
    def retruter_job(cls, *args, **kwargs):
        job = Job.objects.get(id=kwargs.get('job_id'))
        postuler = Postuler.objects.all()
        list_user_postuler = postuler.filter(job_id=job.id)
        # do something with the book
        return Job

    def save(self, *args, **kwargs):
        self.response_status = ('WAITING', 'WAITING')

        return super(Postuler, self).save(*args, **kargs)
               

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