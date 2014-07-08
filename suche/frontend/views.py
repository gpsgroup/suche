from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages


def home(request):
    '''
    This is the search engine home page handler.
    '''

    template = loader.get_template('frontend/home.html')

    context = RequestContext(request, {
        'title': "Suche"
    })
    return HttpResponse(template.render(context))
