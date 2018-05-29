#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''
import time


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root:
            return None
        if root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
        else:
            return None
        self.connect(root.left)
        self.connect(root.right)


def stringToTreeLinkNode(input):
    input = str(input)
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeLinkNode(int(inputValues[0]))
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
            node.left = TreeLinkNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != '-1':
            rightNumber = int(item)
            node.right = TreeLinkNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


if __name__ == "__main__":

    t0 = time.perf_counter()

    #use debug to test
    test_add_list = []
    test_list = (stringToTreeLinkNode(test_add_list))
    test = Solution()
    test.connect(test_list)

    print("\nRun Time is %f s" % (time.perf_counter() - t0))


'''
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.helper(root)
                                                                                                                                             
    def helper(self, node):
        if not node or not node.left:
            return
        node.left.next = node.right
        if node.next:
            node.right.next = node.next.left
        self.helper(node.left)
        self.helper(node.right) 
'''
