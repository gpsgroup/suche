'''
Crawler model for django
Copyright (c) 2014 by anup pokhrel
'''

from django.db import models
from django.utils import timezone
from indexer.models import SucheURL
from datetime import datetime, timedelta
import urllib3



class Rawdata(models.Model):
    '''
    RawData class stores raw data of the website. It contains the whole content
    of the website for further processing. It can conditionally store both old and new data.
    But, it is checked frequently and the old data is removed and new transferred to the old data
    '''
    url = models.OneToOneField(SucheURL)
    new_data = models.TextField(default = '', blank = True)
    old_data = models.TextField(default = '', blank = True)
    operated = models.BooleanField(default = False) # represent if the data has been already operated.

class CrawlData(models.Model):
    '''
    CrawlData records the data regarding to crawling like the last crawl date,
    the scheduled next crawl data, etc
    '''
    url = models.OneToOneField(SucheURL)

    last_crawl = models.DateTimeField(default = timezone.now())
    next_crawl = models.DateTimeField(default = timezone.now())
    timeDiff=models.PositiveIntegerField(default=86400)
    
        

    #uptodate represent if the website is up to date
    def uptodate(self):
        return self.next_crawl > timezone.now()

    uptodate.boolean = True
    uptodate.short_description = 'URL Up to Date?'
    
    #check if content has changed, pass rawdata object
    def isChanged(self,rawdata):
        if rawdata.old_data==rawdata.new_data:
            return False
        else:
            return True
    
    #compute next time
    '''
        timeCalcType =
        0=>HTTP 200
        1=>Others
    '''
    def computeTimeDiff(self,rawdata,timeCalcType):   
        #calculate the next timeDiff
        if(timeCalcType==0):            
            if self.isChanged(rawdata):
                timeDiffCalc=int(self.timeDiff/2)
                if(timeDiffCalc<3600):
                    self.timeDiff=3600
                else:
                    self.timeDiff=timeDiffCalc
            else:
                timeDiffCalc=self.timeDiff*2
                if(timeDiffCalc>2592000):#greater than a month
                    self.timeDiff=2592000
                else:
                    self.timeDiff=timeDiffCalc
                    
        elif(timeCalcType==1):
            timeDiffCalc=self.timeDiff*2
            if(timeDiffCalc>2592000):#greater than a month
                self.timeDiff=2592000
            else:
                self.timeDiff=timeDiffCalc
         
    
    #crawl the web url
    def crawl(self):
        http = urllib3.PoolManager()
        crawled = False
        try:
            r = http.request('GET', self.url.url)
            if r.status == 200:
                #see if the rawdata table has row for the current URL. If no, create one
                rawdata , created = Rawdata.objects.get_or_create(url = self.url)
                if not created:
                    rawdata.old_data=rawdata.new_data
                else:
                    rawdata.old_data=''
                    
                rawdata.new_data = r.data
                rawdata.save()
                crawled = True
                #set timeDiff to new value
                self.computeTimeDiff(rawdata,0)
                self.last_crawl = timezone.now()
                self.next_crawl = timezone.now() + timedelta(seconds=self.timeDiff)
                
            else:
                self.last_crawl = timezone.now()
                self.computeTimeDiff(rawdata,1)
                self.next_crawl = timezone.now() + timedelta(seconds=self.timeDiff)

        except:
            pass # error occured
        #set next update after 10 days. We can surely set it to more logical pattern like
        # crawl frequently for fast changing websites. But for now, set it fixed to 10 days
        self.save(force_update = True)
        return crawled
