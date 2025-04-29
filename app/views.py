from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(
        request,
        'home.html'
    )


def users(request):
    return HttpResponse('users!!!')


def dashboards(request):
    return HttpResponse('dashboards!!!')
