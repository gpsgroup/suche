from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from linguistic.autocompletion import AutoCompletion

def home(request):
    '''
    This is the search engine home page handler.
    '''

    template = loader.get_template('frontend/home.html')

    query = request.REQUEST.get('q','')
    if query:
        # if the user entered some text, record it
        AutoCompletion.register_query(query)

    context = RequestContext(request, {
        'title': "Suche",
        'query' : query,
    })
    return HttpResponse(template.render(context))

def autocomplete(request):
    '''
    Auto complete for suche
    auto completes the user entered sentence
    to test this view,
    http://127.0.0.1:8000/autocomplete?callback=autocomplete&search=a
    '''
    import json
    completions = []
    if 'search' in request.REQUEST:
        completions = AutoCompletion.get_completions(request.REQUEST['search'])
    resp = request.REQUEST['callback']+'('+json.dumps(completions)+');'
    return HttpResponse(resp,content_type = 'application/json')
