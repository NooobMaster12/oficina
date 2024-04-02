from django import forms


class LoginForm(forms.Form):
    usuario = forms.CharField(label='Nome de Usuário', required=True)
    senha = forms.CharField(label='Senha', required=True, widget=forms.PasswordInput())