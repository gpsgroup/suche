from django.conf.urls import patterns, include, url
from django.contrib import admin
import authuser.views as authview


urlpatterns = patterns('',   
    url(r'^signin$',authview.signin, name = 'signin'),
    url(r'^signup$',authview.signup, name = 'signup'),
    url(r'^signout$',authview.signout, name = 'signout'),
    url(r'^userinfo$',authview.userinfo, name = 'userinfo'),
    
)
