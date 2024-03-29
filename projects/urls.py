from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projects, name='projects'),
    path('project/<str:pk>/', views.SingleProject, name='project'),
    
    path('export-projects/', views.ExportProjects, name='export-projects'),
    path('generate-report/', views.GenerateReport, name='generate-report'),
]