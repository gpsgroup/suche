from django.conf.urls import patterns, url

from crawler import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^crawlpage$', views.CrawlPage, name='crawlpage'),
    url(r'^operatedata$', views.OperateData, name='operatedata'),
)
