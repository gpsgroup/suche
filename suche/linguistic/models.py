'''
Models for linguistic classes
Contains model for the following features:

* two gram table for auto completion
* threee gram table for auto completion

Copyright (c) 2014 Suche
'''

from django.db import models
from django.utils import timezone
from django.db.models import Sum

class ngramModel(models.Model):
    '''
    ngrammodel is the base class for 2gram and 3gram models
    '''
    class Meta:
        abstract= True

class Grammar(models.Model):
    '''
      table to store grammar and corresponding action
    '''
    grammar=models.CharField(max_length=1024)
    action=models.CharField(max_length=1024)

class Word(models.Model):
    '''
    this word table is used for spell correction and other purpose
    It is initially populated with dictionary words
    new words in user query are added to this table with time
    '''
    word = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0)
    probability = models.FloatField(default = 0)

    def update():
        '''
        This function recalculates the probability of all words
        '''
        totalwords = Word.objects.aggregate(Sum('count'))['count__sum']
        for word in Word.objects.all():
            word.probability = word.count / totalwords
            word.save()

    def __str__(self):
        return self.word

class BiGram(ngramModel):
    '''
    Birgram language model
    created using user queries
    As we do stupid backoff, probability is not actually
    the probability but like a ranking factor
    '''
    word1 = models.CharField(max_length = 50)
    word2 = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0)
    probability = models.FloatField(default = 0)

    def __str__(self):
        return self.word1+" | "+self.word2

    def update():
        '''
        Updates the bigram model.
        This will calculate the probability of word for bigram model
        '''
        for bigram in BiGram.objects.all():
            onesum = BiGram.objects.filter(word1 = bigram.word1).aggregate(Sum('count'))['count__sum']
            bigram.probability = bigram.count / onesum
            bigram.save()


class TriGram(ngramModel):
    word1 = models.CharField(max_length = 50)
    word2 = models.CharField(max_length = 50)
    word3 = models.CharField(max_length = 50)
    count = models.IntegerField(default = 0)
    probability = models.FloatField(default = 0)
    def __str__(self):
        return self.word1+" | "+self.word2+" | "+self.word3

    def update():
        '''
        Updates the trigram model
        '''
        for trigram in TriGram.objects.all():
            twosum = TriGram.objects.filter(word1 = trigram.word1, word2 = trigram.word2).aggregate(Sum('count'))['count__sum']
            trigram.probability = trigram.count / twosum
            trigram.save()


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
    def __str__(self):
        return self.query

class SpellCache(models.Model):
    '''
    SpellCache is the cache used by the interface to interact with the DB
    '''
    req=models.CharField(max_length=256)
    sol=models.CharField(max_length=512)
