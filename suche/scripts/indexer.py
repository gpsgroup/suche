from indexer.indexer import Indexer
from crawler.models import CrawlData,Rawdata
import time

def run():
    while True:
        try:
            rawdata = Rawdata.objects.filter(operated = False)[0] # get data that has not been operated on yet
            indxr = Indexer()
            indxr.set_raw(rawdata)
            message = indxr.operate()
            print("Finished processing "+rawdata.url.url)
        except IndexError:
            print("All Data have veen operated")
        time.sleep(1)
