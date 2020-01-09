#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 04:41:15 2019

@author: vpapg
"""
from math import sqrt, pi, exp

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def factorialStirling(n):
    return sqrt(2*pi*n) * exp(-n) * n**n

def permutations(n,r=1.234):
    # order does matter (ordered combination)
    # each item can be used only once
    if r==1.234: # repetition=False
        r=n
    return factorial(n)/factorial(n-r)

def combinations(n,r, repetition=False):
    # order does not matter
    if ~repetition: # no repetition
        return factorial(n) / (factorial(n-r) * factorial(r))
    # repetition
    return factorial(r+n-1) / (factorial(n-1) * factorial(r)) 



class Distribution:
    
    
    def binomialCoefficient(self,n,k):
        # or nCk or n_choose_k
        return factorial(n) / (factorial(k) * factorial(n-k))
    
    
    def bernoulli(self,x,p):
        # x = 0 or x = 1
        # if x==0: return q
        # if x==1: return p
        q = 1 - p
        return p**x * q**(1-x)
    
    def bernoulliMean(self,p):
        return p
    
    def BernoulliSTD(self,p):
        q = 1 - p
        return p*q
    
    
    def binomial(self,x,v,p):
        q = 1 - p
        return self.binomialCoefficient(v,x) * p**x * q**(v-x)
    
    def binomialMean(self,v,p):
        return v*p
    
    def binomialSTD(self,v,p):
        q = 1 - p
        return v*p*q
    
    
    def geometric(self,x,p):
        q = 1 - p
        return (q**(x-1)) * p
    
    def geometricMean(self,p):
        return 1/p
    
    def geometricSTD(self,p):
        q = 1 - p
        return (2*q)/(p**2)
    
    
    def negativeBinomial(self,x,r,p):
        q = 1 - p
        return self.binomialCoefficient(x-1,r-1) * p**r *  q**(x-r)
    
    def negativeBinomialMean(self,r,p):
        return r/p
    
    def negativeBinomialSTD(self,r,p):
        q = 1 - p
        return (r*q)/(p**2)
    
    
    def discreteUniform(self,x,k):
        return 1/k
    
    def discreteUniformMean(self,k):
        return (k+1)/2
    
    def discreteUniformSTD(self,k):
        return (k**2 - 1)/12
    
    #def hypergeometric(self,x,v,a,b)
    #def hypergeometricMean(self,v,a,b)
    #def hypergeometricSTD(self,v,a,b)
    
    def poisson(self,x,lamda):
        return exp(-lamda) * ((lamda**x)/factorial(x))
    
    def poissonMean(self,lamda):
        return lamda
    
    def poissonSTD(self,lamda):
        return lamda