from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .utils.metabase import generate_dashboard_url
from .utils.acessos import get_dashboards_do_usuario
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


@never_cache
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        try:
            if not user.last_login:
                login(request, user)
                return redirect('password-change')
            elif user:
                login(request, user)
                return redirect('home')
        except:
            messages.error(
                request, 'Usuário ou senha incorretos. Tente novamente!')
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


@never_cache
@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Sua senha foi alterada com sucesso!')
            return redirect('logout')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'auth/change_password.html', {
        'form': form,
    })
