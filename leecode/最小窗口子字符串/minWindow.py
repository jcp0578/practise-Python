#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
time out 
'''
import sys
import time
from functools import reduce


class Solution:
    def countStr(self,s):
        out_t=[0]*128
        for char in s: 
                out_t[ord(char)]+=1
        return out_t
    

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_len=len(s)
        if not s_len:
            return ""
        t_len=len(t)
        if not t_len:
            return s[0]

        target_list=self.countStr(t)

        def inTargetStr(char):
            return (char in t)
        find_flag=list(map(inTargetStr,s))

        first_t,last_t=0,0
        min_first,min_last=0,s_len+1
        while True:
            while last_t < s_len and reduce(lambda x,y:(x>0)+(y>0),target_list[32:]):
                if find_flag[last_t]:
                    target_list[ord(s[last_t])]-=1
                last_t+=1
            
            while first_t < last_t and (not reduce(lambda x,y:(x>0)+(y>0),target_list[32:])):
                if find_flag[first_t]:
                    target_list[ord(s[first_t])]+=1
                first_t+=1
            else :
                if (last_t - first_t + 1) < (min_last - min_first):
                    min_first,min_last=first_t-1,last_t
            if last_t ==s_len:
                break     
        if min_last ==s_len+1:
            return ""
        return s[min_first:min_last]
        


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = ["DADOBECODEBANCD","A",""]
    test_list_2 = ["ABC","B","A"]
    answer_list = ["BANC","",""]

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
