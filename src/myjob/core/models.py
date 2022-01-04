from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Profil(models.Model):
    """
    Description: Model Description
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)
    Description= models.TextField()
    adresse = models.CharField(max_length=50)
    nationalite = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Formation(models.Model):
    """
    Description: Model Description
    """
    date_debut =models.DateField(auto_now_add=True)
    date_fin = models.DateField()
    nom = models.CharField(max_length=200)
    lieux = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        pass


class Competence(models.Model):
    """
    Description: Model Description
    """
    niveau = models.CharField(max_length=2000)
    description = models.TextField()
    nom = models.CharField(max_length=200)    

    class Meta:
        pass


class Experience(models.Model):
    """
    Description: Model Description
    """
    date_de_debut = models.DateField()
    date_de_fin = models.DateField()
    title = models.CharField(max_length=200)
    Description =models.TextField()
    lieux = models.CharField(max_length=200)




class ProfilRetruteur(Profil):
    """
    Description: Model Description
    """
    web_site = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username}"

    class Meta:
    	abstract = False
    	

class ProfilUser(Profil):
    """
    Description: Model Description
    """
    work= (('developpeur',"dev Android"), ("developpeur", "DEV WEb"), ("DATA SCIENTIST","DATA SCIENTIST"))
    
    birthday = models.DateField(auto_now_add=False)
    metier = models.CharField(max_length=200, choices=work)
    cv = models.FileField(verbose_name='User_Cv', upload_to="Cv_doc", null=True)
    competences = models.ManyToManyField(Competence, related_name="competences_user")
    formations = models.ManyToManyField(Formation, related_name="formation_user")
    experiences = models.ManyToManyField(Experience, related_name="experiences_user")


    def __str__(self):
        return f"{self.user.username}"

    class Meta:
    	abstract = False
    	

class Job(models.Model):
    """
    Description: Model Description
    """
    WORK_LOC = (("remotes", "teletravaille"),)
    WORK_STATUE= (("wait", "en attente"), ("bad", "refuser"), ("poster", "ok"))
    CONTRAT_TYPE = (('TEMP PLEIN ','TEMP PLEIN '),('PERMANENT', 'PERMANENT'), ('OCCASIONNEL', 'OCCASIONNEL'), ('STAGE', 'STAGE'), ('FREELANCER', 'FREELANCER') ,('TEMP PARTIEL', 'TEMP PARTIEL') ,('CONTRACTUEL', 'CONTRACTUEL'))
    titre = models.CharField(max_length=200)
    type_contrat = models.CharField(max_length=50,  choices=CONTRAT_TYPE)
    salaire =  models.PositiveIntegerField(default=0)
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField()
    description = models.TextField()
    competences = models.ManyToManyField(Competence, related_name="competences_job")
    formations = models.ManyToManyField(Formation, related_name="formation_job")
    experiences = models.ManyToManyField(Experience, related_name="experiences_job")
    Job_statue = models.CharField(max_length=150, choices=WORK_STATUE)
    work_location =  models.CharField(max_length=200, choices=WORK_LOC)
    nombres_experiences = models.PositiveIntegerField(default=0)
    postuler = models.ManyToManyField(ProfilUser, related_name='job_postuler')

    def save(self, *args, **kargs):
    	
    	self.Job_statue = ("wait", "en attente")
    	
    	return super().save(*args, **kargs)

    class Meta:
        pass
