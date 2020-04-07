# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:16:40 2020

@author: Ujwal
"""

n,k = map(int,input().split())
listy = list(map(int,input().split()))
s = sum(listy[:k])
maximum = s
for i in range(1,k):
    s = s - listy[k-i] + listy[-i]
    if(s>maximum):
        maximum = s
print(maximum)

