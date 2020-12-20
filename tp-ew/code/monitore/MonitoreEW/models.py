from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Disciplina (models.Model):
    codigo_disciplina = models.CharField ('codigo disciplina', max_length=7, default=None)
    nome_disciplina = models.CharField ('nome dsiciplina', max_length=50, default=None)
    curso = models.CharField('Curso', max_length=50, default=None)
    professor = models.CharField('professor', max_length=50, default=None)

    class Meta:
        ordering = ('codigo_disciplina', )

    def __str__(self):
        return self.codigo_disciplina

    def get_delete_url(self):
        return reverse('disciplina-delete', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('disciplina-update', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('disciplina-detail', kwargs={'pk': self.pk})



class Aluno (models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nome_aluno = models.CharField ('Nome do aluno', max_length=60, default=None)
    matricula_aluno = models.CharField ('Matricula', max_length=11, default=None)
    monitor = models.BooleanField (default=False)
    disciplinas_matriculadas = models.ManyToManyField (Disciplina)

    class Meta:
        ordering = ('nome_aluno', )

    def __str__(self):
        return self.nome_aluno


class monitoria (models.Model):
    disciplina = models.ForeignKey (Disciplina, on_delete=models.CASCADE)
    aluno = models.ForeignKey (Aluno, on_delete=models.CASCADE)
    horario = models.TimeField (default=None)
    data = models.DateField (default=None)
    local = models.CharField("local", max_length=200, default=None)

    class Meta:
        ordering = ('data', )

    def __str__(self):
        return self.data

    def get_delete_url(self):
        return reverse('data-delete', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('data-update', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('data-detail', kwargs={'pk': self.pk})
