#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
'''

import sys
import time


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str=str.lstrip()
        if str == "":
            return 0
        if str[0] =='-' or str[0] =='+':
            start=1
        elif str[0].isdigit():
            start=0 
        else:
            return 0
        i =start
        while i<len(str):
            if str[i].isdigit():
                i+=1
            else:
                break
        if i ==start:
            return 0
        return max(min(int(str[0:i]),2**31-1),-2**31)
        


if __name__ == "__main__":

    t0 = time.perf_counter()
    test = Solution()

    s = ["aadadaadv","+","  2","4193 with words","words and 987","-91283472332","428527825724242"]
    for i in s:
        print(test.myAtoi(i))


    print(time.perf_counter() - t0)


'''
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """        

        str = str.strip()
        if not str:
            return 0
        sum = 0
        flag = 1
        if str[0] == '-':
            str = str[1:]
            flag = -1
        elif str[0] == '+' :
            str = str[1:]
        
        for c in str:
            if c.isdigit():
                sum = sum*10 + ord(c) - ord('0') 
            else:
                break
        sum = flag * sum
        if sum<-2**31:
            sum = -2**31
        if sum>2**31-1:
            sum = 2**31-1
        return sum
'''
