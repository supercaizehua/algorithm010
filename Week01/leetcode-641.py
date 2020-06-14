class MyCircularDeque(object):

    def __init__(self, k):
        # 长度为k时占用k+1的空间，多出来的空间用来区分isEmpty和isFull
        # 首尾两个指针相等的时候为empty，尾部+1等于首部的时候为Full
        self.q = [0] * (k + 1)
        self.len = k + 1
        self.rear = 0
        self.front = 0

    def move_forward(self, pos):
        return (pos + 1) % self.len

    def move_backward(self, pos):
        return (pos - 1) % self.len

    def insertFront(self, value):
        if not self.isFull():
            # 前端插入始终是先插入后移动，self.front始终指向多出来的那个坑
            self.q[self.front] = value
            self.front = self.move_backward(self.front)
            return True
        else:
            return False

    def insertLast(self, value):
        if not self.isFull():
            # 后端插入始终是先移动后插入，self.rear始终指向后端最后插入的元素
            self.rear = self.move_forward(self.rear)
            self.q[self.rear] = value
            return True
        else:
            return False

    # 删除只需要移动
    def deleteFront(self):
        if not self.isEmpty():
            self.front = self.move_forward(self.front)
            return True
        else:
            return False

    def deleteLast(self):
        if not self.isEmpty():
            self.rear = self.move_backward(self.rear)
            return True
        else:
            return False

    def getFront(self):
        if not self.isEmpty():
            return self.q[self.move_forward(self.front)]
        else:
            return -1

    def getRear(self):
        if not self.isEmpty():
            return self.q[self.rear]
        else:
            return -1

    def isEmpty(self):
        if self.front == self.rear:
            return True
        else:
            return False

    def isFull(self):
        if self.move_forward(self.rear) == self.front:
            return True
        else:
            return False
