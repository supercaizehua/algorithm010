'''
author:@supercaizehua
-----------------------------------
二叉树前序遍历 144 https://leetcode-cn.com/problems/binary-tree-preorder-traversal/
中序 94 https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
后序 145 https://leetcode-cn.com/problems/binary-tree-postorder-traversal/
层序(bfs 广度优先) 102 https://leetcode-cn.com/problems/binary-tree-level-order-traversal/
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 前/中/后序遍历
class solution1:
    def preOrder(self, root):
        if not root: return []
        return [root.val] + self.preOrder(root.left) + self.preOrder(root.right)
        # 中序
        # return self.inOrder(root.left) + [root.val] + self.inOrder(root.right)
        # 后序
        # return self.postOrder(root.left) + self.postOrder(root.right) + [root.val]

class solution1_1:
    def preOrder(self, root):
        ans = []
        self.dfs(root, ans)
        return ans
    
    def dfs(self, root, ans):
        if root:
            '''如果是中序和后序, 只要改变ans.append的位置即可'''
            ans.append(root.val)
            self.dfs(root.left, ans)
            self.dfs(root.right, ans)



# 前/中/后序迭代
class solution2_1: #普通栈实现
    def preOrder(self, root):
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans
    
    def postOrder(self, root):
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if node:
                ans.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ans[::-1]    #!!!!!!!! 前序后序的区别仅在这里
    
    def inOrder(self, root):
        stack, ans = [], []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                ans.append(node.val)
                root = node.right
        return ans

class solution2_2: # mark标记 + 栈
    def markOrder(self, root):
        # 0==unvisited 1==visited
        stack, ans = [(0, root)], [] 
        while stack:
            mark, node = stack.pop()
            if not node: continue   #if node is None
            if mark == 0:
                # preorder
                # stack.extend([(0, node.right), (0, node.left), (1, node)])
                # inorder
                # stack.extend([(0, node.right), (1, node), (0, node.left)])
                # postorder
                stack.extend([(1, node), (0, node.right), (0, node.left)])
            else:
                ans.append(node.val)
        return ans

'''优化过的mark标记法, 以后序遍历为例'''
    def op_markOrder(self, root):
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            if node is None: continue
            if isinstance(node, TreeNode):
                stack.extend([node.val, node.right, node.left])
            else:
                ans.append(node)
        return ans


'''二叉树层级遍历
DFS递归 增加变量去记录层级信息
DFS + 栈  有两种实现方式
BFS + 队列
其实这里的DFS不管是用递归也好, 还是用栈也好, 本质上运算的顺序是一样的, 递归充其量也就是系统在背后
实现了一个栈而已, 避免了我们人为实现栈的麻烦
'''
class solution3_1: #dfs 递归
    def levelOrder(self, root):
        ans = []
        self.dfs(root, 0, ans)
        return ans
    
    def dfs(self, root, level, ans):
        if not root:
            return 
        if len(ans) < level+1:
            ans.append([])
        ans[level].append(root.val)
        self.dfs(root.left, level+1, ans)
        self.dfs(root.right, level+1, ans)

class solution3_2: #dfs + stack 1  有点像mark标记法
    def levelOrder(self, root):
        if not root: return []
        ans, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if len(ans) < level + 1: 
                ans.append([])
            ans[level].append(curr.val)
            if curr.right:
                stack.append((curr.right, level + 1))
            if curr.left:
                stack.append((curr.left, level + 1))   
        return ans

class solution3_3: #dfs + stack 2  
    def levelOrder(self, root):
        ans, stack = [], [(root, 0)]
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(curr.val)
                stack.append((curr.right, level + 1))
                stack.append((curr.left, level + 1))
        return ans

class solution3_4: #BFS + queue 使用了list模拟队列, pop(0) 速度有点慢, 改良方式就是导入高性能包
    def levelOrder(self, root):
        ans, queue = [], [(root, 0)]
        while queue:
            curr, level = queue.pop(0)
            if curr:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return ans

class solution3_5: #BFS + deque  高性能
    def levelOrder(self, root):
        from collections import deque
        ans, queue = [], deque([(root, 0)])
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(ans) < level + 1:
                    ans.append([])
                ans[level].append(curr.val)
                queue.append((curr.left, level + 1))
                queue.append((curr.right, level + 1))
        return ans