#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - but not Pythonic
'''

import time
import copy

key_map = {
    "2": [["a"], ["b"], ["c"]],
    "3": [["d"], ["e"], ["f"]],
    "4": [["g"], ["h"], ["i"]],
    "5": [["j"], ["k"], ["l"]],
    "6": [["m"], ["n"], ["o"]],
    "7": [["p"], ["q"], ["r"], ["s"]],
    "8": [["t"], ["u"], ["v"]],
    "9": [["w"], ["x"], ["y"], ["z"]],
}


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        out_t = [[]]
        out = []
        last_out_len = 1
        for i in digits:
            alpha_temp = key_map[i]
            alpha_len = len(alpha_temp)

            copy_temp = copy.copy(out_t)
            for copy_i in range(alpha_len - 1):
                copy_t = copy.deepcopy(copy_temp)
                out_t.extend(copy_t)

            out_len = len(out_t)
            for j in range(out_len):
                out_t[j].extend(alpha_temp[j // last_out_len])

            last_out_len = out_len
        for s in out_t:
            out.append("".join(s))
        return out


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_list = ["23", ""]
    answer_list = [["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], []]
    test = Solution()
    for i in range(len(test_list)):
        out_t = test.letterCombinations(test_list[i])
        if out_t == answer_list[i]:
            print("Pass")
        else:
            print("Fail!! out \"%s\" should \"%s\" by \"%.50s\" " %
                  (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
so beautiful

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        mapping={'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':''}
        if len(digits)==1:
            return list(mapping[digits[0]])
        if len(digits)==0:
            return []
        first=self.letterCombinations(digits[:-1])
        last=mapping[digits[-1]]
        return [s+t for s in first for t in last]


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        
        digit2chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        res = [ i for i in digit2chars[digits[0]] ]
        
        for i in digits[1:]:
            res = [ m+n for m in res for n in digit2chars[i] ]
            
        return res 
'''
