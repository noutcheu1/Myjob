from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:job_id>/', views.detail, name='details'),
    path('<int:job_id>/results/', views.results, name='results'),
    path('<int:job_id>/vote/', views.vote, name='vote'),
]