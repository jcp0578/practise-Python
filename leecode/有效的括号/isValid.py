#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a good solution
'''
import time


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        trantab = s.maketrans("()[]{}", "142536")
        s = s.translate(trantab)
        s = list(map(int, s))
        stack = []
        for i in s:
            if i < 4:
                stack.append(i)
            else:
                try:
                    if i - stack.pop() == 3:
                        pass
                    else:
                        return False
                except IndexError:
                    return False
        else:
            return len(stack)==0


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
