# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:43:14 2022

@author: bhava
"""
import math

def cosine(x,y):
    ytemp=0
    xtemp=0
    num=0
    for i,j in zip(x,y):
        num+=(i*j)
        xtemp+=i*i
        ytemp+=j*j
    print(num/math.sqrt((xtemp*ytemp)))
    
def jaccard(x,y):
    q=0
    r=0
    s=0
    for i,j in zip(x,y):
        if(i==1 and j==1):
            q+=1
        if(i==0 and j==1):
            s+=1
        if(i==1 and j==0):
            r+=1
    jaccard=0
    jaccard=q/(q+r+s)
    print(jaccard)
    
def euc(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    print(math.sqrt(temp))
    

x=list(map(int,input("Enter X value: ").split(" ")))
y=list(map(int,input("Enter Y value: ").split(" ")))

cosine(x,y)
jaccard(x,y)
euc(x,y)

