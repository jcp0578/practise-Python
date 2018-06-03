#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < 1 or n < 1:  
            return 0
        record = [[1]*n for j in range(m)]  
        for i in range(1, m):  
            for j in range(1, n):  
                record[i][j] = record[i - 1][j] + record[i][j - 1]  
        return record[m - 1][n - 1]  


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [3, 7, 23]
    test_list_2 = [2, 3, 12]
    answer_list = [3, 28, 193536720]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.uniquePaths(test_list[i], test_list_2[i])

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
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        超时C(m + n - 2, n - 1)：
        if m < n :
            m,n = n,m
        combins = [c for c in  itertools.combinations(range(m+n-2), n-1)]
        out = len(combins)
        return out
        
        from functools import reduce
        if m < n:
            m, n = n, m
        mul = lambda x, y: reduce(operator.mul, range(x, y), 1)
        return int(mul(m, m + n - 1) / mul(1, n))
        """
        v = [[1] * n for x in range(m) ]
        for i in range(m):
            for j in range(n):
                if i >= 1 and j >= 1:
                    v[i][j] = v[i][j-1]+v[i-1][j]
        return v[m-1][n-1]


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [0 for col in range(n)]
        for i in range(n):
            dp[i] = 1
            
        for i in range(1,m):
            for j in range(1,n):
                dp[j] = dp[j-1] + dp[j]
        
        return dp[n-1]
'''
