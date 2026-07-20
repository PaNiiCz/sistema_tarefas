from django.contrib import admin
from .models import Tarefa

@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'status', 'prioridade', 'responsavel', 'prazo', 'data_criacao')
    list_filter = ('status', 'prioridade', 'responsavel')
    search_fields = ('titulo', 'descricao')
    ordering = ('-data_criacao',)