from pluginServer.models import Wordmeaning
from collections import defaultdict
import os

def run():
    dictionary = defaultdict(lambda : '')
    newword = ''
    newmeaning = ''
    i = 0
    print("loading dictionary file ",os.path.join(os.path.dirname(os.path.realpath(__file__)),'dictionary.txt'))
    for line in open(os.path.join(os.path.dirname(os.path.realpath(__file__)),'dictionary.txt')).read().split("\n"):
        if line.upper() == line and len(line) > 0:
            if len(newword) > 0:
                dictionary[newword] += newmeaning
            newword = line
            newmeaning = ''
            i += 1
        else:
            newmeaning += line+'\n'
    print("Done reading",i)
    print("Uplaoding to database...please wait")
    Wordmeaning.objects.all().delete() # start by clearing the table
    
    for word in dictionary.keys():
        newword = Wordmeaning(word = word.lower(), meaning = dictionary[word])
        newword.save()
