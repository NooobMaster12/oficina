from django.urls import path 

app_name = 'usuarios'

from . import views

urlpatterns = [
    path ('login/', views.login_usuario, name='login'),
    path('sair/', views.sair, name='sair'),
]

