#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
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
        elif n<0:
            return 1/self.myPow(x,-n)
        elif n==2:
            return x*x

        if x == 0:
            return 0.0
        elif x==1:
            return 1.0
        temp= self.myPow(x,n//2)
        if n%2:
            return x*self.myPow(temp,2)
        else:
            return self.myPow(temp,2)


        



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
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        s = 1        
        if n < 0:
            n = -n
            k = 0
        else:
            k = 1
            
        while n > 0: 
            if n % 2 == 1:            
                s *= x                    
            n //= 2
            x *= x
            
        if k:
            return s
        return 1/s


class Solution:

    def myPow(self, x, n):
        """
        求 x 的 n 次幂
        使用递归的方法,每次缩小2的倍数
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n & 1:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)        
'''
