# -*- coding: utf-8 -*-



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 迭代
        # res = []
        # stack = []
        # while stack or root:
        #     if root:
        #         stack.append(root)
        #         root = root.left
        #     else:
        #         tmp = stack.pop()
        #         res.append(tmp.val)
        #         root = tmp.right
        # return res
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(root)
        return res