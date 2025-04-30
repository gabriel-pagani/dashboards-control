from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils.metabase import generate_dashboard_url


@login_required
def home(request):
    dados = dict()

    for dashboard in request.user.dashboards.all():
        setor = dashboard.setor
        dados.setdefault(setor, []).append(
            {
                'titulo': dashboard.titulo,
                'url': generate_dashboard_url(dashboard.codigo)
            }
        )

    return render(request, 'index.html', {'dados': dados})
