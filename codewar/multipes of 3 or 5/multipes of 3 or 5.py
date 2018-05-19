#!/usr/bin/python3
# -*- coding: utf-8 -*-

debug = 1
#kan qing ti yi

#"Multiples of 3 and 5"

#solution(10), 23


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))

def sum_ap(num_max,num_diff):
    num_max=(num_max-1)//num_diff*num_diff
    if num_max :
        n=(num_max-num_diff)//num_diff+1
        return (num_diff+num_max)*n//2
    else:
        return 0


def solution(number):
  
    return (sum_ap(number,3)+sum_ap(number,5)-sum_ap(number,15))


if __name__ == "__main__":
    print(solution(10))
