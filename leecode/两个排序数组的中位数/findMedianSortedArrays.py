#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
not finish
'''
import sys
import time



class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len_t=(len(nums1)+len(nums2))
        k_t=(len_t+1)//2
        while nums1 and nums2:
            if nums1[k_t//2-1] ==nums2[k_t//2-1]:
                return nums1[k_t//2-1]
            elif nums1[k_t//2-1] >nums2[k_t//2-1]:
                nums2=nums2[(k_t//2-1):]
                k_t-=k_t//2-2
            else :
                nums1=nums1[(k_t//2-1):]
                k_t-=k_t//2-2
        else:
            if nums1:
                return nums1[k_t-1] if len_t%2==1 else (nums1[k_t-1]+nums1[k_t-2])/2
            if nums2:
                return nums2[k_t-1] if len_t%2==1 else (nums2[k_t-1]+nums2[k_t-2])/2


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [[1, 3],[1,3],[],[]]
    test_list_2 = [[2],[2,4],[1,2,3],[2,3]]
    answer_list = [2.0,2.5,2.0,2.5]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.findMedianSortedArrays(test_list[i], test_list_2[i])


        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i]) + " " + str(test_list_2[i])))
    
    if sys.version_info.major ==3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
    
'''

'''
