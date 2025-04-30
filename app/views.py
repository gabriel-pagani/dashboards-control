from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .utils.metabase import generate_dashboard_url


@login_required
def home(request):
    dashboard_urls = [
        {
            'titulo': dashboard.titulo,
            'setor': dashboard.setor,
            'url': generate_dashboard_url(dashboard.codigo)
        }
        for dashboard in request.user.dashboards.all()
    ]
    return render(request, 'index.html', {'dashboard_urls': dashboard_urls})
