#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC 
采用两列栈更佳
'''

import time


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack=[]
        self._min=None

    def stack_isempty(self):
        return False if len(self._stack) else True


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """        
        if self.stack_isempty():
            self._min =x
        else :
            self._min=min(x,self._min)
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        out_t=self._stack.pop()
        if self.stack_isempty():
            self._min =None
        else :
            self._min=min(self._stack)
        return out_t
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack_isempty():
            return None
        else :
            return self._stack[-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()



if __name__ == "__main__":

    t0 = time.perf_counter()

    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(0)
    obj.pop()
    print(obj.top())
    print(obj.getMin())

    print(time.perf_counter() - t0)


'''
class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.stack) > 0:
            currMin = self.stack[-1][1]
            self.stack.append((x, min(x, currMin)))
        else:
            self.stack.append((x,x))
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
'''
