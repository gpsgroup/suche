from scripts.SeedClass import *
from linguistic.models import *
import time
import os

def run():
 spCrct=SeedClass(os.path.join(os.path.dirname(os.path.realpath(__file__)),'big.txt'))
 print("Please Wait.. Seeding All the words to dictionary")
 for key,value in spCrct.NWORDS.items():    
    wordd=Word(word=key,count=value)
    wordd.save()
    
    

