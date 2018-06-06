#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
not finish
'''
import sys
import time



class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        out_t=[]
        for index,char in enumerate(s):
            if char in t:
                out_t.append(index)
        


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = ["ADOBECODEBANC",]
    test_list_2 = ["ABC",]
    answer_list = ["BANC"]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.minWindow(test_list[i], test_list_2[i])


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
