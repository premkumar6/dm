# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:01:58 2022

@author: bhava
"""
import math

def man(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=abs(i-j)
    print(temp)

def cos(x,y):
    num=0
    xval=0
    yval=0
    for i,j in zip(x,y):
        num+=(i*j)
        xval+=i*i
        yval+=j*j
    print(num/(math.sqrt(xval*yval)))

def ecu(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    print(math.sqrt(temp))
    
def supremum(x,y):
    m=[]
    temp=0
    for i,j in zip(x,y):
        temp=abs(i-j)
        m.append(temp)
    print(max(m))
    
x=[1.5,2,1.6,1.2,1.5]
y=[1.7,1.9,1.8,1.5,1.0]

for i,j in zip(x,y):    
    x1=[i,j]
    y1=[1.4,1.6]
    man(x1,y1)
    cos(x1,y1)
    ecu(x1,y1)
    supremum(x1, y1)
    print("#################################3")