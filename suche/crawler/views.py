from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.core.exceptions import ObjectDoesNotExist
from crawler.models import CrawlData,Rawdata
from indexer.indexer import Indexer
from django.template import RequestContext, loader
import datetime
import urllib3
from django.utils import timezone

def index(request):
    template = loader.get_template('crawler/index.html')

    context = RequestContext(request, {
        'title': "Suche : Crawler Admin Home",
    })
    return HttpResponse(template.render(context))

def CrawlPage(request):
    ''' this is used to crawl a single page. This function searches
    for any URL having scheduled crawl time less than current time( in the past)
    and crawls the first URL it finds.'''

    #first of all, search for any URL that has scheduled crawl time in the past
    try:
        crawldata = CrawlData.objects.filter(next_crawl__lte = datetime.datetime.now())[0] # get a URL that is expected to be crawl in the past or at the current instance
    except IndexError:
        return HttpResponse("All webpages up to date")

    message = ''

    # try to get the web page from URL
    message += crawldata.url.url+" is not currently crawled. Crawling it..."

    if not crawldata.crawl():
        message += '<font color=red>Error while retriving the web page</font><br/>' # classic HTML :D

    return HttpResponse(message)

def OperateData(request):
    message = ''
    try:
        rawdata = Rawdata.objects.filter(operated = False)[0] # get data that has not been operated on yet
        indxr = Indexer()
        indxr.set_raw(rawdata)
        urls = indxr.operate()
        return HttpResponse("Finished processing "+urls)
    except IndexError:
        return HttpResponse("All Data have veen operated")
