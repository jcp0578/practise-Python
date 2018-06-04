#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC -use dict
'''

import time
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict={}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        try :
            self._dict[val]+=1
            return False
        except KeyError:
            self._dict[val]=1
            return True       

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        try:
            self._dict.pop(val)
            return True
        except KeyError:
            return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        try:
            return random.choice(list(self._dict.keys()))
        except IndexError:
            return None
        




if __name__ == "__main__":

    t0 = time.perf_counter()

    # Your RandomizedSet object will be instantiated and called as such:
    obj = RandomizedSet()
    val=3
    print(obj.insert(val))
    print(obj.getRandom())
    print(obj.remove(val))
    print(obj.getRandom())
    

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr, self.dic = [], {}
        
    def insert(self, val):
        if val not in self.dic:
            self.dic[val] = len(self.arr)
            self.arr.append(val)
            return True
        return False
    
    def remove(self, val):
        if val in self.dic:
            pos, last = self.dic[val], self.arr[-1]
            self.arr[pos], self.dic[last] = last, pos
            self.arr.pop()
            self.dic.pop(val, 0)
            return True
        return False           
    
    def getRandom(self):
        return self.arr[random.randint(0, len(self.arr) - 1)]
'''
