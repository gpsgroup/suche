from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from linguistic.queryhandler import QueryHandler
from engine.result import SucheResult

def home(request):
    '''
    This is the search engine home page handler.
    '''

    template = loader.get_template('frontend/home.html')

    query = request.REQUEST.get('q','')
    correctedquery = ''
    parsedquery=''
    if query:
        # if the user entered some text, record it
        correctedquery = QueryHandler.correct_query(query)
        parsedquery=str(QueryHandler.parse_query(correctedquery))
        QueryHandler.register_query(correctedquery)

        
    context = RequestContext(request, {
        'title': "Suche",
        'query' : query,
        'correctedquery' : correctedquery,
        'parsedquery':parsedquery,
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
        completions = QueryHandler.get_completions(request.REQUEST['search'])
    resp = request.REQUEST['callback']+'('+json.dumps(completions)+');'
    return HttpResponse(resp,content_type = 'application/json')

def searchresult(request):
    '''
      returns the search result div
      the url is /searchresult
      
    '''
    query = request.REQUEST.get('q','')
    if not query:
        return HttpResponse("Please enter your query")
    else:
        correctedquery = QueryHandler.correct_query(query)
        QueryHandler.register_query(correctedquery)

    corrected = False
    if correctedquery != query:
        corrected = True

    results = []
    for i in range(1,100):
        result = SucheResult('','')
        result.title = "Hello world"
        result.body = "This is the body of the result"
        result.url = "http://google.com..."
        result.fullurl = "http://google.com/search?q=Hello+word"
        
        results.append(result)

    template = loader.get_template('frontend/result.html')

    context = RequestContext(request, {
        'query' : query,
        'correctedquery' : correctedquery,
        'corrected' : corrected,
        'results':results,
    })
    return HttpResponse(template.render(context))
