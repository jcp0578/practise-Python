#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
'''

import sys
import time


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "":
            return -1
        d = {}
        len_t = len(s)
        for i in range(len_t):
            if s[i] in d.keys():
                d[s[i]] = len_t
            else:
                d[s[i]] = i

        temp = min(d.values())
        if temp < len_t:
            return temp
        else:
            return -1


if __name__ == "__main__":

    t0 = time.perf_counter()
    test = Solution()

    s = "aadadaadv"
    print(test.firstUniqChar(s))
    print(time.perf_counter() - t0)


'''
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = 'abcdefghijklmnopqrstuvwxyz'
        L_index = [s.index(letter) for letter in letters if s.count(letter) == 1]
        return min(L_index) if L_index else -1
'''
