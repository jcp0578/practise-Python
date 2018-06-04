#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out 
'''

import time
#from math import round

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n ==0:
            return 1
        if x == 0:
            return 0
        elif x==1:
            return 1
        out_t=1
        for i in range(abs(n)):
            out_t*=x
            if out_t ==0:
                return 0.0
        if n<0 and out_t:
            out_t=1/out_t
        return round(out_t,5)


        



if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [2.00000,2.10000,2.00000,2.15000,0.999]
    test_list_2=[10,3,-2,10,2147483647]
    answer_list = [1024.00000,9.26100,0.25,2110.49632,0.0]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.myPow(test_list[i],test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])+"   "+str(test_list_2[i])))

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
