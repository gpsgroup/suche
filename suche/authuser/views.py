from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages


def signin(request):
    ''' This displays  the login page'''
    #first of all, check if the user is already logged in
    if request.user.is_authenticated():
        # redirect to the dashboard
        return HttpResponseRedirect(reverse('homepage'))
    # check if the user logged in
    error = ''
    if request.method == 'POST':
        # username and password are required
        if request.POST.get('username', None) and request.POST.get('password', None):
            # try to log in
            if not request.POST.get('remember', None):
                request.session.set_expiry(0)
            else:
                request.session.set_expiry(86400*30) # remember for 30 days
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                error = "Authentication Error!"
        else:
            error = "Please fill all the fields"
    
    template = loader.get_template('authuser/signin.html')

    context = RequestContext(request, {
        'title': "Suche:Sign In",
        'error' : error,
        'user' : request.user
    })
    return HttpResponse(template.render(context))

def signup(request):
    ''' This displays  the signup page'''
    #first of all, check if the user is already logged in
    if request.user.is_authenticated():
        # redirect to the dashboard
        return HttpResponseRedirect(reverse('homepage'))
    # check if the user logged in
    error = ''
    if request.method == 'POST':
        # username and password are required
        name = request.POST.get('username', None)
        email = request.POST.get('email', None) 
        pw =request.POST.get('password', None)
        pwc =request.POST.get('passwordc', None)

        if name and email and pw and pwc:
            
            if pw == pwc:
                try:
                    user = User.objects.create_user(name, email, pw)
                except:
                    error = "user couldnt be created"
                    
                 # log in
                user = authenticate(username=name,password=pw)
                login(request, user)
                request.session.set_expiry(0)          
                return HttpResponseRedirect(reverse('homepage'))  
            else:
                error = "password dont match"           
                    
        else:
            error = "Please fill all the fields"
    
    template = loader.get_template('authuser/signup.html')

    context = RequestContext(request, {
        'title': "Suche:Sign UP",
        'error' : error,
        'user' : request.user
    })
    return HttpResponse(template.render(context))

@login_required(login_url='/')
def signout(request):
    logout(request)
    messages.success(request, 'Successfully Signed Out')
    return HttpResponseRedirect(reverse('homepage'))


def userinfo(request):
    ''' This displays  the login page'''
    #first of all, check if the user is already logged in
    if request.user.is_authenticated():
        pass
   
    error =''    
            
    template = loader.get_template('authuser/usrinfo.html')

    context = RequestContext(request, {
        'title': "Suche:Sign In",
        
        'user' : request.user
    })
    return HttpResponse(template.render(context))