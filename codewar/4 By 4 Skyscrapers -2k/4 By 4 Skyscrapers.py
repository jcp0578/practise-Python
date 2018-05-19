#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
not worked
'''

import sys
sys.path.append('../')
import cw as test
import time


N=4

def rotate(matrix):  
    """ 
    :contrarotate matrix. 
    """  
    return list(map(list,zip(*matrix[::])))[::-1]

def visible_onerow(array):
    """ 
    :return visible number in one row. 
    """
    out_temp = 1
    len_t=len(array)
    for i in range(len_t - 1):
        for j in range(i+1,len_t):
            if array[i] < array[j]:
                break
            else:
                pass
        else :
            out_temp += 1        
    return out_temp


def visible_cover(array):
    out_temp = []
    for i in range(len(array)):
        out_temp.append(visible_onerow(array[i]))
    return out_temp

def visible_allcover(array):
    out_temp = []
    temp =array
    for i in range(N):
        out_temp.extend(visible_cover(temp))
        temp=rotate(temp)
    out_temp = out_temp[-N:] + out_temp[:-N]    
    return out_temp


def clues_compare(list1,original):
    for i in range(len(list1)):
        if original[i]:
            if original[i] == list1[i] :
                pass
            else :
                return False
        else :
            continue
    else:
        return True



def solve_puzzle(clues):
    temp =[0,0,0,0]*4
    for i in range(N):
        for j in range(N):
            for x in range(1,N+1):


    


    return visible_allcover(clues)
    #return ( (1, 2, 3, 4), (2, 3, 4, 1), (3, 4, 1, 2), (4, 1, 2, 3) )


if __name__ == "__main__":

    t0 = time.perf_counter()

    clues = ((2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3),
             (0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0))

    outcomes = (((1, 3, 4, 2), (4, 2, 1, 3), (3, 4, 2, 1), (2, 1, 3, 4)),
                ((2, 1, 4, 3), (3, 4, 1, 2), (4, 2, 3, 1), (1, 3, 2, 4)))

    test.describe("4 by 4 skyscrapers")
    test.it("should pass all the tests provided")
    print(clues_compare(solve_puzzle(outcomes[0]),clues[0]))
    # test.assert_equals(solve_puzzle(clues[0]), outcomes[0])
    # test.assert_equals(solve_puzzle(clues[1]), outcomes[1])

    print(time.perf_counter() - t0)
'''
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []

'''
