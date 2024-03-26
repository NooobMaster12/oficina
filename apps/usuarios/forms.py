from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label='Nome usuário', required=True)
    senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())