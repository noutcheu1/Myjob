from django.db import models
from core.interface import *
from django.contrib.auth.models import User
import json

with open('core/pays.json') as fp: 

    obj = json.load(fp)
STATES_LOCATION = obj.items()
CONTRAT_TYPE = (('TEMP PLEIN ','TEMP PLEIN '),('PERMANENT', 'PERMANENT'), ('OCCASIONNEL', 'OCCASIONNEL'), ('STAGE', 'STAGE'), ('FREELANCER', 'FREELANCER') ,('TEMP PARTIEL', 'TEMP PARTIEL') ,('CONTRACTUEL', 'CONTRACTUEL'))
RESPONSE_STATUS = (('Retruter', 'Retruter'), ('REFUSER', 'REFUSER'), ('WAITING', 'WAITING'))

class Metier(models.Model):
    """
    Description: Model Description
    """
    nom = models.CharField(max_length=200)
    domaine =models.CharField(max_length=200)
    

    class Meta:
        abstract=True


class Profil(models.Model):
    """
    Description: Model Description
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    Description= models.TextField()
    adresse = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=200, choices=STATES_LOCATION)

    class Meta:
        abstract = True


class ProfilUser(Profil):
    """
    Description: Model Description
    """
    work= (('developpeur',"dev Android"), ("developpeur", "DEV WEb"), ("DATA SCIENTIST","DATA SCIENTIST"))
    
    birthday = models.DateField(auto_now_add=False)
    metier = models.CharField(max_length=200, choices=work)
    cv = models.FileField(verbose_name='User_Cv', upload_to="Cv_doc", blank=True, null=True)


    def __str__(self):
        pass

    class Meta:
        abstract = True


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
        pass
        
    class Meta:
        abstract = True


class Competence(models.Model):
    """
    Description: Model Description
    """
    niveau = models.CharField(max_length=2000)
    description = models.TextField()
    nom = models.CharField(max_length=200)    
    profiluser = models.ForeignKey(ProfilUser, on_delete=models.CASCADE)

    def __str__(self):
        pass

    class Meta:
        abstract = True


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
        abstract = True

    def __str__(self):
      pass


class ProfilRetruteur(Profil):
    """
    Description: Model Description
    """
    web_site = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        pass

    class Meta:
        abstract = True






class Job(models.Model):
    """
    Description: Model Description
    """
    WORK_LOC = STATES_LOCATION
    WORK_STATUE= (("wait", "en attente"), ("bad", "refuser"), ("poster", "ok"))
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
    	pass

   
    class Meta:
        abstract = True
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
   
    class Meta:

        abstract = True
        ordering = ('date_post','id')
        

class Retruter(models.Model):
    """
    Description: Model Description
    """
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    user_id = models.ForeignKey(ProfilUser, on_delete=models.CASCADE)
    user_retruteur_id = models.ForeignKey(ProfilRetruteur, on_delete=models.CASCADE)
    date_post = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True