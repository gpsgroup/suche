from scripts.spellClass import *
from linguistic.models import *
import time
import os

def run():
 spCrct=SpellChecker(os.path.join(os.path.dirname(os.path.realpath(__file__)),'big.txt'))
 print("Running")
 for key,value in spCrct.NWORDS.items():    
    wordd=Word(word=key,count=value)
    wordd.save()
    
    

