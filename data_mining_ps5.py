# -*- coding: utf-8 -*-
"""Data mining PS5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Gu6PmFcgVMvjQoCs8xd0h2IeCe1Yr98Z
"""

data = {"Chicago": {"Q1":[854, 882, 89, 623], "Q2":[943, 890, 64, 698], "Q3":[1032, 924, 59, 789], "Q4":[1129, 992, 63, 870]}, "New York": {"Q1":[1087, 968, 38, 872], "Q2":[1130, 1024, 41, 925], "Q3":[1034, 1048, 45, 1002], "Q4":[1142, 1091, 54, 984]}, "Toronto": {"Q1":[818, 746, 43, 591], "Q2":[894, 769, 52, 682], "Q3":[940, 795, 58, 728], "Q4":[978, 864, 59, 784]}, "Vancouver": {"Q1":[605, 825, 14, 400], "Q2":[680, 952, 31, 512], "Q3":[812, 1023, 30, 501], "Q4":[927, 1038, 38, 580]}}
data

#Vancouver - Canada
#Chicago - USA
#New York - USA
#Toronto - Canada

ans1 = {}

def add(x1, x2):
  ans = [0] * len(x1)
  for i in range(len(x1)):
    ans[i] += (x1[i] + x2[i])
  return ans

def roll_up(t, x, y):
  Q1 = Q2 = Q3 = Q4 = [0]*len(data["Vancouver"]["Q1"])
  
  for i in y:
    Q1 = add(Q1, data[i]["Q1"])
    Q2 = add(Q2, data[i]["Q2"])
    Q3 = add(Q3, data[i]["Q3"])
    Q4 = add(Q4, data[i]["Q4"])

  t[x] = {"Q1":Q1, "Q2":Q2, "Q3":Q3, "Q4":Q4}

roll_up(ans1, "Canada", ["Vancouver", "Toronto"])
roll_up(ans1, "USA", ["Chicago", "New York"])

ans1

map_dict = {0:"Q1", 3:"Q2", 6:"Q3", 9:"Q4"}
ans2 = {}

def divide(a, b):
  ans = [0] * len(a)
  for i in range(len(a)):
    ans[i] = a[i] / b
  return ans

def drill_down(t, y):
  n = 3

  for i in y:
    months = [[]*len(data["Vancouver"]["Q1"]) for i in range(1,13)]
    for j in range(0, 12, n):
      for k in range(n):
        months[j+k] = divide(data[i][map_dict[j]], n)

    t[i] = months

drill_down(ans2, list(data.keys()))
ans2

from collections import defaultdict

ans3 = {}

def dice(t, dim1, dim2, dim3):
  for i in dim1:
    temp1 = {}
    for j in dim2:
      temp2 = []
      for k in dim3:
        temp2 += [data[i][j][k]]
      temp1[j] = temp2
    t[i] = temp1
    
dice(ans3, ["Toronto", "Vancouver"], ["Q1", "Q2"], [0,1])
ans3

ans4 = {}

def slice(t, y, m):
  for i in y:
    t[i] = data[i][m]

slice(ans4, ["Toronto", "Vancouver", "Chicago", "New York"], "Q1")
ans4