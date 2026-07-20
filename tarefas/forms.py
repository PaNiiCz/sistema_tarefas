from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'status', 'prioridade', 'prazo', 'etiqueta']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título da tarefa'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Descrição detalhada...'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'prazo': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'etiqueta': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: bug, feature, melhoria'}),
        }