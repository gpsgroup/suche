from linguistic.models import *
import re
import math
class NLGrammar:
    def __init__(self,request):
        self.query=request
        self.queryWordList=self.query.split()
        self.queryWordList=[x for x in self.queryWordList if x]

    def isOptional(self,query):
        if query[:1]=='?' or query[:1]=='$':
            return True
        return False

    def isQuery(self,query):
        if query[:1]=='$':
            return True
        return False

    def compareGetId(self):
        '''
        <search|find><?for><$query>
        gram.grammar
        '''
        ranks=dict()
        allGrammar=Grammar.objects.all()
        for gram in allGrammar:
            grammarTokens=re.split('<(?P<token>.*?)>',gram.grammar)
            '''
            ignore all empty entries
            '''

            grammarTokens=[x for x in grammarTokens if x]

            validTokenNum=len([x for x in grammarTokens if not self.isOptional(x)])
            #compare words
            j=0
            query=[]
            ranks[str(gram.id)]=0
            for i in range(len(self.queryWordList)):

               #print (str(self.queryWordList[i]))
               if self.isOptional(grammarTokens[j]):
                    stri=grammarTokens[j][1:]
               else:
                    stri=grammarTokens[j]
               if self.queryWordList[i] in stri.split('|'):
                    if(not self.isOptional(grammarTokens[j])):
                        ranks[str(gram.id)]+=1/validTokenNum

                    #increase the value of j
                    j+=1;
               else:
                    while self.isOptional(grammarTokens[j]):
                        if self.isQuery(grammarTokens[j]):
                            if math.floor(ranks[str(gram.id)])==1:
                                for p in self.queryWordList[i:]:
                                    query.append(p)
                                #query.append(self.queryWordList[i:])
                                return [gram.id,query]
                            else:
                                query.append(self.queryWordList[i])
                        #if invalid just break    
                        if j>=len(grammarTokens[j]):
                            break
                        j+=1
        return[-1,[]]
class NLProcess:
    def __init__(self):
        return True
