from django.shortcuts import render
from djangohttp import HttpResponse

def index(request):
    return HttpResponse('This is PeshGallery')

