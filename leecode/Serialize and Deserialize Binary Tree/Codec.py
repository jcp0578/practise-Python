#!/usr/bin/python3
# -*- coding: utf-8 -*-
'''
AC but not a good solution
'''
import sys
import time


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        nodeList = []
        out_t = []
        nodeList.append(root)
        while nodeList:
            size = len(nodeList)
            for i in range(size):
                node = nodeList.pop(0)
                if node:
                    out_t.append(node.val)
                    nodeList.append(node.left)
                    nodeList.append(node.right)
                else:
                    out_t.append("null")
        while out_t and out_t[-1] == "null":
            out_t.pop()
        return str(out_t)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        nodeQueue = []
        front = 0
        nodeData = data[1:-1].split(",")

        try:
            root = TreeNode(int(nodeData[0]))
        except:
            return None

        index = 1
        nodeQueue.append(root)
        while front < len(nodeQueue):
            root_t = nodeQueue[front]
            front += 1

            try:
                root_t.left = TreeNode(int(nodeData[index]))
                nodeQueue.append(root_t.left)
            except:
                root_t.left = None
            finally:
                index += 1

            try:
                root_t.right = TreeNode(int(nodeData[index]))
                nodeQueue.append(root_t.right)
            except:
                root_t.right = None
            finally:
                index += 1

        return root


if __name__ == "__main__":

    if sys.version_info.major == 3:
        t0 = time.perf_counter()
    else:
        t0 = time.time()

    test_list = [
        "[1, 2, 3, 4, null, 5, null, 6, null, null, null, 7]",
        "[4, 2, null, 1, 3]", "[2, 3, 5]", "[]", "[1, null, 2, 3, 4, 5]"
    ]

    # Your Codec object will be instantiated and called as such:
    test = Codec()

    for i in range(len(test_list)):
        out_t = (test.serialize(test.deserialize(test_list[i])))
        if out_t == test_list[i]:
            print("\033[1;32;40m  Pass \033[0m")
        else:
            print(
                "\033[1;31;40m  Fail!!\033[0m\033[0;34;40m out \"%s\" should \"%s\" by \"%.50s\" "
                % (out_t, str(test_list[i]), str(test_list[i])))

    if sys.version_info.major == 3:
        print("\nRun Time is %f s" % (time.perf_counter() - t0))
    else:
        print("\nRun Time is %f s" % (time.time() - t0))



'''
import json



class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """

        def tuplify(node):
            return node and (node.val,
                             tuplify(node.left),
                             tuplify(node.right))

        return json.dumps(tuplify(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """

        def detuplify(t):
            if not t:
                return None
            root = TreeNode(t[0])
            root.left = detuplify(t[1])
            root.right = detuplify(t[2])
            return root

        return detuplify(json.loads(data))

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        if root is None:
            return '[]'
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            val = next(vals)
            if val is '#':
                return None
            root = TreeNode(val)
            root.left = doit()
            root.right = doit()
            return root
        if data == '[]':
            return None
        vals = iter(data.split())
        return doit()


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '#$'
        return '#' + str(root.val) + self.serialize(root.left) + self.serialize(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data[1:].split('#')[::-1]
        
        def buildtree(string):
            val = string.pop()
            if val == '$':
                return None
            node = TreeNode(int(val))
            node.left = buildtree(string)
            node.right = buildtree(string)
            return node

        return buildtree(data)
'''
