from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Tarefa
from .forms import TarefaForm

@login_required
def lista_tarefas(request):
    tarefas = Tarefa.objects.filter(responsavel=request.user)
    
    # Filtros
    status_filter = request.GET.get('status')
    prioridade_filter = request.GET.get('prioridade')
    busca = request.GET.get('busca')
    
    if status_filter:
        tarefas = tarefas.filter(status=status_filter)
    if prioridade_filter:
        tarefas = tarefas.filter(prioridade=prioridade_filter)
    if busca:
        tarefas = tarefas.filter(titulo__icontains=busca)
    
    contexto = {
        'tarefas': tarefas,
        'total_pendentes': Tarefa.objects.filter(responsavel=request.user, status='pendente').count(),
        'total_concluidas': Tarefa.objects.filter(responsavel=request.user, status='concluida').count(),
        'total_atrasadas': sum(1 for t in Tarefa.objects.filter(responsavel=request.user) if t.esta_atrasada),
    }
    return render(request, 'tarefas/lista.html', contexto)

@login_required
def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.responsavel = request.user
            tarefa.save()
            messages.success(request, 'Tarefa criada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm()
    
    return render(request, 'tarefas/form.html', {'form': form, 'titulo': 'Nova Tarefa'})

@login_required
def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, responsavel=request.user)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tarefa atualizada com sucesso!')
            return redirect('lista_tarefas')
    else:
        form = TarefaForm(instance=tarefa)
    
    return render(request, 'tarefas/form.html', {'form': form, 'titulo': 'Editar Tarefa'})

@login_required
def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk, responsavel=request.user)
    tarefa.delete()
    messages.success(request, 'Tarefa excluída com sucesso!')
    return redirect('lista_tarefas')
