#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
中序遍历后，比较是否递增
AC but not a good solution
'''

import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
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


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        out_temp=[]
        def mid_order(root):
            if root:
                mid_order(root.left)
                out_temp.append(root.val)
                mid_order(root.right)
        mid_order(root)
        for i in range(len(out_temp)-1):
            if out_temp[i] >=out_temp[i+1]:
                return False
        else:
            return True
         



if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list = str([10,5,15,-1,-1,6,20])
    test_head = stringToTreeNode(add_list)

    test = Solution()
    print(test.isValidBST(test_head))

    print(time.perf_counter() - t0)
'''

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        sta = []
        res = []
        t = root
        while t or sta:
            while t:
                sta.append(t)
                t = t.left
            t = sta.pop()
            res.append(t.val)
            t = t.right
        for i in range(len(res)-1):
            if res[i]>=res[i+1]:
                return False
        return True

'''
