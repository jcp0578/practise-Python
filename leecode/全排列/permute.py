#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        def generate(arr, rem):
            if len(rem) == 0:
                result.append(arr)
            for i in range(len(rem)):
                new_arr = arr[:]
                new_arr.append(rem[i])
                generate(new_arr, rem[:i] + rem[i+1:])
        
        generate([], nums)
        return result       

if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[-1,2],[0,-1,1]]
    answer_list = [[[-1,2],[2,-1]],[[0,-1,1],[0,1,-1],[-1,0,1],[-1,1,0],[1,0,-1],[1,-1,0]]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.permute(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))

'''
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        if len(nums)<=1:
            ans.append(nums)
        else:
            for i,num in enumerate(nums):
                n = nums[:i]+nums[i+1:]
                for y in self.permute(n):
                    ans.append([num]+y)
        return ans
'''
