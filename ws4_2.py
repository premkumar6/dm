# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 21:43:16 2022

@author: bhava
"""

x=list(map(int,input("Enter X value: ").split(" ")))
y=list(map(int,input("Enter Y value: ").split(" ")))

q=0
r=0
s=0
hamming=0

for i,j in zip(x,y):
    if(i==1 and j==1):
        q+=1
    if(i==1 and j==0):
        r+=1
        hamming+=1
    if(i==0 and j==1):
        s+=1
        hamming+=1

jaccard=0
jaccard=q/(q+r+s)

print(jaccard)
print(hamming)
        
