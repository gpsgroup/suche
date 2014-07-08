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

def autocomplete(request):
    '''
    Auto complete for suche
    auto completes the user entered sentence
    '''
    import json
    
    words = [
        "apple",
        "mango",
        "orange",
        "amanada",
        "anup",
        "amy",
        ]
    completions = []
    if 'search' in request.REQUEST:
        searchkey = request.REQUEST['search']
        for word in words:
            if word.startswith(searchkey):
                completions.append(word)
    resp = request.REQUEST['callback']+'('+json.dumps(completions)+');'
    return HttpResponse(resp,content_type = 'application/json')
