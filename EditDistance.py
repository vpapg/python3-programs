#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:13:23 2018

@author: vpapg
"""

def EditDistance(word1, word2, sub_penalty=1):

    len1 = len(word1)
    len2 = len(word2)
    
    # Initialise D
    D = [[0]*(len2+1) for _ in range(len1+1)]
    D[0][1:] = range(1, len2+1)
    for i in range(len1+1):
        D[i][0] = i
    
    ptr = [['']*len2 for _ in range(len1)]
    
    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            sub = sub_penalty if word1[i-1] != word2[j-1] else 0
            min_operation = min(D[i-1][j-1]+sub, D[i-1][j]+1, D[i][j-1]+1)
            D[i][j] = min_operation
            
            if sub == 0 and min_operation == D[i-1][j-1]+sub:
                ptr[i-1][j-1] = '-'
            elif sub == sub_penalty and min_operation == D[i-1][j-1]+sub:
                ptr[i-1][j-1] = 'SUB'
            elif min_operation == D[i-1][j]+1:
                ptr[i-1][j-1] = 'INS'
            elif min_operation == D[i][j-1]+1:
                ptr[i-1][j-1] = 'DEL'
                
    print('The minimum edit distance between the two words is:',D[-1][-1],'\n')
    
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
      for row in D]),'\n')

    print('\n'.join([''.join(['{:5}'.format(item) for item in row]) 
      for row in ptr]))
