#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - but use "collections.defaultdict" better
'''
import time


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict_t={}
        out_t=[]
        for s in strs:
            str_sort="".join(sorted(list(s)))
            try:
                dict_t[str_sort].append(s)
            except KeyError:
                dict_t[str_sort]=[s]
        for keys in dict_t.keys():
            out_t.append(dict_t[keys])
        return out_t



if __name__ == "__main__":

    t0 = time.perf_counter()
    testlist = [["eat", "tea", "tan", "ate", "nat", "bat"],[],["rar","asd"]]
    test = Solution()
    for i in testlist:
        print(test.groupAnagrams(i))

    print(time.perf_counter() - t0)

'''
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map = collections.defaultdict(list)

        for s in strs:
            map[tuple(sorted(s))] += s,

        return sorted(map.values())
'''
