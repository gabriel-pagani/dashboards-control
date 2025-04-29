from django.db import models
from django.contrib.auth.models import User


class Dashboard(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='dashboards')
    dashboard_id = models.IntegerField()

    def __str__(self):
        return f'Dashboard {self.dashboard_id} de {self.user.username}'
