#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a good solution
'''

import time
import copy

class Solution:
    _out_t=[]
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self._out_t=[]
        temp_out=[]
        nums.sort()
        self.backtrack(temp_out,nums)
        return self._out_t
    def backtrack(self,temp_out,nums):
        _temp_out=copy.copy(temp_out)          
        self._out_t.append(_temp_out)
        if len(_temp_out) < len(nums):
            for num in nums:
                if _temp_out==[] or num> _temp_out[-1]:
                    _temp_out.append(num)
                    self.backtrack(_temp_out,nums)
                    _temp_out.pop()
                else:
                    continue
        else:
            return 1

if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1, 2, 3]]
    answer_list = [[[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []],    ]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.subsets(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''
class Solution:
    
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for index in range(1<<len(nums)):#n^2
            item = []
            for j in range(len(nums)):
                if(index&(1<<j)):item.append(nums[j])
            res.append(item)
        return res

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results=[[]]
        for i in nums:
            results=results+[[i]+num for num in results]
        return results
'''
