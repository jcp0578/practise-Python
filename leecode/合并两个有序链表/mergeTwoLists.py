#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''

'''

import sys
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1,p2=l1,l2
        out = ListNode(0)
        out_temp =out
        while p1 is not None:
            while p2 is not None:
                if p1.val < p2.val:
                    out_temp.next=ListNode(p1.val)
                    out_temp=out_temp.next
                    p1=p1.next
                else:
                    out_temp.next=ListNode(p2.val)
                    out_temp=out_temp.next
                    p2=p2.next
                break
            else :
                out_temp.next=p1
                break
        else:
            out_temp.next=p2
        return out.next

           


if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list_2=[1,2,3,4,5]
    add_list_1=[1,3,5,9,10,11,12]
    test_head_1=ListNode(add_list_1[0])
    test_head_2=ListNode(add_list_2[0])
    p_l=test_head_1
    for i in range(1,len(add_list_1)):
        p_l.next=ListNode(add_list_1[i])
        p_l=p_l.next
        p_l.next=None

    p_l=test_head_2
    for i in range(1,len(add_list_2)):
        p_l.next=ListNode(add_list_2[i])
        p_l=p_l.next
        p_l.next=None
    test=Solution()

    out=test.mergeTwoLists(test_head_1,test_head_2)



    print(time.perf_counter() - t0)


'''

loop
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        h=p
        while l1 and l2:
            if l1.val<=l2.val:
                h.next=l1
                l1=l1.next
            else:
                h.next=l2
                l2=l2.next
            h=h.next
        h.next=l1 or l2
        return p.next

recursion
class Solution(object):
    def mergeTwoLists(self, l1, l2):  
        if not l1:  
            return l2  
        elif not l2:  
            return l1  
        else:  
            if l1.val <= l2.val:  
                l1.next = self.mergeTwoLists(l1.next, l2)  
                return l1  
            else:  
                l2.next = self.mergeTwoLists(l1, l2.next)  
                return l2 
'''
