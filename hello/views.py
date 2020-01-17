from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    c = {
        'name': "sutin injitt",
        'nick_name': "thinny",
        'age': 30,
        'food': ['water', 'pepsi', 'soda']
    }
    t = loader.get_template('index.html')
    return HttpResponse(t.render(c, request))
