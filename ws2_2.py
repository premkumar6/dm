# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 23:20:16 2022

@author: bhava
"""

import math

def man(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=abs(i-j)
    return (temp)

def cos(x,y):
    num=0
    xval=0
    yval=0
    for i,j in zip(x,y):
        num+=(i*j)
        xval+=i*i
        yval+=j*j
    return (num/(math.sqrt(xval*yval)))

def ecu(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(i-j)*(i-j)
    return (math.sqrt(temp))

def h_3(x,y):
    temp=0
    for i,j in zip(x,y):
        temp+=(abs(i-j))**3
    return ((temp)**(1/3))
    
def supremum(x,y):
    m=[]
    temp=0
    for i,j in zip(x,y):
        temp=abs(i-j)
        m.append(temp)
    return (max(m))
    

d=[[5,0,3,0,2,0,0,2,0,0],[3,0,2,0,1,1,0,1,0,1],[0,7,0,2,1,0,0,3,0,0],[0,1,0,0,1,2,2,0,3,0]]


s=[]
d1=[]
d2=[]
d3=[]
d4=[]


for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(man(d[i],d[j]))
    d1.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(ecu(d[i],d[j]))
    d2.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(supremum(d[i],d[j]))
    d3.append(temp)
    
for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(h_3(d[i],d[j]))
    d4.append(temp)

for i in range(0,4):
    temp=[]
    for j in range(0,4):
        temp.append(cos(d[i],d[j]))
    s.append(temp)

print(d1)
print(d2)
print(d3)
print(d4)
print(s)
        