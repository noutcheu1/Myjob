from django.urls import path, include
from .api_view import *
from .views import Home
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views


router = DefaultRouter()
router.register('retruter', RetruterPostuler, basename='retruter')
router.register('Login',AuthViewSet, basename="Login")
router.register('Logout',LogoutView, basename="Logout")
router.register('Retruteur',ProfilRetruteurViewset, basename="Retruteur")
router.register('Competence',CompetenceViewset, basename="Competence")
router.register('Profils', ProfilUserViewset, basename='Profil')
router.register('Job',JobViewset, basename="Job")
router.register('Experience', ExperienceViewset, basename="Experience")
router.register('Formation', FormationViewset, basename='Formation')
router.register('Find', FilterFind, basename='Find')
router.register('Users', UserViewSet, basename='Users')
router.register('postuler_job',PostulerVieset, basename='postuler_job')

urlpatterns = [
   path('', include(router.urls)),
   
   path('api-token-auth/', views.obtain_auth_token),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
  # path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
