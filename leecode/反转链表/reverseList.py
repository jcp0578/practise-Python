#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not good
'''

import sys
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# class List_n:
#     def __init__(self):
#         self.head = None

#     def __str__(self):
#         node = self.head
#         nlist = ''
#         if node is None:
#             return "None"
#         while node:
#             nlist += str(node.val) + ' '
#             node = node.next
#         return nlist
    
#     def __repr__(self):
#         node = self.head
#         nlist = ''
#         while node:
#             nlist += str(node.val) + ' '
#             node = node.next
#         return nlist
#     def get_head(self):
#         return self.head

#     def add_Node(self,x):
#         if not self.head:
#             self.head=ListNode(x)
#         else:
#             node=self.head
#             while node.next:
#                 node=node.next
#             node.next=ListNode(x)
# class Solution:
#     def __init__(self):
#         self.out_t=List_n()

#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         if head.next is None:
#             self.out_t.add_Node(head.val)
#             return self.out_t
#         else :
#             self.reverseList(head.next)
#             self.out_t.add_Node(head.val)
#         return self.out_t 

class Solution:
    # def __init__(self):
    #     self.out_t=List_n()

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        if head.next is None:
            out_temp=ListNode(head.val)
            return out_temp
        else :
            out_temp=self.reverseList(head.next)
            p_temp=out_temp
            while p_temp.next is not None:
                p_temp=p_temp.next
            p_temp.next=ListNode(head.val)
        return out_temp

           


if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list=[1,2,3,4,5]

    test_head=ListNode(0)
    p_l=test_head
    for i in add_list:
        p_l.next=ListNode(i)
        p_l=p_l.next
        p_l.next=None

    test=Solution()

    out=test.reverseList(test_head)



    print(time.perf_counter() - t0)


'''
good Solution

Loop
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_head = None
        p = head
        
        while p:
            temp = p.next
            p.next = new_head
            new_head = p
            p = temp
        
        return new_head


recursion
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverse_list(head):
            if head == None:
                return (None, None)
            if head.next == None:
                return (head, head)
            h, t = reverse_list(head.next)
            t.next = head
            head.next = None
            return h, head
        h, t = reverse_list(head)
        return h
'''
