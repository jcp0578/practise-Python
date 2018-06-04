#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time
from math import log

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """ 
        if n == 0:
            return 0
        five_times = 0
        five_pow = int(log(n, 5))
        for i in range(five_pow):
            five_times = five_times + int(n / pow(5, (i + 1)))
        return (five_times)


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [0, 5, 26, 78, 105, 180, 1800]
    answer_list = [0,1,6,18,25,44,448]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.trailingZeroes(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        res = 0
        while True:
            k = n // (5 ** count)
            if k == 0:
                break
            res += k
            count += 1
        return res
'''
