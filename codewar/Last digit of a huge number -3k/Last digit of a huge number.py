#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
求出上一级结果对4取模的结果
'''


import sys
sys.path.append('../')
import cw as test
import time

refer ={0:[0,0,0,0],
        1:[1,1,1,1],
        2:[6,2,4,8],
        3:[1,3,9,7],
        4:[6,4,6,4],
        5:[5,5,5,5],
        6:[6,6,6,6],
        7:[1,7,9,3],
        8:[6,8,4,2],
        9:[1,9,1,9]}

remainder ={0:[0,0],
            1:[1,1],
            2:[2,0],
            3:[1,3]}           



def last_digit(lst):
    # Your Code Here
    if lst ==[]:
        return 1
    else :
        pass
    len_t =len(lst)
    num_temp = min(lst[-1],3)
    refer_temp =lst[-1] %10
    remainder_temp =lst[-1] % 4

    for i in range(len_t-2,-1,-1):
        if num_temp==0:
            num_temp=1
            refer_temp=1
            remainder_temp=1
        else :
            num_temp_t=min(int(min(lst[i],3)**num_temp),3)
            refer_temp_t=refer[lst[i]%10][remainder_temp]
            temp =lst[i]%4
            if temp ==3:
                remainder_temp_t=remainder[temp][refer_temp%2]
            else:
                remainder_temp_t=remainder[temp][min(num_temp-1,1)]
            num_temp=num_temp_t
            refer_temp=refer_temp_t
            remainder_temp=remainder_temp_t
    return refer_temp


if __name__ == "__main__":

    t0 = time.perf_counter()

    test.it('Basic tests')
    test_data = [
        ([], 1),
        ([0, 0], 1),
        ([0, 0, 0], 0),
        ([1, 2], 1),
        ([3, 4, 5], 1),
        ([4, 3, 6], 4),
        ([7, 6, 21], 1),
        ([12, 30, 21], 6),
        ([2, 2, 2, 0], 4),
        ([937640, 767456, 981242], 0),
        ([123232, 694022, 140249], 6),
        ([499942, 898102, 846073], 6)
    ]
    for test_input, test_output in test_data:
        test.assert_equals(last_digit(test_input), test_output)


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
