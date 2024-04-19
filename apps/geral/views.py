from django.shortcuts import render, redirect, get_object_or_404
from .forms import OficinaForm, MecanicoOficina
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Oficina, Mecanico

@login_required
def home(request):
    template_name = 'geral/home.html'
    context = {}
    return render(request, template_name, context)



@login_required
def nova_oficina(request):
    template_name = 'geral/nova_oficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()
            messages.success(request, 'Oficina cadastrada com sucesso!')
            return redirect('geral:lista_oficina')
        else:
            messagem_erro = list(form.erros.values())[0][0]
            messages.error(request, f'{messagem_erro}')
            return redirect('geral:lista_oficina')
        
    form = OficinaForm()    
    context['form'] = form    
    return render(request, template_name, context)


@login_required
def lista_oficina(request):
    template_name = 'geral/lista_oficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user)
    context = {
        'oficinas': oficinas,
    }
    return render(request, template_name, context)



# @login_required
# def apagar_oficina(request, id):
#     oficina = Oficina.objects.get(usuario=request.user, id=id)    
#     oficina.delete()
#     return redirect('geral:lista_oficina')

@login_required
def apagar_oficina(request, pk):
    oficina = get_object_or_404(Oficina, pk=pk)
    oficina.delete()
    messages.info(request, 'Oficina excluída com sucesso!')
    return redirect('geral:lista_oficina')


@login_required
def editar_oficina(request, pk):
    template_name = 'geral/nova_oficina.html'
    context = {

    }
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina)
        form.save()
        messages.success(request, 'Oficina atualizada com sucesso!')
        return redirect('geral:lista_oficina')
    form = OficinaForm(instance=oficina)
    return render(request, template_name, context)
    


# @login_required
# def atualizar_oficina(request, pk):
#     template_name = 'geral/nova_oficina.html'
#     oficina = Oficina.objects.get(usuario=request.user, id=id)
#     forms = OficinaForm(instance=oficina)
#     context = {
#         'forms': forms,
#     }
#     if request.method == "POST":
#     return render(request, template_name, context)

@login_required
def novo_mecanico(request):
    template_name = 'geral/novo_mecanico.html'
    context = {}
    if request.method == 'POST':
        form = MecanicoOficina(request.POST)
        usuario = request.user
        oficina = get_object_or_404(Oficina, usuario=usuario)
        if form.is_valid():
            form = form.save(commit=False)
            form.oficina = oficina
            form.save()
            messages.success(request, "Mecânico adicionado com sucesso!")
            return redirect('geral:lista_mecanicos')
    form = MecanicoOficina()
    context['form'] = form   
    return render(request, template_name, context)


@login_required
def lista_mecanico(request):
    template_name = 'geral/lista_mecanicos.html'
    usuario = request.user
    oficina = Oficina.objects.get(usuario=usuario)
    mecanicos = Mecanico.objects.filter(oficina=oficina)
    context = {
        'mecanicos': mecanicos,
    }
    return render(request, template_name, context)


@login_required
def editar_mecanico(request, pk):
    template_name = 'servicos/novo_mecanico.html'
    context = {

    }
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=mecanico)
        form.save()
        messages.success(request, 'Mecânico atualizado com sucesso!')
        return redirect('geral:lista_mecanicos')
    form = OficinaForm(instance=mecanico)
    return render(request, template_name, context)


@login_required
def apagar_mecanico(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    mecanico.delete()
    messages.info(request, 'Mecânico excluído com sucesso!')
    return redirect('geral:lista_mecanicos')