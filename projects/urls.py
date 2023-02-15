from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projects, name='projects'),
    path('export-projects/', views.ExportProjects, name='export-projects'),
]