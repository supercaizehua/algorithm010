'''
author:@supercaizehua
'''
'''
so1: 递归
时间复杂度O(n) 递归函数 T(n) = 2T(n/2) + 1
空间复杂度 最坏O(n) 平均 O(logn)
'''
class Solution1:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        return self.inorderTraversal(root.left) + [root.val] + \
            self.inorderTraversal(root.right)

'''
s2: 使用栈来模拟递归
时间 O(n)
空间 O(n)
'''
class Solution2:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = []
        curr = root
        while not curr or not stack:
            while not curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            ans.append(curr.val)
            curr = curr.right
        return ans