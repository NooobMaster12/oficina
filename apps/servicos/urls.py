from django.urls import path

app_name = 'servicos'

from . import views

urlpatterns = [

    path('novo-servico/', views.novoServico, name='novoServico'),
    path('editar/<int:pk>/', views.editarServico, name='editarServico'),
    path('ordens-servicos/', views.listaOrdemServico, name='listaOrdemServico'),
    path('nova-ordem-servico', views.novaOrdemServico, name='novaOrdemServico'),
    path('nova-ordem-servico/<int:pk>/', views.editarOrdemServico, name='editarOrdemServico'),
    path('', views.listaServico, name='listaServico'),
]