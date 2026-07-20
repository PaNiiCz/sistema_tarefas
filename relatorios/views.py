from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from tarefas.models import Tarefa
from django.utils import timezone

@login_required
def relatorio(request):
    tarefas = Tarefa.objects.filter(responsavel=request.user)

    por_status = tarefas.values('status').annotate(total=Count('id')).order_by('status')
    por_prioridade = tarefas.values('prioridade').annotate(total=Count('id')).order_by('prioridade')

    hoje = timezone.now().date()
    atrasadas = tarefas.filter(prazo__lt=hoje).exclude(status__in=['concluida', 'cancelada']).order_by('prazo')

    etiquetas = (
        tarefas.exclude(etiqueta__isnull=True)
        .exclude(etiqueta__exact='')
        .values('etiqueta')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    contexto = {
        'total_tarefas': tarefas.count(),
        'por_status': por_status,
        'por_prioridade': por_prioridade,
        'atrasadas': atrasadas,
        'etiquetas': etiquetas,
    }
    return render(request, 'relatorios/relatorio.html', contexto)