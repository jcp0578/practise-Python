#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a best sulotion
应使用二分法
'''

import time


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        try:
            first=nums.index(target)
            target_len_t=nums.count(target)
            return [first,first+target_len_t-1]
        except ValueError:
            return [-1,-1]
            


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[5, 7, 7, 8, 8, 10], [5,7,7,8,8,10],[]]
    test_list_2 = [8,6, 1]
    answer_list = [[3,4], [-1,-1], [-1,-1]]
    test = Solution()
    for i in range(len(test_list)):
        out_t = test.searchRange(test_list[i], test_list_2[i])
        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''
I think my solution is best,hhh
'''
