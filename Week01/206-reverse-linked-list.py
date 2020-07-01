#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-26 13:56:41

理解题意：
输入: 链表
输出: 反转的链表
有可能是空链表
'''

'''
solution1:
开辟一个数组, 储存每个结点的值, 然后重新替换原链表的值
时间 O(n) 空间O(n)
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None: return None
        temp = []
        curr = head
        while curr.next != None:
            temp.append(curr.val)
            curr = curr.next
        temp.append(curr.val)
        curr = head
        while temp:
            curr.val = temp.pop()
            curr = curr.next
        return head


'''
solution2:
双指针迭代
遍历链表过程中,就改变结点指向
时间 O(n), 空间O(1)
'''
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        while head:
            nex = head.next
            head.next = pre
            pre, head = head, nex
        return pre


'''
solution3:
递归 https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
https://leetcode-cn.com/problems/reverse-linked-list/solution/fan-zhuan-lian-biao-shuang-zhi-zhen-di-gui-yao-mo-/
比较难以理解
时间复杂度O(n), 空间复杂度O(n)
'''
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None: return head
        new_head = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return new_head
        
        #更好理解一点的代码
        curr = head
        curr.next.next = curr
        curr.next = None
        return new_head


