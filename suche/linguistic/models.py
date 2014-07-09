'''
Models for linguistic classes
Contains model for the following features:

* two gram table for auto completion
* threee gram table for auto completion

Copyright (c) 2014 by anup pokhrel
'''

from django.db import models
from django.utils import timezone

class ngramModel(models.Model):
    '''
    ngrammodel is the base class for 2gram and 3gram models
    '''
    class Meta:
        abstract = True

class BiGram(ngramModel):
    word1 = models.CharField(max_length = 50)
    word2 = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0)
    perplexity = models.FloatField(default = 0)

class TriGram(ngramModel):
    word1 = models.CharField(max_length = 50)
    word2 = models.CharField(max_length = 50)
    word3 = models.CharField(max_length = 50)
    count = models.IntegerField(default = 1)
    perplexity = models.FloatField(default = 0)

class CompletionCache(models.Model):
    '''
    CompletionCahe is a table used for compltion of quickly popular
    queries. For example, if some celebreties got married and the
    query for "x marries y" got very high, then it gets stored
    in this table. Any time user searches for the query, count gets increased
    and last_used gets updated. This data will be used for quick completion.
    If the query is not used for about 1 day, it is removed from this
    table.
    '''
    query = models.CharField(max_length = 200)
    count = models.IntegerField(default = 0)
    last_used = models.DateTimeField(auto_now = True, auto_now_add = True)

    def flush_cache():
        '''
        this function will remove queries that are last used before 24 hours.
        '''
        pass
