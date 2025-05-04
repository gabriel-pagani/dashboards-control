from django.db import models
from django.contrib.auth.models import User, Group


class Dashboard(models.Model):
    SETORES = [
        ('Tecnologia da Informação', 'Tecnologia da Informação'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Financeiro', 'Financeiro'),
        ('Administrativo', 'Administrativo'),
    ]

    titulo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100, choices=SETORES)
    codigo = models.IntegerField()
    usuarios = models.ManyToManyField(User, related_name='dashboards', blank=True)
    grupos = models.ManyToManyField(Group, related_name='dashboards', blank=True)

    def __str__(self) -> str:
        return self.titulo

    class Meta:
        ordering = ['setor']
