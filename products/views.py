from django.http import HttpResponse
from django.shortcuts import render

# /products -> index


def index(request):
    return HttpResponse('this is products...')


def new(request):
    return HttpResponse('this is new products...')
