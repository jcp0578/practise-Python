#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

'''
import sys
sys.path.append('../')
import cw as Test
import time

from math import sqrt

debug = 1


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def is_triangle(a, b, c):
    t = [a, b, c]
    max_t = max(t)
    if min(t) <= 0:
        return False
    else:
        if (max_t < (sum(t) - max_t)):
            return True
        else:
            return False


if __name__ == "__main__":

    t0 = time.perf_counter()

    print(time.perf_counter() - t0)
'''
o(nlogn)
I think I'm best，hhhh!
'''
