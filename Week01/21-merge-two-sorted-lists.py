#coding=utf-8
'''
author:@supercaizehua
-------------------
输入, 两个链表头,两个链表升序
需要合并成节点升序的一个链表, 返回链表头
无其它特殊要求
'''

'''
solution1: 直接来
两个遍历
哨兵节点方便输出
时间O(n+m) nm分别为两个链表的长度
空间O(1)
'''
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        p = dummy

        while l1 and l2:#l1和l2都没有遍历完
            if l1.val <= l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        #处理剩下的节点
        p.next = l1 if l1 else l2

        return dummy.next


'''
solution2: 递归
当 list1[0] < list2[0]时, list1[0] + merge(list1[1:], list2)
当 list1[0] >= list2[0] 时, list2[0] + merge(list1, list2[1:])

边界情况
如果l1 or l2 是空, 则返回非空链表
判断 l1 , l2 的头节点的值, 小的添加到结果
如果两个链表有一个为空, 递归结束
时间O(n+m)
空间O(n+m)
'''
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #递归停止条件
        if not l1: return l2
        if not l2: return l1

        #drill down
        if l1.val <= l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2