from scripts.spellClass import *
import time
def run():
 spCrct=SpellChecker('big.txt')
 
 while 1: 
  iptexts=spCrct.spReadWord()
  if(iptexts):
   for iptext in iptexts:
    varr=spCrct.correct(iptext.req)
    iptext.sol=varr
    iptext.save()

