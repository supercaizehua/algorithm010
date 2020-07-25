class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children



'''
递归
'''
class Solution1:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []
        ans = [root.val]
        for child in root.children:
            ans.extend(self.preorder(child))
        return ans

'''
迭代
'''
class Solution2:
    def preorder(self, root: 'Node') -> List[int]:
        if not root: return []

        stack, ans = [root], []
        while stack:
            root = stack.pop()
            ans.append(root.val)
            stack.extend(root.children[::-1])
        
        return ans