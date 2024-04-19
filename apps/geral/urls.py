from django.urls import path
from . import views

app_name = 'geral'

urlpatterns = [
    path('mecanicos', views.lista_mecanico, name='lista_mecanicos'),
    path('novo_mecanico/', views.novo_mecanico, name='novo_mecanico'),
    path('excluir_mecanico/<int:pk>/', views.apagar_mecanico, name='apagar_mecanico'),
    path('editar_mecanico/<int:pk>/', views.editar_mecanico, name='editar_mecanico'),
    path('nova-oficina', views.nova_oficina, name='nova_oficina'),
    path('oficinas/', views.lista_oficina, name='lista_oficina'),
    path('excluir_oficina/<int:pk>/', views.apagar_oficina, name='apagar_oficina'),
    path('editar_oficina/<int:pk>/', views.editar_oficina, name='editar_oficina'),
    path('', views.home, name='home'),
    
]