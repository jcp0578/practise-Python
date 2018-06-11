#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import sys
import time



# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return None
        p=head
        while p:
            add_node=RandomListNode(p.label)
            add_node.next=p.next
            add_node.random=p.random
            p.next=add_node
            p=add_node.next
        p=head
        while p:
            if p.next.random:
                p.next.random=p.random.next
            p=p.next.next
        out_head=head.next
        p=head
        while p:
            temp=p.next.next
            if temp:
                p.next.next=temp.next
            p.next=temp            
            p=p.next
        return out_head


if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()



#   do not have test,it is bad
    
    if sys.version_info.major ==3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
    
'''
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return None
        src = {}
        cpy = {}
        p = head
        q = cpyHead = RandomListNode(p.label)
        src[p] = 0
        cpy[0] = q
        p = p.next
        idx = 1
        while p is not None:
            q.next = RandomListNode(p.label)
            q = q.next
            src[p] = idx
            cpy[idx] = q
            idx += 1
            p = p.next

        p = head
        rand = []
        while p is not None:
            if p.random is None:
                rand.append(None)
            else:
                rand.append(src[p.random])
            p = p.next
        q = cpyHead
        idx = 0
        while q is not None:
            if rand[idx] is None:
                q.random = None
            else:
                q.random = cpy[rand[idx]]
            q = q.next
            idx += 1
        return cpyHead
'''
