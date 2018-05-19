#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
'''

import sys
import time


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
            


if __name__ == "__main__":

    t0 = time.perf_counter()
    test = Solution()

    haystack = "hellohello"
    needle = "ll"   
    print(test.strStr(haystack,needle)) 
    haystack = "aaaaa"
    needle = "bba"
    print(test.strStr(haystack,needle))
    haystack = "aaaaa"
    needle = ""
    print(test.strStr(haystack,needle))


    print(time.perf_counter() - t0)


'''
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
'''
