#!/usr/bin/python3
# -*- coding: utf-8 -*-


'''
AC - but it can be simpler by Python
Manacher 
'''

import time

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        t="#".join(s)
        t="$#"+t+"#&"
        len_t=len(t)
        mid=0
        right=0
        max_t=(0,0)
        max_str_t=""
        p=[1]*len_t
        for i in range(len_t-1):
            if i <right:
                p[i]=min(p[2*mid-i],right-i)
            else:
                p[i]=1
            while(t[i-p[i]]==t[i+p[i]]):
                p[i]+=1
            if right < i+p[i]:
                mid=i
                right=i+p[i]

            if p[i] > max_t[0]:
                max_t=(p[i],i)
                
        max_str_t=t[(max_t[1]-max_t[0]+2):(max_t[1]+max_t[0]-1)]
        return "".join(max_str_t.split("#"))

        




if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list=["babad","bbbbb","cafdabb,","a","","abacd"*200]
    answer_list=["bab","bbbbb","bb","a","","aba"]
    test=Solution()
    for i in range(len(test_list)):
        out_t=test.longestPalindrome(test_list[i])
        if out_t == answer_list[i]:
            print("Pass")
        else:
            print("Fail!! out \"%s\" should \"%s\" by \"%.50s\" "%(out_t,answer_list[i],test_list[i]))
    
    print("\nRun Time is %f s" %(time.perf_counter() - t0))



'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2 or s==s[::-1]:
            return s
        n=len(s)
        start,maxlen=0,1
        for i in range(n):
            odd =s[i-maxlen-1:i+1] #len(odd)=maxlen+2
            even=s[i-maxlen:i+1]    #len(even)=maxlen+1
            if i-maxlen-1>=0 and odd==odd[::-1]:
                start=i-maxlen-1
                maxlen+=2
                continue
            if i-maxlen>=0 and even==even[::-1]:
                start=i-maxlen
                maxlen+=1
        return s[start:start+maxlen]
'''