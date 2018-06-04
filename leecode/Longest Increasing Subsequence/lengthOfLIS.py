#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
O(NlogN)
'''

import time


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_t = len(nums)
        max_t = [0]*len_t #用于保存m个最长上升序列的最后一位数值
        size_t=0
        for num in nums:
            start,end =0,size_t
            while start !=end:
                mid=(start+end)//2
                if max_t[mid] < num:
                    start=mid+1
                else:
                    end=mid
            max_t[start]=num
            size_t=max(size_t,start+1)
        return size_t


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[10, 9, 2, 5, 3, 7, 101, 18], [
        1, 2, 5], [2], [], [1, 3, 6, 7, 9, 4, 10, 5, 6]]
    answer_list = [4, 3, 1, 0, 6]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.lengthOfLIS(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划O(n**2), 超时
        # [0...i]的最大上升子序列,要求必须包含第i个元素,的长度
#         length = len(nums)
#         if length == 0:
#             return 0
#         memo = [1 for i in range(length)]
#         for i in range(1, length):
#             j = 0
#             while j < i:
#                 if nums[j] < nums[i]:
#                     memo[i] = max(memo[i], memo[j] + 1)
#                 j += 1
        
#         return max(memo)
        
        # 加入二分搜索,时间复杂度O(nlogn)
        def BinarySearch(m, maxlength, t):
            low = 1
            high = maxlength
            while low <= high:
                mid = int((low + high) / 2)
                if t == m[mid]:
                    return mid
                elif t > m[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            return low
        
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return 1
        # m[x]存放长度为x的最长上升子序列的最大末尾数
        
        maxlength = 1  # 从1开始,序列长度是从1开始
        m = [-1 for i in range(length+1)]
        m[maxlength] = nums[0]
        
        for i in range(1, length):
            if nums[i] > m[maxlength]:
                maxlength += 1
                m[maxlength] = nums[i]
            else:
                p = BinarySearch(m, maxlength, nums[i])
                m[p] = nums[i]
            
        return maxlength
'''
