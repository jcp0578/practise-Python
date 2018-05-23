#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time
import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._original=tuple(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return list(self._original)
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        original=list(self._original)        
        return [original.pop(int(random.random()*i)) for i in range(len(original),0,-1)]




if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[1,2,3]]
#                 list(range(10000))]
    for i in test_list:
        obj = Solution(i)
        param_2 = obj.shuffle()
        print(param_2)        
        param_1 = obj.reset()
        print(param_1)
        param_2 = obj.shuffle()
        print(param_2)
        print("ok")

    print(time.perf_counter() - t0)


'''
class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.backup = nums[::]
        self.array = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        self.array = self.backup[::]
        return self.array
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        random.shuffle(self.array)
        return self.array
'''
