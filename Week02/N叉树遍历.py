'''
author:@supercaizehua
'''
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        pass


'''
前序/后序 递归
'''
class solution1:
    def preorder1(self, root):
        if not root: return
        ans = []
        ans.append(root.val)
        for child in root.children:
            ans.extend(self.preorder1(child))
        return ans

    def postorder1(self, root):
        if not root: return 
        ans = []
        for child in root.children:
            ans.extend(self.postorder1(child))
        ans.append(root.val)
        return ans

    '''递归 2'''
    def preorder2(self, root):
        ans = []
        def helper(root):
            if not root: return
            ans.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return ans

    def postorder2(self, root):
        ans = []
        def helper(node):
            if not node: return
            for child in node.children:
                helper(child)
            ans.append(node.val)
        helper(root)
        return ans

    '''递归 3'''
    def preorder3(self, root):
        ans = self.helper(root)
        return ans
    
    def helper(self, node):
        if not node: return
        ans = [node.val]
        for child in node.children:
            ans.extend(self.helper(child))
        return ans


'''前序后序迭代'''
class solution2:
    def preorder1(self, root):
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(child for child in node.children[::-1])
        return ans

    def postorder1(self, root):
        if not root: return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            '''与前序遍历的区别在下面两行'''
            stack.extend(child for child in node.children)  
        return ans[::-1]

    def preorder2(self, root):
        if not root: return []
        stack, ans = [(root, 0)], []
        while stack:
            node, mark = stack.pop()
            if mark == 0:
                stack.extend((i, 0) for i in node.children[::-1])
                stack.append((node, 1))
            else:
                ans.append(node.val)
        return ans

    def postorder2(self, root):'''与preorder2一样是mark标记法, 不过实现方法不同'''
        if not root: return []
        stack, ans = [root], []
        while stack:
            curr = stack.pop()
            if isinstance(curr, Node):
                stack.append(curr.val)
                for i in curr.children[::-1]: #stack 先进后出
                    stack.append(i)
            elif isinstance(curr, int):
                ans.append(curr)
        return ans


'''层序遍历'''
class Solution3:
    # bfs
    '''
    BFS
    取出队头, 如果有子节点, 将子节点加入到队尾, 并将当前节点的值加入ans, 注意处理输出的方式
    '''
    def levelOrder1(self, root):
        if not root: return []
        from collections import deque
        queue, ans = deque([root]), []
        while queue:
            curr_level = []
            for i in range(len(queue)):   #当前队列包含的节点都属于同一层
                node = queue.popleft()
                curr_level.append(node.val)
                queue.extend(node.children)
            ans.append(curr_level)
        return ans


    '''DFS + 递归'''
    def levelOrder2(self, root):
        ans = []
        
        def dfs(root, level):
            if not root: return
            if len(ans) < level + 1:
                ans.append([])
            ans[level].append(root.val)
            for child in root.children:
                dfs(child, level + 1)

        dfs(root, 0)
        return ans

    '''dfs'''
    def levelOrder3(self, root):
        if not root: return []
        stack, ans = [(root, 0)], []
        while stack:
            node, level = stack.pop()
            if node:
                if len(ans) <= level:
                    ans.append([])
                ans[level].append(node.val)
                stack.extend((child, level + 1) for child in node.children[::-1])
        return ans        

            



