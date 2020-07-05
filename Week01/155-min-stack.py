#coding=utf-8
'''
author: @supercaizehua
data: 2020-7-2 17:17:35
---------------------------------------------------------------
理解题意:
设计一个栈，操作 push pop top
能在常数时间检索到最小元素 getMin（）
'''


'''
1.使用辅助栈
辅助栈始终保存最小值
- 当新元素入栈时, 判断辅助栈栈顶得出最小值, 最小值压入辅助栈
- 元素出栈, 同时弹出辅助栈栈顶
时间O(1)
空间O(n)
'''
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []


    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)
        else:
            self.minstack.append(self.minstack[-1])

    def pop(self) -> None:
        if self.stack:
            self.minstack.pop()
            return self.stack.pop()

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def getMin(self) -> int:
        if self.stack: return self.minstack[-1]

'''
2 辅助栈
与解法1不同点:
辅助栈与数据栈不同步
- 辅助栈元素空的时候, 必须加入新元素
- 新元素<=辅助栈栈顶元素, 才能进入辅助栈
- 出栈的时候, 辅助栈元素==数据栈出栈元素时, 辅助栈也要出栈
时间O(1), 空间O(n)
'''
class MinStack2:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minstack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minstack or x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self) -> None:
        top = self.stack.pop()
        if self.minstack and top == self.minstack[-1]:
            self.minstack.pop()
        return top

    def top(self) -> int:
        if self.stack: return self.stack[-1]

    def getMin(self) -> int:
        if self.stack: return self.minstack[-1]


'''
3只用一个栈, 不用辅助栈
入栈的时候,不是保存元素, 而是保存一个元组(x, 栈内最小值)
时间O(1), 空间O(n) 
'''
class MinStack3:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            cur_min = min(x, self.stack[-1][-1])
            self.stack.append((x, cur_min))

    def pop(self) -> None:
        if self.stack: return self.stack.pop()[0]

    def top(self) -> int:
        if self.stack:
            top = self.stack[-1][0]
            return top

    def getMin(self) -> int:
        if self.stack:
            cur_min = self.stack[-1][-1]
            return cur_min