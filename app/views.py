from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Dashboard
from .utils.metabase import generate_dashboard_url


@login_required
def home(request):
    dashboard_urls = [
        {
            'id': dash.dashboard_id,
            'url': generate_dashboard_url(dash.dashboard_id)
        }
        for dash in request.user.dashboards.all()
    ]
    return render(request, 'index.html', {'dashboard_urls': dashboard_urls})
