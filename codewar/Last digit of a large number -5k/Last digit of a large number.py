#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''

'''

import sys
sys.path.append('../')
import cw as Test
import time

refer ={0:[0],1:[1],2:[2,4,8,6],3:[3,9,7,1],4:[4,6],
        5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}



def last_digit(n1, n2):
    out_temp=n1%10
    if n2==0:
        out_temp=1
    else :
        refer_temp=refer[out_temp]
        out_temp=refer_temp[(n2%len(refer_temp))-1]
    return out_temp


if __name__ == "__main__":

    t0 = time.perf_counter()

    Test.it("Example tests")
    Test.assert_equals(last_digit(4, 1), 4)
    Test.assert_equals(last_digit(4, 2), 6)
    Test.assert_equals(last_digit(9, 7), 9)
    Test.assert_equals(last_digit(10, 10 ** 10), 0)
    Test.assert_equals(last_digit(2 ** 200, 2 ** 300), 6)
    Test.assert_equals(last_digit(3715290469715693021198967285016729344580685479654510946723, 68819615221552997273737174557165657483427362207517952651), 7)

    Test.it("x ** 0")
    for nmbr in range(1, 9):
        a = nmbr ** nmbr
        Test.it("Testing %d and %d" % (a, 0))
        Test.assert_equals(last_digit(a, 0), 1, "x ** 0 must return 1")



    print(time.perf_counter() - t0)




'''
rules = {
    0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1],
}
def last_digit(n1, n2):
    ruler = rules[int(str(n1)[-1])]
    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]

'''
