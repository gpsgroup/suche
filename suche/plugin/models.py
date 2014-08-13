from django.db import models
import random as rand


class Grammar(models.Model):
    '''
      table to store grammar and corresponding action
    '''
    grammar=models.CharField(max_length=1024)
    action=models.CharField(max_length=1024)


'''
   model for plugin class
   the names of the fields speak for themselves
'''


def randomGen():
    return rand.getrandbits(256)
class Plugin(models.Model):
    name=models.CharField(max_length=256)
    plugin_type=models.CharField(max_length=128)
    showsOp=models.BooleanField(default=False) # whether to show op in opBox in search result
    grammar=models.OneToOneField(Grammar)
    privateKey=models.CharField(max_length=512,default=randomGen)
    pluginKey=models.CharField(max_length=512, default=randomGen)
    updated=models.DateTimeField(auto_now_add=True)
    
    
    
    