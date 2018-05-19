#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
sys.path.append('../')
import cw as test
import time


def rotate(matrix):  
    """ 
    :contrarotate matrix. 
    """  
    return list(map(list,zip(*matrix[::])))[::-1]

def snail(array):
    out_temp= []
    while array:
        out_temp.extend(array[0][:])
        array= rotate(array[1:])
    return out_temp


if __name__ == "__main__":

    t0 = time.perf_counter()

    array = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    expected = [1,2,3,6,9,8,7,4,5]
    test.assert_equals(snail(array), expected)


    array = [[1,2,3],
            [8,9,4],
            [7,6,5]]
    expected = [1,2,3,4,5,6,7,8,9]
    test.assert_equals(snail(array), expected)


    print(time.perf_counter() - t0)




'''
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

'''
