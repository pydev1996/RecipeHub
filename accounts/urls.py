# accounts/urls.py
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = 'accounts'

urlpatterns = [
    
    path('', views.user_login, name='login'),
    path('register', views.register, name='register'),
   path('reset_password/', views.reset_password, name='reset_password'),

     
]
