#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC - but it is not a good solution
Best solution is beautiful
'''
from math import pow
import time


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getListLen(self, head):
        out_t = 0
        p = head
        while head:
            head = head.next
            out_t += 1
        return out_t

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        len_a = self.getListLen(headA)
        len_b = self.getListLen(headB)
        if len_a < len_b:
            p1,p2=headB,headA
            len_diff=len_b-len_a
        else:
            p1,p2=headA,headB
            len_diff=len_a-len_b
        for i in range(len_diff):
            p1=p1.next
        while p1 and p2:
            if p1.val == p2.val :
                return p1
            else:
                p1,p2=p1.next,p2.next
        else:
            return None


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


def listNodeToString(node, one_flag=0):
    if not node:
        return "[]"

    if one_flag:
        return "[" + str(node.val) + "]"
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_add_list = [[11, 12, 13, 4, 5, 6], [2, 3, 5], [], [1]]
    test_add_list_2 = [[21, 22, 23, 4, 5, 6], [4, 2, 3, 5], [], [1]]
    test_list = []
    test_list_2 = []
    for i in range(len(test_add_list)):
        test_list.append(stringToListNode(test_add_list[i]))
        test_list_2.append(stringToListNode(test_add_list_2[i]))

    answer_list = ['[4]', '[2]', '[]', '[1]']
    test = Solution()
    for i in range(len(test_list)):
        out_t = listNodeToString(
            test.getIntersectionNode(test_list[i], test_list_2[i]), one_flag=1)
        if out_t == answer_list[i]:
            print("Pass")
        else:
            print("Fail!! out \"%s\" should \"%s\" by \"%.50s\" " %
                  (out_t, answer_list[i], test_list[i]))

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        while(p1 != p2):
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
        return p1
'''