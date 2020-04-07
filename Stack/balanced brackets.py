# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 13:44:03 2020

@author: Ujwal
"""
def complement(s,l):
    d = [('(',')'),('[',']'),('{','}')]
    if((s,l)) in d:
        return True
    return False

n = int(input())
for _ in range(n):
    listy = list(input())
    myStack = []
    check = ['(','[','{']
    close = [')',']','}']
    for i in listy:
        if i in check:
            myStack.append(i)
        elif(i in close):
            if(len(myStack)>0 and complement(myStack[-1],i)):
                myStack.pop()
        else:
            break
    if(len(myStack)==0):
        print("YES")
    else:
        print("NO")
