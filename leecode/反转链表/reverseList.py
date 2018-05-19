#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
自己构建了链表结构，已通过，不知道测试如何操作链表，未通过
'''

import sys
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List_n:
    def __init__(self):
        self.head = None

    def __str__(self):
        node = self.head
        nlist = ''
        if node is None:
            return "None"
        while node:
            nlist += str(node.val) + ' '
            node = node.next
        return nlist
    
    def __repr__(self):
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.val) + ' '
            node = node.next
        return nlist
    def get_head(self):
        return self.head

    def add_Node(self,x):
        if not self.head:
            self.head=ListNode(x)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=ListNode(x)

class Solution:
    def __init__(self):
        self.out_t=List_n()

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            self.out_t.add_Node(head.val)
            return self.out_t
        else :
            self.reverseList(head.next)
            self.out_t.add_Node(head.val)
        return self.out_t
            


if __name__ == "__main__":

    t0 = time.perf_counter()
    test_l = List_n()
    test_l.add_Node(1)
    test_l.add_Node(2)
    test_l.add_Node(3)
    print(test_l)
    test=Solution()
    print(test.reverseList(test_l.get_head()))
    # haystack = "hellohello"
    # needle = "ll"   
    # print(test.strStr(haystack,needle)) 
    # haystack = "aaaaa"
    # needle = "bba"
    # print(test.strStr(haystack,needle))
    # haystack = "aaaaa"
    # needle = ""
    # print(test.strStr(haystack,needle))


    print(time.perf_counter() - t0)


'''
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle:
            return 0
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
'''
