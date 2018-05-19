#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
'''

import sys
import time

class Solution:
    def count_nums(self,nums):
        dict_t={}
        for i in nums:
            if i in dict_t.keys():
                dict_t[i]+=1
            else:
                dict_t[i]=1
        return dict_t

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out_temp=[]
        dict1=self.count_nums(nums1)
        dict2=self.count_nums(nums2)
        if len(dict1) > len(dict2) :
            dict1,dict2=dict2,dict1
        for key,value in dict1.items():
            if key in dict2.keys():
                out_temp.extend([key]*(min(value,dict2[key])))
            else:
                pass
        return out_temp
        

        


    



if __name__ == "__main__":

    t0 = time.perf_counter()
    test=Solution()
    
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    print(test.intersect(nums1,nums2))
    print(time.perf_counter() - t0)




'''
        res = []

        dict1 = {}
        for i in nums1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        
        for i in nums2:
            if i in dict1:
                res.append(i)
                dict1[i] -= 1
                if dict1[i] == 0:
                    dict1.pop(i)
        return res
    
'''
