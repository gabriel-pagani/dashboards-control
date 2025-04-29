from django.shortcuts import render
from django.http import HttpResponse
from .utils.metabase import generate_dashboard_url


def home(request):
    return render(
        request,
        'index.html',
        {'dashboard': generate_dashboard_url(38)}
    )


def users(request):
    return HttpResponse('users!!!')


def dashboards(request):
    return HttpResponse('dashboards!!!')
