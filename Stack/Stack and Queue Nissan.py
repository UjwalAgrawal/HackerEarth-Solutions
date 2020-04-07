# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:16:40 2020

@author: Ujwal
"""

n,k = map(int,input().split())
listy = list(map(int,input().split()))
maximum = -1
for i in range(k):
    s = sum(listy[:k-i])+sum(listy[:n-i-1:-1])
    if(s>maximum):
        maximum = s
print(maximum)

