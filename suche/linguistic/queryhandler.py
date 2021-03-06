'''
query handler for suche search engine
'''

from linguistic.models import BiGram, TriGram, CompletionCache,SpellCache,Word
from linguistic.interfacee import *
from linguistic.NLProcess import *

class QueryHandler:
    '''
    QueryHandler class handles all the query related stuff in the
    search engine. It uses the bigram and trigram models, and manages them
    '''

    def flush_cache():
        '''
        flushes the query cache. Just calls the flush cache function of
        completion cache
        '''
        CompletionCache.flush_cache()

    def correct_query(query):
        '''
        correct query will take the user query as parameter
        and corrects the spelling of each word int the query
        '''
        words = query.lower().split(" ")
        newwords = []
        interf = DInterface()
        for word in words:
            idd=interf.writeWord(word)
            #newwords.append(str(idd))
            resp = interf.readWord(int(idd))
            key,value=resp.popitem()
            newwords.append(key)
        return ' '.join(newwords)

    def parse_query(query):
        '''parses the query to the specified grammar '''
        nlg=NLGrammar(str(query))
        return (nlg.compareGetId())

    def register_query(uquery):
        '''
        Register a query. The query is any query string that the user
        entered in the website. We will use this data to create the
        language models
        '''
        completion, created = CompletionCache.objects.get_or_create(query = uquery)
        completion.count += 1
        completion.save()

        # create bigram and trigram models from the query
        words = ['#']+uquery.split(' ')+['#'] # we use # to represent start and end of queries
        bigramwords = []
        trigramwords = []
        for word in words:

            wordobj,created = Word.objects.get_or_create(word = word)
            wordobj.count += 1
            wordobj.save()

            bigramwords.append(word)
            trigramwords.append(word)
            if(len(bigramwords) > 2):
                bigramwords = bigramwords[1:]
            if(len(trigramwords) > 3):
                trigramwords = trigramwords[1:]
            #register the words
            if len(bigramwords) >= 2:
                bigram,created = BiGram.objects.get_or_create(word1 = bigramwords[0], word2 = bigramwords[1])
                bigram.count += 1
                bigram.save()
            if len(trigramwords) >= 3:
                trigram,created = TriGram.objects.get_or_create(word1 = trigramwords[0], word2 = trigramwords[1], word3 = trigramwords[2])
                trigram.count += 1
                trigram.save()

    def get_completions(query):
        '''
        Get the auto completions for the query
        '''
        completions = set()
        # search for the query in cache
        caches = CompletionCache.objects.filter(query__startswith = query)
        for cache in caches:
            if len(completions) < 3:
                completions.add(cache.query)
        if len(completions) < 5: #if less than 5 result from the cache
            words = query.split(' ')
            if len(words) >= 2:
                prevwords = words[:-1]
                lastword = words[-1]

                lastwordcompletions = BiGram.objects.filter(word1 = prevwords[-1],word2__startswith = lastword).order_by("count")
                wordalternatives = set()
                for plastword in lastwordcompletions:
                    wordalternatives.add(plastword.word2)
                if len(wordalternatives) > 0:
                    for wordalternative in wordalternatives:
                        completions.add(' '.join(prevwords)+" "+wordalternative+'.')b
                        if len(completions) > 5:
                            break
                #completions.append(' '.join(prevwords))
                #completions.append(lastword)
        return list(completions)

        return completions
    def process_data():
        '''
        process_data will process the 2gram and 3gram data
        to yield perplexity for the words
        '''
        for unigram in Word.objects.all():
            unigram.update()
        for bigram in BiGram.objects.all():
            bigram.update()
        for trigram in TriGram.objects.all():
            trigram.update()
        pass
