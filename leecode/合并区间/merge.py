#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out_t=[]
        intervals.sort(key=lambda x:x.start)
        for val in intervals:
            if out_t ==[]:
                out_t.append(val)
            else:
                compare=out_t[-1]
                if val.start >= compare.start and val.start <= compare.end:
                    compare.end=max(val.end,compare.end)
                else:
                    out_t.append(val)
        return out_t
        
            


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = [[[1,3],[15,18],[2,6],[8,10]], [[1,4],[10,15],[2,12]],[]]
    answer_list = [[[1,6],[8,10],[15,18]],[[1,15]],[]]
    test = Solution()
    for i in range(len(test_list)):
        test_par=[]
        for list_t in test_list[i]:
                test_par.append(Interval(list_t[0],list_t[1]))
        out_t = test.merge(test_par)
        out_tt=[]
        for out_interval in out_t:
            out_tt.append([out_interval.start,out_interval.end]) 
        if out_tt == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_tt, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        starts = []
        ends = []
        for i in range(n):
            starts.append(intervals[i].start)
            ends.append(intervals[i].end)
        
        starts.sort();  
        ends.sort();  
        res = []
        j=0
        for i in range(n):
            if i == n - 1 or starts[i + 1] > ends[i]:
                res.append([starts[j], ends[i]]) 
                j = i + 1;  
        return res;  

class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1].end = max(merged[-1].end, interval.end)
        
        return merged
'''
