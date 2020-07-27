#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-30 04:18:30
---------------------------------------------------------------
理解题意:
k个结点翻转（对比24题，2换成k）
k<=链表长度
如果结点不满k， 保持原有顺序
限定
常数空间
不能只改变结点的值，需要进行实际的操作

'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

'''
解法1
本题的主要思路就是
1.先找到需要翻转的k个节点
2.翻转操作
3.处理翻转后的节点的头和尾
4.返回


翻转操作使用 双指针来进行
时间O(nK), 空间O(1)
'''
class Solution1_1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head

        while head:
            tail = pre
            # 找到k个结点
            for _ in range(k):
                tail = tail.next
                if not tail: return dummy.next #不满k个节点直接返回
            
            #下一段待处理的链表的的头
            next_head = tail.next

            #反转后的新链表的头和尾
            new_head, new_tail = self.reverse(head, tail)

            #将翻转后的头和尾连接到原来的链表上去
            pre.next = new_head
            new_tail.next = next_head
            pre = new_tail
            head = next_head

        return dummy.next

    def reverse(self, head, tail):
        pre = None
        cur = new_head = new_tail = head
        while cur != tail:
            new_head = new_head.next
            cur.next = pre
            pre = cur
            cur = new_head
        cur.next = pre
        return new_head, new_tail


'''
解法2:
递归
1.找到第k+1， 个节点，标记为next_head
2.翻转tail前的节点， 返回的头节点为new_head， 此时翻转后的链表尾巴为head
3. head.next = 下一层的new_head
时间O（nk）空间O（k）
'''
class Solution2:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head

        next_head = head
        for _ in range(k):
            if not next_head: return head
            next_head = next_head.next
        new_head, new_tail = self.reverse(head, next_head)

        new_tail.next = self.reverseKGroup(next_head, k)

        return new_head

    def reverse(self, head, next_head):
        pre = None
        cur = new_head = new_tail = head
        while cur != next_head:
            new_head = new_head.next
            cur.next = pre
            pre = cur
            cur = new_head

        new_head = pre
        return new_head, new_tail


'''
解法3:
栈
k个数压入栈, 再弹出
注意的问题:
1. 剩下链表个数不够 k 的情况
2. 已经翻转的部分如何与剩下的链接起来
时间O(n), 空间O(k)
'''
class Solution3:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        pre = dummy
        while True:
            cnt = k
            stack = []
            tmp = head
            while cnt and tmp:
                stack.append(tmp)
                tmp = tmp.next
                cnt -= 1

            # 处理不足k个的情况
            if cnt: # cnt == 0 ----> False
                pre.next = head
                break
            
            # 如果满足 k 个的情况,弹出栈的同时链接
            while stack:
                pre.next = stack.pop()
                pre = pre.next

            # 链接完k个结点后, 调整指针,准备下一次循环
            pre.next = tmp
            head = tmp
        
        return  dummy.next








if __name__ == "__main__":
    pass