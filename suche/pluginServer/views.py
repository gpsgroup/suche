from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest
from django.template import RequestContext, loader
from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.contrib import messages
from pluginServer.plugins import *
from pluginServer.plugins import Dictionary

# Create your views here.
def pluginProcessServer(request,name):
   
    queriesStr=request.GET.get('queries', '')
    queries=eval(str(queriesStr))
    privateKey=request.GET.get('privateKey', '')
    
    a=name+"("
    for query in queries:
        a=a+'"'+query+'",'
    a=a+'"'+privateKey+'")'
   
    z=eval(a)
    
    appPrivateKey=z.getPrivateKey()
    if(privateKey==appPrivateKey):    
        return HttpResponse(str(z.run()))
    else:
        return HttpResponse('err')
   
