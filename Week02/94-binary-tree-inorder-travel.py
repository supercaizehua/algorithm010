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

'''
s3: 颜色标记法(容易理解的栈方法)
新节点白色,已访问灰色
遇到白色标为灰色, 然后将其右子,自己,左子依次入栈
遇到灰色节点, 输出值
'''
class Solution3:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        ans = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if not node: continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                ans.append(node.val)
        return ans

class Solution3_1: # 优化
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack = [(0, root)]
        while stack:
            mark, node = stack.pop()
            if node is None: continue
            if mark == 0:
                stack.extend([(0, node.right), (1, node), (0, node.left)])
            else:
                ans.append(node.val)
        return ans

class Solution3_2: # 优化 pythonic
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stack = [], [root]
        while stack:
            curr = stack.pop()
            if isinstance(curr, TreeNode):
                stack.extend([curr.right, curr.val, curr.left])
                # 前序
                # stack.extend([curr.right, curr.left, curr.val])
                # 后序
                # stack.extend([curr.val, curr.right, curr.left])
            elif isinstance(curr, int):
                ans.append(curr)
        return ans