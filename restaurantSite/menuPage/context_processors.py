from django.conf import settings
from django.shortcuts import render

def IMAGE_STORAGE(request):
    context = {
        'IMAGE_STORAGE': settings.IMAGE_STORAGE,
    }