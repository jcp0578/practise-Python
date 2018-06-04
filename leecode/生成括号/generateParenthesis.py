#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        temp=""
        out_t=[]
        def process(out,temp,left,right,n):
            if left >n or right >n or left <right:
                return -1
            if left == n and right ==n:
                out.append(temp)
                return 1
            process(out,temp+"(",left+1,right,n)
            process(out,temp+")",left,right+1,n)
        process(out_t,temp,0,0,n)
        return out_t

if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [3,0]
    answer_list = [["((()))", "(()())", "(())()", "()(())", "()()()"],[]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.generateParenthesis(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''
        def generate(S='', left=0, right=0):
            if len(S) == n * 2:
                res.append(S)
            else:
                if left < n:
                    generate(S + '(', left + 1, right)
                if right < left:
                    generate(S + ')', left, right + 1)            
            return 
        
        res = []
        generate()
        
        return res

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return ['']
        r = ['(']
        left = [n - 1]
        right = [n]
        for cnt in range(2 * n - 1):
            rtmp, lefttmp, righttmp = [], [], []
            for i, s in enumerate(r):
                if left[i]:
                    rtmp.append(s + '(')
                    lefttmp.append(left[i] - 1)
                    righttmp.append(right[i])
                if right[i] > left[i]:
                    rtmp.append(s + ')')
                    lefttmp.append(left[i])
                    righttmp.append(right[i] - 1)
            r, left, right = rtmp, lefttmp, righttmp
        return r
'''
