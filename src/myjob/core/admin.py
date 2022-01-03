from django.contrib import admin

# Register your models here.
from .models import (ProfilRetruteur, ProfilUser, Job, Experience, Competence, Formation)






admin.site.register(Job)
admin.site.register(ProfilUser)
admin.site.register(ProfilRetruteur)
admin.site.register(Experience)
admin.site.register(Formation)
admin.site.register(Competence)
