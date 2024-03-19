# import datetime

# from django.db import models

# from geral.models import Oficina, Mecanico
# # Create your models here.

# class Servico(models.Model):
#     oficina = models.ForeignKey(Oficina, verbose_name='Oficina', on_delete=models.CASCADE, null=True)
#     nome = models.CharField(verbose_name='Nome', max_length=70)
#     descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
#     valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
#     comissao = models.DecimalField(verbose_name='Comissão R$', max_digits=19, decimal_places=2)
    
#     def ___str__(self) -> str:
#         return self.nome
    
#     class Meta:
#         verbose_name = 'Serviço'
#         verbose_name_plural = 'Serviços'
#         ordering = ['nome']
        
        
#     class OrdemServico(models.Model):
#         oficina = models.ForeignKey(Oficina, verbose_name='Oficina', on_delete=models.CASCADE)
#         mecanico = models.ForeignKey(Mecanico, verbose_name='Mecânico', on_delete=models.SET_NULL, null=True)
#         cliente = models.CharField(verbose_name='Cliente', max_lenght=100)
#         veiculo = models.CharField(verbose_name='Veículo', max_lenght=100, help_text='Ex: Moto Fan 160')
#         placa = models.CharField(verbose_name='Placa', max_lenght=8, help_text='Ex: AAA-0000')
#         previsao = models.DateField(verbose_name='Previsão', default=datetime.datetime.now)
#         data_entrada = models.DateTimeField(verbose_name='Data/Hora Entrada', auto_now=True)
#         codigo = models.PositiveIntegerField(verbose_name='Código OS', unique=True)
#         servico = models.ManyToManyField(Servico, verbose_name='Serviços', related_name='os')
        
#     def ___str__(self) -> str:
#         return self.oficina.nome
    
#     class Meta:
#         verbose_name = 'Ordem de Serviço'
#         verbose_name_plural = 'Ordem de Serviços'
#         ordering = ['data_entrada']
        
        
import datetime
from django.db import models
from geral.models import Oficina, Mecanico


# Create your models here.

class Servico(models.Model):
    oficina = models.ForeignKey(Oficina, verbose_name='Oficina', on_delete=models.CASCADE, null=True)
    nome = models.CharField(verbose_name='Nome', max_length=70)
    descricao = models.TextField(verbose_name='Descrição', blank=True, null=True)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    comissao = models.DecimalField(verbose_name='Comissão R$', max_digits=19, decimal_places=2)

    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = ['nome']


class OrdemServico(models.Model):
    oficina = models.ForeignKey(Oficina, verbose_name='Oficina', on_delete=models.CASCADE)
    mecanico = models.ForeignKey(Mecanico, verbose_name='Mecânico', on_delete=models.SET_NULL, null=True)
    cliente = models.CharField(verbose_name='Cliente', max_length=100)
    veiculo = models.CharField(verbose_name='Veículo', max_length=100, help_text='Ex: Moto Fan 160')
    placa = models.CharField(verbose_name='Placa', max_length=8, help_text='Ex: AAA-0000')
    previsao = models.DateField(verbose_name='Previsão', default=datetime.datetime.now)
    data_entrada = models.DateTimeField(verbose_name='Data/Hora Entrada', auto_now=True)
    codigo = models.PositiveIntegerField(verbose_name='Código OS', unique=True)
    servico = models.ManyToManyField(Servico, verbose_name='Serviços', related_name='os')

    def __str__(self) -> str:
        return self.oficina.nome
    
    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordem de Serviços'
        ordering = ['data_entrada']
