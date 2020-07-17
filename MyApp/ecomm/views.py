# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import ProductInformation

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    name = "VidishJoshi"
    return render(request, 'home.html', {
        'name': name
    })

def view_info(request):
    value = request.GET.get('category')
    content = ProductInformation.objects.filter(category=value).values_list('id', 'name', 'price')
    return render(request, 'view_info.html', {
        'content' : content
    })

def more_info(request):
    id_from_url = request.GET.get('id')
    content = ProductInformation.objects.filter(id = id_from_url).values_list()
    return HttpResponse(content)