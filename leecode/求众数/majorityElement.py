#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)//2]
        


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[3,2,3],[2,2,3,3,3,2,2]]
    answer_list = [3,2]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.majorityElement(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = list(set(nums))
        for i in tmp:
            if nums.count(i) > len(nums)/2:
                return i

class Solution:
    def majorityElement(self, nums):
        n=len(nums)
        nums.sort()
        return nums[int(n/2)]
        """
        :type nums: List[int]
        :rtype: int
        """
'''
