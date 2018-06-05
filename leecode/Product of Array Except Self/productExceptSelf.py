#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import sys
import time


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        out_t = [1]
        len_t = len(nums)
        for i in range(1, len_t):
            out_t.append(out_t[i - 1] * nums[i - 1])
        back_product=1
        for i in range(len_t-1,-1,-1):
            out_t[i]*=back_product
            back_product*=nums[i]
        return out_t


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 2, 3, 4], [2]]
    answer_list = [[24, 12, 8, 6], [1]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.productExceptSelf(test_list[i])

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
class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        # It calculates the left and right part of the product independently.
        return output


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums: return False
        
        arr = [1] * len(nums)
        pi = pj = 1

        for i in range(len(nums)):
            j = -1-i

            arr[i]*=pi; arr[j]*=pj
            pi *= nums[i]; pj *= nums[j]  
'''
