# 树/图的搜索-遍历

- 每个节点都要访问一次
- 每个节点仅访问一次
- 对于节点的访问顺序不同
  - 深度优先搜索: depth first search
  - 广度优先搜索: breadth first search
  - 优先级优先搜索: 应用于推荐算法等场景

# DFS

## 示例代码

### 套用递归模板

```python
def dfs(node):
    if node in visited:
        return
    
    visited.add(node)
    
    dfs(node.left)
    dfs(node.right)
```

### 代码模板

```python
visited = set()

def dfs(node, visited):
    visited.add(node)
    ...
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

### 上面两个模板的合体(记忆这个)

```python
visited = set()
def dfs(node, visited):
    if node in visited: 
        return
    
    visited.add(node)
    for next_node in node.children():
        if not next_node in visited:
            dfs(next_node, visited)
```

### 非递归写法

```python
def dfs(self, tree):
    if tree.root is None:
        return []
    
    visited, stack = [], [tree.root]
    
    while stack:
        node = stack.pop()
        visited.add(node)
        
        process(node)
        noeds = generate_related_nodes(node)
        stack.push(nodes)
    
    ...其它工作
```



## dfs 的遍历顺序

树的遍历顺序(数字顺序即为遍历的顺序)

![](attachments/lesson9-dfs-tree.png)

图的遍历顺序

![](attachments/lesson9-graph-dfs.png)

# BFS

## bfs 的遍历顺序

![](attachments/lesson9-bfs-tree.png)

## 代码模板

```python
def bfs(graph, start, end):
	queue = []
    queue.append([start])
    visited.add(start)
    
    while queue:
        node = queue.pop()
        visited.add(node)
        
        process(node)
        nodes = generate_related_nodes(node)
        queue.push(nodes)
        
    ...#other processing work
```



# 贪心算法

## 概念解释 以及 对比

### 贪心算法

在每一步选择中都采取在当前状态下最好/最优的选择, **希望导致**结果是全局最好/最优的算法. (粗体字表明: 不一定每次都能导致想要的结果)

### 与dp的对比

贪心: 对于每个子问题的解决方案, 必定会做出一个选择, 且算法不能回退.

动态规划: 保存以前的结果, 根据以前的结果对当前的子问题进行选择, 有回退功能

## 应用场景

最优化问题: 求图中的最小生成树  求哈夫曼编码

PS: 一般不用于工程/生活中的问题

***那么到底什么情况可以使用呢?***

1. 问题能够分解成子问题
2. 子问题的最优解能够递推到最终问题的最优解(最优子结构)



# 二分查找

## 前提

1. 单调性
2. 有界
3. 能够通过索引访问(index)

## 代码模板

部分条件需要根据实际情况微调

```python
left, right = 0, len(array) - 1
while left <= right:
    mid = (left + right) / 2
    if array[mid] == target:
        # target found
        break or return result
    elif array[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

