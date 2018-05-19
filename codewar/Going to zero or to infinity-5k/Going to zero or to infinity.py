#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
sys.path.append('../')
import cw as test
from math import factorial,log,ceil
import decimal

debug = 1


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def going(n):
    # your code
    start_t = 1
    decimal.getcontext().prec = 7
    decimal.getcontext().rounding = decimal.ROUND_DOWN
    
    first_num = factorial(n)
    log_t =ceil(log(1000000,max(2,n)))
    if log_t < n:
        start_t = n-log_t;
    debug_print(1,start_t)
    second_num = sum(factorial(x) for x in range(start_t, n + 1))
    return float(decimal.Decimal(second_num) / decimal.Decimal(first_num))


if __name__ == "__main__":
    print(factorial(100))
    test.assert_equals(going(5), 1.275)
    test.assert_equals(going(40), 1.2125)
    test.assert_equals(going(100), 1.173214)
    test.assert_equals(going(101), 1.005434)
    test.assert_equals(going(501), 1.005025)
    test.assert_equals(going(1000), 1.007246)

    print(going(40000))
'''
def going(n):  
    s = 1.0
    for i in range(2, n + 1):
        s = s/i + 1
    return int(s * 1e6) / 1e6
'''
