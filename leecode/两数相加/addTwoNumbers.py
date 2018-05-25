#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - but it is not a good solution
'''
from math import pow
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def ListToInt(self,l):
        out_t=0
        i=0
        while l:
            out_t+=l.val*pow(10,i)
            i+=1
            l=l.next
        return int(out_t)

    def IntToList(self,num):
        out_head=ListNode(0)
        out_t=out_head
        if num==0:
            return out_head
        while num:
            out_t.next=ListNode(num%10)
            num//=10
            out_t=out_t.next
        return out_head.next


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None
        temp_1=self.ListToInt(l1)
        temp_2=self.ListToInt(l2)
        out_t =temp_1 +temp_2
        return self.IntToList(out_t)




def stringToListNode(input):
    # Generate list from the input
    numbers = (input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_add_list = [[1, 2, 3], [2, 3, 5],[],[]]
    test_add_list_2 = [[1, 2, 3], [2, 3, 5],[],[1]]
    test_list = []
    test_list_2 = []
    for i in range(len(test_add_list)):
        test_list.append(stringToListNode(test_add_list[i]))
        test_list_2.append(stringToListNode(test_add_list_2[i]))

    answer_list = ['[2, 4, 6]', '[4, 6, 0, 1]','[]','[1]']
    test = Solution()
    for i in range(len(test_list)):
        out_t = listNodeToString(
            test.addTwoNumbers(test_list[i], test_list_2[i]))
        if out_t == answer_list[i]:
            print("Pass")
        else:
            print("Fail!! out \"%s\" should \"%s\" by \"%.50s\" " %
                  (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))



'''


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        L = curs = ListNode(0)
        flag = 0
        
        while(l1 or l2 or flag):
            val1 = val2 = 0
            
            if(l1):
                val1 = l1.val
                l1 = l1.next
                
            if(l2):
                val2 = l2.val
                l2 = l2.next
            
            
            val = (val1+val2+flag) % 10
            flag = (val1+val2+flag) // 10
            
            curs.next = ListNode(val)
            curs = curs.next
            

        return L.next
'''