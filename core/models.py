from django.db import models

from django.db import models


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