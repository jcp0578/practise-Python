#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a good solution
'''

import time


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_t=len(nums)
        over_t = len_t//2+len_t%2
        dict_t={}
        for i in range(len_t):
            try:
                dict_t[nums[i]]+=1
                if dict_t[nums[i]] >= over_t:
                    return nums[i]
            except KeyError:
                dict_t[nums[i]]=1
        else:
            return max(dict_t.keys())
        


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[3,2,3],[2,2,1,1,1,2,2,3]]
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
