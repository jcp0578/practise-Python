#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        len_m = len(matrix)
        for i in range(len_m):
            if matrix[i][0]>target:
                break
            elif matrix[i][-1]>=target and matrix[i][0] <= target:
                try:
                    matrix[i].index(target)
                    return True
                except ValueError:
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
    ], [[4, 5, 6, 7, 8, 9, 21]], [[]]]
    test_list_2 = [17, 6, 1]
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
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        for i in range(len(matrix)):
            if target==matrix[i][-1] or target==matrix[i][0]:
                return True
            elif target<matrix[i][-1] and target>matrix[i][0]:
                left,right=0,len(matrix[i])-1
                while left<=right:
                    mid=(left+right)//2
                    if target==matrix[i][mid]:
                        return True
                    elif target>matrix[i][mid]:
                        left=mid+1
                    else:
                        right=mid-1
        return False
'''
