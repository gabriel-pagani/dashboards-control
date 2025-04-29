from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse('home!!!')


def users(request):
    return HttpResponse('users!!!')


def dashboards(request):
    return HttpResponse('dashboards!!!')
