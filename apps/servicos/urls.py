from django.urls import path
from . import views

app_name = 'servicos'


urlpatterns = [
    path('servicos/', views.lista_servicos, name='lista_servicos'),
    path('novo-servicos', views.novo_servico, name='novo_servico'),    
    path('excluir_servico/<int:pk>/', views.apagar_servicos, name='apagar_servico'),
    path('editar_servico/<int:pk>/', views.editar_servico, name='editar_servico'),

]