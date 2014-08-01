'''
indexer for suche Search Engine
copyright (c) 2014 Suche
'''
from indexer.models import SucheURL
class Indexer:
    def set_raw(self,raw):
        '''
        sets the raw data row to which the indexer is to operate.
        '''
        self.raw = raw

    def operate(self):
        '''
        operate on the data. This will extract links, etc
        First of all, we have to revert back the changes of previous website data for eg reduce the number 
        of links, reduce word counts, etc. Then, we have to apply the changes due to new data. Finally, move 
        the new data to old data and set oeprated to true
        '''

        from bs4 import BeautifulSoup, SoupStrainer
        from urllib.parse import urljoin
        soup = BeautifulSoup(self.raw.new_data)

        #extract URLs and operate on them
        urls = []
        for link in soup.find_all('a'):
            filteredurl = SucheURL.filterURL(urljoin(self.raw.url.url,link.get('href')))
            if SucheURL.isvalid(filteredurl): # check if it is a valid URL
                newurl,created = SucheURL.objects.get_or_create(url = filteredurl)
                if created:
                    #create the crawl record for the newly generated url
                    newdata = CrawlData(url = newurl)
                    newdata.save()
                urls.append(filteredurl)
        self.raw.operated = True
        self.raw.save()
        return '<br/>'.join(urls)

