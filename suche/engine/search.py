from indexer.models import SucheURL,Result,Word
from linguistic.queryhandler import QueryHandler
from engine.result import SucheResult
from crawler.models import Rawdata
from indexer.htmlparser import HTMLParser

class SucheSearch:
    def __init__(self):
        pass

    def SetQuery(self,query,correct = True, register = True):
        '''
        Sets the query for the search session
        correct flag determines if the engine should try to autocorrect the query
        register determines if the engine should register query in query handler
        '''
        self.query = query

        if correct:
            self.correctedquery = QueryHandler.correct_query(query)
        else:
            self.correctedquery = query
        if register:
            QueryHandler.register_query(self.correctedquery)

    def isQueryCorrected(self):
        '''
        returns if the search query is corrected by the engine
        '''
        return not self.query == self.correctedquery

    def search(self):
        '''
        searches
        '''
        #get the word list
        words = self.correctedquery.split(' ')
        
        self.results = []
        dictresult = {}
        
        #search for the words in the word list
        totalresult = 0
        shownresult = 0
        for word in words:
            if len(word) <= 2:
                continue
            try:
                wordobj = Word.objects.get(word = word)
                results = Result.objects.filter(word = wordobj)

                for res in results:
                    totalresult += 1
                    if not res.url.url in dictresult.keys() or shownresult < 100:
                        shownresult += 1

                        try:
                            rawdata = Rawdata.get(url = res.url)
                        except:
                            # Error! We should not reach here. This means a URL is indexed but we don't
                            # have the html data
                            pass
                        
                        result = SucheResult()
                        result.setQuery(self.correctedquery)
                        result.fullurl = res.url.url
                        result.url = res.url.url if len(res.url.url) < 50 else res.url.url[:49]+"..."
                        result.urlpoint = res.urlpoint
                        result.fullurl = res.url.url
                        result.body = res.url.body

                        # fullbody contains the complete HTML of the page
                        
                        
                        result.title = res.url.title

                        dictresult[res.url.url] = result
                    else:
                        if res.url.url in dictresult.keys():
                            dictresult[res.url.url].urlpoint += 5
                            #dictresult[res.url.url].title += "MODIFIED!"

            except Word.DoesNotExist:
                # do nothing
                pass
        for url in dictresult.keys():
            self.results.append(dictresult[url])
        #now arrange the result according to ranking
        self.totalresult = totalresult
        self.results.sort(key=lambda x: x.urlpoint, reverse = True)
        
        
