#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-26 16:21:07

理解题意：
两两交换结点
需要实际的节点操作，不能只改变值，也就是说不能开辟外部存储空间
'''

'''
solution1:
双指针迭代, 时间O(n), 空间O(1)
'''
class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        temp = ListNode(-1)
        temp.next = head
        prev = temp

        while head and head.next:
            first, second = head, head.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            head = first.next
        
        return temp.next

