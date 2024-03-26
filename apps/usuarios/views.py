from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse
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
                return HttpResponse('<h1>Você fez login</h1>')
            else:
                return HttpResponse('<h1>Erro no login</h1>')
        form = LoginForm()
        context['form'] = form
        
    return render(request, template_name, context)