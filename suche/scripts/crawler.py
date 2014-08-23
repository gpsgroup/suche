from crawler.models import CrawlData,Rawdata
import time
import datetime

def run():
    while True:
        try:
            crawldata = CrawlData.objects.filter(next_crawl__lte = datetime.datetime.now())[0] # get a URL that is expected to be crawl in the past or at the current instance
        except IndexError:
            print("All URLs are up to date")
            
        # try to get the web page from URL
        print(crawldata.url.url+" is not currently crawled. Crawling it...")
        
        if not crawldata.crawl():
            print('Error  while retriving the web page')
        time.sleep(1) # do some rest 
        
