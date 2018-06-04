#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but ugly
'''

import time


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        flag=0
        out_t =0
        pow_t=1
        if dividend <0:
            flag+=1
            dividend=-dividend
        if divisor <0:
            flag-=1
            divisor=-divisor

        divisor_t=divisor

        if divisor_t >dividend:
            return 0
        while divisor_t <=dividend:
            pow_t=pow_t<<1
            divisor_t<<=1
        divisor_t>>=1
        pow_t>>=1

        while dividend > 0 and divisor_t:
            if dividend >= divisor_t:
                dividend-=divisor_t
                out_t+=pow_t
            else:
                pass
            pow_t>>=1
            divisor_t>>=1
            
        if flag:
            out_t=-out_t
        out_t=min(2147483647,out_t)
        out_t=max(-2147483648,out_t)
        return out_t
        


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [1, 2, -5,10,7,2147483648,-2147483648]
    test_list_2 = [11,1,5,3,-3,1,-3]
    answer_list = [0,2,-1,3,-2,2147483647,715827882]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.divide(test_list[i], test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i]) + " " + str(test_list_2[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))

'''
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        sign = 1 if (dividend < 0) == (divisor < 0) else -1
        
        x, y = abs(dividend), abs(divisor)
        
        if x < y:
            return 0
        
        if x == y:
            return sign
        
        arange = range(y, x, y)
        alen = len(arange)
        if arange[-1] + y <= x:
            alen += 1
        
        if sign == -1:
            alen = -alen
        return min(alen, 2 ** 31 -1)
'''
