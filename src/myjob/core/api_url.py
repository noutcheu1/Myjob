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
router.register('login',AuthViewSet, basename="login")
router.register('logout',LogoutView, basename="logout")
router.register('retruteur',ProfilRetruteurViewset, basename="=retruteur")
router.register('competence',CompetenceViewset, basename="competence")
router.register('profils', ProfilUserViewset, basename='profils')
router.register('job',JobViewset, basename="job")
router.register('experience', ExperienceViewset, basename="experience")

router.register('users', UserViewSet, basename='users')


urlpatterns = [
   path('', include(router.urls)),
   path('api-token-auth/', views.obtain_auth_token),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
   #path('dj-rest-auth/', include('dj_rest_auth.urls')),
]
