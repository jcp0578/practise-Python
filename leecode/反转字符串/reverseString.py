#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
import time

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]


    


if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    
    s = "hello"
    print(test.reverseString(s))
    print(time.perf_counter() - t0)




'''
通过list.reverse
'''
