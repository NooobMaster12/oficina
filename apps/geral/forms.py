from django import forms
from .models import  Oficina

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        exclude = ['usuario']