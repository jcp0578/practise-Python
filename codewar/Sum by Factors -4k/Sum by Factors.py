#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
sys.path.append('../')
import cw as test
import time

import math   
  
def prime(n):  
    out_list = []
    if n <= 1:  
        return out_list  
    else:
        out_list.append(2)
    for j in range(3,n+1):
        for i in range(2,math.ceil(math.sqrt(j)+1)):  
        #for i in range(2,j):  
            if j%i == 0:
                break
        else :  
            out_list.append(j)  
    return out_list  
        


def sum_for_list(lst):
    out_temp=[]
    lst_len=len(lst)
    t =prime(max(list(map(abs, lst))))
    for j in t:
        sum_temp =0
        flag=0
        for i in range (lst_len):            
            if lst[i]%j==0 :
                sum_temp+=lst[i]
                flag=1
            else:
                pass
        else :
            if flag :
                out_temp.append([j,sum_temp])
            else:
                pass
    return out_temp



if __name__ == "__main__":

    t0 = time.perf_counter()

    a = [12, 15]
    test.assert_equals(sum_for_list(a), [[2, 12], [3, 27], [5, 15]])


    print(time.perf_counter() - t0)




'''
def last_digit(lst):
    if not lst:
        return 1
    else:
        out = 1
        for n in lst[len(lst):0:-1]:
            out = n**out
            if out > 2:
                out -= 2
                out %= 4
                out += 2
    return lst[0]**out% 10


from functools import reduce
        
def last_digit(lst):
    return reduce(lambda p, n: 1 if p == 0 or n == 1 else n if p == 1 or n == 0 else pow(n, p, 40) + 40, lst[::-1], 1) % 10


'''
