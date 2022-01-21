from django.contrib import admin

# Register your models here.
from .models import (ProfilRetruteur, ProfilUser, Job, Experience, Competence, Formation, Postuler, Retruter, Metier,Travail, Choix)




admin.site.register(Metier)
admin.site.register(Postuler)
admin.site.register(Job)
admin.site.register(ProfilUser)
admin.site.register(ProfilRetruteur)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Competence)
admin.site.register(Travail)
