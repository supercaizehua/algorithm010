#coding=utf-8
'''
author: @supercaizehua
data: 2020-6-23 10:39:18
---------------------------------------------------------------
理解题意:
输入: 数组, 值都是非负整数, 且数组的元素个数>=2
容积是 (rb - lb)* 最矮的边界
'''

from typing import List
'''
1.暴力法,计算出所有可能的情况
固定左边, 移动右边,找到容积最大的组合,时间 O(n^2) 空间 O(1)
PS:此解法用python, 在leetcode会超时
'''
class Solution1:
    def maxArea(self, height: List[int]) -> int:
        L = len(height)
        res = 0
        for i in range(L-1):
            for j in range(i+1, L):
                V = (j - i) * min(height[i], height[j])
                res = max(res, V)
        return res


'''
2.双指针, 其实是对暴力法的优化
从两边开始往中间缩, 增加收敛的判断条件,找到最大的组合, 时间 O(n), 空间(1)
---------------------------------------------------------------
收敛的判断条件:
lb:左边界, rb:右边界, h:高度为 min(lb, rb)
收敛的对象, lb, rb中较矮的那个, 同时收敛时, 如果遇到比较矮的边界还要矮的柱子,就直接跳过, 只有遇到高于较矮的柱子时, 才停下来判断.
'''
class Solution2:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        res = 0
        while i < j:
            if height[i] < height[j]:
                res = max(res, (j - i) * height[i])
                i += 1
            else:
                res = max(res, (j - i) * height[j])
                j -= 1
        return res



if __name__ == "__main__":
    test_list = [1,8,6,2,5,4,8,3,7]
    a = Solution2()
    ans = a.maxArea(test_list)
    print(ans)
