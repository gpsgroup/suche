from django.db import models


class Wordmeaning(models.Model):
    word = models.CharField(max_length=200,primary_key=True)
    meaning = models.TextField()

    def __str__(self):
        return self.word
