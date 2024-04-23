from django.urls import path


app_name = 'usuarios'

from . import views

urlpatterns = [ 
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.log_out, name='logout'),
]