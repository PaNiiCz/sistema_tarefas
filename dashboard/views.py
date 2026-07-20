from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tarefas.models import Tarefa
from django.utils import timezone

@login_required
def dashboard(request):
    # Buscar tarefas do usuário logado
    tarefas = Tarefa.objects.filter(responsavel=request.user)
    
    total_tarefas = tarefas.count()
    tarefas_pendentes = tarefas.filter(status='pendente').count()
    tarefas_concluidas = tarefas.filter(status='concluida').count()
    tarefas_andamento = tarefas.filter(status='em_andamento').count()
    
    # Tarefas atrasadas (prazo vencido e não concluídas)
    hoje = timezone.now().date()
    tarefas_atrasadas = tarefas.filter(
        prazo__lt=hoje
    ).exclude(status__in=['concluida', 'cancelada']).count()
    
    # Tarefas urgentes
    tarefas_urgentes = tarefas.filter(prioridade='urgente').exclude(status__in=['concluida', 'cancelada']).count()
    
    # Percentual de conclusão
    if total_tarefas > 0:
        percentual_conclusao = round((tarefas_concluidas / total_tarefas) * 100)
    else:
        percentual_conclusao = 0
    
    # Próximas tarefas (prazo mais próximo, não concluídas)
    proximas_tarefas = tarefas.exclude(
        status__in=['concluida', 'cancelada']
    ).order_by('prazo')[:5]
    
    contexto = {
        'tarefas_pendentes': tarefas_pendentes,
        'tarefas_concluidas': tarefas_concluidas,
        'tarefas_andamento': tarefas_andamento,
        'tarefas_atrasadas': tarefas_atrasadas,
        'tarefas_urgentes': tarefas_urgentes,
        'total_tarefas': total_tarefas,
        'percentual_conclusao': percentual_conclusao,
        'proximas_tarefas': proximas_tarefas,
    }
    return render(request, 'dashboard/dashboard.html', contexto)