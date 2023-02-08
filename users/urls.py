from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('', views.Users, name='users'),
    path('user/<str:pk>/', views.SingleUser, name='user'),
    path('create/', views.AddUser, name='add-user'),
    path('user/<str:pk>/edit/', views.EditUser, name='edit-user'),
    path('user/<str:pk>/delete/', views.DeleteUser, name='delete-user'),
    
]