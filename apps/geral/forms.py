from django import forms
from .models import Oficina, Mecanico

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        exclude = ['usuario']
        

class MecanicoOficina(forms.ModelForm):

    class Meta:
        model = Mecanico
        exclude = ['oficina']