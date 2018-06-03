#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC -good
二分法更快
'''

import time


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        try :
            return nums.index(target)
        except ValueError:
            return -1



if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[4, 5, 6, 7, 0, 1, 2], [4, 5, 6, 7, 0, 1, 2], []]
    test_list_2 = [0, 3, 1]
    answer_list = [4, -1, -1]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.search(test_list[i], test_list_2[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        low =0
        high = len(nums)-1
        while low <= high:
            mid = (high - low)//2 + low
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[high]:
                if nums[mid] < target and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid -1
            else:
                if nums[mid] > target and nums[low] <= target:
                    high = mid -1
                else:
                    low = mid+1
        return -1
'''
