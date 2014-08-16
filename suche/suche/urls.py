from django.conf.urls import patterns, include, url
from django.contrib import admin
import frontend.views as frontendview
import pluginServer.views as plSrv
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suche.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', frontendview.home, name='homepage'),
    url(r'^autocomplete$',frontendview.autocomplete, name = 'autocomplete'),
    url(r'^search$',frontendview.searchresult, name = 'searchresult'),
    url(r'^cache$',frontendview.websitecache, name = 'websitecache'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^crawler/', include('crawler.urls', namespace = 'crawler')),
    url(r'^plugin/(?P<name>[a-zA-Z0-9_.-]+)/$',plSrv.pluginProcessServer,name='pluginLink'),
	url(r'^auth/', include('authuser.urls', namespace = 'authuser')),
)
)
