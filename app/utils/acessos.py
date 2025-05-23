from app.models import Dashboard

def get_dashboards_do_usuario(user):
    if user.is_superuser:
        return Dashboard.objects.all()

    dashboards_usuario = Dashboard.objects.filter(usuarios=user)
    grupos_ids = user.groups.values_list('id', flat=True)
    dashboards_grupo = Dashboard.objects.filter(grupos__in=grupos_ids)

    return (dashboards_usuario | dashboards_grupo).distinct()
