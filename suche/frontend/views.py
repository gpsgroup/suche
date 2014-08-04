from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from linguistic.queryhandler import QueryHandler


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
    toOut=""
    divRowHeader='<div class="row">'
    titleSpan='<span style="font-family:Arial, Helvetica, sans-serif; color:#0a5c83; font-weight:bold">'
    linkSpan='<span style="font-family:Arial, Helvetica, sans-serif; color:#070; font-size:12px">'
    contentSpan='<span style="font-family:Verdana, Geneva, sans-serif; font-size:14px;font-weight:lighter">'
    
    
    divEnd='</div>'
    
    #for loop for each result
    for i in range(10):
        toOut+=divRowHeader
        #enter title,link,content for results here
        link="http://google.com"
        title="This is a search Title"
        content='This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.This is content.'
        
        #display formatting
        toOut+=divRowHeader+'<a href="'+link+'" style="text-decoration:none">'+titleSpan+title+'</span></a></div>'
        toOut+=divRowHeader+linkSpan+link+'</span></div>'
        toOut+=divRowHeader+contentSpan+content+'</span></div>'
        toOut+='</div><br>'
    return HttpResponse(toOut)    
    

