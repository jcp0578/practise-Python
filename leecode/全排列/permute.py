#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC -but bad
'''

import time


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = [","+str(i) for i in nums]
        for i in nums[1:]:
            res = [m+","+str(n) for m in res for n in nums if ","+str(n) not in m]
        out_t=[]
        for num in res:
            out_t.append(list(map(int,(list(num[1:].split(","))))))
        return out_t         

if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[-1,2],[0,-1,1]]
    answer_list = [[[-1,2],[2,-1]],[[0,-1,1],[0,1,-1],[-1,0,1],[-1,1,0],[1,0,-1],[1,-1,0]]]

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.permute(test_list[i])

        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i], str(test_list[i])))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))
'''

'''
