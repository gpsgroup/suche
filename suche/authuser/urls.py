from django.conf.urls import patterns, include, url
from django.contrib import admin
import authuser.views as authview


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suche.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^signin$',authview.signin, name = 'signin'),
    url(r'^signup$',authview.signup, name = 'signup'),
    url(r'^signout$',authview.signout, name = 'signout'),
    #url(r'^$', frontendview.home, name='homepage'),
    # url(r'^search$',frontendview.searchresult, name = 'searchresult'),
    # url(r'^cache$',frontendview.websitecache, name = 'websitecache'),
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^crawler/', include('crawler.urls', namespace = 'crawler')),
    #url(r'^plugin/(?P<name>[a-zA-Z0-9_.-]+)/$',plSrv.pluginProcessServer,name='pluginLink'),
    #url(r'^test/$',plSrv.test,name='test'),
)
