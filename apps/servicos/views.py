from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ServicoForm, OrdemServicoForm, RelatorioForm
from .models import Servico, Oficina, OrdemServico

    

@login_required
def home (request):
    template_name = 'servicos/home.html'
    context = {}
    return render(request,template_name, context)

@login_required
def novoServico(request):
    template_name = 'servicos/novoServico.html'
    context = {}
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        usuario = request.user
        oficina = get_object_or_404(Oficina, usuario=usuario)
        if form.is_valid():
            sf = form.save(commit=False)
            sf.oficina = oficina
            sf.save()
            messages.success(request, "Serviço adicionado com sucesso!")
            return redirect('servicos:listaServico')
    form = ServicoForm()
    context['form'] = form   
    return render(request, template_name, context)



@login_required
def listaServico(request):
    template_name = 'servicos/listaServico.html'

    oficina = Oficina.objects.filter(usuario=request.user).first()
    servicos = Servico.objects.filter(oficina = oficina)
    context = {
        'servicos':servicos,
    }
    return render(request, template_name, context)

@login_required
def deletarServico(request, pk):
    oficina = Servico.objects.get(pk=pk)
    oficina.delete()
    messages.info(request, 'Serviço deletado')
    return redirect('servicos:listaServico')

@login_required
def editarServico(request, pk):
    template_name = 'servicos/novoServico.html'
    context = {}
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(data=request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço editado com sucesso.')
            return redirect('servicos:listaServico')
    form = ServicoForm(instance=servico)
    context['form'] = form
    return render(request, template_name, context)

@login_required
def novaOrdemServico(request):
    template_name = 'servicos/novaOrdemServico.html'
    context = {}
    oficina = get_object_or_404(Oficina, usuario = request.user)
    if request.method == 'POST':
        form = OrdemServicoForm(request.POST)
        if form.is_valid():
            osf = form.save(commit = False)
            osf.oficina = oficina
            osf.save()
            form.save_m2m()
            messages.success(request, 'Ordem de Serviço criada com Sucesso')
            return redirect('servicos:listaOrdemServico')
    form = OrdemServicoForm
    context['form'] = form
    return render (request, template_name, context)

@login_required
def listaOrdemServico(request):
    template_name = 'servicos/listaOrdemServico.html'
    oficina = get_object_or_404(Oficina, usuario = request.user)
    ordensServicos = OrdemServico.objects.filter(oficina=oficina)
    context = {
        'ordensServicos':ordensServicos
    }
    return render(request, template_name, context)


@login_required
def editarOrdemServico(request, pk):
    template_name = 'servicos/novaOrdemServico.html'
    context = {}
    ordemServico = get_object_or_404(OrdemServico, pk=pk)
    if request.method == 'POST':
        form = OrdemServicoForm(data=request.POST, instance=ordemServico)
        if form.is_valid():
            form.save()
            messages.success( request,'Ordem de Serviço editada com sucesso')
            return redirect('servicos:listaOrdemServico')
    form = OrdemServicoForm(instance=ordemServico)
    context['form'] = form
    return render (request, template_name, context)
    
    
    
@login_required
def gerar_relatorio(request):
    template_name = 'servicos/gerar_relatorio.html'
    mecanico = request.GET.get('mecanico')
    data_inicial = request.GET.get('data_inicial')
    data_final = request.GET.get('data_final')
    ordem_servicos = OrdemServico.objects.filter(data_entrada__lte=data_inicial, data_entrega__lte=data_final, mecanico=mecanico, status=2)
    form = RelatorioForm()
    context = {
        'form': form,
        'ordens_servicos': ordens_servicos
    }
    return render(request, template_name, context)