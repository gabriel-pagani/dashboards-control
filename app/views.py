from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .utils.metabase import generate_dashboard_url
from .utils.acessos import get_dashboards_do_usuario
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache


@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'auth/login.html')


@never_cache
@login_required
def home_view(request):
    dados = dict()

    for dashboard in get_dashboards_do_usuario(request.user):
        setor = dashboard.setor
        dados.setdefault(setor, []).append(
            {
                'titulo': dashboard.titulo,
                'url': generate_dashboard_url(dashboard.codigo)
            }
        )

    return render(request, 'main.html', {'dados': dados})


@never_cache
def logout_view(request):
    logout(request)
    response = redirect('login')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
