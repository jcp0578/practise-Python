#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
good kata
'''

import sys
sys.path.append('../')
import cw as test
import time

from math import pow
# refer_str =""
# i=1
'''
Low efficiency

def find_position(string):
    refer_str =""
    i=1
    temp =i
    find_len=len(string)*2
    find_pos=0
    while refer_str.find(string) ==-1:
        i=temp
        if refer_str!="":
            find_pos+=len(refer_str)-find_len//2
            refer_str=refer_str[-(find_len//2):]        
        while len(refer_str) < find_len:
            refer_str+=str(i)
            i+=1
        else:
            temp=i
    else:
        return (find_pos+refer_str.find(string))
'''


def find_pos_for_n(n):
    num_len = len(str(n))
    out_temp = (n - int(pow(10, num_len - 1))) * num_len
    num_len -= 1
    while num_len:
        out_temp += (int(pow(10, num_len - 1)) * 9) * num_len
        num_len -= 1
    return out_temp


def find_position_from_n(string, n):
    add_temp = n
    find_temp = ""
    len_t = len(string)
    while len(find_temp) < len_t * 2:
        find_temp += str(add_temp)
        add_temp += 1
    else:
        return find_temp.find(string)


def find_position(string):
    if int(string) == 0:
        return find_pos_for_n(int("1" + string)) + 1
    len_t = len(string)
    find_first = 1
    out_temp = []
    for i in range(1, len_t + 1):
        for j in range(0, min(i, len_t - i + 1)):
            slice_temp = int(string[j:j + i])
            if slice_temp == 0:
                continue
            elif slice_temp == 1:
                find_first = slice_temp
            else:
                find_first = slice_temp - 1

            pos = find_position_from_n(string, find_first)
            if pos != -1:
                out_temp.append(pos + find_pos_for_n(find_first))
            else:
                pass
        else:
            for j in range(1, len_t):
                slice_temp = int(string[-i:] + "0" * j)
                if slice_temp == 0:
                    continue
                else:
                    find_first = slice_temp - 1
                pos = find_position_from_n(string, find_first)
                if pos != -1:
                    out_temp.append(pos + find_pos_for_n(find_first))
                else:
                    pass
    for i in range(1, len_t):
        for j in range(1, len_t - i + 1):
            slice_temp = int(string[i:i + j] + string[:i])
            find_first = slice_temp
            pos = find_position_from_n(string, find_first)
            if pos != -1:
                out_temp.append(pos + find_pos_for_n(find_first))
            else:
                pass
    return min(out_temp)


if __name__ == "__main__":

    t0 = time.perf_counter()
    test.assert_equals(find_position("456"), 3, "...3456...")
    test.assert_equals(find_position("454"), 79, "...444546...")
    test.assert_equals(find_position("455"), 98, "...545556...")
    test.assert_equals(find_position("001"), 190, "...100101...")
    test.assert_equals(find_position("00"), 190, "...100101...")
    test.assert_equals(find_position("99"), 168)
    test.assert_equals(find_position("091"), 170)
    test.assert_equals(find_position("0910"), 2927)
    #    test.assert_equals(find_position("555899959741198") ,1686722738828503)
    test.assert_equals(find_position("09991"), 35286)
    test.assert_equals(find_position("99940"), 14886)
    test.assert_equals(find_position("995"), 1387)
    test.assert_equals(find_position("58257860625"), 24674951477)

    print(time.perf_counter() - t0)
'''
from itertools import count
def num_index(n):
    if(n<10): return n-1
    c = 0
    for i in count(1):
        c += i*9 * 10**(i-1)
        if(n < 10**(i+1)): return c + (i+1)*(n - 10**i)

def find_position(s):
    if not int(s): return num_index(int('1'+s))+1
    for l in range(1,len(s)+1):
        poss = []
        for i in range(0,l+1):
            sdt = s[0:l-i]; end = s[l-i:l]
            for c in ([end+sdt, str(int(end)-1)+sdt] if end and int(end)!=0 else [end+sdt]):
                if(c[0]=='0'): continue
                ds = c; n = int(c)
                while(len(ds) < len(s)+l): n += 1; ds += str(n)
                idx = ds.find(s)
                if(idx != -1): poss.append(num_index(int(c)) + idx)
        if(len(poss) > 0): return min(poss)

'''
