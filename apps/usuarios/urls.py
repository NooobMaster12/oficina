from django.urls import path 

app_name = 'usuarios'

from . import views

urlpatterns = [
    path ('login/', views.login, name='login'),
]

