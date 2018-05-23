#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
AC - but use dict better
'''

import time

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        compare_t=[]
        max_t=0
        for char in s:
            try :
                compare_t=compare_t[compare_t.index(char)+1:]
                compare_t.append(char)
            except ValueError:
                compare_t.append(char)
                max_t=max(max_t,len(compare_t))
        return max_t

        


    



if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list=["abcabcbb","bbbbb","pwwkew","","abcad"]
    answer_list=[3,1,3,0,4]
    test=Solution()
    for i in range(len(test_list)):
        out_t=test.lengthOfLongestSubstring(test_list[i])
        if out_t == answer_list[i]:
            print("Pass")
        else:
            print("Fail!! out \"%s\" by \"%s\" "%(out_t,test_list[i]))
    
    print("\nRun Time is %f s" %(time.perf_counter() - t0))



'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        hashTable = {}
        max_len = 0
        cur = 0

        for i,c in enumerate(s):
            if c in hashTable and cur <= hashTable[c] :
                cur = hashTable[c] + 1
            else:
                max_len = max(max_len,i - cur + 1)
            hashTable[c] = i 

        return max_len
'''