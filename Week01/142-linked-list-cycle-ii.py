#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-30 02:17:54
---------------------------------------------------------------
理解题意:
判断链表是否有环
pos表示尾部连接到的结点
输出： 返回开始入环的结点， 如果无环， 返回null
'''

'''
解法1:
hash表
时间O(n), 空间O(n)
'''
class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        while head:
            if head in visited:
                return head
            else:
                visited.add(head)
            head = head.next
        return None

'''
解法2:
快慢指针
时间O(n), 空间O(1)

解题思路:
a: head到入口的结点数
b: 环内的结点数
fast = 2slow = slow + n * b(fast 比 slow 领先n圈)
可以得到
fast = 2nb
slow = nb
由题可知:
对于任意一个指针,当其走到入环结点时,必有 P= a + nb
由于fast与slow第一次相遇时, slow刚好走过了 nb 
此时, 找第三个指针 k 从head开始走, 当k走了 a步时, slow 走了 a + nb步, 即slow 与 k相遇在入环结点
'''
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = slow = k = head
        while fast:
            if not fast.next: return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while k != slow:
                    k = k.next
                    slow = slow.next
                return k
        return None
