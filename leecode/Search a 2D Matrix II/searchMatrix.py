#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error
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
        len_m = len(matrix)
        len_n = len(matrix[0])
        start = (0, 0)
        end = (len_m, len_n)
        mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        while start != mid:           
            if matrix[mid[0]][mid[1]] == target:
                return True
            elif matrix[mid[0]][mid[1]] > target:
                end = mid
            else:
                start = mid
            mid = ((start[0] + end[0]) // 2, (start[1] + end[1]) // 2)
        try:
            if matrix[mid[0] + 1][mid[1]] == target:
                return True
        except IndexError:
            pass

        try:
            if matrix[mid[0]][mid[1] + 1] == target:
                return True
        except IndexError:
            pass

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
