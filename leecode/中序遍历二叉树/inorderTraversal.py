#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
error

'''
from math import pow
import time
import json


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out_t = []
        save_t = []  # save next root
        out_node_t = []  # save node
        p = root
        while p:
            while p.left is not None and p.left not in out_node_t:
                save_t.append(p)
                p = p.left
            out_node_t.append(p)
            if p.right is not None:
                p = p.right
            else:
                try:
                    p = save_t.pop()
                except IndexError:
                    p = None
        for i in out_node_t:
            out_t.append(i.val)
        return out_t


def stringToTreeNode(input):
    input = str(input)
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != '-1':
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != '-1':
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


if __name__ == "__main__":

    t0 = time.perf_counter()

    test_add_list = [[1, 2, 3, 4, -1, 5, -1, 6, -1, -1, -1, 7],
                     [4, 2, -1, 1, 3], [2, 3, 5], [], [1,-1,2,3,4,5,-1]]
    test_list = []
    answer_list = [[7, 6, 4, 2, 1, 5, 3], [1, 2, 3, 4], [3, 2, 5], [],[1,5,3,2,4]]
    for i in range(len(test_add_list)):
        test_list.append(stringToTreeNode(test_add_list[i]))
    test = Solution()
    for i in range(len(test_list)):
        out_t = test.inorderTraversal(test_list[i])
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
