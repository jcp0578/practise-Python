#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200000000000000) return sum of all '1' occurencies in binary representations of numbers between 'left' and 'right' (including both)

'''
import sys
sys.path.append('../')
import cw as test
import time
from math import log2, pow, ceil

debug = 1
'''
def countOnes_once(x):
    countx = 0
    while x:
        countx += 1
        x = x & (x - 1)
    return countx


def countOnes(left, right):
    out_temp = 0
    if left > right:
        return 0
    elif left == right:
        return countOnes_once(left)
    else:
        pass
    left_log2 = int(log2(max(left - 1, 1 / 2))) + 1
    right_log2 = int(log2(right+1))

    # if left_log2 > right_log2:
    #     out_temp += right - left + 1
    #     out_temp += countOnes(left & int(pow(2, left_log2 - 1) - 1),
    #                           right & int(pow(2, left_log2 - 1) - 1))
    # elif left_log2 == right_log2:
    #     if right == (pow(2, right_log2) - 1):
    #         out_temp += right - left + 1
    #         out_temp += countOnes(left & pow(2, left_log2 - 1) - 1,
    #                               right & pow(2, left_log2 - 1) - 1)
    #     else:
    #         out_temp += countOnes(left, pow(2, left_log2) - 1)
    #         out_temp += countOnes(pow(2, right_log2), right)
    # else:
    for i in range(left_log2, right_log2):
        out_temp += pow(2, i - 1) * (2 + i)
    for i in range (left,int(pow(2, left_log2))):
        out_temp +=countOnes_once(i)
    for i in range (int(pow(2,right_log2)),right+1):
        out_temp +=countOnes_once(i)
    # out_temp += countOnes(left, pow(2, left_log2) - 1)
    # out_temp += countOnes(pow(2, right_log2), right)
    return out_temp
'''


def countOnes_once(x):
    countx = 0
    while x:
        countx += 1
        x = x & (x - 1)
    return countx


def countOnes(left, right):
    out_temp = 0
    if left > right:
        return 0
    elif left == right:
        return countOnes_once(left)
    else:
        pass

    left_log2 = int(log2(max(left - 1, 1 / 2))) + 1
    right_log2 = int(log2(right + 1))

    for i in range(left_log2, right_log2):
        out_temp += int(pow(2, i - 1) * (2 + i))

    if right < int(pow(2, left_log2)):
        out_temp += right - left + 1
        left_t = left & int(pow(2, left_log2 - 1) - 1)
        right_t = right & int(pow(2, left_log2 - 1) - 1)
        out_temp += countOnes(left_t, right_t)
    else:
        left_rest = int(pow(2, left_log2)) - left
        if left_rest:
            out_temp += left_rest
            left_t = left & (int(pow(2, left_log2 - 1) - 1))
            right_t = int(pow(2, left_log2 - 1)) - 1
            out_temp += countOnes(left_t, right_t)
        else:
            pass
        right_rest = right - int(pow(2, right_log2)) + 1
        if right_rest:
            out_temp += right_rest
            left_t =  1
            right_t = right & (int(pow(2, right_log2)) - 1)
            out_temp += countOnes(left_t, right_t)
        else:
            pass
    return out_temp


if __name__ == "__main__":

    t0 = time.perf_counter()

    test.describe("Sample Tests")
    test.it('Easy')
    test.assert_equals(countOnes(5, 7), 7)
    test.assert_equals(countOnes(4, 7), 8)
    test.assert_equals(countOnes(12, 29), 51)
    test.assert_equals(countOnes(12, 2900000000000000), 51)   #test time

    print(time.perf_counter() - t0)



'''
import math

def count(n):
    if n is 0: return 0
    x = int(math.log(n, 2))
    return x * 2 ** (x - 1) + n - 2 ** x + 1 + count(n - 2 ** x)

def countOnes(left, right):
    return count(right) - count(left - 1)


def countOnes(left, right):
    def f(n):
        c = 0
        a = list(reversed(list(bin(n))))
        for i, d in enumerate(a):
            if d == '1':
                c += 1 + 2**i*i/2 + 2**i*a[i+1:].count('1')
        return c
    return f(right) - f(left-1)    
'''
