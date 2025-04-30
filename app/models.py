from django.db import models
from django.contrib.auth.models import User


class Dashboard(models.Model):
    titulo = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    codigo = models.IntegerField()
    usuarios = models.ManyToManyField(User, related_name='dashboards')

    def __str__(self) -> str:
        return self.titulo
