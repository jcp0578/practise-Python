#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC
'''

import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            mid=len(nums)//2
            root=TreeNode(nums[mid])
            root.left=self.sortedArrayToBST(nums[:mid])
            root.right=self.sortedArrayToBST(nums[mid+1:])
            return root
        else:
            return None

         



if __name__ == "__main__":

    t0 = time.perf_counter()

    add_list = [1,2,3,4,5,6,7,8]
#    test_head = stringToTreeNode(add_list)
    test = Solution()
    print(treeNodeToString(test.sortedArrayToBST(add_list)))

    print(time.perf_counter() - t0)
'''

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == None or len(nums) == 0:
            return None
        return self.gettree(nums,0,len(nums)-1)
    
    def gettree(self,nums,l,r):
        if l <= r:
            mid = (l+r)/2
            head = TreeNode(nums[mid])
            head.left = self.gettree(nums,l,mid-1)
            head.right = self.gettree(nums,mid+1,r)
            return head
        else:
            return None

'''
