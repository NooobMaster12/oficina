from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

class Oficina(models.Model):
    usuario = models.ForeignKey(User, verbose_name = 'Usuário', on_delete=models.CASCADE )
    nome = models.CharField(verbose_name='Nome', max_length = 100)
    cnpj = models.CharField(verbose_name='CNPJ', max_length = 18, blank=True, null=True)
    endereco = models.CharField(verbose_name='Endereço',max_length = 200, blank=True, null=True)
    email = models.CharField(verbose_name='Email', blank=True, null=True)
    telefone = models.CharField(verbose_name='Telefone', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.nome
    
    def clean(self):
        model = self.__class__
        if (model.objects.count() > 0 and self.id != model.objects.get().id):
            raise ValidationError('Não é possível criar mais de uma descrição')
    
    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'
        ordering = ['nome']
        

class Mecanico(models.Model):
    oficina = models.ForeignKey(Oficina, verbose_name = 'Oficina', on_delete=models.CASCADE )
    nome = models.CharField(verbose_name='Nome', max_length = 100)
    codigo = models.PositiveSmallIntegerField(verbose_name='Código')
    
    def __str__(self) -> str:
        return self.nome
    
    class Meta:
        verbose_name = 'Mecânico'
        verbose_name_plural = 'Mecânicos'
        ordering = ['nome']