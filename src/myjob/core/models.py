from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class ProfilUser(models.Model):
    """
    Description: Model Description
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telephone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    metier= models.CharField(max_length=200)
    cv = models.FileField(verbose_name='User_Cv', upload_to="Cv_doc")
