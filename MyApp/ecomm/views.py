# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    name = "VidishJoshi"
    return render(request, 'home.html', {
        'name': name
    })

def view_info(request):
    value = request.GET.get('category')
    return HttpResponse(value)