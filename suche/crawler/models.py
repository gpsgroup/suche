
'''
Crawler model for django
Copyright (c) 2014 by anup pokhrel
'''

from django.db import models
from django.utils import timezone
from indexer.models import SucheURL
import datetime
import urllib3



#class Rawdata(models.Model):
#    '''
#    RawData class stores raw data of the website. It contains the whole content
#    of the website for further processing. It can conditionally store both old and new data.
#    But, it is checked frequently and the old data is removed and new transferred to the old data
#    '''
#    url = models.OneToOneField(SucheURL)
#    new_data = models.TextField(default = '', blank = True)
#    old_data = models.TextField(default = '', blank = True)
#    operated = models.BooleanField(default = False) # represent if the data has been already operated.
#
#    def operate(self):
#        '''
#        operate on the data. This will extract links, etc
#        First of all, we have to revert back the changes of previous website data for eg reduce the number 
#        of links, reduce word counts, etc. Then, we have to apply the changes due to new data. Finally, move 
#        the new data to old data and set oeprated to true
#        '''
#        from bs4 import BeautifulSoup, SoupStrainer
#        soup = BeautifulSoup(self.new_data)
#
#        #extract URLs and operate on them
#        urls = []
#        for link in soup.find_all('a'):
#            filteredurl = SucheURL.filterURL(urljoin(self.url.url,link.get('href')))
#            if SucheURL.isvalid(filteredurl): # check if it is a valid URL
#                newurl = SucheURL.objects.get_or_create(url = filteredurl)
#                urls.append(filteredurl)
#        return '<br/>'.join(urls)
#
#class CrawlData(models.Model):
#    '''
#    CrawlData records the data regarding to crawling like the last crawl date,
#    the scheduled next crawl data, etc
#    '''
#    url = models.OneToOneField(SucheURL)
#
#    last_crawl = models.DateTimeField()
#    next_crawl = models.DateTimeField()
#
#    #uptodate represent if the website is up to date
#    def uptodate(self):
#        return self.next_crawl > timezone.now()
#    uptodate.boolean = True
#    uptodate.short_description = 'URL Up to Date?'
#
#
#    #crawl the web url
#    def crawl(self):
#        http = urllib3.PoolManager()
#        crawled = False
#        try:
#            r = http.request('GET', self.url.url)
#            if r.status == 200:
#                #see if the rawdata table has row for the current URL. If no, create one
#                rawdata , created = Rawdata.objects.get_or_create(url = self.url)
#                rawdata.new_data = r.data
#                rawdata.save()
#                crawled = True
#        except:
#            pass # error occured
#        #set next update after 10 days. We can surely set it to more logical pattern like
#        # crawl frequently for fast changing websites. But for now, set it fixed to 10 days
#        self.last_crawl = datetime.datetime.now()
#        self.next_crawl = datetime.datetime.now() + datetime.timedelta(days=10)
#        self.save(force_update = True)
#        return crawled
