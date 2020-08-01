# coding= utf-8
'''
author:@supercaizehua
--------------------
输入 排好序的数组
要求 原地 删除重复重现的元素
输出 数组的长度,根据题目的意思, 仅返回长度是不够的, 原数组也必须真正的删除重复元素
且超出返回的长度的元素不计
'''
from typing import List
'''
solution1: 双指针
当 nums[slow] = nums[fast], fast += 1
当 nums[slow] != nums[fast], nums[slow + 1] = nums[fast]
时间O(n)
空间O(1)
'''
class solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

# 优化, 对于[0,1,2,3,4,5], 函数会全部原地复制一遍, 但实际上是不需要的, 因此添加判断条件
class solution1_2:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                slow += 1
                if slow == fast: continue
                nums[slow] = nums[fast]
        return slow + 1