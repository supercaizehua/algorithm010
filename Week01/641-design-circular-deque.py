#coding=utf-8
'''
author: @supercaizehua
----------------------------
理解题意
MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。
'''

'''
1.列表 + 指针
'''
class MyCircularDeque1:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self._size = 0
        self._front, self._rear = 0, 0
        self._capacity = k
        self._data = [-1] * k
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        if self.isEmpty():
            self._data[self._front] = value
        else:
            # 列表不为空, front 的位置为 原位置-1 mod(capacity)
            # 举例子，如果容量为10， front为0， 那么代表data[0]已经铀元素了
            # 那么新插入的元素应该插入在 data[9], 即新的front就需要变成9
            self._front = (self._front - 1) % self._capacity
            self._data[self._front] = value
        self._size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.isFull(): return False
        if self.isEmpty():
            self._data[self._rear] = value
        else:
            self._rear = (self._rear + 1) % self._capacity
            self._data[self._rear] = value
        self._size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self._data[self._front] = -1
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._rear = self._front
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.isEmpty(): return False
        self._data[self._rear] = -1
        self._rear = (self._rear - 1) % self._capacity
        self._size -= 1
        if self.isEmpty():
            self._front = self._rear
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self._data[self._front]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self._data[self._rear]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return self._size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return self._size == self._capacity



'''
2.双栈实现, 一个栈的栈顶是头部元素, 另一个栈的栈顶是尾部元素
'''
class MyCircularDeque2:
    def __init__(self, k: int):
        self.size = k
        self.head = []
        self.tail = []

    def isEmpty(self):
        return not self.head or not self.tail
    
    def isFull(self):
        # size = len(self.head) + len(self.tail)
        
        return len(self.head) + len(self.tail) == self.size
    
    def insertFront(self, value):
        if self.isFull(): return False
        self.head.append(value)
        return True
    
    def insertLast(self, value):
        if self.isFull(): return False
        self.tail.append(value)
        return True
    
    def deleteFront(self):
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())
        if not self.head: return False
        self.head.pop()
        return True

    def deleteLast(self):
        if not self.tail:
            while self.head:
                self.tail.append(self.head.pop())
        if not self.tail: return False
        self.tail.pop()
        return True
    
    def getFront(self):
        if not self.head:
            while self.tail:
                self.head.append(self.tail.pop())
        if not self.head: return -1
        return self.head[-1]

    def getRear(self):
        if not self.tail:
            while self.head:
                self.tail.append(self.head.pop())
        if not self.tail: return -1
        return self.tail[-1]
