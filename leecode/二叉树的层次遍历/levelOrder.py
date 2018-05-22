#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
递归利用字典保存
利用栈效率更高
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """   
        out_dict={}
        out_temp=[]
        def level_order(root,depth):
            if root:
                if depth in out_dict.keys():
                    out_dict[depth].append(root.val)
                else:
                    out_dict[depth]=[root.val]
                level_order(root.left,depth+1)
                level_order(root.right,depth+1)
        level_order(root,0)
        for i in range(len(out_dict)):
            out_temp.append(out_dict[i])
        return out_temp
         



if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list = str([1,2,3,-1,-1,-1,7,8])
    test_head = stringToTreeNode(add_list)
    test = Solution()
    print(test.levelOrder(test_head))

    print(time.perf_counter() - t0)
'''

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """   
        nodeList = []
        val_all = []
        nodeList.append(root)
        while nodeList:
            val_tmp = []
            size = len(nodeList)
            for i in range(size):
                node = nodeList.pop(0)
                if node:
                    val_tmp.append(node.val)
                    if node.left:
                        nodeList.append(node.left)
                    if node.right:
                        nodeList.append(node.right)
            if val_tmp:
                val_all.append(val_tmp)
        return val_all

'''
