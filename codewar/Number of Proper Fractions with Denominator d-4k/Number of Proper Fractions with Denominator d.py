#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
sys.path.append('../')
import cw as Test
import time

from math import sqrt

#欧拉公式
'''

gcd（m，n）= 1，则φ（mn）= φ（m）φ（n）

ψ（10）=10×（1－1/2）×（1－1/5）=4；
ψ（30）=30×（1－1/2）×（1－1/3）×（1－1/5）=8；
ψ（49）=49×（1－1/7）=  =42。
'''
def is_prime(n):
    if n ==2:
        return True
    for i in range(2,int(sqrt(i)+1)):
        if n%i==0:
            return False
    else:
        return True
def proper_fractions(n):
    #your code here
    if n == 1:
        return 0

    last_i=2
    include_prime=[]
    temp=n
    while temp!=1:
        i=last_i
        while i < int(sqrt(temp)+1):
#若使用for 当n很大则导致range申请空间大
#在python2.7中
            if temp%i==0:
                if i not in include_prime:
                    include_prime.append(i)
                temp=temp/i
                last_i=i
                break
            i+=1
        else :
            if temp not in include_prime:
                include_prime.append(temp)
            temp=temp/temp
            last_i=temp

    out_temp=n
    for i in include_prime:
        out_temp=out_temp*(1-1.0/i)
    return int(out_temp)

        

        


if __name__ == "__main__":

    t0 = time.time()

    Test.assert_equals(proper_fractions(1),0)
    Test.assert_equals(proper_fractions(2),1)
    Test.assert_equals(proper_fractions(5),4)
    Test.assert_equals(proper_fractions(15),8)
    Test.assert_equals(proper_fractions(25),20)
    Test.assert_equals(proper_fractions(12345656798),82260072)

    print(time.time() - t0)




'''
def proper_fractions(n):
    phi = n > 1 and n
    for p in range(2, int(n ** .5) + 1):
        if not n % p:
            phi -= phi // p
            while not n % p:
                n //= p
    if n > 1: phi -= phi // n
    return phi


def euler(n):
    res = 1.0*n
    p = 2
    while p*p <= n:
        if n%p == 0:
            while n%p == 0:
                n = n/p
            res *= (1.0 - (1.0/p) )
        p += 1
    
    if n > 1:
        res *= (1.0 - (1.0/n) )
    
    return int(res)

def proper_fractions(d):
    if d == 1:
        return 0
    return euler(d)
    
'''
