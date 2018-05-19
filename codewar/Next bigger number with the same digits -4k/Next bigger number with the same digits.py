#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

'''
import sys
sys.path.append('../')
import cw as Test
import time
from math import log10

debug = 1

'''
冒泡
'''
def list_to_num(list_t=[]):
    out=0
    for t in list_t:
        out = out *10 +t
    return out

def next_bigger_t(num_list=[]):
    n =list_to_num(num_list)
    num_list_out=[]
    num_list_temp=[]
    len_t = len(num_list)
    for i in range(len_t-1,0,-1):
        for j in range(i-1,-1,-1):
            if num_list[i] > num_list[j]:
                num_list_out=num_list[:j]
                num_list_out.append(num_list[i])
                num_list.pop(i)
                num_list_temp=num_list[j:]
                num_list_temp.sort()
                num_list_out=num_list_out+num_list_temp
                out =list_to_num(num_list_out)
                if out <= n :
                    return -1
                else :
                    return out
    return -1



def next_bigger(n):
    #your code here
    num_list = list(map(int,str(n)))
    n 
    i=2
    len_t =int(log10(n))+2
    for i in range(2,len_t) :
        num_temp = num_list[len_t-1-i:]
        temp=next_bigger_t(num_temp)
        if  temp!= -1:
            return n //10**i * 10**i +temp
        else :
            pass
    return -1



if __name__ == "__main__":

    t0 = time.perf_counter()
    Test.assert_equals(next_bigger(12),21)
    Test.assert_equals(next_bigger(513),531)
    Test.assert_equals(next_bigger(2017),2071)
    Test.assert_equals(next_bigger(414),441)
    Test.assert_equals(next_bigger(144),414)
    Test.assert_equals(next_bigger(54864190394230),54864190394302)
    Test.assert_equals(next_bigger(6119200482),6119200824)
    Test.assert_equals(next_bigger(996540),-1)
    Test.assert_equals(next_bigger(9545044),9545404)
    Test.assert_equals(next_bigger(6877),7678)
    Test.assert_equals(next_bigger(560086),560608)
    print(time.perf_counter() - t0)


'''
import itertools
def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1
'''
