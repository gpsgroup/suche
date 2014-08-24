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

        previousurls = []
        #search for the words in the word list
        totalresult = 0
        shownresult = 0
        for word in words:
            try:
                wordobj = Word.objects.get(word = word)
                results = Result.objects.filter(word = wordobj)

                for res in results:
                    totalresult += 1
                    if not res.url.url in previousurls and shownresult < 100:
                        shownresult += 1
                        previousurls.append(res.url.url)

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
                        self.results.append(result)
                    else:
                        #url already exist...increase it's URL point
                        pass
            except Word.DoesNotExist:
                # do nothing
                pass
        #now arrange the result according to ranking
        self.totalresult = totalresult
        self.results.sort(key=lambda x: x.urlpoint, reverse = True)
        
        
