#an interface function repo for sending and receiving words to and from the spell checker
#test.py contains demo usage
import os
class DInterface:
 rfPath = "./intfr"
 wfPath = "./intfw"
 def __init__(self):
  try:
   os.mkfifo(self.wfPath)
   os.mkfifo(self.rfPath)
  except OSError:
   pass
#used to send word to the spell corrector
 def writeWord(self,wordd):
  try:	
   wp = open(self.wfPath, 'w')
   wp.write(wordd)		
   wp.close()
   return True
  except OSError:
   pass
   return False
#used to receive word from the spell corrector receives 
 def readWord(self):
  try:
   rp = open(self.rfPath, 'r')
   response = rp.read()
   rp.close()
   response=eval(response)
   return response
  except OSError:
   pass
   return False

#used to send word from the spell corrector
 def spWriteWord(self,wordd):
  try:	
   wp = open(self.rfPath, 'w')
   wp.write(wordd)		
   wp.close()
   return True
  except OSError:
   pass
   return False
#used to receive word to the spell corrector
 def spReadWord(self):
  try:
   rp = open(self.wfPath, 'r')
   response = rp.read()
   rp.close()		
   return response
  except OSError:
   pass
   return False
