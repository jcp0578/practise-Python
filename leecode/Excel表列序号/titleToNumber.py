#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time
from math import pow

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        out_t=0
        s=s.upper()[::-1]
        for i in range(len(s)):
            out_t+=int(pow(26,i))*(ord(s[i])-64)
        return out_t



if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = ["ZY","a","AB",""]
    answer_list = [701,1,28,0]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.titleToNumber(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:return None
        num = 0
        for c in s:
            num = ((num*26) + ord(c) -64)
        return num
'''
