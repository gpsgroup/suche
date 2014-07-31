from scripts.spellClass import *
import time
import os

def run():
 spCrct=SpellChecker(os.path.join(os.path.dirname(os.path.realpath(__file__)),'big.txt'))
 
 while 1: 
  iptexts=spCrct.spReadWord()
  if(iptexts):
   for iptext in iptexts:
    varr=spCrct.correct(iptext.req)
    iptext.sol=varr
    iptext.save()

