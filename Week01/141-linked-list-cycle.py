#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-29 15:56:47
---------------------------------------------------------------
理解题意:
判断链表是否有环
pos表示尾部连接到的结点
输出：True or False
'''
'''
solution0:
暴力法
两次循环链表
时间O(n^2)
'''
class Solution0:
    def hasCycle(self, head: ListNode) -> bool:
        p1 = head
        while p1:
            p2 = head
            if p1.next == p1: return True #针对一个元素有环的情况
            while p2 != p1:
                if p1.next == p2: return True
                p2 = p2.next
            p1 = p1.next
        return False

'''
解法1:
暴力法
利用python方法id（）得到结点的地址，存入一个hash表， 如果有环就返回True
没有环的话，循环就会退出
时间O(n), 空间O(n)
'''
class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        while head:
            address_of_node = id(head)
            if address_of_node in visited:
                return True
            else:
                visited.add(address_of_node)
            head = head.next
        return False


'''
解法2:
快慢指针, 如果两个指针相遇, 说明是环
时间O(n), 空间O(1)
'''
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        fast = slow = head
        while fast:
            if not fast.next: return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow: return True
        return False


'''
解法3：
将链表反转leetcode 206
如果最后返回的是head， 则链表有环
时间O（n）， 空间O（1）
'''
class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        if  head and head.next and self.reverseList(head) == head:
            return True
        return False

    def reverseList(self, head):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre