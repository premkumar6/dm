# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 22:54:45 2022

@author: bhava
"""
def bin_d(x,y):
    p=7
    m=0
    for i,j in zip(x,y):
        if(i==j):
            m=m+1
    print ((p-m)/p)
jack=['m','y','n','p','n','n','n']
jim=['m','y','y','n','n','n','n']
marry=['f','y','n','p','n','p','n']


bin_d(jack,jim)
bin_d(jack, marry)
bin_d(jim,marry)