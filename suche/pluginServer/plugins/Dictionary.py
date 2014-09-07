'''
   Plugin Name: Dictionary
   Shows Output: Yes
   
'''
import urllib.parse
import urllib.request
import json
from pluginServer.models import Wordmeaning
class Dictionary:
    
    def __init__(self,word,privateKey):
        self.privateKey="7521540881349157844580958115462201373397910982421428949841118953157992578839" # keep this in app
        self.word = word.lower()
        self.privateKeySent=privateKey
         
    def run(self):
        try:
            word = Wordmeaning.objects.get(word = self.word)
        except Wordmeaning.DoesNotExist:
            return ''
        meaning = '<br/>'.join(word.meaning.split('\n'))
        op='<div class="resultBox" style="height:auto;"><div class="col-md-9"><div class="row"><div class="col-md-12"><span class="helvnu">'+self.word.title()+'</span></div></div><div class="row"><div class="col-md-12">'+meaning+'</div></div></div> <div class="col-md-3"></div></div>'
        return op
        
    def getPrivateKey(self):
        return self.privateKey
