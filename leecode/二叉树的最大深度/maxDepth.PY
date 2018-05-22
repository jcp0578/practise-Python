#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
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
        if item != -1:
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != -1:
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        depth_list = []
        depth = 1

        def add_Depth(root, depth):
            if root.left is not None:
                add_Depth(root.left, depth + 1)
            if root.right is not None:
                add_Depth(root.right, depth + 1)
            if root.left is None and root.right is None:
                depth_list.append(depth)
                return 0
        add_Depth(root, depth)
        return max(depth_list)


if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list = str([1, 2, 3, -1, -1, 4, 5, 6])
    test_head = stringToTreeNode(add_list)

    test = Solution()
    print(test.maxDepth(test_head))

    print(time.perf_counter() - t0)
'''

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """        
        def maxd(node):
            ld = 0; rd = 0
            if node.left :
                ld = maxd(node.left) 
            else:
                ld = 0
            if node.right:
                rd = maxd(node.right) 
            else:
                rd = 0
            return max(ld,rd) + 1
        if root:
            return maxd(root)
        else:
            return 0
'''
