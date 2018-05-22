#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
双指针判断中点，后反序中点后链表，比较前后部分
'''

import sys
import time


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def findListMid(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = p2 = head
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        return p1 if p2 is None else p1.next

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        mid_node = self.findListMid(head)
        mid_t = self.reverseList(mid_node)
        while head and mid_t:
            if head.val == mid_t.val:
                head, mid_t = head.next, mid_t.next
            else:
                return False
        return True


if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list = [1, 2, 3, 3, 2, 1]
    test_head = ListNode(add_list[0])
    p_l = test_head
    for i in range(1, len(add_list)):
        p_l.next = ListNode(add_list[i])
        p_l = p_l.next
        p_l.next = None

    test = Solution()
    print(test.findListMid(test_head).val)
    print(test.isPalindrome(test_head))

    print(time.perf_counter() - t0)

'''

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        mid = ListNode(0)
        mid.next = head
        fast = mid
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
            
        
        prev = mid
        curr = mid.next
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        start = head
        end = prev
        if start.val != end.val:
            return False
        while start != mid.next:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next
        return True


    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, new_head = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            new_head, new_head.next, slow = slow, new_head, slow.next
            
        if fast:
            slow = slow.next
            
        while new_head and new_head.val == slow.val:
            new_head, slow = new_head.next, slow.next
            
        return not new_head
'''
