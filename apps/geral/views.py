from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import OficinaForm, MecanicoForm
from .models import Oficina, Mecanico
from django.views.generic import UpdateView


@login_required
def home (request):
    template_name = 'geral/home.html'
    context = {}
    return render(request,template_name, context)
    


@login_required
def novaOficina(request):
    template_name = 'geral/novaOficina.html'
    context = {}
    if request.method == 'POST':
        form = OficinaForm(request.POST)
        if form.is_valid():
            of = form.save(commit=False)
            of.usuario = request.user
            of.save()            
            messages.success(request, 'Oficina cadastrada com sucesso.')
            return redirect('geral:listaOficina')
        else:
            messagem_erro = list(form.errors.values()[0][0])
            messages.error(request, f'{messagem_erro}')
            return redirect('geral:listaOficina')
    form = OficinaForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required
def listaOficina(request):
    template_name = 'geral/listaOficina.html'
    oficinas = Oficina.objects.filter(usuario=request.user) # select from oficina where usuario = usuario_da_sessao
    context = {
        'oficinas':oficinas,
    }
    return render(request, template_name, context)

@login_required
def deletarOficina(request, pk):
    oficina = Oficina.objects.get(pk=pk)
    oficina.delete()
    messages.info(request, 'Oficina deletada')
    return redirect('geral:listaOficina')

@login_required
def editarOficina(request, pk):
    template_name = 'geral/novaOficina.html'
    context = {}
    oficina = get_object_or_404(Oficina, pk=pk)
    if request.method == 'POST':
        form = OficinaForm(data=request.POST, instance=oficina)
        form.save()
        messages.success(request, 'Oficina editada com sucesso.')
        return redirect('geral:listaOficina')
    form = OficinaForm(instance=oficina)
    context['form'] = form
    return render(request, template_name, context)

# def atualizar(request, id):
#     autor = Autor.objects.get(id=id)
#     form = AutorForm(instance=autor)
#     if request.method == "POST":
#         form = AutorForm(request.POST, request.FILES, instance=autor)
#         if form.is_valid():
#             form.save()
#             return redirect("atualizar", id=id)
#         else:
#             return render(request, 'atualizar.html', {'form': form})
#     else:
#          return render(request, 'atualizar.html', {'form': form})

@login_required
def novoMecanico(request):
    template_name = 'geral/novoMecanico.html'
    context = {}
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        oficina = get_object_or_404(Oficina, usuario = request.user)
        if form.is_valid():
            form = form.save(commit=False)
            form.oficina = oficina
            form.save()            
            messages.success(request, 'Mecanico cadastrada com sucesso.')
            return redirect('geral:listaMecanico')
    form = MecanicoForm()
    context['form'] = form
    return render(request, template_name, context)


@login_required
def listaMecanico(request):
    template_name = 'geral/listaMecanico.html'
    oficina = Oficina.objects.get(usuario=request.user)
    mecanicos = Mecanico.objects.filter(oficina=oficina)
    context = {
        'mecanicos':mecanicos,
    }
    return render(request, template_name, context)

@login_required
def deletarMecanico(request, pk):
    mecanico =Mecanico.objects.get(pk=pk)
    mecanico.delete()
    messages.info(request, 'Mecânico deletado')
    return redirect('geral:listaMecanico')

@login_required
def editarMecanico(request, pk):
    template_name = 'geral/novoMecanico.html'
    context = {}
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = MecanicoForm(data=request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mecânico editada com sucesso.')
            return redirect('geral:listaMecanico')
    form = MecanicoForm(instance=mecanico)
    context['form'] = form
    return render(request, template_name, context)

