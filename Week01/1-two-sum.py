#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-22 18:34:45
'''

from typing import List

'''
1.暴力法, 两个循环, 第一个循环 target-num, 第二个循环遍历一遍, 时间复杂度O(n^2), 空间复杂度O(n), 因为要再创建一个数组
'''

#解法一, 暴力法, 两层循环
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        for num in nums:
            new_list.append(target - num)
        for 