from linguistic.models import *
import re, collections

class SeedClass:
 dictF=""
 NWORDS=[]
 alphabet ='abcdefghijklmnopqrstuvwxyz'
 
 def __init__(self,dictFile): 
  self.dictF=dictFile 
  self.NWORDS=self.train(self.words(open(dictFile).read()))
  print("Inited")
  
 def words(self,text): return re.findall('[a-z]+', text.lower())
 
 def train(self,features):
  model=collections.defaultdict(lambda: 1)
  for f in features:
   model[f]+=1
  return model
