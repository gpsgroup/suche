#an interface function repo for sending and receiving words to and from the spell checker
#test.py contains demo usage
from linguistic.models import SpellCache
import time
class DInterface:
 def __init__(self):
  return
#used to send word to the spell corrector
 def writeWord(self,wordd):
  readClass=SpellCache.objects.filter(req=wordd)[:1]
  if(readClass.count()>0):  
    return readClass[0].id  
  #write to db the word that is to be sent    
  saveWord=SpellCache(req=wordd,sol="")
  saveWord.save()
  return saveWord.id
    
   
#used to receive word from the spell corrector receives 
 def readWord(self,idIn):  
  readClass=SpellCache.objects.get(id=idIn)
  while(not readClass.sol):
   readClass=SpellCache.objects.get(id=idIn)
   time.sleep(0.01)
  return eval(str(readClass.sol))



   
  
