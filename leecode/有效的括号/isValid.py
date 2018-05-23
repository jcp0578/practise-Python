#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import time


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'[': 1, '(':2, '{':3}
        right = {']':1, ')':2, '}':3}
        left_s = []
        for i in s:
            if i in left:
                left_s.append(left[i])
            else:
                if len(left_s) == 0:
                    return False
                if left_s.pop() != right[i]:
                    return False
        return len(left_s) == 0


if __name__ == "__main__":

    t0 = time.perf_counter()
    testlist = ["(", "()[]{}", "(]", "([)]", "{[]}"]
    test = Solution()
    for i in testlist:
        print(test.isValid(i))

    print(time.perf_counter() - t0)

'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in ["{", "(", "["]:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                currBracket = stack[-1] + c
                if currBracket not in ["{}", "[]", "()"]:
                    return False
                stack.pop()
        return len(stack) == 0


'''
