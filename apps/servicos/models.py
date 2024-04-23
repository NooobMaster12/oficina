import datetime

from django.db import models

from geral.models import Oficina, Mecanico

# Create your models here.

class Servico(models.Model):
    oficina = models.ForeignKey(Oficina, verbose_name = 'Oficina', on_delete=models.CASCADE, null=True )
    nome = models.CharField(verbose_name='Nome', max_length=70)
    descricao = models.TextField(verbose_name='Descrição', blank = True, null=True)
    valor = models.DecimalField(verbose_name='Valor R$', max_digits=19, decimal_places=2)
    comissao=models.DecimalField(verbose_name='Comissão R$', max_digits=19, decimal_places=2)
    
    def __str__ (self) -> str:
        return self.nome
    
    class Meta:
        verbose_name='Servico'
        verbose_name_plural='Servicos'
        ordering = ['nome']
        
class OrdemServico(models.Model):
    STATUS_CHOICES = (
        (1, 'Aberto'),
        (2, 'Concluído')
    )

    oficina = models.ForeignKey(Oficina, verbose_name = 'Oficina', on_delete=models.CASCADE )
    mecanico = models.ForeignKey(Mecanico, verbose_name = 'Mecanico', on_delete=models.SET_NULL, null=True )
    cliente = models.CharField(verbose_name='Cliente', max_length=100)
    veiculo = models.CharField(verbose_name='Veiculo', max_length=100, help_text='Ex: Honda Fan 160')
    placa = models.CharField(verbose_name='Veiculo', max_length=8, help_text='Ex: BRA-2145')
    previsao = models.DateTimeField(verbose_name='Previsão', default=datetime.datetime.now)
    data_entrada = models.DateTimeField(verbose_name='Data/Hora Entrada', auto_now=True)
    codigo = models.PositiveIntegerField(verbose_name='Código OS',unique=True)
    servico = models.ManyToManyField(Servico,verbose_name='Serviços', related_name='os')
    status = models.PositiveSmallIntegerField(verbose_name='Status', choices=STATUS_CHOICES, default=1)
    
    def __str__(self) -> str:
        return self.oficina.nome
    
    class Meta:
        verbose_name = 'Ordem de Serviço'
        verbose_name_plural = 'Ordens de Serviços'
        ordering = ['data_entrada']