from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_usuario(request):
    template_name = 'usuarios/login.html'
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            user = authenticate(username=usuario, password=senha)
            if user is not None and user.is_active:
                login(request, user)
                messages.info(request, 'Você fez login com sucesso.')
                return redirect('geral:home')
            else:
                messages.error(request, 'Usuário ou senha incorreto.')
                return redirect('usuarios:login')
        else:
            messages.error(request, 'Formulário inválido')
            return redirect('usuarios:login')
    
    form = LoginForm()
    context['form'] = form  
    return render(request, template_name, context)


@login_required
def sair(request):
    logout(request)
    return redirect('usuarios:login')