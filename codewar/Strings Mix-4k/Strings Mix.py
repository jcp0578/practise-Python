#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
no good way
'''

import sys
sys.path.append('../')
import cw as Test
import time



def count_str_alpha(str):
    out_temp={}
    for i in str:
        if i.islower():
            out_temp[i] =out_temp.get(i,-1)+1
        else:
            pass
    return (out_temp)

def count_alpha(hist):
    out_temp={}
    for key,value in hist.items():
        if value :
            if value in out_temp:
                out_temp[value].append(key)
            else :
                out_temp[value]=[key]
    return out_temp
    #return (sorted(out_temp.items(),reverse=1))

def mix(s1, s2):
    # your code
    t1=(count_str_alpha(s1))
    print(t1)
    t2=(count_str_alpha(s2))
    print(t2)
    t2.update(t1)
    print(t2)
    return 0
    #count_alpha(count_str_alpha(s1))



if __name__ == "__main__":

    t0 = time.perf_counter()
    Test.describe("Mix")
    Test.it("Basic Tests")
    Test.assert_equals(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
    # Test.assert_equals(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
    # Test.assert_equals(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
    # Test.assert_equals(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
    # Test.assert_equals(mix("codewars", "codewars"), "")
    # Test.assert_equals(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")

    print(time.perf_counter() - t0)




'''
def pick_peaks(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]:
            prob_peak = i
        elif arr[i] < arr[i-1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos':pos, 'peaks':[arr[i] for i in pos]}

'''
