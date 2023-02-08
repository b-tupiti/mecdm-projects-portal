from . import views
from django.urls import path

urlpatterns = [
    path('', views.AccountRequests, name='account-requests'),
    path('request-an-account/', views.RequestAccount, name='request-an-account'),
    path('account-request/<str:pk>/', views.SingleAccountRequest, name='account-request'),
]