# coding=utf-8
'''
author: @supercaizehua
data: 2020-6-26 16:21:07

理解题意：
两两交换结点
需要实际的节点操作，不能只改变值，也就是说不能开辟外部存储空间
'''

'''
solution0:
新开一个数组, 存起来, 然后改写结点的值
时间O(n), 空间O(n)
不符合题意
'''

'''
solution1:
双指针迭代, 时间O(n), 空间O(1)
需要注意改变结点指向的顺序
'''


class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = dummy = ListNode(0)

        while head and head.next:
            p1, p2 = head, head.next
            pre.next = p2
            p1.next = p2.next
            p2.next = p1

            head = p1.next
            pre = p1
        pre.next = head

        return dummy.next


'''
solution2:
递归
终止条件:没有节点/只有一个结点
当前层处理逻辑: firstnode = head
              secondnode = head.next
下一层: firstnode.next = swapPairs(second.next)

清理当前层: secondnode.next = firstnode 
返回: return secondnode
时间O(n), 空间O(n)
'''


class Solution2_1:
    def swapPairs(self, head: ListNode) -> ListNode:
        # terminator
        if not head or not head.next:
            return head

        # process curr level
        first = head
        second = head.next

        # drill down
        first.next = self.swapPairs(second.next)

        second.next = first
        return second


class Solution2_2:  # 国际区大神简洁代码
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)
            tmp.next = head
            return tmp
        return head
