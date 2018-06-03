#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out
'''

import time


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m > 0 and n > 0:
            if m == 1:
                return 1
            elif n == 1:
                return 1
            else:
                return self.uniquePaths(m, n - 1) + self.uniquePaths(m - 1, n)
        else:
            return 0


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [3, 7, 2]
    test_list_2 = [2, 3, 2]
    answer_list = [3, 28, 2]

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

'''
