'''
  from output of Grammar, if plugin then parse and get output result
  inputs: grammar selected , queries parsed
'''
import urllib.parse
import urllib.request

from plugin.models import *
class PluginProcessor:
    def __init__(self,grammar,queries):
        self.grammar=grammar
        self.queries=queries
    
    def dispatchandRead(self):
        '''
          dispatch and get output to be displayed if plugin allows
        
        '''
        #plugin server url
        url='http://127.0.0.1:8000/plugin/'+str(self.grammar.plugin.name)+'?queries='+str(self.queries)+'&privateKey='+str(self.grammar.plugin.privateKey)
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        strOut= response.read()
        return strOut
        