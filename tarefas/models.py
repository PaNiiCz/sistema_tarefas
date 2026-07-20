from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tarefa(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]
    
    PRIORIDADE_CHOICES = [
        ('baixa', 'Baixa'),
        ('media', 'Média'),
        ('alta', 'Alta'),
        ('urgente', 'Urgente'),
    ]
    
    titulo = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='media')
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tarefas')
    data_criacao = models.DateTimeField(auto_now_add=True)
    prazo = models.DateField(null=True, blank=True)
    etiqueta = models.CharField(max_length=50, blank=True, null=True)
    
    class Meta:
        ordering = ['-data_criacao']
        verbose_name = 'Tarefa'
        verbose_name_plural = 'Tarefas'
    
    def __str__(self):
        return self.titulo
    
    @property
    def esta_atrasada(self):
        if self.prazo and self.status not in ['concluida', 'cancelada']:
            return self.prazo < timezone.now().date()
        return False