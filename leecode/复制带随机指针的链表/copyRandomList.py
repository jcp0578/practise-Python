#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error
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
        p=out_head
        while p:
            if p.next:
                p.next=p.next.next
            p=p.next
        return out_head



if __name__ == "__main__":

    if sys.version_info.major ==3: 
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = []
    answer_list = []

    test = Solution()
    for i in range(len(test_list)):
        out_t = test.coinChange(test_list[i])


        if out_t == answer_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, answer_list[i],
                   str(test_list[i])))
    
    if sys.version_info.major ==3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))
    
'''

'''
