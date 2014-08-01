'''
indexer for suche Search Engine
copyright (c) 2014 Suche
'''
from indexer.models import SucheURL
from indexer.htmlparser import HTMLParser

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

        parser = HTMLParser(self.raw.new_data, self.raw.url)

        parser.parse()

        #now extract information from the parse and update database
        urls = []
        
        for url,text in parser.get_links():
            urls.append(text+"-"+url)
            newurl,created = SucheURL.objects.get_or_create(url = url)
            if created:
                #create the crawl record for the newly generated url
                newdata = CrawlData(url = newurl)
                newdata.save()
        return '<br/>'.join(urls)

