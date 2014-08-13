'''
result.py
contains class for search result
'''
from indexer.models import SucheURL
from linguistic.queryhandler import QueryHandler

class SucheResult:
    def __init__(self,url,query):
        pass
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
        self.results = []
        
        for i in range(0,100):
            result = SucheResult('','')
            result.title = "Hello world"
            result.body = "This is the body of the result"
            result.url = "http://google.com..."
            result.fullurl = "http://google.com/search?q=Hello+word"
            self.results.append(result)
        
    
