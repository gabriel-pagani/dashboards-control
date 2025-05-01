from django.db import models
from django.contrib.auth.models import User, Group


class Dashboard(models.Model):
    titulo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    codigo = models.IntegerField()
    usuarios = models.ManyToManyField(User, related_name='dashboards', blank=True)
    grupos = models.ManyToManyField(Group, related_name='dashboards', blank=True)

    def __str__(self) -> str:
        return self.titulo
