from django.forms import ModelForm
from .models import *

class MonitoriaForm(ModelForm):
    class Meta:
        model = monitoria
        fields = '__all__'

class AlunoForm(ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class DisciplinaProdutoForm(ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'
