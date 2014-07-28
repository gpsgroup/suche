'''
    Module for computing Page Rank
    
    Usage:
    
    prData=PageRankData(index.size())
    prData.fillData()
    pr=PageRank(prData)
    computedPageRankVector=pr.computePageRank()
    
    
'''
import numpy

class PageRankData:
    #class to store everything related to PageRank into memory
    def __init__(self,n):
        '''init everything'''
        self.size=n
        self.in_links={}
        self.num_out_links={}
        self.stuck_pages={}
        
        for i in xrange(n):
            self.num_out_links[j]=0
            self.in_links[j]=[]
            self.stuck_pages[j]=True
    
    def fillData(self):
    #still to write after indexer is completed    
        '''create matrix representing links
        return True if successful
        '''
        return True
    
    
class PageRank:
    #class to compute pageRank
    
    def __init__(self,prData,s=0.85,tolerance=0.00001):
        self.g=prData
        self.s=s
        self.n=prData.size
        self.tolerance=tolerance
    
    
    def calcSingleValue(self,p):
        leaveVal=1/self.n
        stuckVecSum= sum([p[j] for j in self.g.stuck_pages.keys()])/self.n
        v = numpy.matrix(numpy.zeros((self.n,1))) #vector containing zeros
        for j in xrange(n):
            v[j]=self.s*sum([p[k]/self.g.num_out_links[k] for k in self.g.in_links[j]])+self.s*stuckVecS+(1-self.s)*leaveVal
            
        
        return v/numpy.sum(v) #as prob less than 1 the eigen way
    
    def computePageRank(self):
        '''provides the PageRank Vector '''
        i=1
        change=999
        p=numpy.matrix(numpy.ones((self.n,1)))/self.n #vector for calculating distribution
        while change>self.tolerance:
            p_prime=self.calcSingleValue(p)
            change=numpy.sum(numpy.abs(p-p_prime))
            p=p_prime
            i+=1
        return p
    
        
    
    
    
        
    
        