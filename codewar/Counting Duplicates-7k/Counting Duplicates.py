#!/usr/bin/python3
# -*- coding: utf-8 -*-

import cw as test

debug = 1


def debug_print(flag, out):
    if debug:
        print("temp" + str(flag) + ":" + str(out))


def duplicate_count(text):
    # Your code goes here
    out_temp = 0
    count_t = [0] * 128
    for temp in text:
        if ord(temp) >= ord('a')  :
            count_t[ord(temp)-32] += 1
        else:
            count_t[ord(temp)] += 1
    for i in count_t:
        if i > 1:
            out_temp += 1
    return out_temp


if __name__ == "__main__":

    test.assert_equals(duplicate_count("abcde"), 0)
    test.assert_equals(duplicate_count("abcdea"), 1)
    test.assert_equals(duplicate_count("indivisibility"), 1)
    test.assert_equals(duplicate_count("aabBcde"), 2)
    test.assert_equals(duplicate_count("aA11"), 2)


'''
def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
'''