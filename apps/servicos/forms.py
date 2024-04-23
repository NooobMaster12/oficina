from django import forms

from .models import Servico, OrdemServico
from geral.models import Mecanico


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        exclude = ['oficina']

class OrdemServicoForm(forms.ModelForm):

    class Meta:
        model = OrdemServico
        exclude = ['oficina']


class RelatorioForm(forms.Form):
    mecanico = forms.ModelMultipleChoiceField(label='Mecânico', queryset=Mecanico.objects.all(), required=True)
    data_inicial = forms.DateField(label='Data Inicial', required=True)
    data_final = forms.DateField(label='Data Final', required=True)