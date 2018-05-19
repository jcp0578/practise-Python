#!/usr/bin/python3
# -*- coding: utf-8 -*-

tl1=[1,2,'a','b']
tl2=[1,'a','b',0,15]

l=tl1
out=[]
for temp in l:
    if isinstance(temp,int):
        out.append(temp)
print(out)


#best
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]