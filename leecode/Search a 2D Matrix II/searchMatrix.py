#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - a bad solution
'''

import time


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == []:
            return False
        for list_t in matrix:
            try:
                list_t.index(target)
                return True
            except ValueError:
                pass
        else :
            return False


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ], [[4, 5, 6, 7, 0, 1, 2]], []]
    test_list_2 = [19, 6, 1]
    answer_list = [True, True, False]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.searchMatrix(test_list[i], test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''

'''
