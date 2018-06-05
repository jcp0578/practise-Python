#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import sys
import time


class Solution:
    def rotate(self, matrix):
        """ 
        :contrarotate matrix. 
        """
        return list(map(list, zip(*matrix[::])))[::-1]

    def spiralOrder(self, matrix):
        out_temp = []
        while matrix:
            out_temp.extend(matrix[0][:])
            matrix = self.rotate(matrix[1:])
        return out_temp


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]]
    answer_list = [[1, 2, 3, 6, 9, 8, 7, 4, 5],
                   [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.spiralOrder(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
'''
I think my solution is the best,hhh
'''
